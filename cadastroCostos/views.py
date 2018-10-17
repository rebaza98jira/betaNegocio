from django.core import serializers
import json
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Cad_un_med, Cad_insumos, Cad_stock, Cad_costos, Cad_V_mesas, Cad_V_mesas_detalle
from django.db.models import Sum, F, ExpressionWrapper, Max
from .forms import Cad_un_med_Form, Cad_insumos_Form, Cad_stock_Form, Cad_stock_insumo_Form, Cad_costos_Form, Cad_mesas_Form, Cad_mesas_detalle_Form
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from decimal import Decimal
import pprint
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
            return Cad_un_med.objects.all().order_by('un_med_insumo')

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
    success_url = reverse_lazy('betaNegocio:cad_mesas_listar')

    def get_context_data(self, **kwargs):
        context = super(Cad_mesas_Create, self).get_context_data(**kwargs)
        print("DEBUG CERATE MESAS CONTEXT")
        print(context)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        print("DEBUG POST CREATE MESAS")
        form = self.form_class(request.POST)
        print ("FORM1")
        print(form)

        print("SELF")
        print(self)
        print("REQUEST")
        print(request.POST)
        dict_values_detalle = request.POST
        print ("TYPO YOGA")
        print (type(dict_values_detalle))
        print(dict_values_detalle)
        print ("largo")
        # dict_ = {k: yogafalme.getlist(k) if len(yogafalme.getlist(k)) > 1 else v for k, v in yogafalme.items()}
        dict_values_detalle=  dict(dict_values_detalle.lists())
        print (dict_values_detalle['producto'])
        print(len(dict_values_detalle['producto']))
        print(dict_values_detalle['producto'][0])
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
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
                    detalle = Cad_V_mesas_detalle( cabecera_id=cabecera.slug, linea=linea, cantidad_venta=dict_values_detalle['cantidad'][linea-1], precio_venta=dict_values_detalle['precio'][linea-1])
                    detalle.save()
                    linea +=1

            return HttpResponseRedirect(self.get_success_url())



class Cad_mesas_detalle_Create(CreateView):
    model = Cad_V_mesas_detalle
    form_class = Cad_mesas_detalle_Form
    template_name = 'cadastroCostos/cad_mesas_detalle_ingreso_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_mesas_listar')





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
    insumos_venta = Cad_insumos.objects.all()

    return render(request, 'cadastroCostos/insumo_select_options.html', {'insumos': insumos_venta})