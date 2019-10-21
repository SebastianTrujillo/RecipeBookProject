from django import forms
from .models import User


class RegisterForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'avatar', 'username', 'email', 'password')
		widgets = {
			'first_name': forms.TextInput(attrs = {
					'type' : 'text',
					'class' : 'form-control',
					'placeholder' : 'Nombre'
				}),
			'last_name': forms.TextInput(attrs = {
					'type' : 'text',
					'class' : 'form-control',
					'placeholder' : 'Apellido'
				}),
			'avatar': forms.ClearableFileInput(attrs = {
                    'type' : 'file'
                }),
			'username': forms.TextInput(attrs = {
					'type' : 'text',
					'class' : 'form-control',
					'placeholder' : 'Nombre de usuario'
				}),
			'email': forms.TextInput(attrs = {
					'type' : 'email',
					'class' : 'form-control',
					'placeholder' : 'Correo electrónico'
				}),
			'password': forms.TextInput(attrs = {
					'type': 'password',
					'class' : 'form-control',
					'placeholder': 'Contraseña'
				})
		}


class LoginForm(forms.Form):

	username = forms.CharField(max_length = 50, widget = forms.TextInput(attrs = {
			'type': 'text',
			'class' : 'form-control',
			'placeholder': 'Nombre de usuario'
		}))
	password = forms.CharField(max_length = 50, widget = forms.TextInput(attrs = {
			'type': 'password',
			'class' : 'form-control',
			'placeholder': 'Contraseña'
		}))

	def clean(self):
		try:
			user_found = User.objects.filter(username = self.cleaned_data['username']).exists()

			if(not(user_found)):
				self.add_error('username', 'Nombre de usuario no encontrado.')
			else:
				user = User.objects.get(username = self.cleaned_data['username'])
				if(not(user.check_password(self.cleaned_data['password']))):
					self.add_error('password', 'Contraseña incorrecta.')
		except:
			pass