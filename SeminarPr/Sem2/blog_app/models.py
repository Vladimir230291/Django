from django.db import models


# Create your models here.

class Autor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birth_date = models.DateField()

    @staticmethod
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_views = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)
