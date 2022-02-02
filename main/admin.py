from django.contrib import admin
from .models import FileShare, File
# Register your models here.
@admin.register(FileShare)
class FileShareAdmin(admin.ModelAdmin):
    fields = ['message', 'files']
    list_display = ['id', 'message', 'slug', 'created_at', 'numberOfFiles']
    
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file']