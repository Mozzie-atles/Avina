from django.urls import path
from .views import index
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', index),
    path('login', LoginView, {'template_name': 'index.html'}, name='login'),
]
