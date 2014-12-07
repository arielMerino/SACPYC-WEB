# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView

#def home(request):
#	context={'dicc1':'valor dicc 1'}
#	return render(request,'sd/home.html',context)

class Home(TemplateView):
	def __init__(self):
		self.context = {}
		self.context = {'nombre':'','apellido':'','phone':'','email':'','comuna':'','calle':'','dir':'','block':'','dpto':'','fecha':'','duracion':'','invitados':'','nombre':'','email':'','comment':''}
	def inicio(self,request):
		return render(request,'home.html',self.context)

	def llamadaCotizar(self,request):		
		return render(request,'cotizar.html',self.context)

	def llamadaCotizarEv(self,request):
		request.session['nombre'] =request.POST.get('nombre')
		request.session['apellido'] =request.POST.get('apellido')
		request.session['phone'] =request.POST.get('phone')
		request.session['email'] =request.POST.get('email')
		request.session['comuna'] =request.POST.get('comuna')
		request.session['calle'] =request.POST.get('calle')
		request.session['dir'] =request.POST.get('dir')
		request.session['block'] =request.POST.get('blocke')
		request.session['dpto'] =request.POST.get('dpto')
		return render(request,'cotizarEv.html',self.context)

	def llamadaCotizarCat(self,request):
		request.session['fecha'] = request.POST.get('fecha')
		request.session['hora'] = request.POST.get('hora')
		request.session['duracion'] = request.POST.get('duracion')
		request.session['invitados'] = request.POST.get('invitados')

		return render(request, 'cotizarCat.html', self.context)

	def llamadaContacto(self,request):
		print self.context['nombre']
		print self.context['email']
		print self.context['comment']
		return render(request,'contacto.html',self.context)		
		
