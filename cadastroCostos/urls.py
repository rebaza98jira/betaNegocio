from django.conf.urls import url
from .views import *
# Cad_un_med_List, Cad_un_med_Create, Cad_un_med_Detail, Cad_un_med_Update, Cad_un_med_Delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url('listarUnidad', Cad_un_med_List.as_view(), name='cad_un_med_listar'),
    url('nuevoUnidad', Cad_un_med_Create.as_view(), name='cad_un_med_crear'),
    url('detalleUnidad/(?P<pk>\d+)/$', Cad_un_med_Detail.as_view(), name='cad_un_med_detalle'),
    url('editarUnidad/(?P<pk>\d+)/$', Cad_un_med_Update.as_view(), name='cad_un_med_editar'),
    url('eliminarUnidad/(?P<pk>\d+)/$', Cad_un_med_Delete.as_view(), name='cad_un_med_eliminar'),
    url('listarInsumo', Cad_insumos_List.as_view(), name='cad_insumos_listar'),
    url('nuevoInsumo', Cad_insumos_Create.as_view(), name='cad_insumos_crear'),
    url('detalleInsumo/(?P<pk>\d+)/$', Cad_insumos_Detail.as_view(), name='cad_insumos_detalle'),
    url('editarInsumo/(?P<pk>\d+)/$', Cad_insumos_Update.as_view(), name='cad_insumos_editar'),
    url('eliminarInsumo/(?P<pk>\d+)/$', Cad_insumos_Delete.as_view(), name='cad_insumos_eliminar'),
    url('listarInventario', Cad_stock_Ingresos_List.as_view(), name='cad_stock_listar'),
    url('listarSalidaInventario', Cad_stock_Salida_List.as_view(), name='cad_stock_salida_listar'),
    url('nuevoInventarioIngreso', Cad_stock_Create.as_view(), name='cad_stock_crear_ingreso'),
    url('nuevoInventarioSalida', Cad_stock_Create.as_view(), name='cad_stock_crear_salida'),
    url('detalleInventario/(?P<pk>\d+)/$', Cad_stock_Detail.as_view(), name='cad_stock_detalle'),
    url('detalleInventarioInsumo/(?P<pk>\d+)/$', Cad_stock_Detail_Movimiento.as_view(), name='cad_stock_detalle_insumo'),
    url('editarInventario/(?P<pk>\d+)/$', Cad_Stock_Update.as_view(), name='cad_stock_editar'),
    url('listarCostos', Cad_costos_List.as_view(), name='cad_costos_listar'),
    url('nuevoCosto/(?P<pk>\d+)/$', Cad_costos_Create.as_view(), name='cad_costos_crear'),
    url('eliminarInventario/(?P<pk>\d+)/$', Cad_stock_Delete.as_view(), name='cad_stock_eliminar'),
    url(r'^ajax/valida_siguente_vez_fecha/$', valida_siguente_vez_fecha, name='valida_siguente_vez_fecha'),
    url('verMesas', Cad_mesas_Ver.as_view(), name='cad_costos_ver_mesas'),
    url('listarMesas', Cad_mesas_List.as_view(), name='cad_mesas_listar'),
    url('nuevoMesaIngreso', Cad_mesas_Create.as_view(), name='cad_mesa_crear_ingreso'),
    url(r'^ajax/valida_siguente_vez_fecha_mesa/$', valida_siguente_vez_fecha_mesa, name='valida_siguente_vez_fecha_mesa'),
    url('nuevoMesaDetalleIngreso', Cad_mesas_detalle_Create.as_view(), name='cad_mesa_detalle_crear_ingreso'),
    url(r'^ajax/retorna_insumos_venta/$', retorna_insumos_venta, name='retorna_insumos_venta'),

    # url(r'^unidad/nuevo$', UnidadCreate.as_view(), name='unidad_crear'),
    # url(r'^unidad/listar$', UnidadList.as_view(), name='unidad_listar'),
    # url(r'^unidad/editar/(?P<pk>\d+)/$', UnidadUpdate.as_view(), name='unidad_editar'),
    # url(r'^unidad/eliminar/(?P<pk>\d+)/$', UnidadDelete.as_view(), name='unidad_eliminar'),
    # url(r'^nutriente/nuevo$', NutrienteCreate.as_view(), name='nutriente_crear'),
    # url(r'^nutriente/listar$', NutrienteList.as_view(), name='nutriente_listar'),
    # url(r'^nutriente/editar/(?P<pk>\d+)/$', NutrienteUpdate.as_view(), name='nutriente_editar'),
    # url(r'^nutriente/eliminar/(?P<pk>\d+)/$', NutrienteDelete.as_view(), name='nutriente_eliminar'),
    # url(r'^nutriente/detalle/(?P<pk>\d+)/$', NutrienteDetail.as_view(), name='nutriente_detalle'),
    # url(r'^subnutriente/nuevo$', SubNutrienteCreate.as_view(), name='subnutriente_crear'),
    # url(r'^subnutriente/listar$', SubNutrienteList.as_view(), name='subnutriente_listar'),
    # url(r'^subnutriente/editar/(?P<pk>\d+)/$', SubNutrienteUpdate.as_view(), name='subnutriente_editar'),
    # url(r'^subnutriente/eliminar/(?P<pk>\d+)/$', SubNutrienteDelete.as_view(), name='subnutriente_eliminar'),
    # url(r'^subnutriente/detalle/(?P<pk>\d+)/$', SubNutrienteDetail.as_view(), name='subnutriente_detalle'),
    # url(r'^alim_nutri/nuevo$', Alim_NutriCreate.as_view(), name='alim_nutri_crear'),
    # url(r'^alim_nutri/listar$', Alim_NutriList.as_view(), name='alim_nutri_listar'),
    # url(r'^alim_nutri/editar/(?P<pk>\d+)/$', Alim_NutriUpdate.as_view(), name='alim_nutri_editar'),
    # url(r'^alim_nutri/eliminar/(?P<pk>\d+)/$', Alim_NutriDelete.as_view(), name='alim_nutri_eliminar'),
    # url(r'^nutri_subnutri/listar$', Nutri_SubNutriList.as_view(), name='nutri_subnutri_listar'),
    # url(r'^nutri_subnutri/nuevo$', Nutri_SubNutriCreate.as_view(), name='nutri_subnutri_crear'),
    # url(r'^nutri_subnutri/editar/(?P<pk>\d+)/$', Nutri_SubNutriUpdate.as_view(), name='nutri_subnutri_editar'),
    # url(r'^nutri_subnutri/eliminar/(?P<pk>\d+)/$', Nutri_SubNutriDelete.as_view(), name='nutri_subnutri_eliminar'),
    # url('ajax/load-nutrientes/', views.load_SelectNutriente, name='ajax_load_nutrientes'),
    # url('ajax/load-subnutrientes/', views.load_SelectSubNutriente, name='ajax_load_subnutrientes'),
]