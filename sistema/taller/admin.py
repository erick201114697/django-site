from django.contrib import admin
from .models import Cliente, Vehiculo, Servicio, Cine, Sala, Fila, Pelicula

admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Servicio)
admin.site.register(Cine)
admin.site.register(Sala)
admin.site.register(Fila)
admin.site.register(Pelicula)
