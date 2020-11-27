from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.product.forms import ProductForm
from apps.product.models import Product
from django.contrib import messages

#Listar
def ProductIndex(request):
    product = Product.objects.all().order_by('id')
    context = {'products':product}
    return render(request, 'product/index.html', context)

#Agregar    
def ProductAdd(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente')
            return redirect('/product')
    else:
        form = ProductForm()
    return render(request, 'product/productAdd.html',{'form': form})

#Editar
def ProductEdit(request,idProduct):
    product = Product.objects.get(id=idProduct)
    if request.method == 'GET':
        form = ProductForm(instance=product)
    else:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Producto actualizado correctamente')
        return redirect ('/product')
    return render(request, 'product/productAdd.html',{'form': form})

#Eliminar
def ProductDelete(request,idProduct):
    product = Product.objects.get(id=idProduct)
    if request.method == 'POST':
        product.delete()
        messages.error(request, 'Producto eliminado correctamente')
        return redirect ('/product')
    return render (request, 'product/productDelete.html', {'product':product})