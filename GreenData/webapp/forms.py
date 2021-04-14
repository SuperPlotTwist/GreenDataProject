from django import forms
from .models import Product

class AddForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ("product_name", "packaging", "packaging_mass", "author")

		widget = {
			'product_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insert Product\'s name'}),
			'packaging' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insert Packaging'}),
			'packaging_mass' : forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Insert Packaging\'s mass'}),
			'author' : forms.Select(attrs={'class':'form-control', 'placeholder': 'Choose Author'}),
		}