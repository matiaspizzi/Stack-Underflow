from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', about, name='about'),
]