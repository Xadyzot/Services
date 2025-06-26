from django.db import models
from django.utils.translation import gettext_lazy as _

class ServiceType(models.Model):
    type = models.CharField(max_length=100, verbose_name=_('Type'))
    title_en = models.CharField(max_length=100, verbose_name=_('Title en'))
    description_en = models.TextField(verbose_name=_('Description en'))
    title_ru = models.CharField(max_length=100, verbose_name=_('Title ru'))
    description_ru = models.TextField(verbose_name=_('Description ru'))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=_('Slug'))

    def __str__(self):
        return self.title_en


class Service(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    name_ru = models.CharField(max_length=100, verbose_name=_('Name (RU)'))
    name_en = models.CharField(max_length=100, verbose_name=_('Name (EN)'))
    description_ru = models.TextField(verbose_name=_('Description (RU)'))
    description_en = models.TextField(verbose_name=_('Description (EN)'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    image = models.ImageField(upload_to='images/', verbose_name=_('Image'))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=_('Slug'))

    def __str__(self):
        return self.name_en
