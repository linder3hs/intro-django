from django.db import models

# Tener en cuenta que esto es una clase por ende hay reglas que seguir
# El nombre de mi clase inicia siempre en mayuscula
# Esta clase debe heredar de model.Model
class Person(models.Model):
    # Especificar los atributos de mi clase
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
