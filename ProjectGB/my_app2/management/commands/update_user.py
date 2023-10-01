from django.core.management import BaseCommand
from my_app2.models import User


class Command(BaseCommand):
    help = "update user"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User id')
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f"{user}")