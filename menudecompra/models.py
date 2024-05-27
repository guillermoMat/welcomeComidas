from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, null=False)
    #image_url = models.CharField(max_length=255, null=False, default='product_images/cangreburguer.jpg')  # Valor por defecto
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, default='product_images/default.jpg')

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/product_images/default.jpg"  # URL de imagen predeterminada si no se proporciona una imagen

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    #photo_url = models.CharField(max_length=255, null=False)
    
    photo = models.ImageField(upload_to='product_images/', blank=True, null=True, default='product_images/cangreburguer.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.product_name