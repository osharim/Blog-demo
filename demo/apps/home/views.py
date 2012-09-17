#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.models import producto

def index_view(request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))


def about_view(request):
	#vamos a pasar informacino de las vistas al html
	mensaje = "esto es un mensaje desde mi vista"

	ctx = { 'msg' : mensaje}
	#generamos un contexto proque django obtiene la informacion y la parsea

	return render_to_response('home/about.html' ,ctx, context_instance = RequestContext(request))


def productos_view(request):

	prod  = producto.objects.filter(status=True)   # Select *from ventas where status = True
	
	ctx  = { "producto" : prod}						#creamos un contexto y le enviamos el resultado
	return render_to_response('home/productos.html' ,ctx , context_instance =  RequestContext(request) )


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