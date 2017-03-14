from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter new username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password'}))

	class Meta:
		model = User
		fields = ['username', 'password']

"""class LoginForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

	class Meta:
		model = User
		fields = ['username', 'password']"""

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))