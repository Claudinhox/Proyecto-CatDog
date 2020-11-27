from django.urls import path
from apps.home.views import Index

urlpatterns = [
    path('', Index, name="home"),
    path('home/', Index, name="home"),
]
