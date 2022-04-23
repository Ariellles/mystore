from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    size = models.CharField(max_length=20) #Small or Normal
    colour = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
