from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Location(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=127)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Dono')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Pai')

    def __str__(self):
        return self.name


class Conteiner(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=127)
    location = models.ForeignKey(Location, verbose_name="Local", on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Dono')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Pai')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=127)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=127)
    description = models.TextField(verbose_name="Descrição", max_length=1024, null=True, blank=True)
    conteiner = models.ForeignKey(Conteiner, verbose_name="Conteiner", on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Dono')
    last_conference = models.DateField(verbose_name="Ultima conferência", null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Food(Item):
    expiration_date = models.DateField(verbose_name="Data de vencimento", null=True, blank=True)


class Clothe(Item):

    TYPE_UP = 1
    TYPE_BOTTOM = 2
    TYPE_HEAD = 3
    TYPE_FEET = 4

    TYPES_NAMES = (
        (TYPE_UP, "Superior"),
        (TYPE_BOTTOM, "Inferior"),
        (TYPE_HEAD, "Cabeça"),
        (TYPE_FEET, "Pés")
    )

    size = models.CharField(verbose_name="Tamanho", max_length=127)
    body_place = models.PositiveSmallIntegerField(choices=TYPES_NAMES)


class Medicine(Item):
    expiration_date = models.DateField(verbose_name="Data de vencimento", null=True, blank=True)
