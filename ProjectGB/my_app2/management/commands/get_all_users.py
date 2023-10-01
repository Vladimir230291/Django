from django.core.management import BaseCommand
from my_app2.models import User


class Command(BaseCommand):
    help = "Get all users"

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            self.stdout.write(f"{user}")
