from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from core.erp.forms import EquiposForm, MantencionesProgramadasForm, MantencionesCorrectivasForm, MPRealizadasForm
from core.erp.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView



# Create your views here.


class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'



class ServiciosClinicosListView(LoginRequiredMixin, ListView):
    model = ServiciosClinicos
    template_name = 'listaserviciosclinicos.html'
    context_object_name = 'serviciosclinicos'


class ProveedoresListView(LoginRequiredMixin, ListView):
    model = Proveedores
    template_name = 'listaproveedores.html'
    context_object_name = 'proveedores'


class EquiposMedicosListView(LoginRequiredMixin, ListView):
    model = Equipos
    queryset = Equipos.objects.all().select_related('categoria_equipo').select_related('serv_clinico_equipo')\
        .select_related('estado_del_equipo').select_related('proveedor_del_equipo')
    template_name = 'listaequiposmedicos.html'
    context_object_name = 'equiposmedicos'


class EquiposMedicosCreateView(LoginRequiredMixin, CreateView):
    model = Equipos
    form_class = EquiposForm
    template_name = 'agregarequipo.html'
    success_url = reverse_lazy('equiposmedicos_list')


class EquiposMedicosUpdateView(LoginRequiredMixin, UpdateView):
    model = Equipos
    form_class = EquiposForm
    template_name = 'agregarequipo.html'
    success_url = reverse_lazy('equiposmedicos_list')


class EquiposMedicosDeleteView(LoginRequiredMixin, DeleteView):
    model = Equipos
    template_name = 'eliminarequipo.html'
    success_url = reverse_lazy('equiposmedicos_list')


class MantencionesProgramadasListView(LoginRequiredMixin, ListView):
    model = MantencionesProgramadas
    queryset = MantencionesProgramadas.objects.all().select_related('numero_serie_equipo')
    template_name = 'calendariomantenciones.html'
    context_object_name = 'mantencionesprogramadas'


class MantencionesProgramadasCreateView(LoginRequiredMixin, CreateView):
    model = MantencionesProgramadas
    form_class = MantencionesProgramadasForm
    template_name = 'agregarmantencionprogramada.html'
    success_url = reverse_lazy('mantencionesprogramadas_list')


class MantencionesProgramadasUpdateView(LoginRequiredMixin, UpdateView):
    model = MantencionesProgramadas
    form_class = MantencionesProgramadasForm
    template_name = 'agregarmantencionprogramada.html'
    success_url = reverse_lazy('mantencionesprogramadas_list')


class MantencionesProgramadasDeleteView(LoginRequiredMixin, DeleteView):
    model = MantencionesProgramadas
    template_name = 'eliminarmantencionprogramada.html'
    success_url = reverse_lazy('mantencionesprogramadas_list')


class MantencionesCorrectivasListView(LoginRequiredMixin, ListView):
    model = MantencionesCorrectivas
    queryset = MantencionesCorrectivas.objects.all().select_related('serie_equipo')
    template_name = 'mantencionescorrectivas.html'
    context_object_name = 'mantencionescorrectivas'


class MantencionesCorrectivasCreateView(LoginRequiredMixin, CreateView):
    model = MantencionesCorrectivas
    form_class = MantencionesCorrectivasForm
    template_name = 'agregarmantencioncorrectiva.html'
    success_url = reverse_lazy('mantencionescorrectivas_list')


class MantencionesCorrectivasUpdateView(LoginRequiredMixin, UpdateView):
    model = MantencionesCorrectivas
    form_class = MantencionesCorrectivasForm
    template_name = 'agregarmantencioncorrectiva.html'
    success_url = reverse_lazy('mantencionescorrectivas_list')


class MantencionesCorrectivasDeleteView(LoginRequiredMixin, DeleteView):
    model = MantencionesCorrectivas
    template_name = 'eliminarmantencioncorrectiva.html'
    success_url = reverse_lazy('mantencionescorrectivas_list')


class MPRealizadasListView(LoginRequiredMixin, ListView):
    model = MantencionesPreventivasRealizadas
    queryset = MantencionesPreventivasRealizadas.objects.all().select_related('id_mantencion_programada').select_related('id_mantencion_programada__numero_serie_equipo')
    template_name = 'listadomprealizadas.html'
    context_object_name = 'mprealizadas'


class MPRealizadasCreateView(LoginRequiredMixin, CreateView):
    model = MantencionesPreventivasRealizadas
    form_class = MPRealizadasForm
    template_name = 'agregarmprealizada.html'
    success_url = reverse_lazy('mprealizadas_list')


class MPRealizadasUpdateView(LoginRequiredMixin, UpdateView):
    model = MantencionesPreventivasRealizadas
    form_class = MPRealizadasForm
    template_name = 'agregarmprealizada.html'
    success_url = reverse_lazy('mprealizadas_list')


class MPRealizadasDeleteView(LoginRequiredMixin, DeleteView):
    model = MantencionesPreventivasRealizadas
    template_name = 'eliminarmantencionpreventiva.html'
    success_url = reverse_lazy('mprealizadas_list')


class CumplimientoMPListView(LoginRequiredMixin, ListView):
    model = MantencionesProgramadas
    template_name = 'cumplimientomp.html'
    context_object_name = 'cumplimientomp'


class MPRealizadasDetailView(LoginRequiredMixin, DetailView):
    model = MantencionesPreventivasRealizadas
    template_name = 'detallemp.html'


class LoginFormView(LoginView):
    template_name = 'login.html'




