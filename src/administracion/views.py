# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext

# Create your views here.

class Agenda(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaAgenda(self,request):
		return render(request,'agenda.html',self.context)

class Compras(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaCompras(self,request):
		return render(request,'compras.html',self.context)

class CotizarAd(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaCotizarAd(self,request):
		return render(request,'cotizarAd.html',self.context)

class Garzones(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaGarzones(self,request):
		return render(request,'garzones.html',self.context)

class Menu(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaMenu(self,request):
		return render(request,'menu.html',self.context)

class Notificaciones(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaNotificaciones(self,request):
		return render(request,'notificaciones.html',self.context)

class Proveedores(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaProveedores(self,request):
		return render(request,'proveedores.html',self.context)

class TipoEvento(TemplateView):
	def __init__(self, valor):
		self.valor = valor
		self.context = {}
	def llamadaTipoEvento(self,request):
		return render(request,'tipoevento.html',self.context)