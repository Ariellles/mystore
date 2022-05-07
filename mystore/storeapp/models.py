from django.db import models
from django.contrib.auth.models import User


SIZE_OPTIONS = [
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
]
COLOUR_OPTIONS = [
    ('White', 'White'),
    ('Black', 'Black'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
]


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    size = models.CharField(max_length=20, choices=SIZE_OPTIONS)
    colour = models.CharField(max_length=20, choices=COLOUR_OPTIONS)
    material = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name


class Purchase (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    amount = models.PositiveIntegerField(default=1)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    country = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username


