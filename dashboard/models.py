from django.db.models.signals import post_save
from django.db import models
#from django.utils import timezone
from django.conf import settings
from .tasks import *
#from django.utils.timezone import now
from datetime import datetime
#from django.http import HttpResponseRedirect

#from django.db import models
#from ckeditor.fields import RichTextField
#from django.db import settings
#from django.conf import settings

# Create your models here.


class functions_db_table(models.Model):
	#id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	id = models.AutoField(primary_key=True)
	function = models.CharField(max_length=250, blank=True, verbose_name="Функция")
	result_function = models.ImageField(upload_to="images", default=0, verbose_name="График", blank=True, editable=False)
	interval = models.IntegerField(verbose_name="Интервал t, дней", default=0, blank=True, null=True)
	dt = models.IntegerField(verbose_name="Шаг t, часы", default=0, blank=True, null=True)
	date_of_processing = models.DateTimeField(default=datetime.now, verbose_name="Дата обработки", blank=True, editable=False)
	error = models.CharField(max_length=500, blank=True, default=0, editable=False)

	def save(self, *args, **kwargs):
		super(functions_db_table, self).save(*args, **kwargs) #сохранение


def post_save_functions(sender, instance, created, **kwargs):
	id = instance.id
	function = instance.function
	result_function = instance.result_function
	interval = instance.interval
	dt = instance.dt
	date_of_processing = instance.date_of_processing
	#return HttpResponseRedirect('/admin/dashboard/functions_table/')

	#instance.functions.save(force_update=True)
	#kwargs = {"interval": interval, "dt": dt, "formula": function}
	function_img.apply_async(kwargs = {"id": id, "interval": interval, "dt": dt, "formula": function}, countdown=5) # serializer='json',

post_save.connect(post_save_functions, sender=functions_db_table)
	#return HttpResponseRedirect('/admin/dashboard/functions_table/')


		#print("info_new_functions =", info_new_functions)
		#c = Post.objects.filter

class Meta:
		verbose_name_plural = "Функции"
		verbose_name = "Функцию"
		#date_of_processing = ['date_of_processing'] #Сортировка по умолчанию (выбрал по дате)

"""
id - уникальный индетификатор функции
function - функция текстом
result_function - ссылка на картинку
interval - глубина периода моделирования в днях (вводится с клавы) переводим в unixtime
dt - шаг в часах (вводится с клавы) переводим в unixtime
date_of_processing - Дата обработки
"""