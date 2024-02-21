from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media')


class Testimonial(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name