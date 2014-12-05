from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *
from administracion.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$',Home(0).inicio),
    url(r'^Cotizar/',Cotizar(0).llamadaCotizar),
    url(r'^CotizarEv/$',Cotizar(0).llamadaCotizarEv),
	url(r'^CotizarCat/$',Cotizar(0).llamadaCotizarCat),
	url(r'^Contacto/$', Contacto(0).llamadaContacto),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^Agenda/',Agenda(0).llamadaAgenda),
    url(r'^Compras/',Compras(0).llamadaCompras),
    url(r'^CotizarAd/',CotizarAd(0).llamadaCotizarAd),
    url(r'^Garzones/',Garzones(0).llamadaGarzones),
    url(r'^Menu/',Menu(0).llamadaMenu),
    url(r'^Agenda/',Agenda(0).llamadaAgenda),
    url(r'^Notificaciones/',Notificaciones(0).llamadaNotificaciones),
    url(r'^Proveedores/',Proveedores(0).llamadaProveedores),
    url(r'^Agenda/',Agenda(0).llamadaAgenda),
    url(r'^TipoEvento/',TipoEvento(0).llamadaTipoEvento),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) 


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
