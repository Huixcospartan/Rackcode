from __future__ import unicode_literals
from django.db import models
from django.template import defaultfilters

class Topic (models.Model):
    TIPO = (
    ('v','Video'),
    ('l','Link'),
    ('r','Restringido'),
    ('c','Multimedia'),
    )

    name            = models.CharField(('Tema'),max_length=150)
    duration        = models.CharField(('Duracion'), max_length=5)
    contenido       = models.CharField(('Contenido'),max_length=1, choices=TIPO, default=TIPO)
    published         = models.TimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % (self.name)

class Module(models.Model):
    name            = models.CharField(('Modulo'), max_length=150)
    tema            = models.ManyToManyField(Topic)
    published         = models.TimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "%s" % (self.name)

class Content(models.Model):
    name            = models.CharField(('Contenido'),max_length=150)
    generation      = models.CharField(('Generacion'), max_length=100)
    modulo          = models.ManyToManyField(Module)

    def __unicode__(self):
        return "%s" % (self.name)

class Tag(models.Model):
    name        = models.CharField(('Tag'),max_length = 45)
    smalldetails = models.CharField(('Descripcion Corta'),max_length=400)
    
    def __unicode__(self):
        return "%s" % (self.name)

class Course(models.Model):

    NIVEL = (
    ('b','Basico'),
    ('m','Medio'),
    ('a','Avanzado'),
    )

    TIPO = (
    ('p','Pago'),
    ('e','Exclusivo'),
    ('g','Gratuito'),
    )

    name          	= models.CharField(('Curso'),max_length = 120)
    smalldetails    = models.CharField(('Descripcion Corta'),max_length = 450)
    longdetails 	= models.CharField(('Descripcion Larga'),max_length = 2100)
    level           = models.CharField(('Nivel'),max_length=1, choices=NIVEL, default=NIVEL)
    tipos           = models.CharField(('Tipo'),max_length=1, choices=TIPO, default=TIPO)
    slug            = models.SlugField(('Direccion URL'),max_length=160,editable=False,)
    contenido       = models.ManyToManyField(Content)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Course, self).save(*args, **kwargs)


class Tutorial(models.Model):
    name             = models.CharField(('Tutorial'),max_length=150)
    smalldetails     = models.CharField(('Descripcion Corta'), max_length=450)
    longdetails      = models.CharField(('Descripcion Larga'),max_length=2100)
    duration         = models.TimeField(auto_now_add=True)
    slug             = models.SlugField(('Direccion URL'),max_length=160,editable=False,)
    tags             = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.name

    def admin_tags(self):
        return self.tags.all()

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Tutorial, self).save(*args, **kwargs)

