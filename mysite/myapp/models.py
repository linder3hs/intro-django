from django.db import models

# Tener en cuenta que esto es una clase por ende hay reglas que seguir
# El nombre de mi clase inicia siempre en mayuscula
# Esta clase debe heredar de model.Model
class Person(models.Model):
    # Especificar los atributos de mi clase
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200, default="")
    reference = models.CharField(max_length=200, default="")
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " " + self.address


class PersonProxy(Person):
    class Meta:
        proxy = True

    def get_full_name(self):
        return self.name + " " + self.address

    def get_full_name_and_email(self):
        return self.name + " " + self.address + " " + self.email


class ValidationPersonProxy(Person): 
    class Meta:
        proxy = True

    def checkpassword(self):
        if len(self.password) < 8:
            return False
        else:
            return True

# Como se usa
# from myapp.models import Person
# person = Person(name="Juan", address="Calle 1", email="juan@juan.com")
# person.save()

# Como se usa el proxy
# from myapp.models import PersonProxy
# PersonProxy.objects.get(pk=1).get_full_name() # Juan Calle 1
# PersonProxy.objects.get(pk=1).get_full_name_and_email() # Juan Calle 1 juan@juan.com
