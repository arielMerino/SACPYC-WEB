# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext
from sacpyc.models import *

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
		lista_evento=[]
		tabla = TipoEvento.objects.all()
		cantidad = tabla.count()
		for item in range(cantidad):
			lista_evento.append(tabla[item].nombre_tipo_evento)
		self.context["tipos_evento"] = lista_evento
		return render(request,'tipoevento.html',self.context)

	def llamadaTipoEventoAgregar(self,request):
		lista_menu=[]
		tabla = TipoMenu.objects.all()
		cantidad = tabla.count()
		for item in range(cantidad):
			lista_menu.append(tabla[item].nombre_tipo_menu)
		self.context["tipos_menu"] = lista_menu
		return render(request,'tipoeventoAgregar.html',self.context)

	def llamadaTipoEventoEditar(self,request):
		self.context["nombre_evento"] = request.POST.get("seleccion")
		nombre = self.context["nombre_evento"]
		evento = TipoEvento.objects.get(nombre_tipo_evento=nombre)
		menu = TipoMenu.objects.filter(idtipoevento = evento.idtipoevento)
		self.context["nombre_menu"] = menu[0].nombre_tipo_menu
		return render(request,'tipoeventoEditar.html',self.context)

