from __future__ import absolute_import, unicode_literals
import os
#from .models import functions_db
#from .models import functions_db
#from django.apps import apps

from celery import Celery
from celery import shared_task
import matplotlib.pyplot as plt
import time
import sympy as sy
import random
#from django.conf import settings
from django.db import connection
#from django.db import models
from datetime import datetime
from celery.utils.log import get_task_logger
#from django.http import HttpResponseRedirect
logger = get_task_logger(__name__)
os.environ['DJANGO_SETTINGS_MODULE'] = 'function_modeling.settings'

#if not settings.configured:
#	settings.configure()


#app = Celery('tasks', backend='amqp', broker='amqp://')
app = Celery('tasks', backend='redis://127.0.0.1:6379/', broker='amqp://admin:admin@127.0.0.1:5672//', include=['dashboard.tasks'])

"""
@app.task
def print_hello():
    print("hello there")

"""
#functions_db = apps.get_model('dashboard', 'functions_db')

global filename

def make_upload_path():

	# Переопределение имени загружаемого файла.
	n1 = random.randint(0,10000)
	n2 = random.randint(0,10000)
	n3 = random.randint(0,10000)
	
	filename = str(n1)+"_"+str(n2)+"_"+str(n3)+".jpg"
	return filename


#try:
@shared_task
def function_img(id, interval, dt, formula):
	try:
		timestamp = int(time.time())
		#print("timestamp =", timestamp)

		interval_s = interval * 86400
		#print("interval_s =", interval_s)
		dt_s = dt * 3600
		#print("dt_s =", dt_s)

		t_min = timestamp - interval_s
		#print("t_min =", t_min)
		t_max = timestamp
		#print("t_max =", t_max)

		global t, y
		k = 0
		t = [t_min]
		y = []
		y_f = sy.sympify(formula, locals={"t": t_min})
		y.append(y_f)

		while k != t_max:
			t_min+=dt_s
			k = t_min
			t.append(k)
			y_f = sy.sympify(formula, locals={"t": k})
			y.append(y_f)
			#print("k =", k)

		#print("t =", t)
		#print("y =", y)

		filename = make_upload_path()
		put = "dashboard/media/"
		result_function = put+filename

		plt.plot(t,y)
		plt.savefig(result_function)
		plt.clf()

		cursor = connection.cursor()
		cursor.execute("UPDATE dashboard_functions_db_table SET result_function = '%s', date_of_processing = '%s' WHERE id = '%d';" % (filename, datetime.now(), id))

	except Exception as e:
		error = str(e)
		cursor = connection.cursor()
		cursor.execute("UPDATE dashboard_functions_db_table SET result_function = '', error = $anystring$%s$anystring$, date_of_processing = '%s' WHERE id = '%d';" % (error, datetime.now(), id))

	#cursor.execute("SELECT functions_db_table FROM function_db SET result_function = '%s' WHERE id = '%d';" % (r, id))
	#row = cursor.fetchone()

	#functions_db.objects.filter(id=id).update(result_function=r)


	#j = functions.objects.get(id=id)
	#j.result_function = put_db+filename
	#j.save(force_update=True)

	#os.rename(initial_path, new_path)
	#car.save(force_update=True)

	#return False
	#return t, y # Если возвращать, то в json. Как? гуглим эту ошибку: kombu.exceptions.EncodeError: Object of type sin is not JSON serializable


#except Exception as e:
 #   url = e
  #  print(url)

#db = {"interval": 7, "dt": 4, "formula": "t+2*t"}

#function_img(interval=7, dt=4, formula="sin(t)")


#plt.plot(y)
#plt.show()
#plt.savefig('foo.png')
