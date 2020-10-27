from django.contrib import admin
from core.erp.models import Categoria, Estado, Proveedores, ServiciosClinicos, Equipos, MantencionesCorrectivas, \
    MantencionesProgramadas, EstadoMP, MantencionesPreventivasRealizadas


# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria',)


class EstadoAdmin(admin.ModelAdmin):
    list_display = ('estado_equipo',)


class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('nombre_proveedor', 'tecnico_representante', 'telefono_proveedor', 'email_proveedor',
                    'fecha_vencimiento_contrato', 'direccion_proveedor')


class ServiciosClinicosAdmin(admin.ModelAdmin):
    list_display = ('unidad', 'responsablesc', 'rut_responsablesc', 'email_responsablesc',
                    'telefono_responsablesc')


class EquiposAdmin (admin.ModelAdmin):
    list_display = ('serv_clinico_equipo', 'marca_equipo', 'modelo_equipo', 'numero_serie', 'anio_fabricacion',
                    'nombre_equipo', 'estado_del_equipo', 'categoria_equipo', 'proveedor_del_equipo',
                    'fecha_recepcion_abast', 'fecha_recepcion_sc')


class MantencionesCorrectivasAdmin(admin.ModelAdmin):
    list_display = ('serie_equipo', 'proveedor_mc', 'orden_trabajo_mc', 'fecha_mc', 'copia_digital_mc',
                    'observaciones_mc')


class MantencionesProgramadasAdmin(admin.ModelAdmin):
    list_display = ('numero_serie_equipo', 'proveedor_mantencion_programada', 'fecha_programada', 'estado_mp')


class MantencionesPreventivasRealizadasAdmin(admin.ModelAdmin):
    list_display = ('id_mantencion_programada', 'proveedor_mp', 'orden_trabajo_mp', 'fecha_mp',
                    'copia_digital_mp', 'observaciones_mp')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(ServiciosClinicos, ServiciosClinicosAdmin)
admin.site.register(Equipos, EquiposAdmin)
admin.site.register(MantencionesCorrectivas, MantencionesCorrectivasAdmin)
admin.site.register(MantencionesProgramadas, MantencionesProgramadasAdmin)
admin.site.register(EstadoMP)
admin.site.register(MantencionesPreventivasRealizadas, MantencionesPreventivasRealizadasAdmin)

admin.site.site_url = '/home'
