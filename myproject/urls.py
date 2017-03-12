from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from slrtcebook import views

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^login/', views.login),
	# url(r'^(?P<page_type>login)/$', views.login, name='login'),

    url(r'^admin/', admin.site.urls, name='admin'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)