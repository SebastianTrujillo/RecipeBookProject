from django import forms
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name', 'recipe_type', 'ingredients', 'instructions', 'recipe_img')
        exclude = ('is_enabled','created','modified')
        widgets = {
            'name': forms.TextInput(attrs = {
                    'type' : 'text',
                    'class': 'form-control'
                }),
            'recipe_type': forms.Select(attrs = {
                    'class': 'form-control',
                    'name': 'account'
                }),
            'ingredients': forms.Textarea(attrs = {
                    'type' : 'text',
                    'class': 'form-control',
                    'rows': '3'
                }),
            'instructions': forms.Textarea(attrs = {
                    'type' : 'text',
                    'class': 'form-control',
                    'rows': '3'
                }),
            'recipe_img': forms.ClearableFileInput(attrs = {
                    'type' : 'file'
                })
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs = {
                    'type' : 'text',
                    'class': 'form-control',
                    'rows': '3'
                })
        }