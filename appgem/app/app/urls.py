"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from core.erp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', IndexView.as_view(), name='index'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('listadoserviciosclinicos/', ServiciosClinicosListView.as_view(), name='serviciosclinicos_list'),
    path('listadoproveedores/', ProveedoresListView.as_view(), name='proveedores_list'),
    path('listadoequiposmedicos/', EquiposMedicosListView.as_view(), name='equiposmedicos_list'),
    path('agregarequipo/', EquiposMedicosCreateView.as_view(), name='equipo_create'),
    path('editarequipo/<int:pk>/', EquiposMedicosUpdateView.as_view(), name='equipo_update'),
    path('eliminarequipo/<int:pk>/', EquiposMedicosDeleteView.as_view(), name='equipo_delete'),
    path('calendariomantenciones/', MantencionesProgramadasListView.as_view(), name='mantencionesprogramadas_list'),
    path('agregarmantencionprogramada/', MantencionesProgramadasCreateView.as_view(), name='mantencionprogramada_create'),
    path('editarmantencionprogramada/<int:pk>/', MantencionesProgramadasUpdateView.as_view(), name='mantencionprogramada_update'),
    path('eliminarmantencionprogramada/<int:pk>/', MantencionesProgramadasDeleteView.as_view(), name='mantencionprogramada_delete'),
    path('listadomcorrectivas/', MantencionesCorrectivasListView.as_view(), name='mantencionescorrectivas_list'),
    path('agregarmantencioncorrectiva/', MantencionesCorrectivasCreateView.as_view(), name='mantencioncorrectiva_create'),
    path('editarmantencioncorrectiva/<int:pk>/', MantencionesCorrectivasUpdateView.as_view(), name='mantencioncorrectiva_update'),
    path('eliminarmantencioncorrectiva/<int:pk>/', MantencionesCorrectivasDeleteView.as_view(), name='mantencioncorrectiva_delete'),
    path('listadomprealizadas/', MPRealizadasListView.as_view(), name='mprealizadas_list'),
    path('agregarmprealizada/', MPRealizadasCreateView.as_view(), name='mprealizada_create'),
    path('editarmprealizada/<int:pk>/', MPRealizadasUpdateView.as_view(), name='mprealizada_update'),
    path('eliminarmprealizada/<int:pk>/', MPRealizadasDeleteView.as_view(), name='mprealizada_delete'),
    path('cumplimientomp/', CumplimientoMPListView.as_view(), name='cumplimientomp_list'),
    path('detallemp/<int:pk>/', MPRealizadasDetailView.as_view(), name='detalle_mp'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
