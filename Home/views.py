from django.shortcuts import render
from django.views.generic import TemplateView,FormView,ListView
from django.shortcuts import render_to_response,get_object_or_404, render 
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseForbidden,Http404
from .models import Course, Tutorial,Tag


def home(request):
	cursos = Course.objects.all()
	template = "index.html"
	return render_to_response(template, locals())

def tutoriales(request):
	tutorial = Tutorial.objects.all()
	template = "tutoriales.html"
	return render_to_response(template,locals())


def curso_view(request, slug):
	curso = get_object_or_404(Course, slug=slug)
	return render(request,'curso-detalles.html',{'curso':curso})

def tutorial_view(request, slug):
	tutorial = get_object_or_404(Tutorial, slug=slug)
	return render(request,'tutorial-detalles.html',{'tutorial':tutorial})

def tutorial_tag(request,name):
	#import ipdb; ipdb.set_trace()
	tutoriales = Tutorial.objects.all()
	tag = get_object_or_404(Tag, name=name)
	tutorial = tutoriales.filter(tags=tag)
	template_name ="tutoriales.html"
	
	return render(request,template_name,{'tutorial':tutorial})
	


