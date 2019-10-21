from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings


class TimeStampModel(models.Model):

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class RecipeType(models.Model):

	name = models.CharField(max_length=100)
	slug = models.SlugField(editable=False, max_length=100)

	def save(self, *args, **kwargs):
		if(not(self.id)):
			self.slug = slugify(self.name)
		super(RecipeType, self).save(*args, **kwargs)

	def __str__(self):
		return(self.name)


class Recipe(TimeStampModel):

	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(editable=False)
	recipe_type = models.ForeignKey(RecipeType)
	ingredients = models.TextField()
	instructions = models.TextField()
	recipe_img = models.ImageField(upload_to = 'recipes', null=True, blank=True)
	is_enabled = models.BooleanField(default=True)
	creatorUser = models.ForeignKey(settings.AUTH_USER_MODEL)

	def save(self, *args, **kwargs):
		if(not(self.id)):
			self.slug = slugify(self.name)
		super(Recipe, self).save(*args, **kwargs)

	def __str__(self):
		return(self.name)


class Comment(TimeStampModel):

	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	recipe = models.ForeignKey(Recipe)
	content = models.TextField()

	def __str__(self):
		return ("%s %s" % (self.user.username, self.recipe.name))