from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from .models import RecipeType, Recipe, Comment
from apps.users.models import User
from .forms import RecipeForm, CommentForm
from django.core.urlresolvers import reverse, reverse_lazy


class CreateRecipeView(CreateView):

	form_class = RecipeForm
	template_name = 'create_recipe.html'
	success_url = reverse_lazy('recipes:list_recipe')

	def form_valid(self, form):
		form.instance.creatorUser = self.request.user
		return(super(CreateRecipeView, self).form_valid(form))


class ListRecipeView(TemplateView):

	template_name = 'list_recipe.html'

	def get_context_data(self, **kwargs):
		context = super(ListRecipeView, self).get_context_data(**kwargs)
		context['recipe'] = Recipe.objects.filter(is_enabled = True)
		return(context)


class DetailRecipeView(DetailView):

	context_object_name = 'recipeItem'
	model = Recipe
	template_name = 'detail_recipe.html'

	def get_context_data(self, **kwargs):
		context = super(DetailRecipeView, self).get_context_data(**kwargs)
		pk = Recipe.objects.get(pk = self.kwargs.get('pk'))
		context['recipeComment'] = Comment.objects.filter(recipe = pk)
		return(context)


class EditRecipeView(UpdateView):

    context_object_name = 'recipeItem'
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_recipe.html'
    success_url = reverse_lazy('recipes:list_recipe')

    def form_valid(self, form):
        form.instance.creatorUser = self.request.user
        return(super(EditRecipeView, self).form_valid(form))


class DeleteRecipeView(DeleteView):

    context_object_name = 'recipeItem'
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('recipes:list_recipe')
    

class CreateCommentView(CreateView):

	form_class = CommentForm
	template_name = 'create_comment.html'
	success_url = reverse_lazy('recipes:list_recipe')

	def get_context_data(self, **kwargs):
		context = super(CreateCommentView, self).get_context_data(**kwargs)
		context['recipeItem'] = Recipe.objects.get(pk = self.kwargs.get('pk'))
		return(context)

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.recipe = Recipe.objects.get(pk = self.kwargs.get('pk'))
		return(super(CreateCommentView, self).form_valid(form))