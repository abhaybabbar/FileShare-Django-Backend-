from django.utils.text import slugify
import string
import random

def generateRandomString():
    temp = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
    return temp

def generateSlug():
    from .models import FileShare
    slug = generateRandomString()
    if FileShare.objects.filter(slug = slug).exists():
        slug = generateSlug()
    return slug