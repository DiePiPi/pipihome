from django.contrib import admin
from django.db import models

# Register your models here.

from .models import post, tutorial

admin.site.site_header = 'PiPi\'s Home'
admin.site.site_title = 'Reservation system tutorial'

admin.site.register(post)
admin.site.register(tutorial)
