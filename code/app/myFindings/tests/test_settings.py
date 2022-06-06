import os
from django.test import TestCase
from website.settings import DEBUG, ALLOWED_HOSTS, LOGIN_REDIRECT_URL, \
                             EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
class TestSettings(TestCase):

    def test_secretkey_defined_in_production(self):
        if(not DEBUG):
            result = os.environ.get('SECRET_KEY')
            self.assertNotEqual(result, None)

    def test_emailhostuser_defined(self):
        self.assertNotEqual(EMAIL_HOST_USER, None)

    def test_emailhostpassword_defined(self):
        self.assertNotEqual(EMAIL_HOST_PASSWORD, None)

    def test_login_redirects(self):
        self.assertEqual(LOGIN_REDIRECT_URL, '/')
