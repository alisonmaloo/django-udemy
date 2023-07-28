from django.shortcuts import render


def home(request):
    return render(request, 'receitas/pages/home.html', context={name: 'Alison Matos'})


# Create your views here.
