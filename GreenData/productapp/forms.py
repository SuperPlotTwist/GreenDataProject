from .models import Product, PackagingInfo
from django import forms
from .presets import CATEGORIES, UNITS, MATERIALS


class ProductForm(forms.ModelForm):

    category = forms.TypedChoiceField(choices=CATEGORIES)
    quantity_unit = forms.TypedChoiceField(choices=UNITS)

    class Meta:
        model = Product

        fields = [
            'name', 'brand', 'barcode', 'category', 'origin', 'quantity',
            'quantity_unit'
        ]

    def __init__(self, *args, edit_mode=False, **kwargs):
        self.base_fields['barcode'].disabled = edit_mode
        super(ProductForm, self).__init__(*args, **kwargs)


class PackagingInfoForm(forms.ModelForm):

    material = forms.ChoiceField(choices=MATERIALS, widget=forms.Select())

    class Meta:
        model = PackagingInfo

        fields = [
            'element', 'material', 'mass', 'is_recyclable', 'is_recycled'
        ]
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        super(PackagingInfoForm, self).__init__(*args, **kwargs)
        for v_field in self.visible_fields():
            v_field.field.widget.attrs['class'] = 'formset-field'
