from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]