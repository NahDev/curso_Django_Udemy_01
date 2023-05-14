from recipes.views import home, sobre, mensagem
from django.urls import path
urlpatterns = [
    path("", home),
    path("sobre/", sobre),
    path("mensagem", mensagem)
]
