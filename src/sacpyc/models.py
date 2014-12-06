# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Administrador(models.Model):
    correo_admin = models.CharField(db_column='CORREO_ADMIN', primary_key=True, max_length=45)  # Field name made lowercase.
    clave_admin = models.CharField(db_column='CLAVE_ADMIN', max_length=45, blank=True)  # Field name made lowercase.
    nombre_admin = models.CharField(db_column='NOMBRE_ADMIN', max_length=25, blank=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=25, blank=True)  # Field name made lowercase.
    rol = models.CharField(db_column='ROL', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrador'


class AgendamientoEvento(models.Model):
    idagendamientoevento = models.IntegerField(db_column='IDAGENDAMIENTOEVENTO', primary_key=True)  # Field name made lowercase.
    id_cotizacion = models.ForeignKey('Cotizacion', db_column='ID_COTIZACION')  # Field name made lowercase.
    fecha_agendamiento_evento = models.DateField(db_column='FECHA_AGENDAMIENTO_EVENTO', blank=True, null=True)  # Field name made lowercase.
    hora_agendamiento_evento = models.TimeField(db_column='HORA_AGENDAMIENTO_EVENTO', blank=True, null=True)  # Field name made lowercase.
    duracion_agendamiento_evento = models.IntegerField(db_column='DURACION_AGENDAMIENTO_EVENTO', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agendamiento_evento'


class Auditoria(models.Model):
    id_auditoria = models.IntegerField(db_column='ID_AUDITORIA', primary_key=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='USUARIO', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    tabla = models.CharField(db_column='TABLA', max_length=30, blank=True)  # Field name made lowercase.
    operacion = models.CharField(db_column='OPERACION', max_length=10, blank=True)  # Field name made lowercase.
    atributo = models.CharField(db_column='ATRIBUTO', max_length=20, blank=True)  # Field name made lowercase.
    valorantes = models.CharField(db_column='VALORANTES', max_length=100, blank=True)  # Field name made lowercase.
    valordespues = models.CharField(db_column='VALORDESPUES', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auditoria'


class CantidadHistorica(models.Model):
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.
    numero_personas = models.IntegerField(db_column='NUMERO_PERSONAS', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    idtipoevento = models.ForeignKey('TipoEvento', db_column='IDTIPOEVENTO')  # Field name made lowercase.
    iditem = models.ForeignKey('Item', db_column='IDITEM')  # Field name made lowercase.
    idhistorico = models.IntegerField(db_column='IDHISTORICO', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cantidad_historica'


class Cliente(models.Model):
    mail_cliente = models.CharField(db_column='MAIL_CLIENTE', primary_key=True, max_length=45)  # Field name made lowercase.
    telefono_cliente = models.IntegerField(db_column='TELEFONO_CLIENTE', blank=True, null=True)  # Field name made lowercase.
    nombre_cliente = models.CharField(db_column='NOMBRE_CLIENTE', max_length=25, blank=True)  # Field name made lowercase.
    apellido_cliente = models.CharField(db_column='APELLIDO_CLIENTE', max_length=25, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class CompraIngrediente(models.Model):
    idcompraingrediente = models.IntegerField(db_column='IDCOMPRAINGREDIENTE', primary_key=True)  # Field name made lowercase.
    idproveedoringrediente = models.ForeignKey('ProveedorIngrediente', db_column='IDPROVEEDORINGREDIENTE', blank=True, null=True)  # Field name made lowercase.
    total_compra_ingrediente = models.IntegerField(db_column='TOTAL_COMPRA_INGREDIENTE', blank=True, null=True)  # Field name made lowercase.
    fecha_compra_ingrediente = models.DateTimeField(db_column='FECHA_COMPRA_INGREDIENTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compra_ingrediente'


class CompraIngredienteIngrediente(models.Model):
    idingrediente = models.ForeignKey('Ingrediente', db_column='IDINGREDIENTE')  # Field name made lowercase.
    idcompraingrediente = models.ForeignKey(CompraIngrediente, db_column='IDCOMPRAINGREDIENTE')  # Field name made lowercase.
    cantidad_compra_ingrediente = models.IntegerField(db_column='CANTIDAD_COMPRA_INGREDIENTE', blank=True, null=True)  # Field name made lowercase.
    precio_compra_ingrediente = models.IntegerField(db_column='PRECIO_COMPRA_INGREDIENTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compra_ingrediente_ingrediente'


class CompraUtensilio(models.Model):
    idcomprautensilio = models.IntegerField(db_column='IDCOMPRAUTENSILIO', primary_key=True)  # Field name made lowercase.
    idproveedorutensilio = models.ForeignKey('ProveedorUtensilio', db_column='IDPROVEEDORUTENSILIO', blank=True, null=True)  # Field name made lowercase.
    total_compra_utensilio = models.IntegerField(db_column='TOTAL_COMPRA_UTENSILIO', blank=True, null=True)  # Field name made lowercase.
    fecha_compra_utensilio = models.DateTimeField(db_column='FECHA_COMPRA_UTENSILIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compra_utensilio'


class CompraUtensilioUtensilio(models.Model):
    idutensilio = models.ForeignKey('Utensilio', db_column='IDUTENSILIO')  # Field name made lowercase.
    idcomprautensilio = models.ForeignKey(CompraUtensilio, db_column='IDCOMPRAUTENSILIO')  # Field name made lowercase.
    cantidad_compra_utensilio = models.IntegerField(db_column='CANTIDAD_COMPRA_UTENSILIO', blank=True, null=True)  # Field name made lowercase.
    precio_compra_utensilio = models.IntegerField(db_column='PRECIO_COMPRA_UTENSILIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compra_utensilio_utensilio'


class Cotizacion(models.Model):
    id_cotizacion = models.IntegerField(db_column='ID_COTIZACION', primary_key=True)  # Field name made lowercase.
    idsolicitudcotizacion = models.ForeignKey('SolicitudDeCotizacion', db_column='IDSOLICITUDCOTIZACION')  # Field name made lowercase.
    estado_aceptacion = models.CharField(db_column='ESTADO_ACEPTACION', max_length=10, blank=True)  # Field name made lowercase.
    valor_cotizacion = models.IntegerField(db_column='VALOR_COTIZACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cotizacion'


class Garzon(models.Model):
    mail_garzon = models.CharField(db_column='MAIL_GARZON', max_length=45, blank=True)  # Field name made lowercase.
    telefono_garzon = models.IntegerField(db_column='TELEFONO_GARZON', blank=True, null=True)  # Field name made lowercase.
    nombre_garzon = models.CharField(db_column='NOMBRE_GARZON', max_length=25, blank=True)  # Field name made lowercase.
    apellido_garzon = models.CharField(db_column='APELLIDO_GARZON', max_length=25, blank=True)  # Field name made lowercase.
    idgarzon = models.IntegerField(db_column='IDGARZON', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'garzon'


class GarzonEvento(models.Model):
    idagendamientoevento = models.ForeignKey(AgendamientoEvento, db_column='IDAGENDAMIENTOEVENTO')  # Field name made lowercase.
    idgarzon = models.ForeignKey(Garzon, db_column='IDGARZON')  # Field name made lowercase.
    respuesta = models.CharField(db_column='RESPUESTA', max_length=5, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'garzon_evento'


class Ingrediente(models.Model):
    idingrediente = models.IntegerField(db_column='IDINGREDIENTE', primary_key=True)  # Field name made lowercase.
    nombre_ingrediente = models.CharField(db_column='NOMBRE_INGREDIENTE', max_length=45, blank=True)  # Field name made lowercase.
    stock_ingrediente = models.IntegerField(db_column='STOCK_INGREDIENTE', blank=True, null=True)  # Field name made lowercase.
    stock_minimo_ingrediente = models.IntegerField(db_column='STOCK_MINIMO_INGREDIENTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ingrediente'


class IngredienteItem(models.Model):
    iditem = models.ForeignKey('Item', db_column='IDITEM')  # Field name made lowercase.
    idingrediente = models.ForeignKey(Ingrediente, db_column='IDINGREDIENTE')  # Field name made lowercase.
    cantidad_ingrediente_especial = models.IntegerField(db_column='CANTIDAD_INGREDIENTE_ESPECIAL', blank=True, null=True)  # Field name made lowercase.
    unidad_ingrediente_especial = models.CharField(db_column='UNIDAD_INGREDIENTE_ESPECIAL', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ingrediente_item'


class IngredienteItemEspecial(models.Model):
    idingrediente = models.ForeignKey(Ingrediente, db_column='IDINGREDIENTE')  # Field name made lowercase.
    id_item_especial = models.ForeignKey('ItemEspecial', db_column='ID_ITEM_ESPECIAL')  # Field name made lowercase.
    cantidad_ingrediente_especial = models.IntegerField(db_column='CANTIDAD_INGREDIENTE_ESPECIAL', blank=True, null=True)  # Field name made lowercase.
    unidad_ingrediente_especial = models.CharField(db_column='UNIDAD_INGREDIENTE_ESPECIAL', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ingrediente_item_especial'


class Item(models.Model):
    iditem = models.IntegerField(db_column='IDITEM', primary_key=True)  # Field name made lowercase.
    idtipo = models.ForeignKey('TipoItem', db_column='IDTIPO', blank=True, null=True)  # Field name made lowercase.
    nombre_item = models.CharField(db_column='NOMBRE_ITEM', max_length=25, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item'


class ItemEspecial(models.Model):
    id_item_especial = models.IntegerField(db_column='ID_ITEM_ESPECIAL', primary_key=True)  # Field name made lowercase.
    id_cotizacion = models.ForeignKey(Cotizacion, db_column='ID_COTIZACION')  # Field name made lowercase.
    nombre_item = models.CharField(db_column='NOMBRE_ITEM', max_length=25, blank=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.
    precio = models.IntegerField(db_column='PRECIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_especial'


class ItemMenu(models.Model):
    idtipomenu = models.ForeignKey('TipoMenu', db_column='IDTIPOMENU')  # Field name made lowercase.
    iditem = models.ForeignKey(Item, db_column='IDITEM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_menu'


class ItemSolicitudDeCotizacion(models.Model):
    iditem = models.ForeignKey(Item, db_column='IDITEM')  # Field name made lowercase.
    idsolicitudcotizacion = models.ForeignKey('SolicitudDeCotizacion', db_column='IDSOLICITUDCOTIZACION')  # Field name made lowercase.
    cantidad_item = models.IntegerField(db_column='CANTIDAD_ITEM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_solicitud_de_cotizacion'


class ProveedorIngrediente(models.Model):
    idproveedoringrediente = models.IntegerField(db_column='IDPROVEEDORINGREDIENTE', primary_key=True)  # Field name made lowercase.
    nombre_proveedor_ingrediente = models.CharField(db_column='NOMBRE_PROVEEDOR_INGREDIENTE', max_length=45, blank=True)  # Field name made lowercase.
    telefono_proveedor_ingrediente = models.IntegerField(db_column='TELEFONO_PROVEEDOR_INGREDIENTE', blank=True, null=True)  # Field name made lowercase.
    direccion_proveedor_ingrediente = models.CharField(db_column='DIRECCION_PROVEEDOR_INGREDIENTE', max_length=45, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedor_ingrediente'


class ProveedorUtensilio(models.Model):
    idproveedorutensilio = models.IntegerField(db_column='IDPROVEEDORUTENSILIO', primary_key=True)  # Field name made lowercase.
    nombre_proveedor_utensilio = models.CharField(db_column='NOMBRE_PROVEEDOR_UTENSILIO', max_length=45, blank=True)  # Field name made lowercase.
    telefono_proveedor_utensilio = models.IntegerField(db_column='TELEFONO_PROVEEDOR_UTENSILIO', blank=True, null=True)  # Field name made lowercase.
    direccion_proveedor_utensilio = models.CharField(db_column='DIRECCION_PROVEEDOR_UTENSILIO', max_length=45, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedor_utensilio'


class Seguimiento(models.Model):
    idseguimiento = models.IntegerField(db_column='IDSEGUIMIENTO', primary_key=True)  # Field name made lowercase.
    id_cotizacion = models.ForeignKey(Cotizacion, db_column='ID_COTIZACION')  # Field name made lowercase.
    fecha_acuerdo = models.DateField(db_column='FECHA_ACUERDO', blank=True, null=True)  # Field name made lowercase.
    fecha_vencimiento = models.DateField(db_column='FECHA_VENCIMIENTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seguimiento'


class SolicitudDeCotizacion(models.Model):
    idsolicitudcotizacion = models.IntegerField(db_column='IDSOLICITUDCOTIZACION', primary_key=True)  # Field name made lowercase.
    mail_cliente = models.ForeignKey(Cliente, db_column='MAIL_CLIENTE')  # Field name made lowercase.
    idtipoevento = models.ForeignKey('TipoEvento', db_column='IDTIPOEVENTO', blank=True, null=True)  # Field name made lowercase.
    cantidad_asistentes = models.IntegerField(db_column='CANTIDAD_ASISTENTES', blank=True, null=True)  # Field name made lowercase.
    fecha_tentativa = models.DateTimeField(db_column='FECHA_TENTATIVA', blank=True, null=True)  # Field name made lowercase.
    duracion_tentativa = models.IntegerField(db_column='DURACION_TENTATIVA', blank=True, null=True)  # Field name made lowercase.
    comentarios_field = models.CharField(db_column='COMENTARIOS_', max_length=250, blank=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    nombre_evento = models.CharField(db_column='NOMBRE_EVENTO', max_length=25, blank=True)  # Field name made lowercase.
    direccion_evento = models.CharField(db_column='DIRECCION_EVENTO', max_length=45, blank=True)  # Field name made lowercase.
    estado_solicitud = models.CharField(db_column='ESTADO_SOLICITUD', max_length=20, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'solicitud_de_cotizacion'


class TipoEvento(models.Model):
    idtipoevento = models.IntegerField(db_column='IDTIPOEVENTO', primary_key=True)  # Field name made lowercase.
    nombre_tipo_evento = models.CharField(db_column='NOMBRE_TIPO_EVENTO', max_length=25, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_evento'
    def __str__(self):
        return '%s;%s'%(self.idtipoevento,self.nombre_tipo_evento)


class TipoItem(models.Model):
    idtipo = models.IntegerField(db_column='IDTIPO', primary_key=True)  # Field name made lowercase.
    nombre_tipo = models.CharField(db_column='NOMBRE_TIPO', max_length=25, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_item'


class TipoMenu(models.Model):
    idtipomenu = models.IntegerField(db_column='IDTIPOMENU', primary_key=True)  # Field name made lowercase.
    idtipoevento = models.ForeignKey(TipoEvento, db_column='IDTIPOEVENTO', blank=True, null=True)  # Field name made lowercase.
    nombre_tipo_menu = models.CharField(db_column='NOMBRE_TIPO_MENU', max_length=25, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_menu'
    def __str__(self):
        return '%s;%s;%s'%(self.idtipomenu,self.idtipoevento,self.nombre_tipo_menu)


class TipoUtensilio(models.Model):
    idtipoutensilio = models.IntegerField(db_column='IDTIPOUTENSILIO', primary_key=True)  # Field name made lowercase.
    nombre_tipo_utensilio = models.CharField(db_column='NOMBRE_TIPO_UTENSILIO', max_length=25, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_utensilio'


class Utensilio(models.Model):
    idutensilio = models.IntegerField(db_column='IDUTENSILIO', primary_key=True)  # Field name made lowercase.
    idtipoutensilio = models.ForeignKey(TipoUtensilio, db_column='IDTIPOUTENSILIO', blank=True, null=True)  # Field name made lowercase.
    nombre_utensilio = models.CharField(db_column='NOMBRE_UTENSILIO', max_length=25, blank=True)  # Field name made lowercase.
    stock_utensilio = models.IntegerField(db_column='STOCK_UTENSILIO', blank=True, null=True)  # Field name made lowercase.
    stock_minimo_utensilio = models.IntegerField(db_column='STOCK_MINIMO_UTENSILIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utensilio'


class UtensilioEvento(models.Model):
    idagendamientoevento = models.ForeignKey(AgendamientoEvento, db_column='IDAGENDAMIENTOEVENTO')  # Field name made lowercase.
    idutensilio = models.ForeignKey(Utensilio, db_column='IDUTENSILIO')  # Field name made lowercase.
    utensilios_utilizados = models.IntegerField(db_column='UTENSILIOS_UTILIZADOS', blank=True, null=True)  # Field name made lowercase.
    utensilios_rotos = models.IntegerField(db_column='UTENSILIOS_ROTOS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utensilio_evento'


class UtensilioItem(models.Model):
    iditem = models.ForeignKey(Item, db_column='IDITEM')  # Field name made lowercase.
    idutensilio = models.ForeignKey(Utensilio, db_column='IDUTENSILIO')  # Field name made lowercase.
    cantidaditem = models.IntegerField(db_column='CANTIDADITEM', blank=True, null=True)  # Field name made lowercase.
    cantidadutensilio = models.IntegerField(db_column='CANTIDADUTENSILIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utensilio_item'
