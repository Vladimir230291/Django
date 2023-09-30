from django.http import HttpResponse
from . import html_for_task
import logging

logger = logging.getLogger("hometask_app")

# Create your views here.

# какие то данные о сайте

def index(request):
    logger.info(f'Page was visited: {request.path}')
    return HttpResponse(html_for_task.index)


def about(request):
    logger.info(f'Page was visited: {request.path}')
    return HttpResponse(html_for_task.about)