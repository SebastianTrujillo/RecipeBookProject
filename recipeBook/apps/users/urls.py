from django.conf.urls import include, url
from .views import RegisterView, LoginView, LogoutView


urlpatterns = [
    url(r'^registrar/$', RegisterView.as_view(), name='register'),
    url(r'^ingresar/$', LoginView.as_view(), name='login'),
    url(r'^salir/$', LogoutView.as_view(), name='logout'),
]