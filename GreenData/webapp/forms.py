from django import forms

from django.forms import ModelForm

from .models import Product, Category

#choices = [('Others', 'Others'), ('Household products', 'Household products'), ('Food products', 'Food products')]
choi = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choi:
	choice_list.append(item)

class AddForm(ModelForm):
	category = forms.ChoiceField(choices=choice_list, widget=forms.Select())
	class Meta:
		model = Product
		fields = ["product_name", "category", "packaging", "packaging_mass", "author"]
