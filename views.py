# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from mark.models import Students, Assessment, Labs

def show(request):
    ''' Список студентов с оценками '''

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
        Students(l_name=request.POST['l_name'], f_name=request.POST['f_name'], s_name=request.POST['s_name']).save()
    return HttpResponse("OK")
    
def stud_del(request, stud):
    ''' Удаление студента '''

    Students.objects.get(id=stud).delete()
    return HttpResponse("OK")














