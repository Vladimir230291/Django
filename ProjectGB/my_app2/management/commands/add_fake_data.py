from django.core.management import BaseCommand
from my_app2.models import Author, Post


class Command(BaseCommand):
    help = "Generate fake data"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of posts')


    def handle(self, *args, **options):
        count = options.get('count')
        for i in range(count):
            author = Author(name=f'Fake_name{i}', email=f'fake{i}@mail.ru')
            author.save()
            for j in range(1, count+1):
                post = Post(title=f'Fake_title{j}', content=f'Fake_content{j} by {author.name}', author=author)
                post.save()