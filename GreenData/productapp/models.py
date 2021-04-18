from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse

# Create your models here.


class Product(models.Model):
	"""
		model class for a standart product record in the database
	"""
	# Displayed

	# Primary key is the barcode value
	barcode = models.CharField(max_length=128, unique=True, primary_key=True)
	
	# Attributes
	name = models.CharField(max_length=128)
	brand = models.CharField(max_length=128)
	category = models.CharField(max_length=16, blank=False, null=False) #TODO: make it choice
	origin = CountryField()

	# quantity can be registered as grams, liters... (internal calculus and approximation needed)
	quantity = models.IntegerField()
	quantity_unit = models.CharField(max_length=16) #TODO: make it choice

	# Not displayed, set internally
	eko_score = models.IntegerField(default=0)
	authors = models.TextField()
	last_modified = models.DateTimeField()

	def __str__(self):
		return f'{self.barcode} - {self.name}'
	
	def get_absolute_url(self):
		# view of the item once registered
		return reverse('home')


class PackagingInfo(models.Model):
	# corresponding product:
	product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

	#Displayed in (Creation)
	element = models.CharField(max_length=64)
	material = models.CharField(max_length=255) #TODO: make it choice
	mass = models.IntegerField(null=True, blank=False)
	is_recyclable = models.BooleanField(default=False)
	is_recycled = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.element} : {self.material}({self.mass}g)'
	
