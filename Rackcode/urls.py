from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'Rackcode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #Navegacion Basica de Rackcode
    url(r'^$','Home.views.home',name='home'),
    url(r'^tutoriales/','Home.views.tutoriales',name='tutoriales'),
    #url(r'^$','Home.views.login',name='home'),
    
    #Tutorilaes Tag
    url(r'^tag/(?P<name>[\w-]+)/','Home.views.tutorial_tag',name='tutoriales_tag'),

    #Tutoril Detalle
    url(r'^tutorial/(?P<slug>[\w-]+)/','Home.views.tutorial_view',name='tutoriales_view'),
    
    #Detalles de Curso
    url(r'^curso/(?P<slug>[\w-]+)/','Home.views.curso_view',name='cursodetails'),
    
    #Detalles de Cursos


    url(r'^admin/', include(admin.site.urls)),
]
