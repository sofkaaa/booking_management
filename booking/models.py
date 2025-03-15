from django.db import models

# Create your models here.
class UProfile(models.Model): #userprofile 
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email_confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Computer(models.Model): #бронювання компів у звичайному залі
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    specs = models.TextField()
    available = models.BooleanField(default=True)
    pcroom = models.ForeignKey("PCRoom", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class PCRoom(models.Model): #бронювання кімнати з компами+бронювання компів в кімнаті
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

    class Meta:
        unique_together = ('pcroom', 'start_time', 'end_time')

class BookedComputer(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    uprofile = models.ForeignKey(UProfile, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('computer', 'start_time', 'end_time')
 
