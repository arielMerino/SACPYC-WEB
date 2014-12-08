# -*- encoding: utf-8 -*-
#controlador
from django.shortcuts import render #para llamar a los template
from django.views.generic import TemplateView
from .models import *
from django.core.mail import EmailMessage

#def home(request):
#	context={'dicc1':'valor dicc 1'}
#	return render(request,'sd/home.html',context)

class Home(TemplateView):
	def __init__(self):
		self.context = {}
		
	def inicio(self,request):
		return render(request,'home.html',self.context)

	def llamadaCotizar(self,request):

		return render(request,'cotizar.html',self.context)

	def llamadaCotizarEv(self,request):
		request.session['nombre'] =request.POST.get('nombre')
		request.session['apellido'] =request.POST.get('apellido')
		request.session['phone'] =request.POST.get('phone')
		request.session['email'] =request.POST.get('email')
		comuna=request.POST.get('comuna')
		calle=request.POST.get('calle')
		dire=request.POST.get('dir')
		blocke=request.POST.get('blocke')
		dpto=request.POST.get('dpto')
		request.session['direccion'] = comuna+' , '+calle+' , '+dire+' , '+blocke+' , '+dpto

		return render(request,'cotizarEv.html',self.context)

	def reload(self,request):
		fecha=request.POST.get('fecha')
		hora=request.POST.get('hora')
		duracion=request.POST.get('duracion')
		invitados=request.POST.get('invitados')
		f = fecha.split('/')
		fecha = f[2]+'-'+f[1]+'-'+f[0]+' '+hora+':'+'00'

		request.session['duracion'] = duracion
		request.session['invitados'] = invitados
		request.session['fecha'] = fecha
		return render(request,'reload.html',self.context)

	def llamadaCotizarCat(self,request):
		if request.POST.get('tipoEvento'):

			idTE = request.POST.get('tipoEvento')
			tE = TipoEvento.objects.get(idtipoevento=idTE)
			self.context['descripcion'] = tE.desripcion_evento
			self.context['tipoEvento'] = request.POST.get('tipoEvento')
			self.context['nombretipoevento'] = tE.nombre_tipo_evento

			a = TipoMenu.objects.filter(idtipoevento=tE)
			cruza = []

			for tipo in a:
				dicc={}
				dicc['idtipomenu'] = tipo.idtipomenu
				dicc['idtipoevento'] = tipo.idtipoevento
				dicc['nombretipomenu'] = tipo.nombre_tipo_menu
				cruza.append(dicc)
			self.context['menus'] = cruza
			request.session['idTipoEvento'] = idTE
			request.session['nombreTipoEvento'] = tE.nombre_tipo_evento

		if request.POST.get('tipoMenu'):
			idTM = request.POST.get('tipoMenu')
			self.context['tipoMenu'] = idTM
			self.context['nombretipomenu'] = TipoMenu.objects.get(idtipomenu=idTM).nombre_tipo_menu
			itemsMenu = ItemMenu.objects.filter(idtipomenu=idTM)
			items=[]
			for entrada in itemsMenu:
				idItem = entrada.iditem.iditem
				item = Item.objects.get(iditem=idItem)
				dicc = {}
				dicc['iditem'] = item.iditem
				dicc['idtipo'] = item.idtipo.idtipo
				dicc['nombreitem'] = item.nombre_item
				dicc['nombretipoitem'] = item.idtipo.nombre_tipo
				items.append(dicc)
			
			tipos = []
			for entrada in items:
				if not entrada['nombretipoitem'] in items:
					tipos.append(entrada['nombretipoitem'])
			self.context['tipos'] = tipos
			self.context['cruzaItems'] = items
			request.session['idTipoMenu'] = idTM
			request.session['nombreTipoMenu'] = self.context['nombretipomenu']

		eventos = TipoEvento.objects.all()
		eventosMostrar=[]
		for evento in eventos:
			if int(evento.visible) == 1:
				dicc={}
				dicc['idtipoevento']=evento.idtipoevento
				dicc['nombretipoevento']=evento.nombre_tipo_evento
				dicc['visible']=1
				dicc['descripcion']=evento.desripcion_evento
				eventosMostrar.append(dicc)

		self.context['eventos']=eventosMostrar

		return render(request, 'cotizarCat.html', self.context)


	def cotizarResumen(self,request):
		print request.session['evento']
		items = request.POST.getlist('items')
		request.session['items'] = items
		arreglo = []
		for item in items:
			arreglo.append(Item.objects.get(iditem=item).nombre_item)
		request.session['nombresItems'] = arreglo
		print ':D'
		print request.session['fecha']

		self.context['nombre'] = request.session['nombre'] 
		self.context['apellido'] = request.session['apellido']
		self.context['phone'] = request.session['phone']
		self.context['email'] = request.session['email']
		self.context['direccion'] = request.session['direccion']
		self.context['fecha'] = request.session['fecha']
		self.context['hora'] = request.session['hora']
		self.context['duracion'] = request.session['duracion']
		self.context['invitados'] = request.session['invitados']
		self.context['idevento'] = request.session['idTipoEvento']
		self.context['nombreevento'] = request.session['nombreTipoEvento']
		self.context['idtipomenu'] = request.session['idTipoMenu']
		self.context['nombretipomenu'] = request.session['nombreTipoMenu']
		self.context['iditems'] = request.session['items']
		self.context['nombresitems'] = request.session['nombresItems']

		return render(request,'cotizarResumen.html',self.context)

	def estado(self,request):
		request.session['codigo'] = None
		request.session['email'] = None
		return render(request,'estado.html',self.context)

	def estadoIn(self,request):
		if (request.POST.get('codigo')==None or request.POST.get('email')==None)and(request.session['codigo']==None or request.session['email']==None):
			self.context['error'] = 'ERROR - debe indicar un código y un correo válido*'
			return render(request,'estado.html',self.context)
		codigo = request.POST.get('codigo')
		email = request.POST.get('email')
		solicitud = SolicitudDeCotizacion.objects.filter(idsolicitudcotizacion=codigo)
		if solicitud.count() > 0:
			if solicitud[0].mail_cliente.mail_cliente == email:
				request.session['codigo'] = codigo
				request.session['email'] = email

				sol = SolicitudDeCotizacion.objects.get(idsolicitudcotizacion=codigo)
				

				return render(request,'estadoIn.html',self.context)
		self.context['error'] = 'ERROR - debe indiar un código y un correo válido*'
		return render(request,'estado.html',self.context)

	def mail(self,request):

		c = Cliente.objects.filter(mail_cliente=request.session['email'])

		if c.count() == 0:
			client = Cliente(mail_cliente=request.session['email'], telefono_cliente=request.session['phone'],nombre_cliente=request.session['nombre'],apellido_cliente=request.session['apellido'])
			client.save()
			c = Cliente.objects.filter(mail_cliente=request.session['email'])


		sol = SolicitudDeCotizacion(estado_solicitud='generada',mail_cliente = c[0],idtipoevento = TipoEvento.objects.get(idtipoevento=request.session['idTipoEvento']),cantidad_asistentes = request.session['invitados'],fecha_tentativa = request.session['fecha'],duracion_tentativa = request.session['duracion'],nombre_evento = request.session['nombreTipoEvento'],direccion_evento = request.session['direccion'])
		sol.save()


		sol = SolicitudDeCotizacion.objects.filter(mail_cliente=request.session['email'])
		arr = []
		for s in sol:
			arr.append(s.idsolicitudcotizacion)
		idsol = max(arr)

		items = request.session['items']

		for item in items:
			sol = SolicitudDeCotizacion.objects.get(idsolicitudcotizacion=idsol)
			i = Item.objects.get(iditem=item)
			print sol
			print i
			it = ItemSolicitudDeCotizacion(iditem=i,idsolicitudcotizacion=sol)
			it.save()

		a = 'Su Solicitud de cotizacion ha sido enviada satisfactoriamente, utilice el codigo de seguridad: '
		b = ' para ver el estado de su cotizaci0n.'
		mensaje = a+ str(idsol) +' y su correo '+' '+request.session['email']+b
		email = EmailMessage('testing',mensaje,to = [request.session['email']])
		email.send()
		
		return render(request,'mail.html',self.context)

	def estadoDel(self,request):
		codigo = request.session['codigo']
		sol = SolicitudDeCotizacion.objects.filter(idsolicitudcotizacion=codigo)
		if sol.count() > 0:
			sol[0].delete()

		return render(request,'estadoIn.html',self.context)

	def llamadaContacto(self,request):
		return render(request,'contacto.html',self.context)		