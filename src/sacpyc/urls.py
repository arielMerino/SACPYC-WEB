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

    # url(r'^blog/', include('blog.urls')),
) 


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
