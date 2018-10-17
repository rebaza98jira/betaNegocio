from django.db import models
from django.db.models import Max
from datetime import datetime
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
# Create your models here.



"""FUNCIONES / METODOS """

def slug_Save(sender, instance, *args, **kwargs):
    print("DEBUG SLUGG")
    print(sender)
    prefix = ''
    nombre_campo = ''
    if sender == Cad_un_med:
        print("SON IGUALES CADMED")
        prefix = 'unidad'
        nombre_campo = 'un_med_insumo'
    if sender == Cad_insumos:
        print("SON IGUALES Insumos")
        prefix = 'insumo'
        nombre_campo = 'cod_insumo'
    if sender == Cad_stock:
        print("SON IGUALES CADMED")
        prefix = 'inventario'
        nombre_campo = 'id'
    if sender == Cad_ing_ret:
        print("SON IGUALES Insumos")
        prefix = 'caja'
        nombre_campo = 'id'
    if sender == Cad_costos:
        print("SON IGUALES CADMED")
        prefix = 'costos'
        nombre_campo = 'id'
    if sender == Cad_V_mesas:
        print("SON IGUALES Insumos")
        prefix = 'mesamov'
        nombre_campo = 'id'
    if sender == Cad_est_finan:
        print("SON IGUALES CADMED")
        prefix = 'finanzas'
        nombre_campo = 'id'
    if sender == Cad_insumos:
        print("SON IGUALES Insumos")
        prefix = 'insumo'
        nombre_campo = 'cod_insumo'



    if not instance.pk:
        last_pk = sender.objects.all().aggregate(Max(nombre_campo))
        slug = ''
        if last_pk[nombre_campo+'__max'] == None:
            print("111")
            slug = slugify(prefix + "-1")
        else:
            print("lastpkelse")
            print (last_pk[nombre_campo+'__max'])
            slug = slugify(prefix)

            print("222")
            # object_pk = Cad_un_med.objects.latest('pk')
            # object_pk = object_pk.pk + 1
            correlativo =  last_pk[nombre_campo+'__max'] + 1
            slug = f'{slug}-{correlativo}'
            print (slug)
        print("333")
        instance.slug = slug



    else:
        print("444")
        print (instance.slug)
        print(f'{prefix}-{instance.pk}')
        if instance.slug != f'{prefix}-{instance.pk}':
            print("555")
            instance.slug = f'{prefix}-{instance.pk}'
            instance.save()




        # if not instance.slug:
        #     instance.slug = f'{"insumo"}-{instance.pk}'
        #     instance.save()


"""FIN FUNCIONES / METODOS"""




"""UNIDAD DE MEDIDA"""


class Cad_un_med(models.Model):
    un_med_insumo = models.AutoField(primary_key= True, null= False, blank= False)
    slug = models.SlugField(unique=True)
    descripcion = models.CharField(max_length=8)

    def __str__(self):
        return self.descripcion

    # def get_nextCodigo(*args ):
    #     next_codigo = Cad_un_med.objects.all().aggregate(Max('un_med_insumo'))
    #     print(next_codigo['un_med_insumo__max'])
    #     if next_codigo['un_med_insumo__max'] == None:
    #         return 1
    #     else:
    #         return next_codigo['un_med_insumo__max'] + 1






pre_save.connect(slug_Save, sender=Cad_un_med)
post_save.connect(slug_Save, sender=Cad_un_med)

"""FIN UNIDAD DE MEDIDA"""


"""INSUMOS"""

class Cad_insumos(models.Model):


    cod_insumo = models.AutoField(primary_key= True, null= False, blank= False)
    slug = models.SlugField(unique=True)
    nombre_insumo = models.CharField(max_length=50)
    un_med_insumo = models.ForeignKey(Cad_un_med, null=False, blank=False, on_delete=models.PROTECT)
    fecha_cadastro = models.DateField(default=datetime.now)
    ind_C_V_A_CHOICES = (('C', 'Consumo'), ('V', 'Venta'), ('A', 'Ambos'))
    ind_C_V_A = models.CharField(max_length=1, choices= ind_C_V_A_CHOICES, default= 'C')
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    # def __str__(self):
    #     cadena = "{0} -> {1}"
    #     return cadena.format(self.nombre_insumo, self.un_med_insumo)
    def __str__(self):
        return self.nombre_insumo

    # def get_nextCodigo(*args):
    #     next_codigo = Cad_insumos.objects.all().aggregate(Max('cod_insumo'))
    #     print (next_codigo['cod_insumo__max'])
    #     if next_codigo['cod_insumo__max'] == None:
    #         return 1
    #     else:
    #         return next_codigo['cod_insumo__max'] + 1
        # return next_codigo['cod_insumo__max'] + 1




pre_save.connect(slug_Save, sender=Cad_insumos)
post_save.connect(slug_Save, sender=Cad_insumos)

"""FIN INSUMOS"""


"""INVENTARIO"""

class Cad_stock(models.Model):
    slug = models.SlugField(unique=True)
    cod_insumo = models.ForeignKey(Cad_insumos, null=False, blank=False, on_delete=models.PROTECT)
    fec_movimiento = models.DateField(default=datetime.now)
    num_veces = models.SmallIntegerField()
    cantidad_mov = models.DecimalField(max_digits=8, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    valor_insumo = models.DecimalField(max_digits=12, decimal_places=2)
    ind_ing_sal_CHOICES = (('I', 'Ingreso'),('S', 'Salida'))
    ind_ing_sal = models.CharField(max_length=1, choices= ind_ing_sal_CHOICES, default = 'I')
    modo_pago_m_CHOICES = (('E', 'Efectivo'), ('T', 'Tarjeta'))
    """CONFIRMAR SI DEFAULT DE MODO DE PAGO SERA EFECTIVO"""
    modo_pago_m = models.CharField(max_length=1, choices= modo_pago_m_CHOICES, default= 'E')

    def get_numveces_Fecha(fecha,codigo):
        print(fecha)
        print(type(fecha))
        print(codigo)
        print(type(codigo))
        # data =  Cad_stock.objects.filter(fec_movimiento=fecha, cod_insumo=codigo).exists()
        if str(fecha)=="" or str(codigo)=="":
            return 1

        next_numveces = Cad_stock.objects.filter(fec_movimiento=fecha, cod_insumo=codigo).aggregate(Max('num_veces'))

        if next_numveces['num_veces__max'] == None:
            return 1
        else:
            return next_numveces['num_veces__max'] + 1



    class Meta:
        unique_together = ["cod_insumo", "fec_movimiento", "num_veces"]

    # def getnextNum_veces(*args):
    #     print("Reached1")
    #     print(args)
    #     next_num_veces = Cad_stock.objects.filter(cod_insumo=1, fec_movimiento=args)
    #     print(next_num_veces)
    #     print("Reached2")
    #     return "Works"
    #         # next_num_veces['num_veces__max'] + 1

pre_save.connect(slug_Save, sender=Cad_stock)
post_save.connect(slug_Save, sender=Cad_stock)

"""FIN INVENTARIO"""


"""CAJA"""

class Cad_ing_ret(models.Model):
    slug = models.SlugField(unique=True)
    fecha_trabajo = models.DateField()
    ind_ing_egr_CHOICES = (('I', 'Ingreso'), ('E', 'Egreso'))
    ind_ing_egr = models.CharField(max_length=1, choices= ind_ing_egr_CHOICES)
    num_veces_i = models.SmallIntegerField()
    valor_ing_ret = models.DecimalField(max_digits=12, decimal_places=2)
    notas = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        unique_together = ["fecha_trabajo", "ind_ing_egr", "num_veces_i"]


pre_save.connect(slug_Save, sender=Cad_ing_ret)
post_save.connect(slug_Save, sender=Cad_ing_ret)


"""FINCAJA"""

"""COSTOS"""

class Cad_costos(models.Model):
    slug = models.SlugField(unique=True)
    fecha_trabajo =  models.DateField(default=datetime.now)
    cod_insumo = models.ForeignKey(Cad_insumos, null=False, blank=False, on_delete=models.CASCADE)
    modo_pago_c_CHOICES = (('E', 'Efectivo'), ('T', 'Tarjeta'))
    modo_pago_c = models.CharField(max_length=1, choices=modo_pago_c_CHOICES)
    cantidad_costo = models.DecimalField(max_digits=8, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=12, decimal_places=2)
    valor_costo = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        # unique_together = ["fecha_trabajo", "cod_insumo"]
        unique_together = ["fecha_trabajo", "cod_insumo", "modo_pago_c"]

pre_save.connect(slug_Save, sender=Cad_costos)
post_save.connect(slug_Save, sender=Cad_costos)

"""FIN COSTOS"""

"""MESAS"""

class Cad_V_mesas(models.Model):
    slug = models.SlugField(unique=True)
    fecha_trabajo = models.DateField(default=datetime.now)
    num_mesa = models.SmallIntegerField()
    num_veces = models.SmallIntegerField()
    valor_vendido = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        unique_together = ["fecha_trabajo", "num_mesa", "num_veces"]

    def get_numveces_Fecha(fecha, nro_mesa):
        print(fecha)
        print(type(fecha))
        print(nro_mesa)
        print(type(nro_mesa))
        # data =  Cad_stock.objects.filter(fec_movimiento=fecha, cod_insumo=codigo).exists()
        if str(fecha) == "" or str(nro_mesa) == "":
            return 1

        next_numveces = Cad_V_mesas.objects.filter(fecha_trabajo=fecha, num_mesa=nro_mesa).aggregate(Max('num_veces'))

        if next_numveces['num_veces__max'] == None:
            return 1
        else:
            return next_numveces['num_veces__max'] + 1

pre_save.connect(slug_Save, sender=Cad_V_mesas)
post_save.connect(slug_Save, sender=Cad_V_mesas)

"""FIN MESAS"""

"""MESAS DETALLE"""

class Cad_V_mesas_detalle(models.Model):
    cabecera = models.ForeignKey(Cad_V_mesas, to_field='slug', blank=False, null=False, on_delete=models.PROTECT)
    linea = models.SmallIntegerField()
    # cod_insumo = models.ForeignKey(Cad_insumos, null=False, blank=False, on_delete=models.PROTECT)
    cantidad_venta = models.SmallIntegerField()
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2)



"""FIN MESAS DETALLE"""


"""FINANZAS"""

class Cad_est_finan(models.Model):
    slug = models.SlugField(unique=True)
    mes_año = models.CharField(primary_key=True, max_length=8, null=False, blank=False)
    fec_inicio = models.DateField()
    fec_final = models.DateField()
    ingreso_mes = models.DecimalField(max_digits=12, decimal_places=2)
    ingreso_acum = models.DecimalField(max_digits=12, decimal_places=2)
    costo_tarjeta_mes = models.DecimalField(max_digits=12, decimal_places=2)
    costo_efectivo_mes = models.DecimalField(max_digits=12, decimal_places=2)
    costo_acum = models.DecimalField(max_digits=12, decimal_places=2)
    res_econom_mes = models.DecimalField(max_digits=12, decimal_places=2)
    res_econom_acum = models.DecimalField(max_digits=12, decimal_places=2)
    stock_tarjeta = models.DecimalField(max_digits=12, decimal_places=2)
    stock_efectivo = models.DecimalField(max_digits=12, decimal_places=2)
    saldo_caja_mes = models.DecimalField(max_digits=12, decimal_places=2)
    saldo_caja_acum = models.DecimalField(max_digits=12, decimal_places=2)
    saldo_caja_neto = models.DecimalField(max_digits=12, decimal_places=2)
    res_finan_mes = models.DecimalField(max_digits=12, decimal_places=2)
    res_finan_acum = models.DecimalField(max_digits=12, decimal_places=2)

pre_save.connect(slug_Save, sender=Cad_est_finan)
post_save.connect(slug_Save, sender=Cad_est_finan)

"""FIN FINANZAS"""

