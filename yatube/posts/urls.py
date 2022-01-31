app_name = 'posts'

from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Список групп
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]