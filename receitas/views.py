from django.shortcuts import render


def home(request):
    return render(request, 'receitas/home.html', context={name: 'Alison Matos'})


# Create your views here.
