from .models import Product, PackagingInfo
from django import forms

class ProductForm(forms.ModelForm):

	class Meta:
		model = Product

		fields = [
			'barcode',
			'name',
			'brand',
			'origin',
			'quantity',
			'quantity_unit'
		]


class PackagingInfoForm(forms.ModelForm):
	
	class Meta:
		model = PackagingInfo

		fields = [
			'element',
			'material',
			'mass',
			'is_recyclable',
			'is_recycled'
		]
