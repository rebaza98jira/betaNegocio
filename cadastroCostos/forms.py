from django.db.models import Max
from django import forms
from datetime import datetime
from .models import *
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


class Cad_V_mesas_Detalle_Form(forms.ModelForm):

    class Meta:
        model = Cad_V_mesas

        fields = [
            'fecha_trabajo',
            'num_mesa',
            'num_veces',
            'slug',
            'valor_vendido',
        ]
        labels = {
            'fecha_trabajo': 'Fecha',
            'num_mesa': '   Mesa',
            'num_veces': '   Veces',
            'slug': '   Cabecera',
            'valor_vendido': 'Valor Vendido',
        }
        widgets = {
            'fecha_trabajo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'num_mesa': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'num_veces': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'readonly':'True'}),
            'slug':forms.TextInput(attrs={'class': 'form-control','style': 'width:150px'}),
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



class Cad_mesas_Pagar_Form(forms.ModelForm):
    class Meta:
        model = Cad_V_mesas

        fields = [
            'fecha_trabajo',
            # 'num_mesa',
            'num_veces',
            # 'valor_vendido',
        ]
        labels = {
            'fecha_trabajo': 'Fecha',
            # 'num_mesa': '   Mesa',
            'num_veces': '   Veces',
            # 'valor_vendido': 'Valor Vendido',
        }
        widgets = {
            'fecha_trabajo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # 'num_mesa': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'num_veces': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'readonly':'True'}),
            # 'valor_vendido': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),

        }



class Cad_master_Form(forms.ModelForm):

    class Meta:
        model = Cad_Master

        fields = [
            'cod_tributario',
            'razon_social',
            'giro_negocio',
            'imp_venta',
            'imp_restaurante',
            'imp_renta',
            'mesas',
            'billetes',
            'accesorapido',


        ]
        labels = {
            'cod_tributario':'Codigo Tributario',
            'razon_social': 'Razon Social',
            'giro_negocio': 'Giro de Negocio',
            'imp_venta':'Impuesto de Venta',
            'imp_restaurante':'Impuesto de Restaurante',
            'imp_renta': 'Impuesto de Renta',
            'mesas': 'Numero de Mesas',
            'billetes': 'Billetes en Uso',
            'accesorapido': 'Acceso Rapido',
        }
        widgets = {
            'cod_tributario': forms.TextInput(attrs={'class':'form-control', 'maxlength':'20', 'style': "width:auto"}),
            'razon_social':forms.TextInput(attrs={'class':'form-control', 'maxlength':'80', 'style': "width:auto"}),
            'giro_negocio': forms.TextInput(attrs={'class':'form-control', 'maxlength':'50', 'style': "width:auto"}),
            'imp_venta': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'imp_restaurante': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'imp_renta': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'mesas': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'billetes': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100', 'style': "width:auto"}),
            'accesorapido': forms.Textarea(attrs={'class': 'form-control', 'maxlength': '200', 'style': "width:auto"}),
        }



class Cad_ing_ret_Form(forms.ModelForm):

    class Meta:
        model = Cad_ing_ret

        fields = [
            'fecha_trabajo',
            # 'ind_ing_egr',
            # 'num_veces_i',
            # 'valor_ing_ret',
            # 'notas',

        ]
        labels = {
            'fecha_trabajo': 'Fecha',
            # 'ind_ing_egr': 'Ingreso/Egreso',
            # 'num_veces_i': 'Veces',
            # 'valor_ing_ret': 'Valor',
            # 'notas': 'Notas',
        }
        widgets = {
            'fecha_trabajo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width:auto'}),
            # 'ind_ing_egr': forms.Select(attrs={'class': 'form-control', 'style': 'width:auto'}),
            # 'num_veces_i': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'readonly':'True'}),
            # 'valor_ing_ret': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'pattern':"\d+((\.|,)\d+)?"}),
            # 'notas': forms.TextInput(attrs={'class':'form-control', 'maxlength':'8', 'style': "width:auto"}),
        }


class Cad_ing_ret_Form_I(forms.ModelForm):

    class Meta:
        model = Cad_ing_ret

        fields = [
            'fecha_trabajo',
            'ind_ing_egr',
            'num_veces_i',
            'valor_ing_ret',
            'notas',

        ]
        labels = {
            'fecha_trabajo': 'Fecha',
            'ind_ing_egr': 'Ingreso/Egreso',
            'num_veces_i': 'Veces',
            'valor_ing_ret': 'Valor',
            'notas': 'Notas',
        }
        widgets = {
            'fecha_trabajo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width:auto'}),
            'ind_ing_egr': forms.Select(attrs={'class': 'form-control', 'style': 'width:auto','readonly':'True','disabled':'disabled'}),
            'num_veces_i': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'readonly':'True'}),
            'valor_ing_ret': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'pattern':"\d+((\.|,)\d+)?"}),
            'notas': forms.TextInput(attrs={'class':'form-control', 'maxlength':'8', 'style': "width:auto"}),
        }



class Cad_ing_ret_Form_E(forms.ModelForm):

    class Meta:
        model = Cad_ing_ret

        fields = [
            'fecha_trabajo',
            'ind_ing_egr',
            'num_veces_i',
            'valor_ing_ret',
            'notas',

        ]
        labels = {
            'fecha_trabajo': 'Fecha',
            'ind_ing_egr': 'Ingreso/Egreso',
            'num_veces_i': 'Veces',
            'valor_ing_ret': 'Valor',
            'notas': 'Notas',
        }
        widgets = {
            'fecha_trabajo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width:auto'}),
            'ind_ing_egr': forms.Select(attrs={'class': 'form-control', 'style': 'width:auto','readonly':'True'}),
            'num_veces_i': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'readonly':'True'}),
            'valor_ing_ret': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px', 'pattern':"\d+((\.|,)\d+)?"}),
            'notas': forms.TextInput(attrs={'class':'form-control', 'maxlength':'8', 'style': "width:auto"}),
        }


class Cad_est_finan_Form(forms.ModelForm):

    class Meta:
        model = Cad_est_finan

        fields = [
            'año',
            'mes',
            'fec_inicio',
            'fec_final',
            'ingreso_mes',
            'ingreso_acum',
            'costo_tarjeta_mes',
            'costo_efectivo_mes',
            'costo_acum',
            'res_econom_mes',
            'res_econom_acum',
            'stock_tarjeta',
            'stock_efectivo',
            'saldo_caja_mes',
            'saldo_caja_acum',
            'res_finan_mes',
            'res_finan_acum',
            # 'estado_mes',


        ]
        labels = {
            'año':'Año',
            'mes':'Mes',
            'fec_inicio':'Fecha Inicio',
            'fec_final':'Fecha Fin',
            'ingreso_mes':'Ingreso Mensual',
            'ingreso_acum':'Ingreso Acumulado',
            'costo_tarjeta_mes':'Costo Tarjeta Mensual',
            'costo_efectivo_mes':'Costo Efectivo Mensual',
            'costo_acum':'Costo Acumulado',
            'res_econom_mes':'Resultado Economico Mensual',
            'res_econom_acum':'Resultado Economuco Acumulado',
            'stock_tarjeta':'Stock Tarjeta',
            'stock_efectivo':'Stock Efectivo',
            'saldo_caja_mes':'Saldo Caja Mensual',
            'saldo_caja_acum':'Saldo Caja Acumulado',
            'res_finan_mes':'Resultado Financiero Mensual',
            'res_finan_acum':'Resultado Financiero Acumulado',
            # 'estado_mes':'Estado Mensual',
        }
        widgets = {
            'año': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'mes': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'fec_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width:auto'}),
            'fec_final': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'width:auto'}),
            'ingreso_mes': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'ingreso_acum': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'costo_tarjeta_mes': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'costo_efectivo_mes': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'costo_acum': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'res_econom_mes': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'res_econom_acum': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'stock_tarjeta': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'stock_efectivo': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'saldo_caja_mes': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'saldo_caja_acum': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'res_finan_mes': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px' }),
            'res_finan_acum': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),
            # 'estado_mes': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:100px'}),

        }

