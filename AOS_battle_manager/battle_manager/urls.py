from django.urls import path
from . import views

app_name = 'battle_manager'
urlpatterns = [
  path('', views.battle_manager, name='battle_manager'),
  path('generate', views.generate_battle, name='generate'),
]