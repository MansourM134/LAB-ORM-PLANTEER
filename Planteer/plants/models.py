from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Country(models.Model):

    name = models.CharField(max_length=2048, unique=True)
    flag = models.ImageField(upload_to="images/", default="images/world.png")


    def __str__(self):
        return self.name
    

class Plant(models.Model):

    class CategoryChoices(models.TextChoices):
        HERB = 'HERB', 'Herb'
        TREE = 'TREE', 'Tree'
        FLOWER = 'FLOWER', 'Flower'
        VEGETABLE = 'VEG', 'Vegetable'
        FRUIT = 'FRUIT', 'Fruit'
        OTHER = 'OTHER', 'Other'


    name = models.CharField(max_length=2048)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(choices=CategoryChoices.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    countries = models.ManyToManyField(Country)

    def __str__(self):
        return self.name


class Comment(models.Model):

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=2048)
    content = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.plant.name}"