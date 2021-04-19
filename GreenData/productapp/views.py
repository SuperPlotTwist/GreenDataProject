from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction, IntegrityError
from django.forms import inlineformset_factory, modelformset_factory

from django.utils import timezone
import pytz

from .models import Product, PackagingInfo
from .forms import ProductForm, PackagingInfoForm, ProductEditForm

# Create your views here.


def create_product_view(request, *args, **kwargs):
	ctxt = {}

	PackagingFormSet = modelformset_factory(model=PackagingInfo, form=PackagingInfoForm, max_num=10)

	product_form = ProductForm(request.POST or None, edit_mode=False)

	packaging_formset = PackagingFormSet(
		request.POST or None,
		queryset=PackagingInfo.objects.none(),
		prefix='packaging_info'
		)

	if request.method == 'POST':
		if product_form.is_valid() and packaging_formset.is_valid():
			try:
				with transaction.atomic():
					product = product_form.save(commit=False)
					product.last_modified = timezone.now()
					#product.author = request.user.name
					product.save()
					for pkg in packaging_formset:
						packaging = pkg.save(commit=False)
						if packaging.element != '':
							packaging.product = product
							packaging.save()
					
					return redirect('product_detail', pk=product.pk)
			except:
				raise "Form ERROR"
			product_form = ProductForm()
			packaging_formset = PackagingFormSet(queryset=PackagingInfo.objects.none(), prefix='packaging_info')
		else:
			print(product_form.errors, packaging_formset.errors)
	
	ctxt['product_form'] = product_form
	ctxt['packaging_formset'] = packaging_formset
	ctxt['user'] = request.user
	return render(request, 'create_product.html', ctxt)



def product_detail_view(request, pk='', **kwargs):
	"""
		Display a detailed view of a product, showing all specifications
	"""
	ctxt = {'good_pk': True, 'pk': pk}

	if pk == '': #Invalid pk
		ctxt['good_pk'] = False
		return render(request, 'product_detail2.html', ctxt)

	matching_products = Product.objects.filter(pk=pk)

	# if the barcode value doesn't find a match or if there are several matches
	if len(matching_products) != 1:
		ctxt['good_pk'] = False
		return render(request, 'product_detail2.html', ctxt)
	
	product = matching_products[0]
	packagings = product.packaginginfo_set.all()

	ctxt['product'] = product
	ctxt['packaging'] = packagings
	ctxt['user'] = request.user

	return render(request, 'product_detail2.html', ctxt)



PackagingInfoFormSet = inlineformset_factory(Product, PackagingInfo, form=PackagingInfoForm, extra=0, max_num=10)


def edit_product_view(request, pk=''):
	"""
		Display a view where the user can modify data of a product
	"""
	prod_instance = get_object_or_404(Product, pk=pk)
	print(prod_instance	)
	prod_form = ProductForm(request.POST or None, request.FILES or None, instance=prod_instance, edit_mode=True)
	pack_formset = PackagingInfoFormSet(request.POST or None, request.FILES or None, instance=prod_instance)
	if prod_form.is_valid() and pack_formset.is_valid():
		product = form.save()
		product.authors = request.user.name
		product.save()
		for pack_form in pack_formset:
			pkg = pack_form.save()
			pkg.product = product
			pkg.save()
		return redirect('product_detail', pk=product.pk)
	ctxt = {}
	ctxt['instance'] = prod_instance
	ctxt['form'] = prod_form
	ctxt['formset'] = pack_formset
	print("PRINTTTTTTTTT", pack_formset.as_p())
	return render(request, 'edit_product.html', ctxt)





	##################
	ctxt = {'good_pk': True, 'pk': pk}

	matching_products = Product.objects.filter(pk=pk)

	# handle the case of non existent pk
	if len(matching_products) != 1:
		ctxt['good_pk'] = False
		return render(request, 'product_detail2.html', ctxt)
	


	ctxt = {}

	PackagingFormSet = modelformset_factory(model=PackagingInfo, form=PackagingInfoForm, max_num=10)

	product_form = ProductForm(request.POST or None, edit_mode=True)

	packaging_formset = PackagingFormSet(
		request.POST or None,
		queryset=PackagingInfo.objects.none(),
		prefix='packaging_info'
		)

	if request.method == 'POST':
		if product_form.is_valid() and packaging_formset.is_valid():
			try:
				with transaction.atomic():
					product = product_form.save(commit=False)
					product.last_modified = timezone.now()
					#product.author = request.user.name
					product.save()
					for pkg in packaging_formset:
						packaging = pkg.save(commit=False)
						if packaging.element != '':
							packaging.product = product
							packaging.save()
					
					return redirect('product_detail', pk=product.pk)
			except:
				raise "Form ERROR"
			product_form = ProductForm()
			packaging_formset = PackagingFormSet(queryset=PackagingInfo.objects.none(), prefix='packaging_info')
		else:
			print(product_form.errors, packaging_formset.errors)
	
	ctxt['product_form'] = product_form
	ctxt['packaging_formset'] = packaging_formset
	ctxt['user'] = request.user
	return render(request, 'create_product.html', ctxt)
	