# -*- coding: utf-8 -*-
from django.db import models, connection

class Students(models.Model):
    f_name = models.CharField(max_length=100, null = False, blank = False, verbose_name='Фамилия')
    l_name = models.CharField(max_length=100, null = False, blank = False, verbose_name='Имя')
    s_name = models.CharField(max_length=100, null = False, blank = False, verbose_name='Отчество')

    class Meta:
        db_table = u'students'
        ordering = ['l_name', 'f_name', 's_name']
        verbose_name = ('студента')
        verbose_name_plural = ('студенты')

    def __unicode__(self):
        return u'%s %s %s' % (self.l_name, self.f_name, self.s_name)

class Labs(models.Model):
    name    = models.CharField(max_length=255, null = False, blank = False)

    class Meta:
        db_table = u'labs'
        verbose_name = ('лабораторную работу')
        verbose_name_plural = ('лабораторные работы')

    def __unicode__(self):
        return u'%s' % self.name


class Assessment(models.Model):
    student  = models.ForeignKey(Students, blank=True, related_name='assessments')
    lab      = models.ForeignKey(Labs, blank=True, related_name='assessments')
    mark     = models.IntegerField(null=True, blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = u'mark'
        unique_together = ('student', 'lab',)
        verbose_name = ('оценку')
        verbose_name_plural = ('оценки')

    def __unicode__(self):
        return u'%s' % self.mark