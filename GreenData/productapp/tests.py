from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Product

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
        user_b = User.objects.create_user('userb', "userb@test.com", 'passwordazerty')
        user_b.is_active = False
        self.user_b = user_b

    def test_user_count(self):
        # verifying that the users have been created
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    """def test_invalid_request(self):
        # verifying that a user not logged in can't add go on the edit profile page
        response = self.client.post("/members/edit_profile/", {"title":"this is a valid test"})
        print(response.status_code)
        self.assertTrue(response.status_code!=200)"""

    def test_valid_edit_profile(self):
        """
        Verifying if when a user is logged in, it can access the
        edit profile page
        """
        self.client.login(username=self.user_a.username, password=self.user_a_pw)
        response = self.client.post("/members/edit_profile/", {"title":"this a valid test"})
        print(response.status_code)
        self.assertTrue(response.status_code==200)
