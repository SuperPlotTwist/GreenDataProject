from django.contrib import admin

from .models import Product, PackagingInfo

# Register your models here.

admin.site.register([Product, PackagingInfo])