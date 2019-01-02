from django.core import serializers
import json
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Cad_un_med, Cad_insumos, Cad_stock, Cad_costos, Cad_V_mesas, Cad_V_mesas_detalle, Cad_Master, Cad_ing_ret, Cad_est_finan
from django.db.models import Sum, F, ExpressionWrapper, Max
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView, FormView, View
from django.urls import reverse_lazy
from decimal import Decimal
from datetime import datetime
from datetime import timedelta

import pprint
from django.db.models import Q, Value, DecimalField, F
# Create your views here.

def index(request):
  #  return HttpResponse("Index")
    return render(request, 'cadastroCostos/index.html')


class Cad_un_med_List(ListView):
    model = Cad_un_med
    template_name = 'cadastroCostos/cad_un_med_List.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query :
            context = Cad_un_med.objects.filter(descripcion__icontains=query)
            return context
        else:
            context = Cad_un_med.objects.all().order_by('un_med_insumo')
            return context

class Cad_un_med_Create(CreateView):
    model = Cad_un_med
    form_class = Cad_un_med_Form
    template_name = 'cadastroCostos/cad_un_med_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_un_med_listar')








class Cad_un_med_Detail(DetailView, UpdateView):
    model = Cad_un_med
    form_class = Cad_un_med_Form
    template_name = 'cadastroCostos/cad_un_med_Detail.html'

class Cad_un_med_Update(UpdateView):
    model = Cad_un_med
    form_class = Cad_un_med_Form
    template_name = 'cadastroCostos/cad_un_med_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_un_med_listar')

class Cad_un_med_Delete(DeleteView,UpdateView):
    model = Cad_un_med
    form_class = Cad_un_med_Form
    template_name = 'cadastroCostos/cad_un_med_Delete.html'
    success_url = reverse_lazy('betaNegocio:cad_un_med_listar')


    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        # Explicitly states what get to call:
        return DeleteView.get(self, request, *args, **kwargs)





class Cad_insumos_List(ListView):
    model = Cad_insumos
    template_name = 'cadastroCostos/cad_insumos_List.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query :
            context = Cad_insumos.objects.filter(nombre_insumo__icontains=query)
            return context
        else:
            return Cad_insumos.objects.all().order_by('cod_insumo')

class Cad_insumos_Create(CreateView):
    model = Cad_insumos
    form_class = Cad_insumos_Form
    template_name = 'cadastroCostos/cad_insumos_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_insumos_listar')

class Cad_insumos_Detail(DetailView, UpdateView):
    model = Cad_insumos
    form_class = Cad_insumos_Form
    template_name = 'cadastroCostos/cad_insumos_Detail.html'

class Cad_insumos_Update(UpdateView):
    model = Cad_insumos
    form_class = Cad_insumos_Form
    template_name = 'cadastroCostos/cad_insumos_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_insumos_listar')

class Cad_insumos_Delete(DeleteView, UpdateView):
    model = Cad_insumos
    form_class = Cad_insumos_Form
    template_name = 'cadastroCostos/cad_insumos_Delete.html'
    success_url = reverse_lazy('betaNegocio:cad_insumos_listar')


    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        # Explicitly states what get to call:
        return DeleteView.get(self, request, *args, **kwargs)



class Cad_stock_Ingresos_List(ListView, UpdateView):
    model = Cad_stock
    template_name = 'cadastroCostos/cad_stock_ingreso_List.html'
    paginate_by = 10
    form_class = Cad_stock_insumo_Form

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        # Explicitly states what get to call:
        return ListView.get(self, request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get("cod_insumo")
        context = Cad_stock.objects.all().order_by('fec_movimiento')

        if query:

            if query.isdigit():
                context = context.filter(cod_insumo=query)
            else:
                context2 = Cad_insumos.objects.filter(nombre_insumo__icontains=query).values_list('cod_insumo',flat=True)
                context = context.filter(cod_insumo__in=context2)
            # return context
        # else:
        #     context = Cad_stock.objects.all()

        return context

class Cad_stock_Salida_List(ListView, UpdateView):
    model = Cad_stock
    template_name = 'cadastroCostos/cad_stock_salida_List.html'
    paginate_by = 10
    form_class = Cad_stock_insumo_Form

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        # Explicitly states what get to call:
        return ListView.get(self, request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get("cod_insumo")
        context = Cad_stock.objects.all().order_by('fec_movimiento')

        if query:

            if query.isdigit():
                context = context.filter(cod_insumo=query)
            else:
                context2 = Cad_insumos.objects.filter(nombre_insumo__icontains=query).values_list('cod_insumo',flat=True)
                context = context.filter(cod_insumo__in=context2)
            # return context
        # else:
        #     context = Cad_stock.objects.all()

        return context




class Cad_stock_Create(CreateView):
    model = Cad_stock
    form_class = Cad_stock_Form
    template_name = 'cadastroCostos/cad_stock_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_stock_listar')


class Cad_stock_Detail(DetailView,UpdateView):
    model = Cad_stock
    form_class = Cad_stock_insumo_Form
    template_name = 'cadastroCostos/cad_stock_Detail.html'

    """SLUG PRUEBA"""



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        cadinsumo_value = Cad_stock.objects.only('cod_insumo').get(pk=self.kwargs['pk']).cod_insumo
        context['mov_insumos'] = Cad_stock.objects.all().filter(cod_insumo=cadinsumo_value)
        # context['saldo'] = cantidad_mov_ingresos_suma['cantidad_mov__sum'] - cantidad_mov_salida_suma['cantidad_mov__sum']
        # print (context)
        return context

class Cad_stock_Detail_Movimiento(DetailView, UpdateView):
    model = Cad_stock
    form_class = Cad_stock_Form
    template_name = 'cadastroCostos/cad_stock_detalle_insumo_Detail.html'

class Cad_Stock_Update(UpdateView):
    model = Cad_stock
    form_class = Cad_stock_Form
    template_name = 'cadastroCostos/cad_stock_Form_Editar.html'
    success_url = reverse_lazy('betaNegocio:cad_stock_listar')

class Cad_stock_Delete(DeleteView, UpdateView):
    model = Cad_stock
    form_class = Cad_stock_Form
    template_name = 'cadastroCostos/cad_stock_Delete.html'
    success_url = reverse_lazy('betaNegocio:cad_stock_listar')

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        # Explicitly states what get to call:
        return DeleteView.get(self, request, *args, **kwargs)


class Cad_costos_List(ListView):
    model = Cad_costos
    template_name = 'cadastroCostos/cad_costos_List.html'
    paginate_by = 10

    def get_queryset(self):
        context = Cad_costos.objects.all().order_by('fecha_trabajo')
        return context




class Cad_costos_Create(CreateView,UpdateView):
    model = Cad_stock
    second_model = Cad_costos
    form_class = Cad_costos_Form
    second_form_class = Cad_stock_Form
    template_name = 'cadastroCostos/cad_costos_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_stock_salida_listar')


    def get_context_data(self, **kwargs):
        context = super(Cad_costos_Create, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        stock = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance= stock)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        print("SelfOBJECT")
        print (self.object)
        id_stock = kwargs['pk']

        stock = self.model.objects.get(id=id_stock)
        print ("DEBUG SALIDA ")
        stock.ind_ing_sal = 'S'
        print (stock.ind_ing_sal)
        form = self.form_class(request.POST)


        costo = self.second_model.objects.all().filter(fecha_trabajo=form['fecha_trabajo'].value(),cod_insumo=form['cod_insumo'].value(),modo_pago_c=form['modo_pago_c'].value()).first()
        # costo = self.second_model.objects.all().filter(fecha_trabajo=form['fecha_trabajo'].value(), cod_insumo= form['cod_insumo'].value(),modo_pago_c='E')
        # file_s = Share.objects.filter(shared_user_id=log_id).values_list('files_id', flat=True).order_by('id')

        if(costo):
            print("Actualiza")
            costo.cantidad_costo = Decimal(costo.cantidad_costo) + Decimal(form['cantidad_costo'].value())
            costo.valor_costo = Decimal(costo.valor_costo) + Decimal(form['valor_costo'].value())
            form = self.second_form_class(request.POST, instance=costo)

        else:
            print("CREA")


        if 'Baja_Total' in request.POST:
            print("DesdeBotonBAJATOTAL")

            if form.is_valid():
                form.save()
                stock.delete()
                return HttpResponseRedirect(self.get_success_url())



        form2 = self.second_form_class(request.POST, instance=stock)
        print("THIS IS AHONTER DEBUGGGGGGGGG")
        print(form2)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            print("ekse")
            return HttpResponseRedirect(self.get_success_url())









def valida_siguente_vez_fecha(request):
    fec_movimiento = request.GET.get('fec_movimiento', None)
    cod_insumo = request.GET.get('cod_insumo', None)
    print ("DEBUG AJAXEC")
    print(fec_movimiento)
    print(cod_insumo)

    data = {
        'numveces': Cad_stock.get_numveces_Fecha(fec_movimiento,cod_insumo)
    }
    print("DEBUG AJAXDATA")
    print (data)
    return JsonResponse(data)


class Cad_mesas_Ver(TemplateView):
    # template_name = 'cadastroCostos/cad_mesas_ver_mesas.html'

    template_name = 'cadastroCostos/cad_mesas_ver_mesas.html'


class Cad_mesas_List(ListView):
    model = Cad_V_mesas
    template_name = 'cadastroCostos/cad_mesas_List.html'
    paginate_by = 10

    def get_queryset(self):
        context = Cad_V_mesas.objects.all().order_by('fecha_trabajo')
        return context


class Cad_mesas_Create(CreateView):
    model = Cad_V_mesas
    form_class = Cad_mesas_Form
    template_name = 'cadastroCostos/cad_mesas_ingreso_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_costos_ver_mesas')

    def get_context_data(self, **kwargs):
        print("REQUEST DEBYG MESAS")
        print(self.request.GET)
        mesa = self.kwargs.get('mesa', 0)
        print("Lo Llamo la mesa!!!")
        print(mesa)
        context = super(Cad_mesas_Create, self).get_context_data(**kwargs)
        print("DEBUG CERATE MESAS CONTEXT")
        print(context)
        context['mesa'] = mesa


        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        print("DEBUG POST CREATE MESAS")
        form = self.form_class(request.POST)
        print ("FORM1")
        print(form)

        dict_values_detalle = request.POST
        # dict_ = {k: yogafalme.getlist(k) if len(yogafalme.getlist(k)) > 1 else v for k, v in yogafalme.items()}
        dict_values_detalle=  dict(dict_values_detalle.lists())
        print("OJO DE")
        print(dict_values_detalle)
        print (dict_values_detalle['producto'])
        print(len(dict_values_detalle['producto']))
        print(dict_values_detalle['producto'][0])
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            print("OJO DE valid")
            if (len(dict_values_detalle['producto'])) == (len(dict_values_detalle['cantidad'])) and (len(dict_values_detalle['cantidad'])) == (len(dict_values_detalle['precio'])):
                print ("SIN SON IUGALES 3")
                # form = self.form_class(request.POST, instance=Cad_V_mesas)
                cabecera = Cad_V_mesas.objects.all().filter(fecha_trabajo=form['fecha_trabajo'].value(),
                                                            num_mesa=form['num_mesa'].value(),
                                                            num_veces=form['num_veces'].value()).first()
                print("llegacabecera")
                print (cabecera.slug)
                linea=1
                while (linea <= len(dict_values_detalle['producto'])):
                    detalle = Cad_V_mesas_detalle( cabecera_id=cabecera.slug, linea=linea, cod_insumo_id = dict_values_detalle['codigo'][linea-1], cantidad_venta=dict_values_detalle['cantidad'][linea-1], precio_venta=dict_values_detalle['precio'][linea-1])
                    detalle.save()
                    linea +=1
                cabecera.estado='O'
                cabecera.save()
            return HttpResponseRedirect(self.get_success_url())


class Cad_mesas_orden_Create(UpdateView):
    model = Cad_V_mesas
    form_class = Cad_mesas_Form
    template_name = 'cadastroCostos/cad_mesas_orden_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_costos_ver_mesas')

    def get_context_data(self, **kwargs):

        print("REQUEST DEBYG MESAS")
        print(self.request.GET)
        slug = self.kwargs.get('slug', 0)
        context = super(Cad_mesas_orden_Create, self).get_context_data(**kwargs)
        mesa_object = self.model.objects.get(slug=slug)
        mesa = mesa_object.num_mesa
        print("DEBUG CERATE MESAS CONTEXT")
        print(context)
        context['ordenes'] = Cad_V_mesas_detalle.objects.filter(cabecera_id=slug).order_by('linea')
        # context['mesa'] = context['ordenes'][0].
        print("ORDENES")
        print(context['ordenes'])
        context['mesa'] = mesa
        context['cabecera'] = slug
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        print("DEBUG POST CREATE MESAS")
        form = self.form_class(request.POST)
        print ("FORM1")
        print(form)

        dict_values_detalle = request.POST
        # dict_ = {k: yogafalme.getlist(k) if len(yogafalme.getlist(k)) > 1 else v for k, v in yogafalme.items()}
        dict_values_detalle=  dict(dict_values_detalle.lists())
        print("OJO DE")
        print(dict_values_detalle)
        print (dict_values_detalle['producto'])
        print(len(dict_values_detalle['producto']))
        print(dict_values_detalle['producto'][0])
        slug = self.kwargs.get('slug', 0)
        mesa_object = self.model.objects.get(slug=slug)
        form = self.form_class(request.POST, instance=mesa_object)
        if form.is_valid():
            form.save()
            print("OJO DE valid")
            if (len(dict_values_detalle['producto'])) == (len(dict_values_detalle['cantidad'])) and (len(dict_values_detalle['cantidad'])) == (len(dict_values_detalle['precio'])):
                print ("SIN SON IUGALES 3")
                # form = self.form_class(request.POST, instance=Cad_V_mesas)
                cabecera = Cad_V_mesas.objects.all().filter(fecha_trabajo=form['fecha_trabajo'].value(),
                                                            num_mesa=form['num_mesa'].value(),
                                                            num_veces=form['num_veces'].value()).first()
                print("llegacabecera")
                print (cabecera.slug)
                detalle_previo = Cad_V_mesas_detalle.objects.all().filter(cabecera_id=cabecera.slug).order_by('linea')
                print("DetallePrevioLen")
                print(len(detalle_previo))
                print(detalle_previo[0].linea)
                # detalle_previo[0].linea = 99
                # detalle_previo[0].save()
                linea=1
                while (linea <= len(dict_values_detalle['producto'])):
                    print("Linea ")
                    print (linea)
                    print("DETALLE PREIVO ")
                    print(len(detalle_previo))
                    if (linea<=(len(detalle_previo))):
                        detalle_previo[linea - 1].cod_insumo_id = dict_values_detalle['codigo'][linea-1]
                        detalle_previo[linea - 1].cantidad_venta = dict_values_detalle['cantidad'][linea-1]
                        detalle_previo[linea - 1].precio_venta = dict_values_detalle['precio'][linea - 1]
                        detalle_previo[linea - 1].save()
                        print("PREVIOS")
                    else:
                        print("Nuevos")
                        detalle = Cad_V_mesas_detalle( cabecera_id=cabecera.slug, linea=linea, cod_insumo_id = dict_values_detalle['codigo'][linea-1], cantidad_venta=dict_values_detalle['cantidad'][linea-1], precio_venta=dict_values_detalle['precio'][linea-1])
                        detalle.save()
                    linea +=1
                while (linea <= len(detalle_previo)):
                    print("Borra")
                    detalle_previo[linea-1].delete()
                    linea += 1

                cabecera.estado='O'
                if 'Pagar_Pedido' in request.POST:
                    cabecera.estado = 'C'
                    cabecera.save()
                    url = reverse_lazy('betaNegocio:cad_mesa_pagar_orden', kwargs={'slug': slug})
                    return HttpResponseRedirect(url)


                cabecera.save()
            return HttpResponseRedirect(self.get_success_url())


class Cad_mesas_Detalle(DetailView, UpdateView):
    model = Cad_V_mesas
    form_class = Cad_V_mesas_Detalle_Form
    template_name = 'cadastroCostos/cad_mesas_Detalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("SLUG MANEJADA")
        print(self.kwargs['slug'])

        # cadmesasdetalle = Cad_mesas_Detalle.objects.only('slug').get(slug=self.kwargs['slug']).slug
        context['mov_mesas'] = Cad_V_mesas_detalle.objects.all().filter(cabecera=self.kwargs['slug']).annotate(
            importe=ExpressionWrapper(
                F('cantidad_venta') * F('precio_venta'), output_field=DecimalField(max_digits=12, decimal_places=2)
            )).order_by('linea')
        # context['saldo'] = cantidad_mov_ingresos_suma['cantidad_mov__sum'] - cantidad_mov_salida_suma['cantidad_mov__sum']
        print (context)
        return context





class Cad_mesas_detalle_Create(CreateView):
    model = Cad_V_mesas_detalle
    form_class = Cad_mesas_detalle_Form
    template_name = 'cadastroCostos/cad_mesas_detalle_ingreso_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_mesas_listar')

class Cad_mesas_Pagar(UpdateView):
    model = Cad_V_mesas
    form_class = Cad_mesas_Pagar_Form
    template_name = 'cadastroCostos/cad_mesas_Form_Pagar.html'
    success_url = reverse_lazy('betaNegocio:cad_costos_ver_mesas')


    def get_context_data(self, **kwargs):

        slug = self.kwargs.get('slug', 0)
        context = super(Cad_mesas_Pagar, self).get_context_data(**kwargs)
        mesa_object = self.model.objects.get(slug=slug)
        master_object = Cad_Master.objects.all().first()
        context['ordenes'] = Cad_V_mesas_detalle.objects.filter(cabecera_id=slug).annotate(
            importe=ExpressionWrapper(
                F('cantidad_venta') * F('precio_venta'), output_field=DecimalField(max_digits=12, decimal_places=2)
            )).order_by('linea')
        subtotal = 0
        for key in context['ordenes']:
            subtotal+=key.importe

        context['fecha'] = mesa_object.fecha_trabajo
        context['hora'] = mesa_object.editado
        context['mesa'] = mesa_object.num_mesa
        context['vez'] = mesa_object.num_veces
        context['cabecera'] = slug
        context['subtotal'] = subtotal
        context['impuesto1'] = subtotal * (master_object.imp_venta/100)
        context['impuesto2'] = subtotal * (master_object.imp_restaurante/100)
        context['total'] = subtotal + context['impuesto1'] + context['impuesto2']
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        dict_values_detalle = request.POST
        dict_values_detalle=  dict(dict_values_detalle.lists())
        slug = self.kwargs.get('slug', 0)
        mesa_object = self.model.objects.get(slug=slug)
        cabecera = Cad_V_mesas.objects.all().filter(fecha_trabajo=mesa_object.fecha_trabajo,
                                                    num_mesa=mesa_object.num_mesa,
                                                    num_veces=mesa_object.num_veces).first()
        detalle_previo = Cad_V_mesas_detalle.objects.all().filter(cod_insumo__ind_C_V_A='A',cabecera_id=cabecera.slug).order_by('cod_insumo')
        # detalle_previo[0].linea = 99
        # detalle_previo[0].save()

        if 'volver_orden' in request.POST:
            cabecera.estado = 'O'
            cabecera.save()
            url = reverse_lazy('betaNegocio:cad_mesa_crear_orden_ingreso', kwargs={'slug': slug})
            return HttpResponseRedirect(url)

        if 'btn_pagado' in request.POST:
            print("PAADO")
            linea=1
            stock_insumo = Cad_stock.objects.filter(cod_insumo__ind_C_V_A='A').order_by('cod_insumo','fec_movimiento')
            """CONSULTAS ANIDADAS SE PUEDE MEJORAR ALGORITMO"""
            while (linea<=(len(detalle_previo))):
                print("MATA")
                stock_consumido = detalle_previo[linea - 1].cantidad_venta
                for key in stock_insumo:
                    print("MATA2")
                    print("(detalle_previo[linea - 1].cod_insumo_id" )
                    print(detalle_previo[linea - 1].cod_insumo_id)
                    print("key.cod_insumo")
                    print(key.cod_insumo.cod_insumo)
                    print("StockCosnumod")
                    print(stock_consumido)
                    print("KEY")
                    print(key)
                    if (detalle_previo[linea - 1].cod_insumo_id == key.cod_insumo.cod_insumo):
                        print("MATA3")
                        if stock_consumido >= key.cantidad_mov:
                            print("MATA4")
                            stock_consumido = stock_consumido - key.cantidad_mov
                            costo = Cad_costos.objects.all().filter(fecha_trabajo=key.fec_movimiento,
                                                                           cod_insumo=key.cod_insumo.cod_insumo,
                                                                           modo_pago_c=key.modo_pago_m).first()
                            # costo = self.second_model.objects.all().filter(fecha_trabajo=form['fecha_trabajo'].value(), cod_insumo= form['cod_insumo'].value(),modo_pago_c='E')
                            # file_s = Share.objects.filter(shared_user_id=log_id).values_list('files_id', flat=True).order_by('id')

                            if (costo):
                                print("MATA5")
                                print("Actualiza")
                                costo.cantidad_costo = Decimal(costo.cantidad_costo) + Decimal(
                                    key.cantidad_mov)
                                costo.valor_costo = Decimal(costo.valor_costo) + Decimal(key.valor_insumo)
                                costo.save()
                            else:
                                print("MATA6")
                                print("CREA")
                                costo = Cad_costos(fecha_trabajo=key.fec_movimiento, cod_insumo_id=key.cod_insumo.cod_insumo,
                                                   modo_pago_c=key.modo_pago_m,
                                                   cantidad_costo=key.cantidad_mov,
                                                   precio_costo=key.precio_unitario,
                                                   valor_costo=(key.cantidad_mov *key.precio_unitario))
                                costo.save()

                            key.delete()
                            if (stock_consumido == 0):
                                print("MATA7")
                                break

                        else:
                            print("MATA8")
                            costo = Cad_costos.objects.all().filter(fecha_trabajo=key.fec_movimiento,
                                                                    cod_insumo=key.cod_insumo,
                                                                    modo_pago_c=key.modo_pago_m).first()
                            """SE MATA CON EL PRECIO DE STOCK NO DE VENTA"""
                            if (costo):
                                print("MATA9")
                                print("Actualiza")
                                costo.cantidad_costo = Decimal(costo.cantidad_costo) + Decimal(
                                    stock_consumido)
                                costo.valor_costo = Decimal(costo.valor_costo) + (Decimal(key.precio_unitario)*Decimal(stock_consumido))
                                costo.save()
                            else:
                                print("MATA10")
                                print("CREA")
                                print(stock_consumido)
                                print(key.precio_unitario)
                                costo = Cad_costos(fecha_trabajo=key.fec_movimiento, cod_insumo_id=key.cod_insumo.cod_insumo,
                                                   modo_pago_c=key.modo_pago_m,
                                                   cantidad_costo=stock_consumido,
                                                   precio_costo=key.precio_unitario,
                                                   valor_costo=(stock_consumido*key.precio_unitario))
                                costo.save()
                            key.cantidad_mov = key.cantidad_mov - stock_consumido
                            key.valor_insumo = key.cantidad_mov * key.precio_unitario
                            key.ind_ing_sal = 'S'
                            key.save()
                            print("MATA11")
                            break
                print("MATA12")
                linea += 1

        cabecera.valor_vendido = request.POST.get('monto')
        cabecera.estado = 'P'

        num_veces_i = Cad_ing_ret.get_num_veces_i_Fecha(cabecera.fecha_trabajo)
        nota = "Mesa: " + str(cabecera.num_mesa) + "-" + "Op:" + str(cabecera.num_veces)
        ingreso = Cad_ing_ret(fecha_trabajo=cabecera.fecha_trabajo, ind_ing_egr="I",
                              num_veces_i=num_veces_i,
                              valor_ing_ret=cabecera.valor_vendido,
                              notas=nota)
        print("MATA13")
        print(request.POST.get('monto'))
        cabecera.save()
        ingreso.save()


        return HttpResponseRedirect(self.get_success_url())

class Cad_Estado_Eco_Fin(ListView):
    # template_name = 'cadastroCostos/cad_mesas_ver_mesas.html'
    model = Cad_est_finan
    template_name = 'cadastroCostos/cad_estado_eco_fin.html'
    paginate_by = 10

    def get_queryset(self):
        print("QERYDATE")
        query = self.request.GET.get("q")
        fecha_inicio = self.request.GET.get("inicio_date")
        fecha_fin = self.request.GET.get("fin_date")
        context = query
        print(query)
        print(fecha_inicio)
        print(fecha_fin)

        if (query) :
            print(query)
            print("QERYDATE2")
            context = self.model.objects.filter(fec_inicio__range=[fecha_inicio, fecha_fin], fec_final__range=[fecha_inicio, fecha_fin])
            return context
        else:
            print("QERYDATE3")
            context = self.model.objects.all()
            return context

    def get_context_data(self, **kwargs):
        print("CONTEXT1111111")
        slug = self.kwargs.get('slug', 0)
        context = super(Cad_Estado_Eco_Fin, self).get_context_data(**kwargs)
        master_object = Cad_Master.objects.all().first()
        ingreso_mes = Cad_ing_ret.objects.filter(ind_ing_egr='I').aggregate(Sum('valor_ing_ret'))
        costo_tarjeta = Cad_costos.objects.filter(modo_pago_c = 'T').aggregate(Sum('valor_costo'))
        costo_efectivo = Cad_costos.objects.filter(modo_pago_c='E').aggregate(Sum('valor_costo'))
        stock_tarjeta = Cad_stock.objects.filter(modo_pago_m='T').aggregate(Sum('valor_insumo'))
        stock_efectivo = Cad_stock.objects.filter(modo_pago_m='E').aggregate(Sum('valor_insumo'))
        egresos_caja = Cad_ing_ret.objects.filter(ind_ing_egr='E').aggregate(Sum('valor_ing_ret'))
        # context['ordenes'] = Cad_V_mesas_detalle.objects.filter(cabecera_id=slug).annotate(
        #     importe=ExpressionWrapper(
        #         F('cantidad_venta') * F('precio_venta'), output_field=DecimalField(max_digits=12, decimal_places=2)
        #     )).order_by('linea')
        # subtotal = 0
        # for key in context['ordenes']:
        #     subtotal+=key.importe

        acumulado = 0
        context['ingreso_mes'] = ingreso_mes['valor_ing_ret__sum']
        context['ingreso_mes_acum'] = acumulado + ingreso_mes['valor_ing_ret__sum']
        context['costo_tarjeta'] = costo_tarjeta['valor_costo__sum']
        context['costo_efectivo'] = costo_efectivo['valor_costo__sum']
        context['costo_acum'] = acumulado + costo_tarjeta['valor_costo__sum'] + costo_efectivo['valor_costo__sum']
        context['res_econom_mes'] = ingreso_mes['valor_ing_ret__sum'] - (costo_tarjeta['valor_costo__sum'] + costo_efectivo['valor_costo__sum'])
        context['res_econom_acum'] = acumulado + (ingreso_mes['valor_ing_ret__sum'] - (costo_tarjeta['valor_costo__sum'] + costo_efectivo['valor_costo__sum']))
        context['stock_tarjeta'] = stock_tarjeta['valor_insumo__sum']
        context['stock_efectivo'] = stock_efectivo['valor_insumo__sum']
        context['saldo_caja_mes'] = ingreso_mes['valor_ing_ret__sum'] - (egresos_caja['valor_ing_ret__sum'] + costo_tarjeta['valor_costo__sum'])
        context['saldo_caja_acum'] = acumulado + (ingreso_mes['valor_ing_ret__sum'] - (egresos_caja['valor_ing_ret__sum'] + costo_tarjeta['valor_costo__sum']))
        context['res_finan_mes'] = (ingreso_mes['valor_ing_ret__sum'] - (egresos_caja['valor_ing_ret__sum'] + costo_tarjeta['valor_costo__sum'])) + (stock_efectivo['valor_insumo__sum']) + (stock_tarjeta['valor_insumo__sum'])
        context['res_finan_mes_acum'] = acumulado + context['saldo_caja_acum'] + stock_tarjeta['valor_insumo__sum'] + stock_efectivo['valor_insumo__sum']



        return context


class Cad_Cierre_Eco_Fin_Actual(TemplateView):
    template_name = 'cadastroCostos/cad_cierre_eco_fin_actual.html'
    def get_context_data(self, **kwargs):
        print("CONTEXT1111111")
        fechaSimula = self.request.GET.get("q")
        fecha_inicio = self.request.GET.get("inicio_date")
        fecha_fin = self.request.GET.get("fin_date")
        if fecha_inicio == None or fecha_fin == None:
            fecha_inicio = datetime.now().date()
            fecha_fin = datetime.now().date()

        print (fechaSimula)
        print(fecha_inicio)
        print(fecha_fin)
        slug = self.kwargs.get('slug', 0)
        context = super(Cad_Cierre_Eco_Fin_Actual, self).get_context_data(**kwargs)
        master_object = Cad_Master.objects.all().first()
        ultimo_historico = Cad_est_finan.objects.filter(fec_final__range=[fecha_inicio, fecha_fin]).last()

        ultimo_historico_tarjeta = 0
        ultimo_historico_stock_efectivo = 0

        ingreso_acumulado = 0
        costo_acumulado = 0
        res_econom_acum = 0
        saldo_caja_acum = 0
        res_finan_acum = 0

        if (ultimo_historico):

            print("ultimo")
            print(ultimo_historico)
            print(ultimo_historico.año)
            print(ultimo_historico.fec_final)
            print(ultimo_historico.fec_final + timedelta(days=1))

            ultimo_historico_tarjeta = ultimo_historico.stock_tarjeta
            ultimo_historico_stock_efectivo = ultimo_historico.stock_efectivo

            ingreso_acumulado = ultimo_historico.ingreso_acum
            costo_acumulado = ultimo_historico.costo_acum
            res_econom_acum = ultimo_historico.res_econom_acum
            saldo_caja_acum = ultimo_historico.saldo_caja_acum
            res_finan_acum = ultimo_historico.res_finan_acum

            fecha_inicio = ultimo_historico.fec_final + timedelta(days=1)





        ingreso_mes = Cad_ing_ret.objects.filter(ind_ing_egr='I',
                                                 fecha_trabajo__range=[fecha_inicio, fecha_fin]).aggregate(
            Sum('valor_ing_ret'))
        if ingreso_mes['valor_ing_ret__sum'] == None:
            ingreso_mes['valor_ing_ret__sum'] = 0
        costo_tarjeta = Cad_costos.objects.filter(modo_pago_c='T',
                                                  fecha_trabajo__range=[fecha_inicio, fecha_fin]).aggregate(
            Sum('valor_costo'))
        if costo_tarjeta['valor_costo__sum'] == None:
            costo_tarjeta['valor_costo__sum'] = 0
        costo_efectivo = Cad_costos.objects.filter(modo_pago_c='E',
                                                   fecha_trabajo__range=[fecha_inicio, fecha_fin]).aggregate(
            Sum('valor_costo'))
        if costo_efectivo['valor_costo__sum'] == None:
            costo_efectivo['valor_costo__sum'] = 0
        stock_tarjeta = Cad_stock.objects.filter(modo_pago_m='T',
                                                 fec_movimiento__range=[fecha_inicio, fecha_fin]).aggregate(
            Sum('valor_insumo'))
        if stock_tarjeta['valor_insumo__sum'] == None:
            stock_tarjeta['valor_insumo__sum'] = 0
        stock_efectivo = Cad_stock.objects.filter(modo_pago_m='E',
                                                  fec_movimiento__range=[fecha_inicio, fecha_fin]).aggregate(
            Sum('valor_insumo'))
        if stock_efectivo['valor_insumo__sum'] == None:
            stock_efectivo['valor_insumo__sum'] = 0
        egresos_caja = Cad_ing_ret.objects.filter(ind_ing_egr='E',
                                                  fecha_trabajo__range=[fecha_inicio, fecha_fin]).aggregate(
            Sum('valor_ing_ret'))
        if egresos_caja['valor_ing_ret__sum'] == None:
            egresos_caja['valor_ing_ret__sum'] = 0

        # ingreso_mes = Cad_ing_ret.objects.filter(ind_ing_egr='I').aggregate(Sum('valor_ing_ret'))
        # costo_tarjeta = Cad_costos.objects.filter(modo_pago_c = 'T').aggregate(Sum('valor_costo'))
        # costo_efectivo = Cad_costos.objects.filter(modo_pago_c='E').aggregate(Sum('valor_costo'))
        # stock_tarjeta = Cad_stock.objects.filter(modo_pago_m='T').aggregate(Sum('valor_insumo'))
        # stock_efectivo = Cad_stock.objects.filter(modo_pago_m='E').aggregate(Sum('valor_insumo'))
        # egresos_caja = Cad_ing_ret.objects.filter(ind_ing_egr='E').aggregate(Sum('valor_ing_ret'))
        # context['ordenes'] = Cad_V_mesas_detalle.objects.filter(cabecera_id=slug).annotate(
        #     importe=ExpressionWrapper(
        #         F('cantidad_venta') * F('precio_venta'), output_field=DecimalField(max_digits=12, decimal_places=2)
        #     )).order_by('linea')
        # subtotal = 0
        # for key in context['ordenes']:
        #     subtotal+=key.importe


        context['ingreso_mes'] = ingreso_mes['valor_ing_ret__sum']
        context['ingreso_mes_acum'] = ingreso_acumulado + ingreso_mes['valor_ing_ret__sum']
        context['costo_tarjeta'] = costo_tarjeta['valor_costo__sum']
        context['costo_efectivo'] = costo_efectivo['valor_costo__sum']
        context['costo_acum'] = costo_acumulado + costo_tarjeta['valor_costo__sum'] + costo_efectivo['valor_costo__sum']
        context['res_econom_mes'] = ingreso_mes['valor_ing_ret__sum'] - (costo_tarjeta['valor_costo__sum'] + costo_efectivo['valor_costo__sum'])
        context['res_econom_acum'] = res_econom_acum + (ingreso_mes['valor_ing_ret__sum'] - (costo_tarjeta['valor_costo__sum'] + costo_efectivo['valor_costo__sum']))
        context['stock_tarjeta'] = stock_tarjeta['valor_insumo__sum']
        context['stock_efectivo'] = stock_efectivo['valor_insumo__sum']
        context['saldo_caja_mes'] = ingreso_mes['valor_ing_ret__sum'] - (egresos_caja['valor_ing_ret__sum'] + costo_tarjeta['valor_costo__sum'])
        context['saldo_caja_acum'] = saldo_caja_acum + (ingreso_mes['valor_ing_ret__sum'] - (egresos_caja['valor_ing_ret__sum'] + costo_tarjeta['valor_costo__sum']))
        # context['res_finan_mes'] = (ingreso_mes['valor_ing_ret__sum'] - (egresos_caja['valor_ing_ret__sum'] + costo_tarjeta['valor_costo__sum'])) + (stock_efectivo['valor_insumo__sum']) + (stock_tarjeta['valor_insumo__sum'])
        context['res_finan_mes'] = context['saldo_caja_mes'] + (stock_tarjeta['valor_insumo__sum'] - ultimo_historico_tarjeta) + (stock_efectivo['valor_insumo__sum'] - ultimo_historico_stock_efectivo)
        context['res_finan_mes_acum'] = context['saldo_caja_acum'] + stock_tarjeta['valor_insumo__sum'] + stock_efectivo['valor_insumo__sum']



        return context

class Cad_Cierre_Create(CreateView):
    model = Cad_est_finan
    form_class = Cad_est_finan_Form
    template_name = 'cadastroCostos/cad_cierre_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_estado_eco_fin')


def estado_mesas(request):
    master = Cad_Master.objects.all().first()
    mesas = master.mesas
    cont = 1
    dictionary = {}

    while cont<=mesas:
        estadomesa=Cad_V_mesas.objects.all().filter(num_mesa=cont).values('slug','estado', 'creado', 'valor_vendido').order_by('creado').last()
        print ("ESTADO MESA")
        print(estadomesa)
        dictionary[cont] = estadomesa
        cont=cont+1

    # data = {
    #     'mesas': mesas,
    # }
    return JsonResponse(dictionary, safe=False)
    # return JsonResponse(data)

def valida_siguente_vez_fecha_mesa(request):
    print ("AJAX FIRST LINE")
    fecha_trabajo = request.GET.get('fecha_trabajo', None)
    num_mesa = request.GET.get('num_mesa', None)
    print ("DEBUG AJAXEC")
    print(fecha_trabajo)
    print(num_mesa)

    data = {
        'numveces': Cad_V_mesas.get_numveces_Fecha(fecha_trabajo,num_mesa)
    }
    print("DEBUG AJAXDATA")
    print (data)
    return JsonResponse(data)


def retorna_insumos_venta(request):
    # alim_nutri_id = request.GET.get('alim_nutri')
    # filtra subnutrientes que no estan linkeados a relacion Alim-Nutri
    insumos_venta = Cad_insumos.objects.filter(~Q(ind_C_V_A='C'))

    return render(request, 'cadastroCostos/insumo_select_options.html', {'insumos': insumos_venta})

def retorna_precio_insumo(request):
    cod_insumo = request.GET.get('cod_insumo', None)
    precio = Cad_insumos.objects.get(pk=cod_insumo)
    precio_venta= precio.precio_venta
    data = {
        'precio_venta': precio_venta
    }

    print("DATA PRECIOS")
    print(data)



    return JsonResponse(data)


def retornaJsonInsumos(request):
    data = list(Cad_insumos.objects.filter(~Q(ind_C_V_A='C')).values('cod_insumo', 'nombre_insumo', 'precio_venta', 'ind_C_V_A').annotate(stock = Value(999, output_field=DecimalField())))
    stock_insumo = Cad_stock.objects.filter(cod_insumo__ind_C_V_A='A').values('cod_insumo', 'cantidad_mov')
    stock_orden = Cad_V_mesas_detalle.objects.filter(~Q(cabecera_id__estado='P'),cod_insumo__ind_C_V_A='A').values('cod_insumo', 'cantidad_venta')
    print("STOCKORDEN")
    print(stock_orden)
    print("STOCKINSUMO")
    print(stock_insumo)
    dictInsumoStock = {}
    for key in stock_insumo:
        if key['cod_insumo'] in dictInsumoStock:
            dictInsumoStock[key['cod_insumo']] += key['cantidad_mov']
        else:
            dictInsumoStock[key['cod_insumo']] = key['cantidad_mov']

    dictOrdenStock = {}
    print("STOCKORDEN")
    print(stock_orden)
    for key in stock_orden:
        if key['cod_insumo'] in dictOrdenStock:
            dictOrdenStock[key['cod_insumo']] += key['cantidad_venta']
        else:
            dictOrdenStock[key['cod_insumo']] = key['cantidad_venta']

    dictionary = {}

    for key in data:
        index = key['cod_insumo']
        if (key['ind_C_V_A'] == 'A') and (key['cod_insumo'] in dictInsumoStock) :
            if (key['cod_insumo'] in dictOrdenStock):
                key['stock']= dictInsumoStock[key['cod_insumo']] - dictOrdenStock[key['cod_insumo']]
            else:
                key['stock'] = dictInsumoStock[key['cod_insumo']]
        if (key['ind_C_V_A'] == 'A') and (key['cod_insumo'] not in dictInsumoStock) :
            key['stock']= 0
        del key['cod_insumo']
        dictionary[index]= key

    print ("DATA JSON")
    print (dictionary)
    return JsonResponse(dictionary, safe=False)



def retorna_parametros_master(request):
    master = Cad_Master.objects.all().first()
    imp_venta = master.imp_venta
    imp_restaurante = master.imp_restaurante
    imp_renta = master.imp_renta
    mesas = master.mesas
    billetes= master.billetes
    accesorapido= master.accesorapido
    data = {
        'imp_venta' : imp_venta,
        'imp_restaurante' : imp_restaurante,
        'imp_renta' : imp_renta,
        'mesas' : mesas,
        "billetes" : billetes,
        "accesorapido": accesorapido,
    }
    return JsonResponse(data)

def retorna_fecha_servidor(request):
    fecha_servidor = datetime.now().date()
    data = {
        'fecha_servidor' : fecha_servidor
    }
    return JsonResponse(data)


class Cad_master_List (ListView):
    model = Cad_Master
    template_name = 'cadastroCostos/cad_master_List.html'
    paginate_by = 10


class Cad_master_Create(CreateView):
    model = Cad_Master
    form_class = Cad_master_Form
    template_name = 'cadastroCostos/cad_master_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_master_listar')

# class Cad_master_Detail(DetailView, UpdateView):
#     model = Cad_Master
#     form_class = Cad_master_Form
#     template_name = 'cadastroCostos/cad_master_Detail.html'

class Cad_master_Update(UpdateView):
    model = Cad_Master
    form_class = Cad_master_Form
    template_name = 'cadastroCostos/cad_master_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_master_listar')

# class Cad_master_Delete(DeleteView,UpdateView):
#     model = Cad_Master
#     form_class = Cad_master_Form
#     template_name = 'cadastroCostos/cad_master_Delete.html'
#     success_url = reverse_lazy('betaNegocio:cad_master_listar')



class Cad_ing_ret_List(ListView):
    model = Cad_ing_ret
    template_name = 'cadastroCostos/cad_ing_ret_List.html'
    paginate_by = 10

class Cad_ing_ret_List_I(ListView):
    model = Cad_ing_ret
    template_name = 'cadastroCostos/cad_ing_ret_List_I.html'
    paginate_by = 10

    def get_queryset(self):
        # query = self.request.GET.get("cod_insumo")
        context = Cad_ing_ret.objects.filter(ind_ing_egr="I").order_by('fecha_trabajo')
        return context


class Cad_ing_ret_Create_I(CreateView):
    model = Cad_ing_ret
    form_class = Cad_ing_ret_Form_I
    template_name = 'cadastroCostos/cad_ing_ret_Form_I.html'
    success_url = reverse_lazy('betaNegocio:cad_ing_ret_listar_i')


class Cad_ing_ret_Update_I(UpdateView):
    model = Cad_ing_ret
    form_class = Cad_ing_ret_Form_I
    template_name = 'cadastroCostos/cad_ing_ret_Form_I.html'
    success_url = reverse_lazy('betaNegocio:cad_ing_ret_listar_i')


class Cad_ing_ret_List_E(ListView):
    model = Cad_ing_ret
    template_name = 'cadastroCostos/cad_ing_ret_List_E.html'
    paginate_by = 10

    def get_queryset(self):
        # query = self.request.GET.get("cod_insumo")
        context = Cad_ing_ret.objects.filter(ind_ing_egr="E").order_by('fecha_trabajo')

        return context

class Cad_ing_ret_Create_E(CreateView):
    model = Cad_ing_ret
    form_class = Cad_ing_ret_Form_E
    template_name = 'cadastroCostos/cad_ing_ret_Form_E.html'
    success_url = reverse_lazy('betaNegocio:cad_ing_ret_listar_e')

class Cad_ing_ret_Update_E(UpdateView):
    model = Cad_ing_ret
    form_class = Cad_ing_ret_Form_I
    template_name = 'cadastroCostos/cad_ing_ret_Form_E.html'
    success_url = reverse_lazy('betaNegocio:cad_ing_ret_listar_e')


class Cad_ing_ret_Create(FormView):
    model = Cad_ing_ret
    form_class = Cad_ing_ret_Form
    template_name = 'cadastroCostos/cad_ing_ret_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_ing_ret_listar')



def valida_siguente_vez_fecha_ing_ret(request):
    fecha_trabajo = request.GET.get('fecha_trabajo', None)

    print(fecha_trabajo)
    print(request.GET)
    print(request.POST)
    data = {
        'num_veces': Cad_ing_ret.get_num_veces_i_Fecha(fecha_trabajo)
    }
    print("DEBUG AJAXDATA")
    print (data)
    return JsonResponse(data)

def graba_ing_ret(request):
    fecha_trabajo = request.POST.get('fecha_trabajo', None)
    ind_ing_egr = request.POST.get('ind_ing_egr', None)
    num_veces_i = Cad_ing_ret.get_num_veces_i_Fecha(fecha_trabajo)
    valor_ing_ret = request.POST.get('entry', None)
    notas = request.POST.get('notas', None)

    caja = Cad_ing_ret(fecha_trabajo=fecha_trabajo, ind_ing_egr=ind_ing_egr,num_veces_i=num_veces_i,valor_ing_ret=valor_ing_ret, notas=notas)
    caja.save()
    print(fecha_trabajo)
    print(request.GET)
    print(request.POST)

    caja = Cad_ing_ret.objects.all().filter(fecha_trabajo=fecha_trabajo,
                                            num_veces_i=num_veces_i,
                                            valor_ing_ret=valor_ing_ret).first()
    data = {
        'num_veces_i': Cad_ing_ret.get_num_veces_i_Fecha(fecha_trabajo)
    }
    print("DEBUG CAJAJA")
    print (caja)
    return JsonResponse(data)

def retornaJsonCajaMov(request):
    fecha_trabajo = request.GET.get('fecha_trabajo', None)
    print ("CAJMOVEFECHA")
    print (fecha_trabajo )
    data = list(Cad_ing_ret.objects.filter(fecha_trabajo=fecha_trabajo).values('id','ind_ing_egr', 'num_veces_i', 'valor_ing_ret', 'notas'))
    # queryset = Cad_insumos.objects.filter(~Q(ind_C_V_A='C'))
    # data = serializers.serialize("json", queryset)
    print (data)
    dictionary = {}

    for key in data:
        print (type(key))
        index = key['id']
        del key['id']
        dictionary[index]= key

    print ("DATA JSON")
    print (dictionary)
    return JsonResponse(dictionary, safe=False)