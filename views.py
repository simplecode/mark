# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from mark.models import Students, Mark, Labs
from datetime import datetime

def show(request):
    ''' Список студентов с оценками '''

    students = Students.objects.filter().order_by('pk')
    stud = Students.objects.all()
    labs = Labs.objects.all()
    lb = dict()
    for l in labs:
        lb[l.id] = ""
    mrk = dict()
    for s in stud:
        mrk[s.id] = {'name' : s, 'labs' : lb.copy()}
    
    m = Mark.objects.all()
    for i in m:
        mrk[i.student.id]['labs'][i.lab.id] = i.mark
    return render_to_response('show.html',locals())

def put(request):
    ''' Добавление оценки '''

    if request.method == 'POST':
        stud = Students.objects.get(id=request.POST['stud'])
        lab = Labs.objects.get(id=request.POST['lab'])
        mark = request.POST['mark']
        m = Mark.objects.filter(student=stud, lab=lab)
        m.delete()
        if mark != "0":
            m = Mark.objects.create(mark=mark, student=stud, lab=lab)
            print m
            return HttpResponse(m.mark)
        else:
            return HttpResponse("")
    else:
        return HttpResponse("")

def stud_add(request):
    ''' Добавление студента '''

    if request.method == 'POST':
        Students(l_name=request.POST['l_name'], f_name=request.POST['f_name'], s_name=request.POST['s_name']).save()
    return HttpResponse("OK")
    
def stud_del(request, stud):
    ''' Удаление студента '''

    Students.objects.get(id=stud).delete()
    return HttpResponse("OK")














