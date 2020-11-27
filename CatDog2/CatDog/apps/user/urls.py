from django.conf.urls import url
from django.urls import path
from apps.user.views import RegisterUser

urlpatterns = [
    path('newuser/', RegisterUser.as_view(), name="RegisterUser"),
]