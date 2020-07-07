from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Realm, RealmFeature, CommandAbility, Spell, TerrainFeature, AdditionalRule, BattlePlan, BattleType, Source

# Create your views here.
def battle_manager(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'battle_manager/battle_manager.html', context)


def generate_battle(request):
    context = {
        'Types': BattleType.objects.all(),
        'Realms': Realm.objects.all(),
        'RealmFeatures': RealmFeature.objects.all(),
        'TerrainFeatures': TerrainFeature.objects.all(),
        'BattlePlans': BattlePlan.objects.all()
    }
    return render(request, 'battle_manager/generate.html', context)

