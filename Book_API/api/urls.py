from django.contrib import admin
from django.urls import path
from .views import BookAPIView
urlpatterns = [
    path('', BookAPIView.as_view())
]