from tabnanny import verbose
from autoslug import AutoSlugField as Slug
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#   TABLA DE TIPO DE MOVIMIENTO     #
class Type(models.Model):
    type = models.CharField(max_length=100, verbose_name="Tipo")
    slug = Slug(populate_from='type', unique=True, max_length=150) # type: ignore

    class Meta:
        verbose_name = 'Tipo de Movimiento'
        verbose_name_plural = 'Tipos de Movimientos'

    def __str__(self):
        return self.type

#   TABLA DE ORIGEN DEL MOVIMIENTO     #
class Origin(models.Model):
    origin = models.CharField(max_length=100, verbose_name="Origen")
    slug = Slug(populate_from='origin', unique=True, max_length=150) # type: ignore

    class Meta:
        verbose_name = 'Origen del Movimiento'
        verbose_name_plural = 'Orígenes del Movimientos'

    def __str__(self):
        return self.origin


#   TABLA DE CATEGORÍA DE MOVIMIENTO     #
class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name="Categoría")
    idType = models.ForeignKey(Type, verbose_name="Tipo", on_delete=models.CASCADE, null=True, blank=True)
    slug = Slug(populate_from='category', unique=True, max_length=150) # type: ignore

    class Meta:
        verbose_name = 'Categoría de Movimiento'
        verbose_name_plural = 'Categoría de Movimientos'
        unique_together = ('id', 'idType')

    def __str__(self):
        return self.category
    

#   TABLA DE MÉTODO DE PAGO     #
class Pay_Method(models.Model):
    payMethod = models.CharField(max_length=100, verbose_name="Método de Pago")
    slug = Slug(populate_from='payMethod', unique=True, max_length=150) # type: ignore

    class Meta:
        verbose_name = 'Método de Pago'
        verbose_name_plural = 'Métodos de Pago'

    def __str__(self):
        return self.payMethod
    

#   TABLA DE MOVIMIENTOS     #
class Movement(models.Model):
    idOrigin = models.ForeignKey(Origin, verbose_name="Origen", on_delete=models.CASCADE, null=False, blank=False)
    idType = models.ForeignKey(Type, verbose_name="Tipo", on_delete=models.CASCADE, null=False, blank=False)
    idCategory = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE, null=False, blank=False)
    idPayMethod = models.ForeignKey(Pay_Method, verbose_name="Método de Pago", on_delete=models.CASCADE, null=False, blank=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    observations = models.CharField(max_length=100, verbose_name="Observaciones")
    date = models.DateField(verbose_name="Fecha")
    idUser = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.CASCADE, null=False, blank=False)
    slug = Slug(populate_from='id', unique=True, max_length=150) # type: ignore

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        unique_together = ('id', 'idOrigin','idType', 'idCategory', 'idPayMethod', 'idUser')

    def __str__(self):
        return self.observations