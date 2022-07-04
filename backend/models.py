from distutils.command.upload import upload
from django.db import models

# Create your models here.
class FoodItem(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='FoodItems')
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=30)


class BookTable(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    email = models.CharField(max_length=40)
    number_of_persons = models.IntegerField()
    date = models.DateField()

