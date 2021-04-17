from django.shortcuts import render, redirect
from django.db import transaction, IntegrityError
from django.forms import modelformset_factory

from .models import Product, PackagingInfo
from .forms import ProductForm, PackagingInfoForm

# Create your views here.


def create_product_view(request, *args, **kwargs):
	ctxt = {}

	PackagingFormSet = modelformset_factory(model=PackagingInfo, form=PackagingInfoForm )

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
					product.save
					for pkg in packaging_formset:
						packaging = pkg.save(commit=False)
						packaging.product = product
						packaging.save()
			except IntegrityError:
				raise "Form ERROR"
			product_form = ProductForm()
			packaging_formset = PackagingFormSet(queryset=PackagingInfo.objects.none(), prefix='packaging_info')
			return redirect('/')
	
	ctxt['product_form'] = product_form
	ctxt['packaging_formset'] = packaging_formset
	return render(request, 'create_product.html', ctxt)
