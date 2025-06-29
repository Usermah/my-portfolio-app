from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Creates an admin user if none exists'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'AdminPassword123')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created!"))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))
