from django.contrib.admin import site, ModelAdmin
from models import Labs, Students, Assesment

class AdminLabs(ModelAdmin):
        list_display = ('name', 'pos',)

class AdminStudents(ModelAdmin):
        list_display = ('f_name', 'l_name', 's_name')

class AdminAssesment(ModelAdmin):
        list_display = ('student', 'lab', 'mark', 'date_pub')

site.register(Labs, AdminLabs)
site.register(Students, AdminStudents)
site.register(Assesment, AdminAssesment)
