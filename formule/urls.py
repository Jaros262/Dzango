from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('racers/', views.racerListView.as_view(), name='racers'),
    path('racers/<int:pk>', views.racerDetailView.as_view(), name='racer_detail'),
    path('nations/', views.nationsListView.as_view(), name='nations'),
    path('nations/<int:pk>', views.nationsDetailView.as_view(), name='nation_detail'),
]