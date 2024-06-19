from django.db import models

# Create your models here.
class Funko(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    collection = models.CharField(max_length=128)
    is_backlight = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name

# modelo creado, sino anda comentar y listo
class Libro(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    editorial = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

class User(models.Model):
    name = models.CharField(max_length=128)
    funkos = models.ManyToManyField(Funko, blank=True)
    libros = models.ManyToManyField(Libro, blank=True)
    
    def __str__(self) -> str:
        return self.name
