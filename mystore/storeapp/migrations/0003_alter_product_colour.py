# Generated by Django 4.0.4 on 2022-04-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colour',
            field=models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow')], max_length=20),
        ),
    ]
