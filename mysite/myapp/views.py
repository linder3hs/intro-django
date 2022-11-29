from django.shortcuts import render
from .models import Person

# Siempre las funciones reciben un request
def index(request):
    people = Person.objects.all()
    # creando un diccionario
    context = { 
      "people": people
    }
    # context es una palabra reservada 
    # si usamos context al momento de pasar nuestro diccionario de datos
    # unicamente hay que usar el lo keys
    return render(request, "index.html", context)
