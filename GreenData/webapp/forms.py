from django import forms
from django.db.utils import OperationalError
from django.forms import ModelForm

from .models import Product, Category

#choices = [('Others', 'Others'), ('Household products', 'Household products'), ('Food products', 'Food products')]
"""
choi = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choi:
	choice_list.append(item)
"""
class AddForm(ModelForm):
	try:
		choices = [i for i in Category.objects.all().values_list('name', 'name')]
	except OperationalError:
		choices = [('Others', 'Others'), ('Household products', 'Household products'), ('Food products', 'Food products')]
	category = forms.ChoiceField(choices=choices, widget=forms.Select())
	class Meta:
		model = Product
		fields = ["product_name", "category", "packaging", "packaging_mass", "author"]
		
	def __init__(self, *args, **kwargs):
		super(AddForm, self).__init__(*args, **kwargs)
		self.fields['product_name'].widget.attrs['class']='form-control'
		self.fields['category'].widget.attrs['class']='form-control'
		self.fields['packaging'].widget.attrs['class']='form-control'
		self.fields['packaging_mass'].widget.attrs['class']='form-control'
		self.fields['author'].widget.attrs['class']='form-control'