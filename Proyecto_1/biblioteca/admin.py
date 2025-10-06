from django.contrib import admin

# Register your models here.
from .models import Autor,Biblioteca,Cliente,DatosCliente,Libro

admin.site.register(Autor)
admin.site.register(Biblioteca)
admin.site.register(Cliente)
admin.site.register(DatosCliente)
admin.site.register(Libro)