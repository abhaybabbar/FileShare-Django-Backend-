from rest_framework import serializers
from .models import FileShare, File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class FileShareSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)
    class Meta:
        model = FileShare
        fields = ['message', 'files']