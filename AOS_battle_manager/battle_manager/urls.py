from django.urls import path
from . import views

app_name = 'battle_manager'
urlpatterns = [
  path('', views.battle_manager, name='battle_manager'),
  path('generate', views.generate_battle, name='generate'),
  path('get_realm_features', views.get_realm_features, name='get_realm_features'),
  path('get_battle_plans', views.get_battle_plans, name='get_battle_plans'),
  path('create_battle', views.create_battle, name='create_battle'),
  path('battle/<int:id>', views.battle, name='battle'),
]