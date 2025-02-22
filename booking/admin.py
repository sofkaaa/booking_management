from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Computer)
admin.site.register(models.PCRoom) 
admin.site.register(models.BookedComputer) 
admin.site.register(models.BookedPCRoom)
admin.site.register(models.UProfile)  