# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render, render_to_response #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext
from sacpyc.models import *
from django.http import HttpResponse
# Create your views here.
class Administracion(TemplateView):
	def __init__(self):
		self.context={}
	def llamadaAgenda(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			return render(request,'login.html',self.context)
		return render(request,'agenda.html',self.context)

	def llamadaCompras(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			return render(request,'login.html',self.context)
		return render(request,'compras.html',self.context)

	def llamadaCotizarAd(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			return render(request,'login.html',self.context)
		return render(request,'cotizarAd.html',self.context)

	def llamadaGarzones(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			return render(request,'login.html',self.context)
		return render(request,'garzones.html',self.context)

	def llamadaMenu(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			return render(request,'login.html',self.context)
		return render(request,'menu.html',self.context)

	def llamadaNotificaciones(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			return render(request,'login.html',self.context)
		return render(request,'notificaciones.html',self.context)

	def llamadaProveedores(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			return render(request,'login.html',self.context)
		return render(request,'proveedores.html',self.context)

	def llamadaTipoEvento(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			return render(request,'login.html',self.context)
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

	def llamadaLogin(self,request):
		return render(request,'login.html',self.context)

	def validarLogin(self,request):
		self.context['error']=''
		correo = request.POST.get('mail')
		clave = request.POST.get('pass')
		Q = Administrador.objects.filter(correo_admin=correo)
		if Q.count() > 0:
			if Q[0].clave_admin==clave:
				self.context={'correo':correo,'nombre':Q[0].nombre_admin,'apellido':Q[0].apellido,'rol':Q[0].rol}
				return render(request,'agenda.html',self.context)
			else:
				self.context['error']='Usuario o contraseña incorrecta*'
				print 'no'
		else:
			self.context['error']='Usuario o contraseña incorrecta*'
			print 'no'
		return render(request,'login.html',self.context)
