from django.test import TestCase
from apps.users.models import User


class SimpleTest(TestCase):

	def setUp(self):
		self.user = User.objects.create(
			username = 'prueba',
			email = 'prueba@prueba.com',
			password = 'prueba',
		)

	def test_get_short_name(self):
		self.assertEqual(self.user.get_short_name(), 'prueba')