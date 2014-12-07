from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *
from administracion.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Home().inicio),
    url(r'^Cotizar/',Home().llamadaCotizar),
    url(r'^CotizarEv/$',Home().llamadaCotizarEv),
	url(r'^CotizarCat/$',Home().llamadaCotizarCat),
	url(r'^Contacto/$', Home().llamadaContacto),
    url(r'^Agenda/',Administracion().llamadaAgenda),
    url(r'^Compras/',Administracion().llamadaCompras),
    url(r'^CotizarAd/',Administracion().llamadaCotizarAd),
    url(r'^Garzones/',Administracion().llamadaGarzones),
    url(r'^GarzonesAd/',Administracion().crearGarzon),
    url(r'^ValidarCrearGarzon',Administracion().validarCrearGarzon),
    url(r'^GarzonesEd/',Administracion().editarGarzon),
    url(r'^ValidarGarzon/',Administracion().validarGarzon),
    url(r'^GarzonesDel/',Administracion().eliminarGarzon),
    url(r'^Menu/',Administracion().llamadaMenu),
    url(r'^Agenda/',Administracion().llamadaAgenda),
    url(r'^Notificaciones/',Administracion().llamadaNotificaciones),
    url(r'^Proveedores/',Administracion().llamadaProveedores),
    url(r'^Agenda/',Administracion().llamadaAgenda),
    url(r'^TipoEvento/',Administracion().llamadaTipoEvento),
    url(r'^TipoEventoAgregar/',Administracion().llamadaTipoEventoAgregar),
    url(r'^TipoEventoEditar/',Administracion().llamadaTipoEventoEditar),
    url(r'^Login/',Administracion().llamadaLogin),
    url(r'^ValidarUsr/',Administracion().validarLogin),
    url(r'^TipoEventoAddMenu/',Administracion().llamadaTipoEventoAddMenu),
    url(r'^TipoEventoEdMenu/',Administracion().llamadaTipoEventoEdMenu),
    url(r'^TipoEventoEdCheck/',Administracion().llamadaTipoEventoEdCheck),
    url(r'^TipoEventoEMenu/',Administracion().llamadaTipoEventoEMenu),

    # url(r'^blog/', include('blog.urls')),
) 


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
