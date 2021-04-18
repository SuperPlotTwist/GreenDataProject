from .models import Product, PackagingInfo
from django import forms
from .presets import CATEGORIES, UNITS, MATERIALS

class ProductForm(forms.ModelForm):

	category = forms.TypedChoiceField(choices=CATEGORIES)
	quantity_unit = forms.TypedChoiceField(choices=UNITS)

	class Meta:
		model = Product

		fields = [
			'name',
			'brand',
			'barcode',
			'category',
			'origin',
			'quantity',
			'quantity_unit'
		]


class PackagingInfoForm(forms.ModelForm):

	material = forms.ChoiceField(choices=MATERIALS)
	
	class Meta:
		model = PackagingInfo

		fields = [
			'element',
			'material',
			'mass',
			'is_recyclable',
			'is_recycled'
		]
