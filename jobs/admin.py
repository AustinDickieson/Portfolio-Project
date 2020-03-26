from django.contrib import admin
# Register your models here.
#Write code to show in admin page for superuser to change
from .models import Job
#. says current directory

admin.site.register(Job)
