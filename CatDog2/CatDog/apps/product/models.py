from django.db import models

# Create your models here.
class Product(models.Model):
    description = models.CharField(max_length=200)
    value = models.IntegerField(default=0)
    class Meta:
        db_table = 'Product'