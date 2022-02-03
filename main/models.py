from django.db import models
from .helpers import generateSlug

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to="uploads/")
    
    def __str__(self):
        return self.file.name
    
class FileShare(models.Model):
    message = models.TextField(blank=True)
    slug = models.SlugField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField(File, blank=True)
    
    def numberOfFiles(self):
        return self.files.count()
    
    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        self.slug = generateSlug()
        super(FileShare, self).save(*args, **kwargs)
        

    