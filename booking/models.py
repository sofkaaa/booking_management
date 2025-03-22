from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
# Create your models here.
class UProfile(models.Model): #userprofile 
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email_confirmed = models.EmailField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Computer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    specs = models.TextField()
    available = models.BooleanField(default=True)
    pcroom = models.ForeignKey("PCRoom", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class PCRoom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    number = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    

class BookedPCRoom(models.Model):
    pcroom = models.ForeignKey(PCRoom, on_delete=models.CASCADE)
    uprofile = models.ForeignKey(UProfile, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        unique_together = ('pcroom', 'start_time', 'end_time')
    
    def clean(self):
        overlapping_bookings = BookedPCRoom.objects.filter(
            pcroom=self.pcroom,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exists()
        if overlapping_bookings:
            raise ValidationError("Ця кімната вже заброньована на цей період.")
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        send_mail(
            'Підтвердження бронювання',
            f'Ваше бронювання підтверджено: {self.pcroom.name} з {self.start_time} до {self.end_time}',
            'admin@example.com',
            [self.email]
        )


class BookedComputer(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    uprofile = models.ForeignKey(UProfile, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('computer', 'start_time', 'end_time')
 
