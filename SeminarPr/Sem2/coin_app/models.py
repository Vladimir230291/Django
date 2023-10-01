from django.db import models
from django.utils import timezone


# Create your models here.

class HeadsTails(models.Model):
    objects = None
    rest_time = models.DateTimeField(default=timezone.now)
    result = models.CharField(max_length=10)

    def __str__(self):
        return f"time {self.rest_time} result {self.result}"

    @staticmethod
    def stat_coin(n):
        n = int(n)
        dict_res = {"Орел": 0, "Решка": 0}
        queryset = list(HeadsTails.objects.all())
        list_res = queryset[-n:]
        for item in list_res:
            dict_res[item.result] += 1
        return dict_res
