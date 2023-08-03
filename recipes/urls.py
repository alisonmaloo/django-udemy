from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]