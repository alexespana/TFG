import os
from django.test import TestCase
from website.settings import DEBUG, ALLOWED_HOSTS, LOGIN_REDIRECT_URL
class TestSettings(TestCase):

    def test_secretkey_defined_in_production(self):
        if(not DEBUG):
            result = os.environ.get('SECRET_KEY')
            self.assertNotEqual(result, None)

    def test_debug_is_false_in_production(self):
        if(ALLOWED_HOSTS):
            self.assertFalse(DEBUG)
        else:
            self.assertTrue(DEBUG)

    def test_emailhostuser_defined(self):
        result = os.environ.get('EMAIL_HOST_USER')
        self.assertNotEqual(result, None)

    def test_emailhostpassword_defined(self):
        result = os.environ.get('EMAIL_HOST_PASSWORD')
        self.assertNotEqual(result, None)

    def test_login_redirects(self):
        self.assertEqual(LOGIN_REDIRECT_URL, '/')
