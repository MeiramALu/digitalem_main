from django import forms
from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from import_export.admin import ImportExportModelAdmin
from parler.admin import TranslatableAdmin

# --- ФОРМЫ С РЕДАКТОРОМ CKEDITOR ---
# (остаются без изменений)

class LabAdminForm(forms.ModelForm):
    # description = forms.CharField(widget=CKEditorWidget()) # Parler сам подхватит перевод
    class Meta:
        model = Lab
        fields = '__all__'

class ProjectAdminForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget()) # Parler сам подхватит перевод
    class Meta:
        model = Project
        fields = '__all__'


# --- АДМИН-КЛАССЫ ДЛЯ МОДЕЛЕЙ ---

# -- Непереводимые модели --

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'topic', 'email')
    search_fields = ('full_name', 'topic')

@admin.register(Mailing)
class MailingAdmin(ImportExportModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)

# -- Переводимые модели (наследуются от TranslatableAdmin) --

@admin.register(Lab)
class LabAdmin(TranslatableAdmin):
    # form = LabAdminForm # Parler автоматически использует CKEditor для RichTextField
    list_display = ('name',)
    search_fields = ('translations__name',) # Для поиска по переводимым полям

@admin.register(Project)
class ProjectAdmin(TranslatableAdmin):
    # form = ProjectAdminForm # Parler автоматически использует CKEditor для RichTextField
    list_display = ('name', 'lab', 'field')
    list_filter = ('lab', 'field')
    search_fields = ('translations__name', 'lab__translations__name') # Поиск по названию проекта и названию лаборатории

@admin.register(Field)
class FieldAdmin(TranslatableAdmin):
    list_display = ('name',)
    search_fields = ('translations__name',)

@admin.register(TeamMember)
class TeamMemberAdmin(TranslatableAdmin):
    list_display = ('name', 'position')
    search_fields = ('translations__name', 'translations__position')

@admin.register(SuccessFact)
class SuccessFactAdmin(TranslatableAdmin):
    list_display = ('title', 'value')
    search_fields = ('translations__title',)