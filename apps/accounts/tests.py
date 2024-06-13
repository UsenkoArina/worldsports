from django.test import TestCase, Client
from django.urls import reverse
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class AccountViewTests(TestCase):
    def test_signin_view(self):
        # Test the response status code of the sign-in view
        response = self.client.get(reverse('accounts:signin'))
        self.assertEqual(response.status_code, 200)

    def test_registration_view(self):
        # Test the response status code of the registration view
        response = self.client.get(reverse('accounts:registration'))
        self.assertEqual(response.status_code, 200)

class AccountsTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a user for testing purposes
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123',
            birth_date='2000-01-01',
            first_name='testname',
            last_name='testsurname'
        )
        
class SigninViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a user for testing the sign-in functionality
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123',
            first_name='testname',
            last_name='testsurname'
        )

    def test_signin_view_get(self):
        # Test the GET request to the sign-in view
        response = self.client.get(reverse('accounts:signin'))
        self.assertEqual(response.status_code, 200)
        # Check if the correct template is used
        self.assertTemplateUsed(response, 'authentication/signin.html')

    def test_signin_view_post(self):
        # Test the POST request to the sign-in view with user credentials
        data = {
            'username': 'testuser',
            'password': 'password123'
        }
        response = self.client.post(reverse('accounts:signin'), data)
        # Check if the response status code is 302 (redirection after successful login)
        self.assertEqual(response.status_code, 302)
        # Check if the response redirects to the home page of articles
        self.assertRedirects(response, reverse('articles:home'))

