from django.http import HttpResponse
from django.shortcuts import render


def vise_versa(request):
	return render(request, 'index.html' )



