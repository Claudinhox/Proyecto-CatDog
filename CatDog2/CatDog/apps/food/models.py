from django.db import models

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    type_of_pet = models.CharField(max_length=100)
    food_cost = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    class Meta:
        db_table = 'Food'