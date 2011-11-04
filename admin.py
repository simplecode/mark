from django.contrib.admin import site, ModelAdmin
from models import Labs, Students, Assessment

class AdminLabs(ModelAdmin):
        list_display = ('name',)

class AdminStudents(ModelAdmin):
        list_display = ('f_name', 'l_name', 's_name')

class AdminAssessment(ModelAdmin):
        list_display = ('student', 'lab', 'mark', 'date_pub')

site.register(Labs, AdminLabs)
site.register(Students, AdminStudents)
site.register(Assessment, AdminAssessment)
