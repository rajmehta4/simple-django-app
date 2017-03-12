# from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request, title='Create a new account on SLRTCE Book'):
	return render(request, "index.html", {'title': title})

def login(request, title='Log in to SLRTCE Book'):
	return render(request, "login.html", {'title': title})