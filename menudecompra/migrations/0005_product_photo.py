# Generated by Django 5.0.6 on 2024-05-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menudecompra', '0004_category_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='img/product_images/default.jpg', null=True, upload_to='img/product_images/'),
        ),
    ]
