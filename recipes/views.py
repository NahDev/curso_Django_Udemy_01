from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(
        request,
        "recipes/home.html",
        context={
            "name": "Chapolim",
        },
    )


def sobre(request):
    return render(request, "me-apague/me_apague.html")


def mensagem(request):
    return HttpResponse("Olha a Palhaço")
