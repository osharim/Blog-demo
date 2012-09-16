
from django.contrib import admin 							#importamos el admin de django
from demo.apps.ventas.models import cliente,producto		

admin.site.register(cliente)							    #los registramos dentro del admin
admin.site.register(producto)