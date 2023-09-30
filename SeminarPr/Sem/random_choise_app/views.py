import random
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)
# Create your views here.


# рандомный выбор монетки
def one(request):
    logger.info('random_choise_app_one')
    return HttpResponse(random.choice(['Орел', 'Решка']))


# рандомный выбор игрального кубика(шесть граней)
def two(request):
    logger.info('random_choise_app_two')
    return HttpResponse(random.randint(1, 6))


# Случайное число от 0 до 100
def three(request):
    logger.info('random_choise_app_three')
    return HttpResponse(random.randint(0, 100))
