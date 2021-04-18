from django.shortcuts import render, redirect
from django.db import transaction, IntegrityError
from django.forms import modelformset_factory

from django.utils import timezone
import pytz

from .models import Product, PackagingInfo
from .forms import ProductForm, PackagingInfoForm

# Create your views here.


def create_product_view(request, *args, **kwargs):
	ctxt = {}

	PackagingFormSet = modelformset_factory(model=PackagingInfo, form=PackagingInfoForm, max_num=10)

	product_form = ProductForm(request.POST or None)

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
	return render(request, 'create_product.html', ctxt)




def product_detail_view(request, pk='', **kwargs):
	ctxt = {'good_pk': True, 'pk': pk}

	if pk == '': #Invalid pk
		ctxt['good_pk'] = False
		return render(request, 'product_detail2.html', ctxt)

	product = Product.objects.filter(pk=pk)

	# if the barcode value doesn't find a match or if there are several matches
	if len(product) != 1:
		ctxt['good_pk'] = False
		return render(request, 'product_detail2.html', ctxt)
	
	packagings = product[0].packaginginfo_set.all()

	ctxt['product'] = product[0]
	ctxt['packaging'] = packagings
	ctxt['user'] = request.user

	return render(request, 'product_detail2.html', ctxt)
		