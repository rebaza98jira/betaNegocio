from django.db.models import Max
from django import forms
from datetime import datetime
from .models import Cad_un_med, Cad_insumos, Cad_stock, Cad_costos, Cad_V_mesas, Cad_V_mesas_detalle
from django.db.models import Q



class Cad_un_med_Form(forms.ModelForm):

    class Meta:
        model = Cad_un_med

        fields = [
            'un_med_insumo',
            'descripcion',
        ]
        labels = {
            'un_med_insumo': 'Codigo',
            'descripcion': 'Descripcion',
        }
        widgets = {
            'un_med_insumo': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'readonly':'True'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control', 'maxlength':'8', 'style': "width:auto"}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(Cad_un_med_Form, self).__init__(*args, **kwargs)
    #     self.fields['un_med_insumo'].initial = Cad_un_med.get_nextCodigo()
    #     print("DEBUG VECESN STOCK")
    #     print(datetime.now())
    #     # print(Cad_stock.getnextNum_veces(datetime.now()))
    #





class Cad_insumos_Form(forms.ModelForm):

    class Meta:


        model = Cad_insumos


        fields = [
            'cod_insumo',
            'nombre_insumo',
            'un_med_insumo',
            'fecha_cadastro',
            'ind_C_V_A',
            'precio_venta',

        ]
        labels = {
            'cod_insumo': 'Codigo',
            'nombre_insumo': 'Nombre',
            'un_med_insumo': 'Unidad',
            'fecha_cadastro': 'Fecha Cadastro',
            'ind_C_V_A': 'Indicador C/V/A',
            'precio_venta':'Precio de Venta',
        }
        widgets = {
            'cod_insumo': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'readonly':'True'}),
            'nombre_insumo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50', 'style': 'width:auto'}),
            'un_med_insumo': forms.Select(attrs={'class': 'js-example-basic-single', 'style': 'width:auto'}),
            'fecha_cadastro': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ind_C_V_A': forms.Select(attrs={'class': 'form-control', 'style': 'width:auto'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
        }

    def __init__(self, *args, **kwargs):
        super(Cad_insumos_Form, self).__init__(*args, **kwargs)
        # self.fields['cod_insumo'].initial = Cad_insumos.get_nextCodigo()
        # self.fields['un_med_insumo'].initial =  Cad_un_med.objects.all().values('descripcion')




class Cad_stock_Form(forms.ModelForm):


    class Meta:
        model = Cad_stock

        fields = [
            'cod_insumo',
            'fec_movimiento',
            'num_veces',
            'cantidad_mov',
            'precio_unitario',
            'valor_insumo',
            'modo_pago_m',
            'ind_ing_sal',

        ]
        labels = {
            'cod_insumo': 'Codigo',
            'fec_movimiento': 'Fecha de Movimiento',
            'num_veces': 'Numero de Veces',
            'cantidad_mov': 'Cantidad en Stock',
            'precio_unitario': 'Precio Unitario',
            'valor_insumo': 'Valor de Insumo',
            'modo_pago_m': 'Modo de Pago',
            'ind_ing_sal': 'Estado',

        }
        widgets = {
            'cod_insumo': forms.Select(attrs={'class': 'js-example-basic-single', 'style': 'width:auto'}),
            'fec_movimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'num_veces': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'readonly':'True'}),
            'cantidad_mov': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'valor_insumo': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'readonly':'True'}),
            'modo_pago_m': forms.Select(attrs={'class': 'form-control', 'style': 'width:auto'}),
            'ind_ing_sal': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:40px', 'readonly': 'True'}),
        }

    def __init__(self, *args, **kwargs):
        super(Cad_stock_Form, self).__init__(*args, **kwargs)
        # self.fields['cod_insumo'].initial = Cad_insumos.get_nextCodigo()
        listchoices = list(Cad_insumos.objects.filter(~Q(ind_C_V_A='V')).values_list('cod_insumo', 'nombre_insumo'))
        print(listchoices)
        print (type(listchoices))
        listchoices.insert(0,('0','Seleccione'))
        self.fields['cod_insumo'].choices = listchoices
        print("EXCLUDES")
        print(Cad_insumos.objects.filter(~Q(ind_C_V_A='V')))


class Cad_stock_insumo_Form(forms.ModelForm):


    class Meta:
        model = Cad_stock

        fields = [
            'cod_insumo',
            # 'fec_movimiento',
            # 'num_veces',
            # 'cantidad_mov',
            # 'precio_unitario',
            # 'valor_insumo',
            # 'ind_ing_sal',
            # 'modo_pago_m',
        ]
        labels = {
            'cod_insumo': 'Insumo',
            'nombre_insumo': 'Nombre',
            'fec_ult_mov': 'Ultimo Movimiento',
            # 'cantidad_mov': 'Cantidad de Movimiento',
            # 'precio_unitario': 'Precio Unitario',
            # 'valor_insumo': 'Valor de Insumo',
            # 'ind_ing_sal': 'Ingreso/Salida',
            # 'modo_pago_m': 'Modo de Pago',
        }
        widgets = {
            'cod_insumo': forms.Select(attrs={'class': 'js-example-basic-single', 'style': 'width:100px', 'type':'text', 'name':'q', 'value':'{{ request.GET.q }}'}),
            # 'nombre_insumo' :forms.CharField(attrs={'class': 'form-control', 'style': 'width:100px'}),
            # 'fec_movimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # 'num_veces': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            # 'cantidad_mov': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            # 'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            # 'valor_insumo': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            # 'ind_ing_sal': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:auto'}),
            # 'modo_pago_m': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:auto'}),
        }




class Cad_costos_Form(forms.ModelForm):

    class Meta:
        model = Cad_costos

        fields = [
            'cod_insumo',
            'fecha_trabajo',
            'cantidad_costo',
            'precio_costo',
            'valor_costo',
            'modo_pago_c',
        ]
        labels = {
            'cod_insumo': 'Codigo',
            'fecha_trabajo': 'Fecha de Movimiento',
            'cantidad_costo': 'Cantidad de Costo',
            'precio_costo': 'Precio de Costo',
            'valor_costo': 'Valor de Costo',
            'modo_pago_c': 'Modo de Pago',
        }
        widgets = {
            'cod_insumo': forms.Select(attrs={'class': 'js-example-basic-single', 'style': 'width:auto', 'id':'id_cod_insumo_salida'}),
            'fecha_trabajo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad_costo': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'precio_costo': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'valor_costo': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'modo_pago_c': forms.Select(attrs={'class': 'form-control', 'style': 'width:auto'}),

        }



class Cad_mesas_Form(forms.ModelForm):

    class Meta:
        model = Cad_V_mesas

        fields = [
            'fecha_trabajo',
            'num_mesa',
            'num_veces',
            'valor_vendido',
        ]
        labels = {
            'fecha_trabajo': 'Fecha',
            'num_mesa': '   Mesa',
            'num_veces': '   Veces',
            'valor_vendido': 'Valor Vendido',
        }
        widgets = {
            'fecha_trabajo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'num_mesa': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'num_veces': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'readonly':'True'}),
            'valor_vendido': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),

        }


class Cad_mesas_detalle_Form(forms.ModelForm):

    class Meta:


        model = Cad_V_mesas_detalle


        fields = [
            'cabecera',
            'linea',
            # 'cod_insumo',
            'cantidad_venta',
            'precio_venta',

        ]
        labels = {
            'cabecera': 'Codigo',
            'linea': 'Linea',
            # 'cod_insumo': 'codisnimo',
            'cantidad_venta': 'cantidad',
            'precio_venta': 'precio',
        }
        widgets = {
            'cabecera': forms.Select(attrs={'class': 'js-example-basic-single', 'style': 'width:auto'}),
            'linea': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            # 'cod_insumo': forms.Select(attrs={'class': 'js-example-basic-single', 'style': 'width:auto'}),
            'cantidad_venta': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),

        }

    def __init__(self, *args, **kwargs):
        super(Cad_mesas_detalle_Form, self).__init__(*args, **kwargs)
        # self.fields['cod_insumo'].initial = Cad_insumos.get_nextCodigo()
        # self.fields['cabecera'].initial =  Cad_V_mesas.objects.all().values('slug')
        # self.fields['cod_insumo'].initial = Cad_insumos.objects.all().values('nombre_insumo')