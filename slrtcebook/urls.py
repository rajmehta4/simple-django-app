from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from . import views

app_name = 'slrtcebook'

urlpatterns = [
	url(r'^$', views.home, name='home'),

	url(r'^register/$', views.RegisterFormView.as_view(), name='register'),

	url(r'^login/$', views.LoginFormView.as_view(), name='user_login'),

	url(r'^logout/$', views.logout_view, name='logout'), 

	# url(r'^login/$', views.LoginFormView.as_view(), name='login'),

	# url(r'^login/', views.login),
	# url(r'^(?P<page_type>login)/$', views.login, name='login'),

]