from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase, Client


class LoginGETTest(TestCase):
    def setUp(self):
        self.url = reverse('user_login')
        self.response = self.client.get(self.url)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_response_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_login_view_is_rendered(self):
        self.assertTemplateUsed(self.response, 'login.html')
        self.assertTemplateUsed(self.response, 'base.html')

    def test_contains_signup_link(self):
        url = reverse('register')
        self.assertContains(self.response, 'href="' + url + '"')

    def test_contains_forgot_password_link(self):
        url = reverse('password_change')
        self.assertContains(self.response, url)

    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 4)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="password"', 1)


class LoginPostTest(TestCase):
    def setUp(self):
        self.url = reverse('user_login')
        self.user = User.objects.create_user('foo',  'bar')

    def test_empty_password_post_data(self):
        data = {
            'username': self.user.username,
            'password': '',
        }

        response = self.client.post(self.url, data)

        # Assert that the form has error on `password` field.
        error_message = ['This field is required.']
        self.assertFormError(response, 'form', 'password', error_message)

        # Test that the user is not logged in.
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)

        # Test that the template is same.
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'login.html')

        # Test that the redirect does not occur.
        # Redirect shouldn't occur after invalid login.
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 302)

    def test_wrong_user_password_post_data(self):
        data = {
            'username': self.user.username,
            'password': 'foobar',  # Wrong password data
        }
        response = self.client.post(self.url, data)

        # Test that the redirect does not occur.
        # Redirect occurs after successful login.
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 302)

        # Assert that the form has error.
        error_message = 'Please enter a correct username and password. ' 'Note that both fields may be case-sensitive.'
        self.assertFormError(response, 'form', None, error_message)

        # Test that the template is same
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'login.html')

        # Test that the user is not logged in.
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_empty_username_post_data(self):
        data = {
            'username': '',
            'password': 'bababa',
        }
        response = self.client.post(self.url, data)

        # Assert that the form has error.
        error_message = ['This field is required.']
        self.assertFormError(response, 'form', 'username', error_message)

        # Test that the user is not logged in.
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)

        # Test that the template is same
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'login.html')

        # Test that the redirect doesnot occur.
        # Redirect occurs after successful login.
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 302)

    def test_wrong_username_post_data(self):
        data = {
            'username': 'fppnar',
            'password': 'foobar',
        }
        response = self.client.post(self.url, data)

        # Test that the redirect doesnot occur.
        # Redirect occurs after successful login.
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 302)

        # Assert that the form has error.
        error_message = 'Please enter a correct username and password. ' 'Note that both fields may be case-sensitive.'
        self.assertFormError(response, 'form', None, error_message)

        # Test that the template is same
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'login.html')

        # Test that the user is not logged in.
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)


class LogoutTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'hansolo',
            'princessleia'
        )
        self.url = reverse('logout')
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        self.response = self.client.get(self.url)

    def test_logout_user_is_deauthenticated(self):
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)


class SignupGetTest(TestCase):
    def setUp(self):
        self.url = reverse('register')
        self.response = self.client.get(self.url)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_response_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_view_is_rendered(self):
        self.assertTemplateUsed(self.response, 'registration.html')
        self.assertTemplateUsed(self.response, 'base.html')


    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="password"', 2)


class ProfileTest(TestCase):
    def setUp(self) :
        self.c = Client()
        self.user = User.objects.create_user(username="vasya2005",
                                             password="vasya")

    def test_profile_page(self):
        profile_response = self.c.get("/profile/vasya2005/", follow=True)
        self.assertEqual(profile_response.status_code, 200)

