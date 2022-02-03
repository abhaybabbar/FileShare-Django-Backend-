from django.urls import path
from .views import GetFiles,UploadFiles 

urlpatterns = [
    path('file-upload/', UploadFiles.as_view(), name='file-upload'),
    path('<slug>/', GetFiles.as_view(), name='getfiles'),
]
