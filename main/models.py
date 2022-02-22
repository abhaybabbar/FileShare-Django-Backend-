from django.db import models
from .helpers import generateSlug

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to="uploads/")
    
    def __str__(self):
        return self.file.name
    
    def fileSizeInStr(self):
        fileSize = self.file.size
        sizeArray = ["Bytes", "KB", "MB", "GB"]
        i = 0
        while (fileSize > 900):
            fileSize /= 1024
            i+=1
        return str(round(fileSize * 100) / 100) + " " + sizeArray[i]
    
    @property
    def fileSize(self):
        return self.file.size
    
class FileShare(models.Model):
    message = models.TextField(blank=True)
    slug = models.SlugField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField(File, blank=True)
    
    def numberOfFiles(self):
        return self.files.count()
    
    
    def totalFilesSize(self):
        fileSize = 0
        for file in self.files.all():
            fileSize += file.fileSize
        
        sizeArray = ["Bytes", "KB", "MB", "GB"]
        i = 0
        while (fileSize > 900):
            fileSize /= 1024
            i+=1
        return str(round(fileSize * 100) / 100) + " " + sizeArray[i]
    
    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        self.slug = generateSlug()
        super(FileShare, self).save(*args, **kwargs)
        

    