from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction, IntegrityError
from django.forms import inlineformset_factory, modelformset_factory

from django.utils import timezone
import pytz

from .models import Product, PackagingInfo
from .forms import ProductForm, PackagingInfoForm
from .ecoscore import getEcoScore

from productapp.presets import ctxt_cat


def create_product_view(request, *args, **kwargs):
	
	# Packaging form manager class
	# max_num is the max number of packagings
	PackagingFormSet = modelformset_factory(model=PackagingInfo, form=PackagingInfoForm, max_num=10)

	# set of product attributes
	product_form = ProductForm(request.POST or None, edit_mode=False)

	# formset object
	packaging_formset = PackagingFormSet(
		request.POST or None,
		queryset=PackagingInfo.objects.none(),
		prefix='packaging_info'
		)

	# If request updates data
	if request.method == 'POST':
		if product_form.is_valid() and packaging_formset.is_valid():
			try:
				with transaction.atomic():

					# Save product data in DB
					product = product_form.save(commit=False)
					product.last_modified = timezone.now()
					#product.author = request.user.username
					product.save()

					for pkg in packaging_formset:
						# Save each packaging
						packaging = pkg.save(commit=False)
						if packaging.element != '':
							packaging.product = product
							packaging.save()
					product.eko_score = getEcoScore(product)
					product.save()
					return redirect('productapp:product_detail', pk=product.pk)
			except:
				raise Exception("Form ERROR")
			
	
	# build the context for template
	ctxt = {}
	ctxt['product_form'] = product_form
	ctxt['packaging_formset'] = packaging_formset
	ctxt['user'] = request.user
	
	return render(request, 'create_product.html', ctxt_cat(ctxt))



def product_detail_view(request, pk='', **kwargs):
	"""
		Display a detailed view of a product, showing all specifications
	"""
	ctxt = {'good_pk': True, 'pk': pk}

	if pk == '': #Invalid pk
		ctxt['good_pk'] = False
		return render(request, 'product_detail2.html', ctxt_cat(ctxt))

	matching_products = Product.objects.filter(pk=pk)

	# if the barcode value doesn't find a match or if there are several matches
	if len(matching_products) != 1:
		ctxt['good_pk'] = False
		return render(request, 'product_detail2.html', ctxt_cat(ctxt))
	
	product = matching_products[0]
	packagings = product.packaginginfo_set.all()

	ctxt['product'] = product
	ctxt['packaging'] = packagings
	ctxt['user'] = request.user

	return render(request, 'product_detail.html', ctxt_cat(ctxt))





def edit_product_view(request, pk=''):
	"""
		Display a view where the user can modify data of a product
	"""
	
	# formset manager class
	PackagingInfoFormSet = inlineformset_factory(Product, PackagingInfo, form=PackagingInfoForm, extra=1, max_num=10, can_delete=True, min_num=1, validate_min=True)

	# Get instance of the product
	prod_instance = get_object_or_404(Product, pk=pk)

	# Instantiate the product formset
	prod_form = ProductForm(request.POST or None, instance=prod_instance, edit_mode=True)

	# Instanciate the packaging formset
	pack_formset = PackagingInfoFormSet(request.POST or None, request.FILES or None, instance=prod_instance)
	
	if prod_form.is_valid() and pack_formset.is_valid():
		product = prod_form.save()
		#product.authors = request.user.name
		product.last_modified = timezone.now()
		product.save()
		for pack_form in pack_formset:
			if not pack_form.is_valid():
				continue
			pkg = pack_form.save()
			if pack_form in pack_formset.deleted_forms:
				pkg.delete()
			else:
				pkg.product = product
				pkg.save()
		product.eko_score = getEcoScore(product)
		product.save()
		return redirect('productapp:product_detail', pk=product.pk)
	ctxt = {}
	ctxt['instance'] = prod_instance
	ctxt['form'] = prod_form
	ctxt['formset'] = pack_formset
	return render(request, 'edit_product.html', ctxt_cat(ctxt))


