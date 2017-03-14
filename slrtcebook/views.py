# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from . forms import *

def home(request):
	if request.user.is_authenticated():
		return render(request, "home.html")
	else:
		return redirect('slrtcebook:register')

# def user_login(request):
#	return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('slrtcebook:home')

class LoginFormView(View):
	form_class = LoginForm
	template_name = 'login.html'

	# display a blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# authenticate user
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('slrtcebook:home')

		return render(request, self.template_name, {'form': form})


class RegisterFormView(View):
	form_class = RegisterForm
	template_name = 'register.html'

	# display a blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			# cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns User object if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:

					login(request, user)
					return redirect('slrtcebook:home')

		return render(request, self.template_name, {'form': form})