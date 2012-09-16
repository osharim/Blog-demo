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