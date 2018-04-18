from django.shortcuts import render, redirect, reverse


def landing (request):
	return render(request, 'store/landing.html')

def products(request):
	return render(request, 'store/products.html')