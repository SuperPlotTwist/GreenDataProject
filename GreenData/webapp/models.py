from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Product(models.Model):
	product_name = models.CharField(max_length=255)
	packaging = models.CharField(max_length=255)
	packaging_mass = models.IntegerField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.product_name

	def get_absolute_url(self):
		return reverse('productDetail', args=(str(self.id)) )