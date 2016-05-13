from django.shortcuts import render, redirect
from .forms import CreatePacientForm


def home(request):
	return render(request, 'dashboard.html', {})


def user(request):
	form = CreatePacientForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return render(request, 'success.html', {})
		else:
			print(form.errors)
	return render(request, 'user.html', {})


def waitlist(request):
	return render(request, 'table.html', {})


def appointments(request):
	return render(request, 'tomadehoras.html', {})


def calendar(request):
	return render(request, 'calendario.html', {})


# INICIO LISTAS (POR BORRAR)

def cardiologia(request):
	return render(request, 'listaesperacardiologia.html', {})

def traumatologia(request):
	return render(request, 'listaesperatraumatologia.html', {})


def urologia(request):
	return render(request, 'listaesperaurologia.html', {})


def todas(request):
	return render(request, 'todaslaslistas.html', {})

# TÉRMINO LISTAS