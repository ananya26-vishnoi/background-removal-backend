# urls.py

from django.urls import path
from .views import upload_and_remove_background

urlpatterns = [
    path('uploadAndRemoveBackground', upload_and_remove_background, name='upload_and_remove_background'),
]
