from django.contrib import admin

from .models import *
from django.utils.html import format_html

#from django.db import models
#import useradmin
#from useradmin import ModelAdmin


class CategoryAdmin(admin.ModelAdmin):

	def result_function_img(self, obj):
		#return '<img src="%s"/>' % obj.result_function
		if obj.result_function == "0":
			return format_html("График создаётся")
		elif obj.error != "0":
			return format_html("%s" % (obj.error))
		else:
			return format_html("<img href='/media/%s' src='/media/%s' width='440' height='280' />" % (obj.result_function.name, obj.result_function.name))

		#return '<a href="{0}"><img src="{0}" width = "120" height = "120"></a>'.format(obj.result_function)
	result_function_img.allow_tags = True
	result_function_img.short_description = 'График'


	def date_of_processing_f(self, obj):
		#return '<img src="%s"/>' % obj.result_function
		return format_html("%s" % (obj.date_of_processing))
		#return '<a href="{0}"><img src="{0}" width = "120" height = "120"></a>'.format(obj.result_function)
	date_of_processing_f.allow_tags = True
	date_of_processing_f.short_description = 'Дата обработки'


	list_display = ('function', 'result_function_img', 'interval', 'dt', 'date_of_processing_f')
	#list_display = ('url', 'title', 'admin_image')


admin.site.register(functions_db_table, CategoryAdmin)