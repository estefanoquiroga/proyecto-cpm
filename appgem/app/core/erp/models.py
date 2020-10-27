from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.db import models


# Create your models here.

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=30, null=False, blank=False, default=" ", verbose_name='CATEGORIZACIÓN')

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        verbose_name = 'CATEGORIA'
        verbose_name_plural = 'CATEGORIAS DE EQUIPOS'


class Estado(models.Model):
    estado_equipo = models.CharField(max_length=30, null=False, blank=False, verbose_name='ESTADO')

    def __str__(self):
        return self.estado_equipo

    class Meta:
        verbose_name = 'ESTADO'
        verbose_name_plural = 'ESTADOS DE EQUIPOS'


class Proveedores(models.Model):
    nombre_proveedor = models.CharField(max_length=40, null=False, blank=False, verbose_name='NOMBRE PROVEEDOR')
    tecnico_representante = models.CharField(max_length=60, null=True, blank=True, verbose_name='TECNICO REPRESENTANTE')
    telefono_proveedor = models.CharField(max_length=30, null=True, blank=True, verbose_name='TELEFONO PROVEEDOR')
    email_proveedor = models.EmailField(max_length=40, null=True, blank=True, verbose_name='EMAIL PROVEEDOR')
    fecha_vencimiento_contrato = models.DateField(null=True, blank=True, verbose_name='FECHA VENCIMIENTO DE CONTRATO')
    direccion_proveedor = models.CharField(max_length=50, null=True, blank=True, verbose_name='DIRECCION PROVEEDOR')

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        verbose_name = 'PROVEEDORES'
        verbose_name_plural= 'PROVEEDORES'
        ordering = ['nombre_proveedor']


class ServiciosClinicos(models.Model):
    unidad = models.CharField(max_length=40, null=False, blank=False, verbose_name='UNIDAD')
    responsablesc = models.CharField(max_length=40, null=True, blank=True, verbose_name='RESPONSABLE')
    rut_responsablesc = models.CharField(max_length=20, null=True, blank=True, verbose_name='RUT RESPONSABLE')
    email_responsablesc = models.EmailField(max_length=40, null=True, blank=True, verbose_name='EMAIL RESPONSABLE')
    telefono_responsablesc = models.CharField(max_length=20, null=True, blank=True, verbose_name='TELEFONO RESPONSABLE')

    def __str__(self):
        return self.unidad

    class Meta:
        verbose_name = 'SERVICIOS CLINICOS'
        verbose_name_plural = 'SERVICIOS CLINICOS'
        ordering = ['unidad']


class Equipos(models.Model):
    categoria_equipo = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='CATEGORÍA')
    serv_clinico_equipo = models.ForeignKey(ServiciosClinicos, on_delete=models.CASCADE, verbose_name='SERVICIO CLÍNICO')
    estado_del_equipo = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name='ESTADO')
    proveedor_del_equipo = models.ForeignKey(Proveedores, on_delete=models.CASCADE, verbose_name='PROVEEDOR')
    numero_serie = models.CharField(max_length=50, null=False, blank=False, verbose_name='NUMERO DE SERIE')
    nombre_equipo = models.CharField(max_length=40, null=False, blank=False, verbose_name='NOMBRE DEL EQUIPO')
    marca_equipo = models.CharField(max_length=40, null=True, blank=True, verbose_name='MARCA DEL EQUIPO')
    modelo_equipo = models.CharField(max_length=50, null=True, blank=True, verbose_name='MODELO DEL EQUIPO')
    anio_fabricacion = models.DateField(null=True, blank=True, verbose_name='AÑO DE FABRICACIÓN')
    fecha_recepcion_abast = models.DateField(null=True, blank=True, verbose_name='FECHA DE RECEPCIÓN EN ABASTECIMIENTO')
    fecha_recepcion_sc = models.DateField(null=True, blank=True,
                                          verbose_name='FECHA DE INSTALACIÓN EN SERVICIO CLÍNICO')
    frecuencia_mantencion = models.IntegerField(null=True, blank=True, verbose_name='FRECUENCIA DE '
                                                                                    'MANTENCIÓN')

    def __str__(self):
        return '%s / %s /%s / %s' % (self.nombre_equipo, self.marca_equipo, self.modelo_equipo, self.numero_serie)

    class Meta:
        verbose_name = 'EQUIPOS MEDICOS'
        verbose_name_plural = 'EQUIPOS MEDICOS'
        ordering = ['nombre_equipo']


class MantencionesCorrectivas(models.Model):
    serie_equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    proveedor_mc = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    orden_trabajo_mc = models.CharField(unique=True,max_length=50,  null=False, blank=False, verbose_name='ORDEN DE TRABAJO MC')
    fecha_mc = models.DateField(null=True, blank=True, verbose_name='FECHA REALIZACION MC')
    copia_digital_mc = models.FileField(null=True, blank=True, verbose_name='COPIA DIGITAL OT')
    observaciones_mc = models.CharField(max_length=500, verbose_name='OBSERVACIONES', null=True, blank=True)

    def __str__(self):
        return self.orden_trabajo_mc

    class Meta:
        verbose_name = 'MANTENCIONES CORRECTIVAS'
        verbose_name_plural = 'MANTENCIONES CORRECTIVAS'

    @property
    def copia_digital_mc_url(self):
        if self.copia_digital_mc and hasattr(self.copia_digital_mc, 'url'):
            return self.copia_digital_mc.url


class EstadoMP(models.Model):
    nombre_estado = models.CharField(max_length=40, null=False, blank=False, verbose_name='ESTADO MP')

    def __str__(self):
        return self.nombre_estado

    class Meta:
        verbose_name = 'ESTADO MP'
        verbose_name_plural = 'ESTADOS MP'


class MantencionesProgramadas(models.Model):
    numero_serie_equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE, verbose_name= 'EQUIPO')
    estado_mp = models.ForeignKey(EstadoMP, on_delete=models.CASCADE, null=True, blank=True, verbose_name= 'ESTADO')
    proveedor_mantencion_programada = models.ForeignKey(Proveedores, on_delete=models.CASCADE,
                                                        verbose_name='PROVEEDOR ADJUDICADO')
    fecha_programada = models.DateField(verbose_name='FECHA PROGRAMADA', null=False, blank=False)

    def __str__(self):
        return '%s / %s / %s' % (self.id, self.numero_serie_equipo.modelo_equipo,
                                    self.numero_serie_equipo.numero_serie)

    class Meta:
        verbose_name = 'MANTENCIONES PROGRAMADAS'
        verbose_name_plural = 'MANTENCIONES PROGRAMADAS'




class MantencionesPreventivasRealizadas(models.Model):
    id_mantencion_programada = models.OneToOneField(MantencionesProgramadas, on_delete=models.CASCADE)
    proveedor_mp = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    orden_trabajo_mp = models.CharField(unique=True, max_length=50,  null=False, verbose_name='ORDEN DE TRABAJO MP')
    fecha_mp = models.DateField(null=True, blank=True, verbose_name='FECHA REALIZACION MP')
    copia_digital_mp = models.FileField(null=True, blank=True, verbose_name='COPIA DIGITAL OT')
    carta_reprogramacion = models.FileField(null=True, blank=True, verbose_name='CARTA REPROGRAMACIÓN')
    carta_retiro = models.FileField(null=True, blank=True, verbose_name='CARTA DE RETIRO DEL SERVICIO')
    observaciones_mp = models.CharField(max_length=500, verbose_name='OBSERVACIONES', null=True, blank=True)

    class Meta:
        verbose_name = 'MANTENCIONES PREVENTIVAS REALIZADAS'
        verbose_name_plural = 'MANTENCIONES PREVENTIVAS REALIZADAS'

    @property
    def copia_digital_mp_url(self):
        if self.copia_digital_mp and hasattr(self.copia_digital_mp, 'url'):
            return self.copia_digital_mp.url

    def carta_reprogramacion_url(self):
        if self.carta_reprogramacion and hasattr(self.carta_reprogramacion, 'url'):
            return self.carta_reprogramacion.url

    def carta_retiro_url(self):
        if self.carta_retiro and hasattr(self.carta_retiro, 'url'):
            return self.carta_retiro.url

    def id_url(self):
        if self.id and hasattr(self.id, 'url'):
            return self.id.url


""" Whenever ANY model is deleted, if it has a file field on it, delete the associated file too"""


@receiver(post_delete)
def delete_files_when_row_deleted_from_db(sender, instance, **kwargs):
    for field in sender._meta.concrete_fields:
        if isinstance(field, models.FileField):
            instance_file_field = getattr(instance, field.name)
            delete_file_if_unused(sender, instance, field, instance_file_field)


""" Delete the file if something else get uploaded in its place"""


@receiver(pre_save)
def delete_files_when_file_changed(sender, instance, **kwargs):
    # Don't run on initial save
    if not instance.pk:
        return
    for field in sender._meta.concrete_fields:
        if isinstance(field, models.FileField):
            # its got a file field. Let's see if it changed
            try:
                instance_in_db = sender.objects.get(pk=instance.pk)
            except sender.DoesNotExist:
                # We are probably in a transaction and the PK is just temporary
                # Don't worry about deleting attachments if they aren't actually saved yet.
                return
            instance_in_db_file_field = getattr(instance_in_db, field.name)
            instance_file_field = getattr(instance, field.name)
            if instance_in_db_file_field.name != instance_file_field.name:
                delete_file_if_unused(sender, instance, field, instance_in_db_file_field)


""" Only delete the file if no other instances of that model are using it"""


def delete_file_if_unused(model, instance, field, instance_file_field):
    dynamic_field = {}
    dynamic_field[field.name] = instance_file_field.name
    other_refs_exist = model.objects.filter(**dynamic_field).exclude(pk=instance.pk).exists()
    if not other_refs_exist:
        instance_file_field.delete(False)