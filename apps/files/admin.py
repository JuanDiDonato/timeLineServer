from importlib.metadata import files
from django.contrib import admin

# model
from .models import Files

admin.site.register(Files)
