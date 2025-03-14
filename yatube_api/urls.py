from django.shortcuts import render
from rest_framework.authtoken import views
from django.urls import path

# Create your views here.
urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token)
]

