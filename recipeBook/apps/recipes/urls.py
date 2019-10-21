from django.conf.urls import include, url
from .views import CreateRecipeView, ListRecipeView, DetailRecipeView, EditRecipeView, DeleteRecipeView, CreateCommentView


urlpatterns = [
	url(r'^recipe/new/$', CreateRecipeView.as_view(), name='create_recipe'),
	url(r'^recipe/list/$', ListRecipeView.as_view(), name='list_recipe'),
	url(r'^recipe/list/detail/(?P<pk>\d+)/$', DetailRecipeView.as_view(), name='detail_recipe'),
	url(r'^recipe/list/edit/(?P<pk>\d+)/$', EditRecipeView.as_view(), name='edit_recipe'),
	url(r'^recipe/list/delete/(?P<pk>\d+)/$', DeleteRecipeView.as_view(), name='delete_recipe'),
	url(r'^recipe/list/detail/comment/(?P<pk>\d+)/$', CreateCommentView.as_view(), name='create_comment'),
]