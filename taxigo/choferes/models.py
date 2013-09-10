#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class vehiculos(models.Model):
	"""Datos generales de los vehiculos"""
	marca = models.CharField(max_length = 50, verbose_name = 'Marca')
	modelo = models.CharField(max_length = 100, verbose_name = 'Modelo')
	placa = models.CharField(max_length = 50, verbose_name = 'Placa')
	numero = models.IntegerField(default = 0, verbose_name = 'Numero de vehiculo')
	adicionales = models.TextField(verbose_name = 'Caracteristicas',help_text = 'Color del carro, rodado de llantas, golpes, etc..')
	usuario = models.ForeignKey(User)
	class Meta:
		verbose_name = u'Control de Vehiculo'
		verbose_name_plural = u'Control de Vehiculos'
	def __unicode__(self):
		return str(self.numero)

class choferes(models.Model):
	"""Datos generales de choferes"""
	DIAS_CHOICES = (
		('L','Lunes'),
		('M','Martes'),
		('X','Miercoles'),
		('J','Jueves'),
		('V','Viernes'),
		('S','Sabado'),
		('D','Domingo'),
	)
	foto = models.ImageField(upload_to = 'fotografias/')
	nombre = models.CharField(max_length = 140, verbose_name = 'Nombre')
	direccion = models.CharField(max_length = 200, verbose_name = 'Direccion')
	telefono = models.CharField(max_length = 20, verbose_name = 'Telefono')
	celular = models.CharField(max_length = 20, verbose_name = 'Celular')
	vehiculoAsig = models.ForeignKey(vehiculos,verbose_name = 'Vehiculo asignado')
	diasTrabaja = models.CharField(max_length = 7, choices = DIAS_CHOICES, verbose_name = 'Dias de trabajo')
	activo = models.BooleanField(default = True, verbose_name = 'Activo')
	usuario = models.ForeignKey(User)
	class Meta:
		verbose_name = u'Control de chofer'
		verbose_name_plural = u'Control de choferes'
	def __unicode__(self):
		return self.nombre

		
