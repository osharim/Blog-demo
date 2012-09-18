#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm
from demo.apps.ventas.models import producto

def add_product_view(request):

	info = "datos nuevos"

	if request.method == "POST":

		form = addProductForm(request.POST)
		info = "inicializando"

		if form.is_valid(): #limpiamos los datos y los guardamos
			nombre = form.cleaned_data["nombre"]
			descripcion = form.cleaned_data["descripcion"]

			p = producto()
			p.nombre = nombre
			p.descripcion = descripcion
			p.status = True
			p.save() #Guardamos la informacion en la DB

			info = "Se guardo correctamente los datos"


		else: #GET

			info = "informacion con datos incorrectos"


	form = addProductForm()

	ctx = {'form' : form , "info" : info }

	return render_to_response ( "ventas/addProduct.html" ,ctx , context_instance = RequestContext(request))


#La vista

#La vista se presenta en forma de funciones en Python, su propósito es determinar que datos serán visualizados,
#entre otras cosas más que iremos viendo conforme avanzamos con el curso. El ORM de Django permite escribir código
#Python en lugar de SQL para hacer las consultas que necesita la vista. La vista también se encarga de tareas conocidas
#como el envío de correo electrónico, la autenticación con servicios externos y la validación de datos a través de formularios.
#Lo mas importante a entender con respecto a la vista es que no tiene nada que ver con el estilo de presentación de los datos,
#sólo se encarga de los datos, la presentación es tarea de la plantilla.

#NOTA!!


# La plantilla recibe los datos de la vista y luego los organiza para la presentación al navegador web. Las etiquetas que Django
# usa para las plantillas permiten que sea flexible para los diseñadores del frontend, incluso tiene estructuras de datos como if,
# por por si es necesaria una presentación lógica de los datos, estas estructuras son límitadas para evitar un desorden poniendo cualquier tipo de código Python. 