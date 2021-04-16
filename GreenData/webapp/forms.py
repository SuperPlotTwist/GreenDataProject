from django import forms
from .models import Product, Category

#choices = [('Others', 'Others'), ('Household products', 'Household products'), ('Food products', 'Food products')]
choices = Category.objects.all().values_list('name', 'name')


class AddForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ("product_name", "category", "packaging", "packaging_mass", "author")

		widget = {
			'product_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insert Product\'s name'}),
			'category' : forms.Select(choices=choices, attrs={'class':'form-control'}),
			'packaging' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insert Packaging'}),
			'packaging_mass' : forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Insert Packaging\'s mass'}),
			'author' : forms.Select(attrs={'class':'form-control', 'placeholder': 'Choose Author'}),
		}