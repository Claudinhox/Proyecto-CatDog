from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.user.forms import RegisterUsers

#Registro Usuario
class RegisterUser(CreateView):
    model = User
    template_name = "user/addUser.html"
    form_class = RegisterUsers
    success_url = reverse_lazy('home')

