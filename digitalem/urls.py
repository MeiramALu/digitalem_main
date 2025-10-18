# digitalem/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


# Импортируем TemplateView для отображения статической страницы
from django.views.generic import TemplateView
from users import views as user_views
from django.contrib.auth import views as auth_views

# ШАГ 1: Определяем URL-адреса, которые НЕ будут переводиться
urlpatterns_main = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', user_views.login, name='login'),
    path('accounts/', include('allauth.urls')),

    # ИЗМЕНЕНИЕ №1: Этот URL теперь ТОЛЬКО для выполнения выхода.
    # Он перенаправляет на 'logout_page' после успешного выхода.
    path('logout/', auth_views.LogoutView.as_view(next_page='logout_page'), name='logout'),

    # ИЗМЕНЕНИЕ №2: Этот URL ТОЛЬКО для отображения страницы "Вы вышли".
    # Он использует ваш шаблон, который лежит в users/templates/logout.html
    path('logged-out/', TemplateView.as_view(template_name='users/logout.html'), name='logout_page'),
]

# ШАГ 2: Определяем URL-адреса, которые БУДУТ переводиться
urlpatterns_i18n = i18n_patterns(
    path('', include('digitapp.urls')),
)

# ШАГ 3: Объединяем оба списка
urlpatterns = urlpatterns_main + urlpatterns_i18n

# ШАГ 4: Добавляем медиа-файлы для режима разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)