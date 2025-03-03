from django.db import models
from django.contrib.auth.models import User
from inventory.models import Location, Conteiner

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class UserGroup(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=127)
    description = models.TextField(verbose_name="Descrição", max_length=1024, null=True, blank=True)
    users = models.ManyToManyField(User, blank=True)
    locations = models.ManyToManyField(Location, blank=True)
    conteiners = models.ManyToManyField(Conteiner, blank=True)

    def __str__(self):
        return self.name
