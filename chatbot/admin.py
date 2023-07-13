from django.contrib import admin
from .models import Application, Citizen
# Register your models here.

admin.site.register(Citizen)
admin.site.register(Application)