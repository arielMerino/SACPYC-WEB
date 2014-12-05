# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext

# Create your views here.
class Administracion(TemplateView):
	def __init__(self):
		self.context={}
	def llamadaAgenda(self,request):
		return render(request,'agenda.html',self.context)

	def llamadaCompras(self,request):
		return render(request,'compras.html',self.context)

	def llamadaCotizarAd(self,request):
		return render(request,'cotizarAd.html',self.context)

	def llamadaGarzones(self,request):
		return render(request,'garzones.html',self.context)

	def llamadaMenu(self,request):
		return render(request,'menu.html',self.context)

	def llamadaNotificaciones(self,request):
		return render(request,'notificaciones.html',self.context)

	def llamadaProveedores(self,request):
		return render(request,'proveedores.html',self.context)
		
	def llamadaTipoEvento(self,request):
		return render(request,'tipoevento.html',self.context)