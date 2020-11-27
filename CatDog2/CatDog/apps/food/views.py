from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from apps.food.forms import FoodForm
from apps.food.models import Food
from django.contrib import messages

# Create your views here.
def addFood(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alimento agregado correctamente')
            return redirect('/listfood')
    else:
        form = FoodForm()
    return render(request, 'food/addFood.html', {'form': form})

def listFood(request):
    food = Food.objects.all().order_by('id')
    context = {'food': food}
    return render(request, 'food/listFood.html', context)

def editFood(request, idFood):
    food = Food.objects.get(id=idFood)
    if request.method == 'GET':
        form = FoodForm(instance=food)
    else:
        form = FoodForm(request.POST, instance=food, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Alimento actualizado correctamente')
            return redirect('/listfood')
    return render(request, 'food/addFood.html', {'form': form})

def deleteFood(request, idFood):
    food = Food.objects.get(id=idFood)
    if request.method == 'POST':
        food.delete()
        messages.error(request, 'Producto eliminado correctamente')
        return redirect('/listfood')
    return render(request, 'food/deleteFood.html', {'food': food})

def detailsFood(request, idFood):
    food = Food.objects.get(id=idFood)
    return render(request, 'food/detailsFood.html', {'food': food})

def foods(request):
    food = Food.objects.all()
    return render(request, 'food/foods.html', {'food': food})

def viewFood(request, idFood):
    food = get_object_or_404(Food, pk=idFood)
    return render(request, 'food/viewFood.html', {'food': food})