# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from mark.models import Students, Mark, Labs
from datetime import datetime

def show(request):
    ''' Список студентов с оценками '''

    stud = Students.objects.all()
    print stud
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
    return render_to_response('show.html', {'mrk': mrk, 'labs': labs})

def put(request):
    if request.method == 'POST':
        stud = Students.objects.get(id=request.POST['stud'])
        lab = Labs.objects.get(id=request.POST['lab'])
        mark = request.POST['mark']
        m = Mark.objects.filter(student=stud, lab=lab)
        m.delete()
        if mark != "0":
            m = Mark.objects.create(mark=mark, student=stud, lab=lab, mark_date=datetime.now())
            return HttpResponse(m.mark)
        else:
            return HttpResponse("")
    else:
        return HttpResponse("")

def stud_add(request):
    if request.method == 'POST':
        stud = Students(l_name=request.POST['l_name'], f_name=request.POST['f_name'], s_name=request.POST['s_name'])
        stud.save()
    return HttpResponse(stud)