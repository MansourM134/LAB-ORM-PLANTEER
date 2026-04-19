from django.db import models

# Create your models here.

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