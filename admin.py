from django.contrib.admin import site, ModelAdmin
from models import Labs, Students, Assessment, Student, Teacher

class AdminLabs(ModelAdmin):
        list_display = ('name',)

class AdminStudents(ModelAdmin):
        list_display = ('f_name', 'l_name', 's_name')

class AdminAssessment(ModelAdmin):
        list_display = ('student', 'lab', 'mark', 'date_pub')


class AdminStudent(ModelAdmin):
    list_display = ('user', 'id_card', )

class AdminTeacher(ModelAdmin):
    pass

site.register(Teacher, AdminTeacher)
site.register(Student, AdminStudent)
site.register(Labs, AdminLabs)
site.register(Students, AdminStudents)
site.register(Assessment, AdminAssessment)
