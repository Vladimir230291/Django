from django.core.management import BaseCommand
from my_app2.models import Author, Post


class Command(BaseCommand):
    help = 'get post by author id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = "all posts by author id\n"
        text = '\n'.join(post.content for post in posts)
        self.stdout.write(f"{intro}{text}")