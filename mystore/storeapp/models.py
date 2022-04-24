from django.db import models


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

