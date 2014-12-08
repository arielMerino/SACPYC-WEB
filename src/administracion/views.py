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
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'agenda.html',self.context)

	def llamadaCompras(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'compras.html',self.context)

	def llamadaCotizarAd(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'cotizarAd.html',self.context)

	def llamadaGarzones(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		garzones = Garzon.objects.all()
		listaGarzones = []
		for i in range(garzones.count()):
			dicc={}
			dicc['nombre']=garzones[i].nombre_garzon
			dicc['apellido']=garzones[i].apellido_garzon
			dicc['correo']=garzones[i].mail_garzon
			dicc['telefono']=garzones[i].telefono_garzon
			listaGarzones.append(dicc)
		self.context['garzones']=listaGarzones
		print len(self.context['garzones'])
		for a in self.context['garzones']:
			print a['nombre'].encode('utf-8')+' '+a['apellido'].encode('utf-8')+'; '+a['correo'].encode('utf-8')+'; '+str(a['telefono'])
		return render(request,'garzones.html',self.context)

	def crearGarzon(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		self.context['correoG']=request.POST.get('correo_garzon')

		return render(request,'garzonesCrear.html',self.context)

	def validarCrearGarzon(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		correo = request.POST.get('correo_garzon')
		nombre = request.POST.get('nombre_garzon')
		apellido = request.POST.get('apellido_garzon')
		telefono = request.POST.get('telefono_garzon')
		garzon = Garzon(mail_garzon=correo, nombre_garzon=nombre, apellido_garzon=apellido,telefono_garzon=telefono)
		garzon.save()

		garzones = Garzon.objects.all()
		listaGarzones = []
		for i in range(garzones.count()):
			dicc={}
			dicc['nombre']=garzones[i].nombre_garzon
			dicc['apellido']=garzones[i].apellido_garzon
			dicc['correo']=garzones[i].mail_garzon
			dicc['telefono']=garzones[i].telefono_garzon
			listaGarzones.append(dicc)
		self.context['garzones']=listaGarzones

		return render(request,'garzones.html',self.context)

	def eliminarGarzon(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		correo=request.POST['correo_garzon']

		garzon = Garzon.objects.get(mail_garzon=correo)
		garzon.delete()

		garzones = Garzon.objects.all()
		listaGarzones = []
		for i in range(garzones.count()):
			dicc={}
			dicc['nombre']=garzones[i].nombre_garzon
			dicc['apellido']=garzones[i].apellido_garzon
			dicc['correo']=garzones[i].mail_garzon
			dicc['telefono']=garzones[i].telefono_garzon
			listaGarzones.append(dicc)
		self.context['garzones']=listaGarzones

		return render(request,'garzones.html',self.context)

	def editarGarzon(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		correo=request.POST.get('correo_garzon')
		garzon=Garzon.objects.get(mail_garzon=correo)
		self.context['correoG']=correo
		self.context['nombreG']=garzon.nombre_garzon
		self.context['apellidoG']=garzon.apellido_garzon
		self.context['telefonoG']=garzon.telefono_garzon
		return render(request,'garzonesEd.html',self.context)

	def validarGarzon(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		correoAntiguo = request.POST.get('correo_garzon_a')
		correo = request.POST.get('correo_garzon')
		nombre = request.POST.get('nombre_garzon')
		apellido = request.POST.get('apellido_garzon')
		telefono = request.POST.get('telefono_garzon')

		garzon = Garzon.objects.get(mail_garzon=correoAntiguo)
		garzon.nombre_garzon=nombre
		garzon.apellido_garzon=apellido
		garzon.mail_garzon=correo
		garzon.telefono_garzon=telefono
		garzon.save()

		garzones = Garzon.objects.all()
		listaGarzones = []
		for i in range(garzones.count()):
			dicc={}
			dicc['nombre']=garzones[i].nombre_garzon
			dicc['apellido']=garzones[i].apellido_garzon
			dicc['correo']=garzones[i].mail_garzon
			dicc['telefono']=garzones[i].telefono_garzon
			listaGarzones.append(dicc)
		self.context['garzones']=listaGarzones

		return render(request,'garzones.html',self.context)

	def adminIngredientes(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		ingredientes = Ingrediente.objects.all()
		listaIngredientes = []

		for tipo in ingredientes:
			dicc = {}
			dicc["idI"] = tipo.idingrediente
			dicc["nombreIng"] = tipo.nombre_ingrediente
			dicc["stockAct"] = tipo.stock_ingrediente
			dicc["stockMin"] = tipo.stock_minimo_ingrediente
			listaIngredientes.append(dicc)
		self.context["lista_ingredientes"] = listaIngredientes
		return render(request,'ingredientes.html',self.context)

	def llamadaItem(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		items = Item.objects.all()
		tipositem = TipoItem.objects.all()

		listaItems = []
		listaTipos = []

		for tipo in tipositem:
			dicc = {}
			contador = 0
			dicc['idT'] = tipo.idtipo
			dicc['nombreT'] = tipo.nombre_tipo
			for item in items:
				if item.idtipo == tipo:
					contador+=1
			dicc['cantidadT'] = contador
			listaTipos.append(dicc)

		for item in items:
			dicc = {}
			dicc['idI'] = item.iditem
			dicc['idT'] = item.idtipo
			dicc['idTstr'] = item.idtipo.nombre_tipo
			dicc['nombreI'] = item.nombre_item
			dicc['cantidadIn'] = 0
			listaItems.append(dicc)

		self.context['tiposItem'] = listaTipos
		self.context['items'] = listaItems

		return render(request,'item.html',self.context)

	def crearIngrediente(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		ingredientes = Ingrediente.objects.all()
		listaIngredientes = []

		for tipo in ingredientes:
			dicc = {}
			dicc["idI"] = tipo.idingrediente
			dicc["nombreIng"] = tipo.nombre_ingrediente
			dicc["stockAct"] = tipo.stock_ingrediente
			dicc["stockMin"] = tipo.stock_minimo_ingrediente
			listaIngredientes.append(dicc)
		self.context["lista_ingredientes"] = listaIngredientes
		return render(request,'ingredientesAd.html',self.context)

	def validarCrearIngrediente(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		nombreIng = request.POST.get('nombreIng')
		stockMin = request.POST.get('stockMin')
		stockAct = request.POST.get('stockAct')
		ingrediente = Ingrediente(nombre_ingrediente=nombreIng, stock_ingrediente=stockAct, stock_minimo_ingrediente= stockMin)
		ingrediente.save()

		ingredientes = Ingrediente.objects.all()
		listaIngredientes = []

		for tipo in ingredientes:
			dicc = {}
			dicc["idI"] = tipo.idingrediente
			dicc["nombreIng"] = tipo.nombre_ingrediente
			dicc["stockAct"] = tipo.stock_ingrediente
			dicc["stockMin"] = tipo.stock_minimo_ingrediente
			listaIngredientes.append(dicc)
		self.context["lista_ingredientes"] = listaIngredientes
		return render(request,'ingredientes.html',self.context)

	def editarIngrediente(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		idI = request.POST.get('ingr')
		ingrediente = Ingrediente.objects.get(idingrediente=idI)
		self.context['idingr'] = idI
		self.context['nombre_ingrediente'] = ingrediente.nombre_ingrediente
		self.context['stockMin'] = ingrediente.stockMin
		self.context['stockAct'] = ingrediente.stockAct

		ingredientes = Ingrediente.objects.all()
		listaIngredientes = []

		for tipo in ingredientes:
			dicc = {}
			dicc["idI"] = tipo.idingrediente
			dicc["nombreIng"] = tipo.nombre_ingrediente
			dicc["stockAct"] = tipo.stock_ingrediente
			dicc["stockMin"] = tipo.stock_minimo_ingrediente
			listaIngredientes.append(dicc)
		self.context["lista_ingredientes"] = listaIngredientes
		return render(request,'ingredientesE.html',self.context)

	def crearItem(self,request):
		items = Item.objects.all()
		tipositem = TipoItem.objects.all()

		listaItems = []
		listaTipos = []

		for tipo in tipositem:
			dicc = {}
			contador = 0
			dicc['idT'] = tipo.idtipo
			dicc['nombreT'] = tipo.nombre_tipo
			for item in items:
				if item.idtipo == tipo:
					contador+=1
			dicc['cantidadT'] = contador
			listaTipos.append(dicc)

		for item in items:
			dicc = {}
			dicc['idI'] = item.iditem
			dicc['idT'] = item.idtipo
			dicc['idTstr'] = item.idtipo.nombre_tipo
			dicc['nombreI'] = item.nombre_item
			dicc['cantidadIn'] = 0
			listaItems.append(dicc)

		self.context['tiposItem'] = listaTipos
		self.context['items'] = listaItems

		return render(request,'itemAd.html',self.context)
	def validarEditarItem(self,request):

		iditem = request.session['iditem']
		nombre = request.POST.get('nombreI')
		idtipo = request.POST.get('tipoI')

		listaItems = Item.objects.filter(nombre_item=nombre)
		if listaItems.count() == 1:
			print listaItems[0].iditem
			print iditem
			if int(listaItems[0].iditem) == int(iditem):
				
				item = Item.objects.get(iditem=iditem)
				tipo = TipoItem.objects.get(idtipo=idtipo)

				item.nombre_item=nombre
				item.idtipo = tipo
				item.save()

				items = Item.objects.all()
				tipositem = TipoItem.objects.all()

				listaItems = []
				listaTipos = []

				for tipo in tipositem:
					dicc = {}
					contador = 0
					dicc['idT'] = tipo.idtipo
					dicc['nombreT'] = tipo.nombre_tipo
					for item in items:
						if item.idtipo == tipo:
							contador+=1
					dicc['cantidadT'] = contador
					listaTipos.append(dicc)

				for item in items:
					dicc = {}
					dicc['idI'] = item.iditem
					dicc['idT'] = item.idtipo
					dicc['idTstr'] = item.idtipo.nombre_tipo
					dicc['nombreI'] = item.nombre_item
					dicc['cantidadIn'] = 0
					listaItems.append(dicc)

				self.context['tiposItem'] = listaTipos
				self.context['items'] = listaItems

				return render(request,'item.html',self.context)

		if listaItems.count() > 0:

			self.context['error'] = 'ERROR - el nombre selsccionado ya existe*'

			item = Item.objects.get(iditem=iditem)
			self.context['iditem'] = iditem
			self.context['idtipo'] = item.idtipo.idtipo
			self.context['nombre_item'] = item.nombre_item
			self.context['tipoItem'] = item.idtipo.nombre_tipo

			items = Item.objects.all()
			tipositem = TipoItem.objects.all()

			listaItems = []
			listaTipos = []

			for tipo in tipositem:
				dicc = {}
				contador = 0
				dicc['idT'] = tipo.idtipo
				dicc['nombreT'] = tipo.nombre_tipo
				for item in items:
					if item.idtipo == tipo:
						contador+=1
				dicc['cantidadT'] = contador
				listaTipos.append(dicc)

			for item in items:
				dicc = {}
				dicc['idI'] = item.iditem
				dicc['idT'] = item.idtipo
				dicc['idTstr'] = item.idtipo.nombre_tipo
				dicc['nombreI'] = item.nombre_item
				dicc['cantidadIn'] = 0
				listaItems.append(dicc)

			self.context['tiposItem'] = listaTipos
			self.context['items'] = listaItems

			return render(request,'itemUp.html',self.context)

		item = Item.objects.get(iditem=iditem)
		tipo = TipoItem.objects.get(idtipo=idtipo)

		item.nombre_item=nombre
		item.idtipo = tipo
		item.save()

		items = Item.objects.all()
		tipositem = TipoItem.objects.all()

		listaItems = []
		listaTipos = []

		for tipo in tipositem:
			dicc = {}
			contador = 0
			dicc['idT'] = tipo.idtipo
			dicc['nombreT'] = tipo.nombre_tipo
			for item in items:
				if item.idtipo == tipo:
					contador+=1
			dicc['cantidadT'] = contador
			listaTipos.append(dicc)

		for item in items:
			dicc = {}
			dicc['idI'] = item.iditem
			dicc['idT'] = item.idtipo
			dicc['idTstr'] = item.idtipo.nombre_tipo
			dicc['nombreI'] = item.nombre_item
			dicc['cantidadIn'] = 0
			listaItems.append(dicc)

		self.context['tiposItem'] = listaTipos
		self.context['items'] = listaItems

		return render(request,'item.html',self.context)

	def editarItem(self,request):
		idI = request.POST.get('item')

		request.session['iditem'] = idI

		item = Item.objects.get(iditem=idI)
		self.context['iditem'] = idI
		self.context['idtipo'] = item.idtipo.idtipo
		self.context['nombre_item'] = item.nombre_item
		self.context['tipoItem'] = item.idtipo.nombre_tipo

		items = Item.objects.all()
		tipositem = TipoItem.objects.all()

		listaItems = []
		listaTipos = []

		for tipo in tipositem:
			dicc = {}
			contador = 0
			dicc['idT'] = tipo.idtipo
			dicc['nombreT'] = tipo.nombre_tipo
			for item in items:
				if item.idtipo == tipo:
					contador+=1
			dicc['cantidadT'] = contador
			listaTipos.append(dicc)
			print dicc['idT']

		for item in items:
			dicc = {}
			dicc['idI'] = item.iditem
			dicc['idT'] = item.idtipo
			dicc['idTstr'] = item.idtipo.nombre_tipo
			dicc['nombreI'] = item.nombre_item
			dicc['cantidadIn'] = 0
			listaItems.append(dicc)

		self.context['tiposItem'] = listaTipos
		self.context['items'] = listaItems

		return render(request,'itemUp.html',self.context)


	def eliminarItem(self,request):
		item = request.POST.get('item')
		q = Item.objects.get(iditem=item)
		q.delete()
		
		items = Item.objects.all()
		tipositem = TipoItem.objects.all()

		listaItems = []
		listaTipos = []

		for tipo in tipositem:
			dicc = {}
			contador = 0
			dicc['idT'] = tipo.idtipo
			dicc['nombreT'] = tipo.nombre_tipo
			for item in items:
				if item.idtipo == tipo:
					contador+=1
			dicc['cantidadT'] = contador
			listaTipos.append(dicc)

		for item in items:
			dicc = {}
			dicc['idI'] = item.iditem
			dicc['idT'] = item.idtipo
			dicc['idTstr'] = item.idtipo.nombre_tipo
			dicc['nombreI'] = item.nombre_item
			dicc['cantidadIn'] = 0
			listaItems.append(dicc)

		self.context['tiposItem'] = listaTipos
		self.context['items'] = listaItems

		return render(request,'item.html',self.context)
		return render(request,'item.html',self.context)


	def validarCrearItem(self,request):
		nombreI = request.POST.get('nombreI')
		tipoI = request.POST.get('tipoI')
		idtipo = TipoItem.objects.get(idtipo=tipoI)
		item = Item(nombre_item=nombreI,idtipo=idtipo)
		item.save()

		items = Item.objects.all()
		tipositem = TipoItem.objects.all()

		listaItems = []
		listaTipos = []

		for tipo in tipositem:
			dicc = {}
			contador = 0
			dicc['idT'] = tipo.idtipo
			dicc['nombreT'] = tipo.nombre_tipo
			for item in items:
				if item.idtipo == tipo:
					contador+=1
			dicc['cantidadT'] = contador
			listaTipos.append(dicc)

		for item in items:
			dicc = {}
			dicc['idI'] = item.iditem
			dicc['idT'] = item.idtipo
			dicc['idTstr'] = item.idtipo.nombre_tipo
			dicc['nombreI'] = item.nombre_item
			dicc['cantidadIn'] = 0
			listaItems.append(dicc)

		self.context['tiposItem'] = listaTipos
		self.context['items'] = listaItems

		return render(request,'item.html',self.context)

	def crearTipoItem(self,request):
		return render(request,'tipoItemAd.html',self.context)

	def editarTipoItem(self,request):
		idT = request.POST.get('tipoI')
		tipo = TipoItem.objects.get(idtipo=idT)

		self.context['idT']=idT
		self.context['nombreT']=tipo.nombre_tipo
		request.session['idT'] = idT

		return render(request,'tipoItemEditar.html',self.context)

	def eliminarTipoItem(self,request):
		idT = request.POST.get('tipoI')
		tipo = TipoItem.objects.get(idtipo=idT)
		tipo.delete()

		items = Item.objects.all()
		tipositem = TipoItem.objects.all()

		listaItems = []
		listaTipos = []

		for tipo in tipositem:
			dicc = {}
			contador = 0
			dicc['idT'] = tipo.idtipo
			dicc['nombreT'] = tipo.nombre_tipo
			for item in items:
				if item.idtipo == tipo:
					contador+=1
			dicc['cantidadT'] = contador
			listaTipos.append(dicc)

		for item in items:
			dicc = {}
			dicc['idI'] = item.iditem
			dicc['idT'] = item.idtipo
			dicc['idTstr'] = item.idtipo.nombre_tipo
			dicc['nombreI'] = item.nombre_item
			dicc['cantidadIn'] = 0
			listaItems.append(dicc)

		self.context['tiposItem'] = listaTipos
		self.context['items'] = listaItems

		return render(request,'redirect.html',self.context)

	def validarCrearTipoItem(self,request):
		nombreT = request.POST.get('nombreT')

		tiposI = TipoItem.objects.filter(nombre_tipo=nombreT)
		if tiposI.count() > 0:
			items = Item.objects.all()
			tipositem = TipoItem.objects.all()

			listaItems = []
			listaTipos = []

			for tipo in tipositem:
				dicc = {}
				contador = 0
				dicc['idT'] = tipo.idtipo
				dicc['nombreT'] = tipo.nombre_tipo
				for item in items:
					if item.idtipo == tipo:
						contador+=1
				dicc['cantidadT'] = contador
				listaTipos.append(dicc)

			for item in items:
				dicc = {}
				dicc['idI'] = item.iditem
				dicc['idT'] = item.idtipo
				dicc['idTstr'] = item.idtipo.nombre_tipo
				dicc['nombreI'] = item.nombre_item
				dicc['cantidadIn'] = 0
				listaItems.append(dicc)

			self.context['tiposItem'] = listaTipos
			self.context['items'] = listaItems
			self.context['error'] = 'ERROR - El tipo de ítem ya ue ingresado*'
			return render(request,'tipoItemAd.html',self.context)

		tipoItem = TipoItem(nombre_tipo=nombreT)
		tipoItem.save()

		items = Item.objects.all()
		tipositem = TipoItem.objects.all()

		listaItems = []
		listaTipos = []

		for tipo in tipositem:
			dicc = {}
			contador = 0
			dicc['idT'] = tipo.idtipo
			dicc['nombreT'] = tipo.nombre_tipo
			for item in items:
				if item.idtipo == tipo:
					contador+=1
			dicc['cantidadT'] = contador
			listaTipos.append(dicc)

		for item in items:
			dicc = {}
			dicc['idI'] = item.iditem
			dicc['idT'] = item.idtipo
			dicc['idTstr'] = item.idtipo.nombre_tipo
			dicc['nombreI'] = item.nombre_item
			dicc['cantidadIn'] = 0
			listaItems.append(dicc)

		self.context['tiposItem'] = listaTipos
		self.context['items'] = listaItems

		return render(request,'item.html',self.context)

	def validarEditarTipoItem(self,request):
		idT = request.session['idT']
		nombreT = request.POST.get('nombreT')
		request.session['idT'] = None

		original = TipoItem.objects.get(idtipo=idT)
		nombreOr = original.nombre_tipo
		listaMatch = TipoItem.objects.filter(nombre_tipo=nombreT)

		if listaMatch.count() > 0 and nombreT!=nombreOr:
			self.context['error'] = 'ERROR - el nombre ya ha sido utilizado*'

			tipo = TipoItem.objects.get(idtipo=idT)

			self.context['idT']=idT
			self.context['nombreT']=nombreOr
			request.session['idT'] = idT

			return render(request,'tipoItemEditar.html',self.context)
		else:
			actualizado = TipoItem.objects.get(idtipo=idT)
			actualizado.nombre_tipo = nombreT
			actualizado.save()

		items = Item.objects.all()
		tipositem = TipoItem.objects.all()

		listaItems = []
		listaTipos = []

		for tipo in tipositem:
			dicc = {}
			contador = 0
			dicc['idT'] = tipo.idtipo
			dicc['nombreT'] = tipo.nombre_tipo
			for item in items:
				if item.idtipo == tipo:
					contador+=1
			dicc['cantidadT'] = contador
			listaTipos.append(dicc)

		for item in items:
			dicc = {}
			dicc['idI'] = item.iditem
			dicc['idT'] = item.idtipo
			dicc['idTstr'] = item.idtipo.nombre_tipo
			dicc['nombreI'] = item.nombre_item
			dicc['cantidadIn'] = 0
			listaItems.append(dicc)

		self.context['tiposItem'] = listaTipos
		self.context['items'] = listaItems

		return render(request,'item.html',self.context)

	def llamadaNotificaciones(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'notificaciones.html',self.context)

	def llamadaProveedores(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		ProvI = ProveedorIngrediente.objects.all()
		ProvU = ProveedorUtensilio.objects.all()
		proveedores = []
		for prov in ProvI:
			proveedor = {}
			proveedor['id']=prov.idproveedoringrediente
			proveedor['nombre']=prov.nombre_proveedor_ingrediente
			proveedor['telefono']=prov.telefono_proveedor_ingrediente
			proveedor['direccion']=prov.direccion_proveedor_ingrediente
			proveedor['tipo']='ingredientes'
			proveedores.append(proveedor)

		for prov in ProvU:
			proveedor = {}
			proveedor['id']=prov.idproveedorutensilio
			proveedor['nombre']=prov.nombre_proveedor_utensilio
			proveedor['telefono']=prov.telefono_proveedor_utensilio
			proveedor['direccion']=prov.direccion_proveedor_utensilio
			proveedor['tipo']='utensilios'
			proveedores.append(proveedor)

		self.context['proveedores']=proveedores
		return render(request,'proveedores.html',self.context)

	def proveedoresAd(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'proveedoresAd.html',self.context)

	def proveedoresUp(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		datosProv = request.POST.get('proveedor')
		tipo = datosProv.split(';')[0]
		ID = datosProv.split(';')[1]
		self.context['tipoP']=tipo
		self.context['idP']=ID
		request.session['tipoP']=tipo
		request.session['idP']=ID

		if tipo == 'ingredientes':
			prov = ProveedorIngrediente.objects.get(idproveedoringrediente=ID)
			self.context['nombreP'] = prov.nombre_proveedor_ingrediente
			self.context['telefonoP'] = prov.telefono_proveedor_ingrediente
			self.context['direccionP'] = prov.direccion_proveedor_ingrediente
		else:
			prov = ProveedorUtensilio.objects.get(idproveedorutensilio=ID)
			self.context['nombreP'] = prov.nombre_proveedor_utensilio
			self.context['telefonoP'] = prov.telefono_proveedor_utensilio
			self.context['direccionP'] = prov.direccion_proveedor_utensilio

		return render(request,'proveedoresUp.html',self.context)

	def proveedoresDel(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		datosProv = request.POST.get('proveedor')
		tipo = datosProv.split(';')[0]
		ID = datosProv.split(';')[1]
		self.context['tipoP']=tipo
		self.context['idP']=ID

		if tipo == 'ingredientes':
			prov = ProveedorIngrediente.objects.get(idproveedoringrediente=ID)
		else:
			prov = ProveedorUtensilio.objects.get(idproveedorutensilio=ID)
		prov.delete()

		ProvI = ProveedorIngrediente.objects.all()
		ProvU = ProveedorUtensilio.objects.all()
		proveedores = []
		for prov in ProvI:
			proveedor = {}
			proveedor['id']=prov.idproveedoringrediente
			proveedor['nombre']=prov.nombre_proveedor_ingrediente
			proveedor['telefono']=prov.telefono_proveedor_ingrediente
			proveedor['direccion']=prov.direccion_proveedor_ingrediente
			proveedor['tipo']='ingredientes'
			proveedores.append(proveedor)

		for prov in ProvU:
			proveedor = {}
			proveedor['id']=prov.idproveedorutensilio
			proveedor['nombre']=prov.nombre_proveedor_utensilio
			proveedor['telefono']=prov.telefono_proveedor_utensilio
			proveedor['direccion']=prov.direccion_proveedor_utensilio
			proveedor['tipo']='utensilios'
			proveedores.append(proveedor)

		self.context['proveedores']=proveedores
		return render(request,'proveedores.html',self.context)

	def validarProveedoresUp(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		tipo = request.session['tipoP']
		print tipo

		if tipo == 'Proveedor de Ingredientes' or tipo == 'ingredientes':
			tipo = 'ingredientes'
		else:
			tipo = 'utensilios'
		ID = request.session['idP']
		request.session['tipoP']=None
		request.session['idP']=None
		if tipo == 'ingredientes':
			prov = ProveedorIngrediente.objects.get(idproveedoringrediente=ID)
			prov.nombre_proveedor_ingrediente = request.POST.get('nombreP')
			prov.telefono_proveedor_ingrediente = request.POST.get('telefonoP')
			prov.direccion_proveedor_ingrediente = request.POST.get('direccionP')
		else:
			prov = ProveedorUtensilio.objects.get(idproveedorutensilio=ID)
			prov.nombre_proveedor_utensilio = request.POST.get('nombreP')
			prov.telefono_proveedor_utensilio = request.POST.get('telefonoP')
			prov.direccion_proveedor_utensilio = request.POST.get('direccionP')
		prov.save()

		ProvI = ProveedorIngrediente.objects.all()
		ProvU = ProveedorUtensilio.objects.all()
		proveedores = []
		for prov in ProvI:
			proveedor = {}
			proveedor['id']=prov.idproveedoringrediente
			proveedor['nombre']=prov.nombre_proveedor_ingrediente
			proveedor['telefono']=prov.telefono_proveedor_ingrediente
			proveedor['direccion']=prov.direccion_proveedor_ingrediente
			proveedor['tipo']='ingredientes'
			proveedores.append(proveedor)

		for prov in ProvU:
			proveedor = {}
			proveedor['id']=prov.idproveedorutensilio
			proveedor['nombre']=prov.nombre_proveedor_utensilio
			proveedor['telefono']=prov.telefono_proveedor_utensilio
			proveedor['direccion']=prov.direccion_proveedor_utensilio
			proveedor['tipo']='utensilios'
			proveedores.append(proveedor)

		self.context['proveedores']=proveedores
		return render(request,'proveedores.html',self.context)

	def validarProveedoresAd(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		nombre = request.POST.get('nombreP')
		telefono = request.POST.get('telefonoP')
		direccion = request.POST.get('direccionP')
		tipo = request.POST.get('tipoP')

		if tipo == 'ingredientes':
			prov = ProveedorIngrediente(nombre_proveedor_ingrediente=nombre, telefono_proveedor_ingrediente=telefono,direccion_proveedor_ingrediente=direccion)
		else:
			prov = ProveedorUtensilio(nombre_proveedor_utensilio=nombre,telefono_proveedor_utensilio=telefono,direccion_proveedor_utensilio=direccion)

		prov.save()

		ProvI = ProveedorIngrediente.objects.all()
		ProvU = ProveedorUtensilio.objects.all()
		proveedores = []
		for prov in ProvI:
			proveedor = {}
			proveedor['id']=prov.idproveedoringrediente
			proveedor['nombre']=prov.nombre_proveedor_ingrediente
			proveedor['telefono']=prov.telefono_proveedor_ingrediente
			proveedor['direccion']=prov.direccion_proveedor_ingrediente
			proveedor['tipo']='ingredientes'
			proveedores.append(proveedor)

		for prov in ProvU:
			proveedor = {}
			proveedor['id']=prov.idproveedorutensilio
			proveedor['nombre']=prov.nombre_proveedor_utensilio
			proveedor['telefono']=prov.telefono_proveedor_utensilio
			proveedor['direccion']=prov.direccion_proveedor_utensilio
			proveedor['tipo']='utensilios'
			proveedores.append(proveedor)

		self.context['proveedores']=proveedores

		return render(request,'proveedores.html',self.context)

	def llamadaTipoEvento(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		lista_evento=[]
		tabla = TipoEvento.objects.all()
		cantidad = tabla.count()
		for item in range(cantidad):
			lista_evento.append(tabla[item].nombre_tipo_evento)
		self.context["tipos_evento"] = lista_evento
		return render(request,'tipoevento.html',self.context)

	def llamadaTipoEventoAgregar(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		lista_menu=[]
		tabla = TipoMenu.objects.all()
		cantidad = tabla.count()
		for item in range(cantidad):
			lista_menu.append(tabla[item].nombre_tipo_menu)
		self.context["tipos_menu"] = lista_menu
		return render(request,'tipoeventoAgregar.html',self.context)

	def llamadaTipoEventoAddMenu(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		self.context["nombre_e"] = request.POST.get("nombre_evento")
		self.context["descripcion"] = request.POST.get("comment")

		nombre = self.context["nombre_e"]
		descripcion = self.context["descripcion"]
		evento = TipoEvento(nombre_tipo_evento=nombre, visible=0,desripcion_evento=descripcion)
		evento.save()
		evento = TipoEvento.objects.get(nombre_tipo_evento=nombre)
		menu1 = TipoMenu(nombre_tipo_menu="Básico",idtipoevento=evento)
		menu2 = TipoMenu(nombre_tipo_menu="Estandar",idtipoevento=evento)
		menu3 = TipoMenu(nombre_tipo_menu="Premium",idtipoevento=evento)
		menu1.save()
		menu2.save()
		menu3.save()
		self.context["evento"] = evento
		request.session["nombre_tipo_evento"] = evento.nombre_tipo_evento
		return render(request,'tipoeventoredirect2.html',self.context)

	def llamadaTipoEventoConfMenu(self,request):
		self.context["nombre_tipo_evento"] = request.session["nombre_tipo_evento"]
		nombre = self.context["nombre_tipo_evento"]
		evento = TipoEvento.objects.get(nombre_tipo_evento=nombre)
		menu = TipoMenu.objects.filter(idtipoevento = evento.idtipoevento)
		self.context["menus"] = menu
		self.context["evento"] = evento
		return render(request,'tipoeventoAddMenu.html',self.context)

	def llamadaTipoEventoEdMenu(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		lista_item = []
		lista_tipos = []
		tipos = TipoItem.objects.all()
		for i in range(tipos.count()):
			dicc = {}
			lista_aux = Item.objects.filter(idtipo = tipos[i].idtipo)
			dicc["item"] = lista_aux
			dicc["tipo"] = tipos[i].nombre_tipo
			lista_item.append(dicc)
			lista_tipos.append(tipos[i].nombre_tipo)
		self.context["lista_items"] = lista_item
		self.context["tipos_item"] = lista_tipos
		self.context["nombre_menu"] = request.POST.get("seleccion")
		self.context["nombre_tipo_evento"] = request.session["nombre_tipo_evento"]
		request.session["nombre_tipo_evento"] = self.context["nombre_tipo_evento"]
		request.session["nombre_menu"] = self.context["nombre_menu"]
		return render(request,'tipoeventoMenuItem.html',self.context)

	def agregarItemMenu(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		self.context["nombre_tipo_evento"] = request.session["nombre_tipo_evento"]
		self.context["nombre_tipo_menu"] = request.session["nombre_tipo_menu"]
		request.session["nombre_tipo_evento"] = None
		request.session["nombre_tipo_menu"] = None
		nombre_e = self.context["nombre_tipo_evento"]
		evento = TipoEvento.objects.get(nombre_tipo_evento = nombre_e)
		menu = TipoMenu.objects.get(idtipoevento = evento.idtipoevento, nombre_tipo_menu=self.context["nombre_tipo_menu"])
		lista_itemMen = ItemMenu.objects.filter(idtipomenu=menu.idtipomenu)
		lista_item = []
		for i in lista_itemMen:
			lista_item.append(i.iditem)
		total_item = Item.objects.all()
		lista_agregar=[]
		for item in total_item:
			if item not in lista_item:
				print item.nombre_item
				print "ok"
				lista_agregar.append(item)
		
		lista_item2 = []
		lista_tipos = []
		tipos = TipoItem.objects.all()
		for i in range(tipos.count()):
			dicc = {}
			lista_aux = Item.objects.filter(idtipo = tipos[i].idtipo)
			lista_aux2 = []
			for item in lista_aux:
				if item in lista_agregar:
					lista_aux2.append(item)
			dicc["item"] = lista_aux2
			dicc["tipo"] = tipos[i].nombre_tipo
			lista_item2.append(dicc)
			lista_tipos.append(tipos[i].nombre_tipo)
		self.context["lista_items"] = lista_item2
		self.context["tipos_item"] = lista_tipos
		request.session["nombre_tipo_evento"] = self.context["nombre_tipo_evento"]
		request.session["nombre_tipo_menu"] = self.context["nombre_tipo_menu"]
		return render(request,'tipoeventoEAgregaritem.html',self.context)


	def llamadaTipoEventoEdCheck2(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		self.context["nombre_tipo_menu"] = request.session["nombre_tipo_menu"]
		request.session["nombre_tipo_menu"] = None
		self.context["nombre_tipo_evento"] = request.session["nombre_tipo_evento"]
		request.session["nombre_tipo_evento"] = None
		lista_checks = request.POST.getlist('checks')
		print 
		evento = TipoEvento.objects.get(nombre_tipo_evento=self.context["nombre_tipo_evento"])
		menu = TipoMenu.objects.get(nombre_tipo_menu=self.context["nombre_tipo_menu"], idtipoevento=evento.idtipoevento)
		print menu.nombre_tipo_menu
		for seleccion in lista_checks:
			check = Item.objects.get(nombre_item=seleccion)
			print check.nombre_item
			relacion = ItemMenu(idtipomenu=menu, iditem=check)
			relacion.save()
		menus = TipoMenu.objects.filter(idtipoevento = evento.idtipoevento)
		lista_id_items = ItemMenu.objects.filter(idtipomenu=menu.idtipomenu)
		lista_item=[]
		for i in lista_id_items:
			item_aux = Item.objects.get(iditem = i.iditem.iditem)
			lista_item.append(item_aux)
		self.context["lista_item"] = lista_item
		self.context["menus"] = menus
		self.context["evento"] = evento
		return render(request,'tipoeventoEMenu.html',self.context)

	def llamadaTipoEventoEdCheck(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		self.context["nombre_menu"] = request.session["nombre_menu"]
		request.session["nombre_menu"] = None
		self.context["nombre_tipo_evento"] = request.session["nombre_tipo_evento"]
		lista_checks = request.POST.getlist('checks')
		evento = TipoEvento.objects.get(nombre_tipo_evento=self.context["nombre_tipo_evento"])
		menu = TipoMenu.objects.get(nombre_tipo_menu=self.context["nombre_menu"], idtipoevento=evento.idtipoevento)
		print menu.nombre_tipo_menu
		for seleccion in lista_checks:
			check = Item.objects.get(nombre_item=seleccion)
			print check.nombre_item
			relacion = ItemMenu(idtipomenu=menu, iditem=check)
			relacion.save()

		menus = TipoMenu.objects.filter(idtipoevento = evento.idtipoevento)
		self.context["menus"] = menus
		self.context["evento"] = evento
		return render(request,'tipoeventoAddMenu.html',self.context)


	def eliminarItemMenu(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
			
		self.context["nombre_tipo_menu"] = request.session["nombre_tipo_menu"]
		request.session["nombre_tipo_menu"] = None
		self.context["nombre_evento"] = request.session["nombre_tipo_evento"]
		request.session["nombre_tipo_evento"] = None
		lista_checks = request.POST.getlist('checks')
		evento = TipoEvento.objects.get(nombre_tipo_evento=self.context["nombre_evento"])
		menu = TipoMenu.objects.get(nombre_tipo_menu=self.context["nombre_tipo_menu"], idtipoevento=evento.idtipoevento)
		for seleccion in lista_checks:
			item = Item.objects.get(nombre_item=seleccion)
			idItMen = ItemMenu.objects.get(idtipomenu=menu.idtipomenu, iditem=item.iditem)
			idItMen.delete()

		lista_id_items = ItemMenu.objects.filter(idtipomenu=menu.idtipomenu)
		lista_item=[]
		for i in lista_id_items:
			item_aux = Item.objects.get(iditem = i.iditem.iditem)
			lista_item.append(item_aux)
		self.context["lista_item"] = lista_item
		request.session["nombre_tipo_evento"] = self.context["nombre_evento"]
		request.session["nombre_tipo_menu"] = self.context["nombre_tipo_menu"]
		return render(request,'tipoeventoEMenu.html',self.context)


	def llamadaTipoEventoEMenu(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		self.context["nombre_tipo_menu"] = request.POST.get("seleccion")
		self.context["nombre_evento"] = request.session["nombre_tipo_evento"]
		request.session["nombre_tipo_evento"] = None
		nombre_e = self.context["nombre_evento"]
		evento = TipoEvento.objects.get(nombre_tipo_evento=nombre_e)
		menu = TipoMenu.objects.get(idtipoevento = evento.idtipoevento, nombre_tipo_menu=self.context["nombre_tipo_menu"])
		print menu.nombre_tipo_menu
		print menu.idtipomenu
		lista_id_items = ItemMenu.objects.filter(idtipomenu=menu.idtipomenu)
		lista_item=[]
		for i in lista_id_items:
			item_aux = Item.objects.get(iditem = i.iditem.iditem)
			lista_item.append(item_aux)
		self.context["lista_item"] = lista_item
		request.session["nombre_tipo_evento"] = self.context["nombre_evento"]
		request.session["nombre_tipo_menu"] = self.context["nombre_tipo_menu"]
		return render(request,'tipoeventoEMenu.html',self.context)

	def llamadaTipoEventoEditar(self,request):
		self.context["error"] = ""
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context["error"]='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		self.context["nombre_evento"] = request.POST.get("seleccion")
		nombre = self.context["nombre_evento"]
		evento = TipoEvento.objects.get(nombre_tipo_evento=nombre)
		menu = TipoMenu.objects.filter(idtipoevento = evento.idtipoevento)
		if menu.count() == 0:
			self.context["error"] = "Aun no existen menus asociados"
			return render(request,'tipoeventoEditar.html',self.context)
		request.session["nombre_tipo_evento"] = evento.nombre_tipo_evento
		self.context["menus"] = menu
		return render(request,'tipoeventoEditar.html',self.context)

	def llamadaTipoEventoEliminar(self,request):
		self.context["error"] = ""
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context["error"]='Debes iniciar sesión*'
			return render(request,'login.html',self.context)

		self.context["nombre_evento"] = request.POST.get("seleccion")
		nombre = self.context["nombre_evento"]
		evento = TipoEvento.objects.get(nombre_tipo_evento=nombre)
		evento.delete()
		lista_evento=[]
		tabla = TipoEvento.objects.all()
		cantidad = tabla.count()
		for item in range(cantidad):
			lista_evento.append(tabla[item].nombre_tipo_evento)
		self.context["tipos_evento"] = lista_evento
		return render(request,'tipoeventoredirect.html',self.context)

	def llamadaLogin(self,request):
		request.session['nombre']=None
		request.session['apellido']=None
		return render(request,'login.html',self.context)

	def validarLogin(self,request):
		self.context['error']=''
		correo = request.POST.get('mail')
		clave = request.POST.get('pass')
		Q = Administrador.objects.filter(correo_admin=correo)
		if Q.count() > 0:
			if Q[0].clave_admin==clave:
				request.session['nombre']=Q[0].nombre_admin
				request.session['apellido']=Q[0].apellido
				request.session['rol']=Q[0].rol
				request.session['correo']=Q[0].correo_admin
				self.context={'correo':correo,'nombre':Q[0].nombre_admin,'apellido':Q[0].apellido,'rol':Q[0].rol}
				return render(request,'agenda.html',self.context)
			else:
				self.context['error']='Usuario o contraseña incorrecta*'
				print 'no'
		else:
			self.context['error']='Usuario o contraseña incorrecta*'
			print 'no'
		return render(request,'login.html',self.context)

	def llamadaCocina(self,request):
		self.context['nombre']=request.session['nombre']
		self.context['apellido']=request.session['apellido']
		if self.context['nombre']==None:
			self.context['error']='Debes iniciar sesión*'
			return render(request,'login.html',self.context)
		return render(request,'cocina.html',self.context)

	def adminUtensilios(self,request):
		return render(request,'cocina.html',self.context)



