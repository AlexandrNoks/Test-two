from django.http import HttpResponse
from django.shortcuts import render


def vise_versa(request):
	return render(request, 'index.html' )

def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text})

