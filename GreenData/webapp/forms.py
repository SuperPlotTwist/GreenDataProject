from django import forms
#from django.forms import ModelForm
from .models import Product, Category

#choices = [('Others', 'Others'), ('Household products', 'Household products'), ('Food products', 'Food products')]
choi = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choi:
	choice_list.append(item)

'''class AddForm(ModelForm):
	class Meta:
		model = Product
		fields = ["product_name", "category", "packaging", "packaging_mass", "author"]
'''

class AddForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ("product_name", "category", "packaging", "packaging_mass", "author", "country")

		widget = {
			'product_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insert Product\'s name'}),
			'category' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
			'packaging' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insert Packaging'}),
			'packaging_mass' : forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Insert Packaging\'s mass'}),
			'author' : forms.Select(attrs={'class':'form-control', 'placeholder': 'Choose Author'}),
		}