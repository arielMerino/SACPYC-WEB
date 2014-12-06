# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render, render_to_response #para llamar a los template
from django.views.generic import TemplateView
from django.template import RequestContext
from sacpyc.models import Administrador
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
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'agenda.html',self.context)

	def llamadaCompras(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'compras.html',self.context)

	def llamadaCotizarAd(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'cotizarAd.html',self.context)

	def llamadaGarzones(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'garzones.html',self.context)

	def llamadaMenu(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'menu.html',self.context)

	def llamadaNotificaciones(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'notificaciones.html',self.context)

	def llamadaProveedores(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'proveedores.html',self.context)

	def llamadaTipoEvento(self,request):
		self.context['nombre']=request.POST.get('nombre')
		self.context['apellido']=request.POST.get('apellido')
		self.context['correo']=request.POST.get('correo')
		self.context['rol']=request.POST.get('rol')
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'tipoevento.html',self.context)

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