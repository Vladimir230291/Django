import random
import logging
from django.http import HttpResponse
from coin_app.models import HeadsTails

logger = logging.getLogger("random_choice_app")


# Create your views here.


def heads_or_tails(request):
    result = random.choice(['Орел', 'Решка'])
    HeadsTails(result=result).save()
    return HttpResponse(result)


# вывод поличества орлов и решек. Количество определяется параметром get запроса

def statistic(request):
    dict_res = HeadsTails.stat_coin(request.GET.get('n', 10))
    return HttpResponse(f"Орлов: {dict_res['Орел']} Решек: {dict_res['Решка']}")
