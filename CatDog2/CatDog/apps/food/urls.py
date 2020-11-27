from django.urls import path
from apps.food.views import addFood, listFood, editFood, deleteFood, detailsFood, foods, viewFood

urlpatterns = [
    path('addfood/', addFood, name="addFood"),
    path('listfood/', listFood, name="listFood"),
    path('editfood/<int:idFood>/', editFood, name='editFood'),
    path('deletefood/<int:idFood>/', deleteFood, name='deleteFood'),
    path('detailsfood/<int:idFood>/', detailsFood, name='detailsFood'),
    path('foods/', foods, name='foods'),
    path('viewfood/<int:idFood>/', viewFood, name='viewFood'),
]
