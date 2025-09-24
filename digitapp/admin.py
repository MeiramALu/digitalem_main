from django import forms
from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget


class LabAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Lab
        fields = '__all__'

class ProjectAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Project
        fields = '__all__'


class LabAdmin(admin.ModelAdmin):
    form = LabAdminForm
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

admin.site.register(Lab, LabAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Application)
admin.site.register(Mailing)
admin.site.register(Field)




