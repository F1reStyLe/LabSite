from django.db import models


class Base(models.Model):
    """Основа эмали-пасты"""
    name = models.CharField(max_length=100, verbose_name='Наименование')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'База'
        verbose_name_plural = 'Базы'


class PigmentGroup(models.Model):
    """Группа пигментов"""
    name = models.CharField(max_length=100, verbose_name='Группа пигментов')

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Группа пигментов'
        verbose_name_plural = 'Группы пигментов'


class Pigment(models.Model):
    """Пигмент"""
    name = models.CharField(max_length=100, verbose_name='Наименование пигмента')
    pigment_group = models.ForeignKey(PigmentGroup, on_delete=models.SET_NULL, null=True, verbose_name='Пигментная группа')

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Пигмент'
        verbose_name_plural = 'Пигменты'


class PigmentPaste(models.Model):
    """Пигментная паста"""
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование пигментной пасты')
    grid = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Перетир')
    time = models.TimeField(blank=True, null=True, verbose_name='Время затирания')
    production_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата изготовления')
    base = models.OneToOneField(Base, on_delete=models.SET_NULL, null=True, verbose_name='Основа')
    pigment = models.OneToOneField(Pigment, on_delete=models.SET_NULL, null=True, verbose_name='Пигмент')

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Пигментная паста'
        verbose_name_plural = 'Пигментные пасты'


class Enamel(models.Model):
    """Эмаль"""
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование эмали')
    colour = models.CharField(max_length=100, verbose_name='Цвет')
    base = models.OneToOneField(Base, on_delete=models.SET_NULL, null=True, verbose_name='Основа')
    pigment_paste = models.ForeignKey(PigmentPaste, on_delete=models.SET_NULL, null=True, verbose_name='Пигментная паста')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Эмаль'
        verbose_name_plural = 'Эмали'
