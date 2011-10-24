# -*- coding: utf-8 -*-
from django.db import models, connection

class Students(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    s_name = models.CharField(max_length=100)

    def get_marks(self):
        return Mark.objects.filter(student=self)

    class Meta:
        db_table = u'students'
        ordering = ['l_name', 'f_name', 's_name']

    def __unicode__(self):
        return u'%s %s %s' % (self.l_name, self.f_name, self.s_name)

class Labs(models.Model):
    name = models.CharField(max_length=255)
    pos = models.IntegerField()

    def get_mark(self):
        return Mark.objects.get(lab=self)

    class Meta:
        db_table = u'labs'

    def __unicode__(self):
        return u'%s' % self.name


class Mark(models.Model):
    mark     = models.IntegerField(null=True, blank=True)
    student  = models.ForeignKey(Students, blank=True)
    lab      = models.ForeignKey(Labs, blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def labs(self):
        pass

    class Meta:
        db_table = u'mark'
    def __unicode__(self):
        return u'%s' % self.mark