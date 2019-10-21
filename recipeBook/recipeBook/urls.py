from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	url(r'^', include('apps.main.urls', namespace="main")),
	url(r'^', include('apps.users.urls', namespace="users")),
	url(r'^', include('apps.recipes.urls', namespace="recipes")),
    url(r'^admin/', include(admin.site.urls)),
]

if(settings.DEBUG):
	urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    )