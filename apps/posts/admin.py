from django.contrib import admin

# models
from .models import Posts
from ..camera.models import Camera
from ..files.models import Files

class CameraAdmin(admin.TabularInline):
    model = Camera

class FilesAdmin(admin.TabularInline):
    model = Files

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CameraAdmin,
        FilesAdmin
    ]


# Register your models here.
admin.site.register(Posts, PostAdmin)



    

