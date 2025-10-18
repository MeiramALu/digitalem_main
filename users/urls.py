# users/urls.py (или ваш главный urls.py)

from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [

    path('logout/', auth_views.LogoutView.as_view(next_page='logout_page'), name='logout'),

    path('logged-out/', TemplateView.as_view(template_name='users/logout.html'), name='logout_page'),
]