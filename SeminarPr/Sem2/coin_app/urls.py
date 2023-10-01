from django.urls import path
from . import views

urlpatterns = [
    path('', views.heads_or_tails, name='start_coin'),
    path('statistic/', views.statistic, name='statistic')
]