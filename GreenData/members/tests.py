from django.test import TestCase

from django.contrib.auth import get_user_model

# Tests for user accounts

User = get_user_model()
class UserTestCase(TestCase):

    def setUp(self):

        # Setting up user_a
        user_a = User(username="usera", email='usera@test.com')
        user_a_pw = 'passwordpassword123'
        self.user_a_pw = user_a_pw
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        self.assertTrue(self.user_a.check_password(self.user_a_pw))
    
    #verifying the urls
    def test_login_url(self):
        login_url = "/members/login/"
        data = {"username":"usera", "password":self.user_a_pw}
        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        # verifying the redirect
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path, "/")
        # verifyng the status code
        self.assertEqual(status_code, 200)
