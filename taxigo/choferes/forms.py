#encoding:utf-8
from django.forms import ModelForm
from django import forms
from choferes.models import choferes,vehiculos

class addChoferForm(ModelForm):
	"""Registro de choferes"""
	class Meta:
		model = choferes
		exclude = ('usuario')

class addVehiculoForm(ModelForm):
	"""Registro de vehiculos"""
	class Meta:
		model = vehiculos
		

