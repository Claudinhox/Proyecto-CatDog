from django import forms
from apps.food.models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food

        fields = [
            'food_name',
            'description',
            'type_of_pet',
            'food_cost',
            'image',
        ]
        labels = {
            'food_name': 'Nombre del alimento',
            'description': 'Descripción del alimento',
            'type_of_pet': 'Tipo de mascota',
            'food_cost': 'Valor del alimento',
            'image': 'Imagen del alimento',
        }
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'validate'}),
            'description': forms.TextInput(attrs={'class': 'validate'}),
            'type_of_pet': forms.TextInput(attrs={'class': 'validate'}),
            'food_cost': forms.NumberInput(attrs={'class': 'validate'}),
        }
