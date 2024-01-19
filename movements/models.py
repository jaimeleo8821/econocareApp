from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#   TABLA DE TIPO DE MOVIMIENTO     #
class Type(models.Model):
    type = models.CharField(max_length=100, verbose_name="Tipo")

    class Meta:
        verbose_name = 'Tipo de Movimiento'
        verbose_name_plural = 'Tipos de Movimientos'

    def __str__(self):
        return self.type


#   TABLA DE CATEGORÍA DE MOVIMIENTO     #
class Category(models.Model):
    idType = models.ForeignKey(Type, verbose_name="Tipo", on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name="Categoría")

    class Meta:
        verbose_name = 'Categoría de Movimiento'
        verbose_name_plural = 'Categoría de Movimientos'

    def __str__(self):
        return self.category
    

#   TABLA DE MÉTODO DE PAGO     #
class Pay_Method(models.Model):
    payMethod = models.CharField(max_length=100, verbose_name="Método de Pago")

    class Meta:
        verbose_name = 'Método de Pago'
        verbose_name_plural = 'Métodos de Pago'

    def __str__(self):
        return self.payMethod
    

#   TABLA DE MOVIMIENTOS     #
class Movement(models.Model):
    date = models.DateField(verbose_name="Fecha")
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    idType = models.ForeignKey(Type, verbose_name="Tipo", on_delete=models.CASCADE, null=False, blank=False)
    idCategory = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE, null=False, blank=False)
    idPayMethod = models.ForeignKey(Pay_Method, verbose_name="Método de Pago", on_delete=models.CASCADE, null=False, blank=False)
    observations = models.CharField(max_length=100, verbose_name="Observaciones")
    user = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'

    def __str__(self):
        return self.observations