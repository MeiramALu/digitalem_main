# management/commands/send_newsletter.py
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from ...models import Mailing # Укажите правильный путь к модели

class Command(BaseCommand):
    help = 'Sends a newsletter to all subscribers'

    def handle(self, *args, **kwargs):
        subscribers = Mailing.objects.all()
        emails = [s.email for s in subscribers]

        subject = 'Наша еженедельная рассылка!'
        message = 'Привет! Это наши последние новости...'
        from_email = 'info@digitalem.kz'

        send_mail(subject, message, from_email, emails)

        self.stdout.write(self.style.SUCCESS(f'Successfully sent newsletter to {len(emails)} subscribers.'))