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
        data = {"username": "usera", "password": self.user_a_pw}
        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        # verifying the redirect
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path, "/")
        # verifyng the status code
        self.assertEqual(status_code, 200)

    def test_user_count(self):
        # verifying that the users have been created
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_invalid_request(self):
        # verifying that a user not logged in can't add go on the edit profile page
        response = self.client.get("/members/edit_profile/", )
        self.assertTrue(response.status_code == 403)

    def test_valid_edit_profile(self):
        """
        Verifying if when a user is logged in, it can access the
        edit profile page
        """
        self.client.login(username=self.user_a.username,
                          password=self.user_a_pw)
        response = self.client.post("/members/edit_profile/",
                                    {"title": "this a valid test"})
        self.assertTrue(response.status_code == 200)

    def test_already_registered_redirection(self):
        """
        Verify the redirection when logged in and accessing registration url
        """
        self.client.login(username=self.user_a.username,
                          password=self.user_a_pw)
        response = self.client.get("/members/register/",
                                   {'title': "valid test"})
        # Check redirection
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

    def test_logout_redirection(self):
        """
        Verify that the user is redirected towards the home page when logged out
        """
        self.client.login(username=self.user_a.username,
                          password=self.user_a_pw)
        response = self.client.get("/members/logout/",
                                   {'title': "valid test"})
        # Check redirection
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')