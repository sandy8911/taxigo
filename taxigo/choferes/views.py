#encoding:utf-8
from choferes.models import vehiculos,choferes
from django.shortcuts import render_to_response,get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from forms import addChoferForm,addVehiculoForm
from choferes.models import choferes,vehiculos

def inicio(request):
	chofer = choferes.objects.all()
	template = 'index.html'
	return render(request,template,{
		'choferes':chofer,
		'request':request
	})

@login_required
def addChofer(request):
	'''Agregando un nuevo chofer'''
	if request.POST:
		form = addChoferForm(request.POST)
		if form.is_valid():
			#Creamos el nuevo chofer pero aun no lo guardo
			choferes = form.save(commit = False)
			#Verifico que usuario realizo el registro 
			choferes.usuario = request.user
			#Guardo el nuevo chofer
			choferes.save()
			return HttpResponseRedirect('/')
	else:
		form = addChoferForm()
	template = 'addChofer.html'
	return render_to_response(template,context_instance = RequestContext(request,locals()))

