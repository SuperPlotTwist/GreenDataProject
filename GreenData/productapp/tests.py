from datetime import datetime
from django.urls.base import reverse
from django.utils import timezone
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Product, PackagingInfo
from .ecoscore import getEcoScore

# Tests for products

User = get_user_model()


class ProductTestCase(TestCase):
    def setUp(self):
        # Setting up user_a
        user_a = User(username="usera", email='usera@test.com')
        user_a_pw = 'passwordpassword123'
        self.user_a_pw = user_a_pw
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a

        # Setting up user_b
        user_b = User.objects.create_user('userb', "userb@test.com",
                                          'passwordazerty')
        user_b.is_active = False
        self.user_b = user_b

        # Setting test product
        prod = Product(barcode=226,
                       name="test",
                       brand="test",
                       category="FOOD",
                       origin='FR',
                       quantity=150,
                       quantity_unit='g',
                       last_modified=timezone.make_aware(datetime(2021, 1, 1)))
        prod.save()

    def test_user_count(self):
        """
        verifying that the users have been created
        """
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_product_count(self):
        """
        Check the number of saved products
        """
        prd_count = Product.objects.all().count()
        self.assertEqual(prd_count, 1)

    def test_duplicate_pk_insertion_handling(self):
        """
        Check the system doesn't add duplicate primary key items
        """
        initial_count = Product.objects.all().count()
        prd2 = Product(barcode=226,
                       name='test',
                       brand='test',
                       category='FOOD',
                       origin='ES',
                       quantity=30,
                       quantity_unit='KG',
                       last_modified=timezone.make_aware(datetime(2020, 1, 2)))
        prd2.save()
        prd_count = Product.objects.all().count()
        self.assertEqual(prd_count, initial_count)

    def test_existing_product_request(self):
        """
        Check the product request when using existing id
        """
        self.client.login(username=self.user_a.username,
                          password=self.user_a_pw)

        response = self.client.get('/product/226', follow=True)
        self.assertEqual(response.context['product'].barcode, '226')
        self.assertEqual(response.status_code, 200)

    def test_product_creation(self):
        """
        Check product insertion
        """
        initial_prd_count = Product.objects.all().count()
        initial_pkg_count = PackagingInfo.objects.all().count()

        self.client.login(username=self.user_a.username,
                          password=self.user_a_pw)

        data_bis = {
            'csrfmiddlewaretoken': [
                'CBOr5gVz4JBcoKEF61EUjt3U7k71WhAADeJM9x4MQ3PcB75JnRSPmny0DOZ1yIFB'
            ],
            'name': ['test'],
            'brand': ['test'],
            'barcode': ['test5'],
            'category': ['FOOD'],
            'origin': ['AF'],
            'quantity': ['100'],
            'quantity_unit': ['G'],
            'packaging_info-0-element': ['aze'],
            'packaging_info-0-material': ['GLASS'],
            'packaging_info-0-mass': ['50'],
            'packaging_info-TOTAL_FORMS': ['1'],
            'packaging_info-INITIAL_FORMS': ['0'],
            'packaging_info-MIN_NUM_FORMS': ['0'],
            'packaging_info-MAX_NUM_FORMS': ['10']
        }

        response = self.client.post(reverse('productapp:add_product'),
                                    data=data_bis)

        # Check product insertion
        self.assertEqual(Product.objects.all().count(), initial_prd_count + 1)
        self.assertEqual(PackagingInfo.objects.all().count(),
                         initial_pkg_count + 1)

        # Check product ecoscore accuracy
        inserted_prd = Product.objects.get(pk='test5')
        self.assertEqual(inserted_prd.eko_score, 35)
        # 1 * 0.7 * 0.5 * 100 (GLASS * not recyclable * not recycled)

    def test_product_wo_packaging_creation(self):
        initial_prd_count = Product.objects.all().count()
        initial_pkg_count = PackagingInfo.objects.all().count()

        self.client.login(username=self.user_a.username,
                          password=self.user_a_pw)

        data_bis = {
            'csrfmiddlewaretoken': [
                'CBOr5gVz4JBcoKEF61EUjt3U7k71WhAADeJM9x4MQ3PcB75JnRSPmny0DOZ1yIFB'
            ],
            'name': ['test'],
            'brand': ['test'],
            'barcode': ['test5'],
            'category': ['FOOD'],
            'origin': ['AF'],
            'quantity': ['100'],
            'quantity_unit': ['G'],
            'packaging_info-TOTAL_FORMS': ['1'],
            'packaging_info-INITIAL_FORMS': ['0'],
            'packaging_info-MIN_NUM_FORMS': ['0'],
            'packaging_info-MAX_NUM_FORMS': ['10']
        }

        try: 
            # Should raise error
            response = self.client.post(reverse('productapp:add_product'),
                                    data=data_bis)
        except:
            response = None
        # Check unsuccessful product insertion
        self.assertIsNone(response)
        self.assertEqual(Product.objects.all().count(), initial_prd_count)
        self.assertEqual(PackagingInfo.objects.all().count(),
                         initial_pkg_count)
