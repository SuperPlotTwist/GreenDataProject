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
	
	element = forms.CharField(required=True, strip=True, widget=forms.TextInput(attrs={'class':'formset-field'}))
	
	material = forms.ChoiceField(choices=MATERIALS, widget=forms.Select(attrs={'class':'formset-field'}))
	
	mass = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'formset-field'}))

	is_recyclable = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'formset-field'}))

	is_recycled = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'formset-field'}))

	class Meta:
		model = PackagingInfo

		fields = [
			'element',
			'material',
			'mass',
			'is_recyclable',
			'is_recycled'
		]

		# mandatory for JS parsing and dynamic packaging number
		widget = {
			'element': forms.TextInput(attrs={'class':'formset-field'}),
			'material': forms.TextInput(attrs={'class':'formset-field'}),
			'mass': forms.TextInput(attrs={'class':'formset-field'}),
			'is_recyclable': forms.TextInput(attrs={'class':'formset-field'}),
			'is_recycled': forms.TextInput(attrs={'class':'formset-field'}),
		}
