from django.contrib import admin
from models import *

class CourseAdmin(admin.ModelAdmin):
	list_display=('id','name','smalldetails','longdetails','level','tipos','slug',)
	list_filter =('name','smalldetails','longdetails','level',)
	search_fields = ('name','smalldetails',)
	list_editable=('name','smalldetails','longdetails','level',)

class TutorialAdmin(admin.ModelAdmin):
	list_display=('id','name','smalldetails','longdetails','duration','admin_tags','slug','admin_tags',)
	list_filter=('name','duration',)
	search_fields=('name','longdetails',)
	list_editable=('name','smalldetails','longdetails')
	filter_horizontal =('tags',)

class TagAdmin(admin.ModelAdmin):
	list_display=('id','name','smalldetails',)
	search_fields=('name','smalldetails',)
	list_editable=('name','smalldetails',)
	list_filter=('name','smalldetails',)

class TopicAdmin(admin.ModelAdmin):
	list_display=('id','name','duration','contenido','published',)
	search_fields=('name',)
	list_editable=('name','duration',)
	list_filter=('name','duration',)

class ModuleAdmin(admin.ModelAdmin):
	list_display=('id','name',)
	search_fields=('name',)
	list_editable=('name',)
	list_filter=('name',)
	filter_horizontal =('tema',)

class ContentAdmin(admin.ModelAdmin):
	list_display=('id','name','generation',)
	search_fields=('name','generation',)
	list_editable=('name','generation',)
	list_filter=('name','generation',)
	filter_horizontal =('modulo',)	

admin.site.register(Topic, TopicAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Course, CourseAdmin)