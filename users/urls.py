# urls.py
from django.urls import path
from .views import UserloginView
from .views import UserRegistrationView 

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserloginView.as_view(), name='login'),
]