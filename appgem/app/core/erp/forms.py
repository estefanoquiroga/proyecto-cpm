from django.forms import ModelForm

from core.erp.models import Equipos, MantencionesProgramadas, MantencionesCorrectivas, MantencionesPreventivasRealizadas


class EquiposForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre_equipo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Equipos
        fields = ['nombre_equipo', 'marca_equipo', 'modelo_equipo', 'numero_serie', 'categoria_equipo',
                  'serv_clinico_equipo', 'estado_del_equipo', 'proveedor_del_equipo', 'anio_fabricacion',
                  'fecha_recepcion_abast', 'fecha_recepcion_sc', 'frecuencia_mantencion']


class MantencionesProgramadasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = MantencionesProgramadas
        fields = ['numero_serie_equipo', 'proveedor_mantencion_programada', 'fecha_programada', 'estado_mp']


class MantencionesCorrectivasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = MantencionesCorrectivas
        fields = '__all__'


class MPRealizadasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = MantencionesPreventivasRealizadas
        fields = '__all__'
