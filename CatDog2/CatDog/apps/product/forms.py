from django import forms
from apps.product.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        
        fields = [
            'description',
            'value',
        ]
        
        labels = {
            'description':"Descripción",
            'value':"Valor",
        }
        
        widgets = {
            'description':forms.TextInput(attrs={'class':'validate'}),
            'value':forms.TextInput(attrs={'class':'validate'}),
        }