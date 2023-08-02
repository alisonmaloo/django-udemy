from django.shortcuts import render
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Receitas da Regi',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/home.html', context={'name': 'Receitas da Regi',
    })
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Receitas da Regi',
    })