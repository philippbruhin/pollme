from django.contrib import admin
from .models import Poll, Choice

admin.site.register(Choice)
admin.site.register(Poll)
