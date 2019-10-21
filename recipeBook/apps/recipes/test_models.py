from django.test import TestCase
from apps.recipes.models import RecipeType


class SimpleTest(TestCase):

	def setUp(self):
		self.recipeType = RecipeType.objects.create(
			name = 'Receta de Prueba'
		)

	def test_save(self):
		self.assertEqual(self.recipeType.slug, 'receta-de-prueba')