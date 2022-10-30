from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Rooms)
admin.site.register(models.Person)
admin.site.register(models.Appointment)
