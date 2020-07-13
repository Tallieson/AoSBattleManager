import re
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import User, Realm, RealmFeature, CommandAbility, Spell, TerrainFeature, AdditionalRule, BattlePlan, BattleType, Source, Battle


def battle_manager(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'battle_manager/battle_manager.html', context)


def generate_battle(request):
    context = {
        'Types': BattleType.objects.all(),
        'Realms': Realm.objects.all(),
    }
    return render(request, 'battle_manager/generate.html', context)


#localhost:8000/get_realm_features/?realm_id=**
def get_realm_features(request):
    realm_id = request.GET['realm_id']
    realm_features = RealmFeature.objects.filter(specific_realm_id_id=realm_id)
    realm_features_json = []
    for realm_feature in realm_features:
        realm_features_json.append({
            'id': realm_feature.id,
            'name': realm_feature.name
        })
    return JsonResponse({'realm_features': realm_features_json})

def get_battle_plans(request):
    battle_type_id = request.GET['battle_type_id']
    battle_plans = BattlePlan.objects.filter(battle_type_id=battle_type_id)
    battle_plans_json = []
    for battle_plan in battle_plans:
        battle_plans_json.append({
            'id': battle_plan.id,
            'name': battle_plan.name,
            'source': battle_plan.source.name,
        })
    return JsonResponse({'battle_plans': battle_plans_json})


def create_battle(request):
    new_battle = Battle(
        battle_type = BattleType.objects.get(id=request.POST["battle_type"]),
        battle_plan = BattlePlan.objects.get(id=request.POST["battle_plan"]),
        realm = Realm.objects.get(id=request.POST["realm"]),
        realm_feature = RealmFeature.objects.get(id=request.POST["realm_feature"]),
        terrain = request.POST["terrain"]
        # terrain_features = request.POST["terrain"]
    )
    new_battle.save()
    return redirect(f'battle/{new_battle.id}')


def battle(request, id):
    this_battle = Battle.objects.get(id=id)
    additional_rules = this_battle.battle_plan.battle_specific_rules
    if additional_rules:
        print(additional_rules)
    context = {
       'Battle': this_battle
    }
    return render(request, 'battle_manager/battle.html', context)

   




    