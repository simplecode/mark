# -*- coding: utf-8 -*-
from django.db import models, connection

class Students(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    s_name = models.CharField(max_length=100)

    class Meta:
        db_table = u'students'
        ordering = ['l_name', 'f_name', 's_name']
        verbose_name = ('студента')
        verbose_name_plural = ('студенты')

    def __unicode__(self):
        return u'%s %s %s' % (self.l_name, self.f_name, self.s_name)

class Labs(models.Model):
    name    = models.CharField(max_length=255)
    pos     = models.IntegerField()

    class Meta:
        db_table = u'labs'
        verbose_name = ('лабораторную работу')
        verbose_name_plural = ('лабораторные работы')

    def __unicode__(self):
        return u'%s' % self.name


class Assesment(models.Model):
    student  = models.ForeignKey(Students, blank=True, related_name='assesments')
    lab      = models.ForeignKey(Labs, blank=True, related_name='assesments')
    mark     = models.IntegerField(null=True, blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = u'mark'
        unique_together = ('student', 'lab',)
        verbose_name = ('оценку')
        verbose_name_plural = ('оценки')

    def __unicode__(self):
        return u'%s' % self.mark