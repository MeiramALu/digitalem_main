from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

class Lab(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("Название"), max_length=100),
        description = models.TextField(_("Описание"))
    )
    # Эти поля не переводятся
    fields = models.ManyToManyField('Field', related_name='labs') # Я изменил related_name на 'labs' для ясности
    image = models.ImageField(upload_to='labs/')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lab', kwargs={'lab_slug': self.slug})

    class Meta:
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатории'


class Field(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("Название"), max_length=100),
        description = models.TextField(_("Описание"))
    )
    # Эти поля не переводятся
    image = models.ImageField(upload_to='fields/')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Project(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("Название"), max_length=100),
        description = models.TextField(_("Описание")),
        content = RichTextField(_("Содержание"))
    )
    # Эти поля не переводятся
    lab = models.ForeignKey('Lab', on_delete=models.CASCADE, related_name='projects')
    field = models.ForeignKey('Field', on_delete=models.CASCADE, related_name='projects')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)
    date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='project_images/')
    pdf_file = models.FileField(upload_to='project_pdfs/', blank=True, null=True, verbose_name="PDF Файл")
    youtube_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на YouTube")


    def save(self, *args, **kwargs):
        if not self.slug:
            # Берём русское название для создания слага
            self.slug = slugify(self.safe_translation_getter('name', language_code='ru'), allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project',
                       kwargs={'lab_slug': self.lab.slug, 'field_slug': self.field.slug, 'project_slug': self.slug})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Application(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    topic = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.full_name} - {self.topic}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Mailing(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class TeamMember(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('Имя и фамилия'), max_length=100),
        position = models.CharField(_('Должность'), max_length=100),
        description = models.TextField(_('Описание'))
    )
    # Это поле не переводится
    photo = models.ImageField(_('Фотография'), upload_to='team_photos/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Участник команды'
        verbose_name_plural = 'Участники команды'


class SuccessFact(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Заголовок"), max_length=100),
        value = models.CharField(_("Значение"), max_length=20)
    )

    def __str__(self):
        return f'{self.title}: {self.value}'

    class Meta:
        verbose_name = 'Факт об успехе'
        verbose_name_plural = 'Факты об успехе'