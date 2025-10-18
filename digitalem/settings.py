# settings.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Безопасность ---
SECRET_KEY = os.getenv('SECRET_KEY', 'default-insecure-key-for-local-dev')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# --- Приложения ---
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Сторонние приложения
    'ckeditor',
    'import_export',
    'parler',
    #'captcha',  # <-- Добавлено для reCAPTCHA
    'allauth',  # <-- Добавлено для регистрации
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google', # <-- Раскомментируйте для входа через Google

    # Ваши приложения
    'digitapp',
    'users',
]

# ID сайта (требуется для allauth)
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'digitalem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'digitapp.context_processors.labs'
            ],
        },
    },
]

# Аутентификация (требуется для allauth)
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'digitalem.wsgi.application'

# ... (База данных и Валидация паролей остаются без изменений) ...
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}}
AUTH_PASSWORD_VALIDATORS = [{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
                            {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
                            {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
                            {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}]

# ... (Интернационализация и Статика/Медиа остаются без изменений) ...
LANGUAGE_CODE = 'ru'
LANGUAGES = [('ru', 'Русский'), ('kk', 'Қазақша'), ('en', 'English')]
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [BASE_DIR / 'locale']
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Настройки входа и выхода ---
# LOGIN_URL и LOGIN_REDIRECT_URL теперь управляются через allauth,
# но их можно оставить для совместимости.
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'account_login'  # <-- allauth использует это имя
LOGOUT_REDIRECT_URL = 'index'

# --- Настройки сторонних библиотек ---

# Настройки Gmail для отправки писем
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  # <-- Берется из .env
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # <-- Берется из .env
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Настройки reCAPTCHA
#RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')  # <-- Берется из .env
#RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')  # <-- Берется из .env

# Настройки django-allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3 # Срок действия ссылки (в днях)
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'account_login'# Куда перенаправить, если пользователь уже залогинен


# ... (CKEditor и Jazzmin остаются без изменений) ...
CKEDITOR_CONFIGS = {'default': {'height': 'full', 'width': 'full'}}
JAZZMIN_SETTINGS = {
    "site_title": "Digitalem Admin", "site_header": "Digitalem", "site_brand": "Digitalem",
    "welcome_sign": "Добро пожаловать в панель Digitalem", "copyright": "Digitalem Ltd.", "show_ui_builder": True,
    "topmenu_links": [{"name": "Главная", "url": "index"}, {"model": "auth.User"}],
    "icons": {"auth": "fas fa-users-cog", "auth.user": "fas fa-user", "auth.Group": "fas fa-users",
              "digitapp.Application": "fas fa-file-alt", "digitapp.Field": "fas fa-atom",
              "digitapp.Lab": "fas fa-flask", "digitapp.Mailing": "fas fa-envelope-open-text",
              "digitapp.Project": "fas fa-project-diagram", "digitapp.TeamMember": "fas fa-user-friends",
              "digitapp.SuccessFact": "fas fa-trophy"},
    "changeform_format": "horizontal_tabs",
}

X_FRAME_OPTIONS = 'SAMEORIGIN'