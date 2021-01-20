from django.urls import path
from .views import index
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', index),
    # Commented out login view because it didn't work, and we should build the view in the frontend.
    # path('login', LoginView, {'template_name': 'index.html'}, name='login'),
]
