from django.urls import path
from .views import GetFiles

urlpatterns = [
    path('<slug>/', GetFiles.as_view(), name='getfiles'),
]
