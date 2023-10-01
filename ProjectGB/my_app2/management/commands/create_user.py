from django.core.management import BaseCommand
from my_app2.models import User


class Command(BaseCommand):
    help = 'Create user'

    def handle(self, *args, **kwargs):
        user = User(name='John', email='admin@mail.ru', password='admin', age=18)
        user.save()
        self.stdout.write(f"{user}")
