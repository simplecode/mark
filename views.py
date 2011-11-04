# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from mark.models import Students, Assessment, Labs
from mark.forms import StudentForm

def show(request):
    ''' Список студентов с оценками '''
    
    forms = StudentForm(label_suffix='')
    students = Students.objects.filter().order_by('pk')
    labs = Labs.objects.all()
    return render_to_response('show.html',locals())

def put(request):
    ''' Добавление оценки '''

    if request.method == 'POST':
        stud = Students.objects.get(id=request.POST['stud'])
        lab = Labs.objects.get(id=request.POST['lab'])
        mark = request.POST['mark']
        if mark != "0":
            mark = Assessment(mark=mark, student=stud, lab=lab)
            mark.save()
            return HttpResponse(mark.mark)
        else:
            Assessment.objects.filter(student=stud, lab=lab).delete()
            return HttpResponse("")
    else:
        return HttpResponse("")

def stud_add(request):
    ''' Добавление студента '''

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            student = Students.objects.filter(f_name=data['f_name'], l_name=data['l_name'], s_name=data['s_name']).order_by('-id')[0]
            tr = "<tr id = 'st_%d'><td class='name' id='stud_%d'>%s %s %s</td>" % (student.id, student.id, data['f_name'], data['l_name'], data['s_name'])
            for lab in Labs.objects.all():
                tr += "<td class='mark' id='%d_%d' s='%d' l='%d'></td>" % (student.id, lab.id, student.id, lab.id,)
            tr += "</tr>"
            return HttpResponse(tr)
        else:
            return HttpResponse('not ok')



def stud_del(request, stud):
    ''' Удаление студента '''

    Students.objects.get(id=stud).delete()
    return HttpResponse("OK")














