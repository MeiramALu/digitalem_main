from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('how/', views.how, name='how'),
    path('how/<slug:lab_slug>/', views.lab, name='lab'),
    path('how/<slug:lab_slug>/<slug:field_slug>/projects/', views.projects, name='projects'),
    path('how/<slug:lab_slug>/projects/', views.all_projects, name='all_projects'),
    path('how/<slug:lab_slug>/<slug:field_slug>/<slug:project_slug>/', views.project, name='project'),

    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),

    path('contact_form/', views.contact_form, name='contact_form'),
    path('mailing_form/', views.mailing_form, name='mailing_form'),

    path('admin/', admin.site.urls),
]