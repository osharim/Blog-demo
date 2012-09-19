from django.db import models
# sudo apt-get install python-mysqldb install on linux

#------------------------------------------------------------------------------------------------------
"""#El modelo define los datos almacenados, se encuentra en forma de clases de Python,
#cada tipo de dato que debe ser almacenado se encuentra en una variable con ciertos 
#parametros, posee metodos tambien. Todo esto permite indicar y controlar el comportamiento de los datos. """

class cliente(models.Model):  				#hereda de models para modelar la DB
	nombre  				= models.CharField(max_length=200) 		#char maxima 200 caracteres
	apellidos				= models.CharField(max_length=200) 
	status					= models.BooleanField(default=True)	 #tipo-->Bololean campo-->Field


	def __unicode__(self):	#para que regrese el nombre y apellidos en el admin de django
		nombreCompleto = "%s %s "% (self.nombre , self.apellidos)
		return nombreCompleto


class producto(models.Model):
	nombre 					= models.CharField(max_length=100)
	descripcion				= models.TextField(max_length=300)
	status					= models.BooleanField(default=True)

	def __unicode__(self): #para que cuando se construya en el admin ponga el nombre del producto
		return self.nombre

"""#ahora para que el admin lo pueda registrar agregamos un archivo admin.py y lo editamos
#ahi vamos a importar el django.contrib que tiene el admin de django
"""
