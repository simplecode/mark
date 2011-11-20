# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from mark.models import Students
from models import Labs

class StudentForm(ModelForm):
    def as_p(self):
        return self._html_output(
            normal_row = u'<p%(html_class_attr)s>%(field)s %(label)s%(help_text)s</p>',
            error_row = u'%s',
            row_ender = '</p>',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)

    class Meta:
        model = Students

class LabForm(ModelForm):
    def as_p(self):
        return self._html_output(
            normal_row = u'<p%(html_class_attr)s>%(field)s %(label)s%(help_text)s</p>',
            error_row = u'%s',
            row_ender = '</p>',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)

    class Meta:
        model = Labs
