from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^demo/', include('demo.foo.urls')),


    url(r'^' , include('demo.apps.home.urls')) , # va a jalar las urls de nuestra aplicacion home
    url(r'^' , include('demo.apps.ventas.urls')) ,
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)) 
    #levantamos esta url para poder usar estos archivos en nuestro servidor de prueblas DEPLOY 
    #ya cuando se corre con apache o modulos como fastCGI ellos lo hacen automaticamente
)



if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    ) 
