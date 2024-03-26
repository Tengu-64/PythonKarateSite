from django.db import models

class Dictionary(models.Model):
    name = models.CharField(max_length=50, verbose_name='термин')
    translate = models.CharField(max_length=50, verbose_name='значение')

    class Meta:
        verbose_name = 'словарь'
        verbose_name_plural = 'словарь'
        ordering = ['name']


class Belt(models.Model):
    kyu = models.CharField(max_length=3, null=True, verbose_name='кю')
    color = models.TextField(verbose_name='пояс')
    belt_img = models.ImageField('photos/', null=True)
    about_belt = models.TextField(null=True, verbose_name='значение пояса')

    class Meta:
        verbose_name = 'пояса'
        verbose_name_plural = 'пояса'
        ordering = ['kyu']


class Info(models.Model):
    kata = models.TextField(verbose_name='ката')
    kata_img = models.ImageField('photos/', null=True)
    hits = models.TextField(verbose_name='удары')
    blocks = models.TextField(verbose_name='блоки')
    sit_ups = models.PositiveSmallIntegerField(verbose_name='кол-во приседаний')
    push_ups = models.PositiveSmallIntegerField(verbose_name='кол-во отжиманий')
    press = models.PositiveSmallIntegerField(verbose_name='пресс')
    kumite = models.PositiveSmallIntegerField(verbose_name='кумитэ(поединок)')
    info = models.ForeignKey(Belt, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'информация об экзамене'
        verbose_name_plural = 'информация об экзамене'

