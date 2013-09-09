from choferes.models import vehiculos,choferes
from django.shortcuts import render_to_response,get_object_or_404, render

# Create your views here.

def inicio(request):
	chofer = choferes.objects.all()
	template = 'index.html'
	return render(request,template,{'choferes':chofer,'request':request})
