import re
from random import shuffle
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import User, Realm, RealmFeature, CommandAbility, Spell, TerrainFeature, AdditionalRule, BattlePlan, BattleType, Source, Battle


def battle_manager(request):
    context = {
        'message': "<br><br><h2>IT'S ALLIIVVVVEEEE!!<h2><br><br>"
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
    )
    new_battle.save()
    return redirect(f'battle/{new_battle.id}')


def battle(request, id):
    this_battle = Battle.objects.get(id=id)
    realm_spells = Spell.objects.filter(specific_realm_id=this_battle.realm.id)
    realm_commands = CommandAbility.objects.filter(specific_realm_id=this_battle.realm.id)
    terrain_effects = TerrainFeature.objects.all()
    terrain_effect_list = list(terrain_effects)
    terrain_dict = {}
    spell_dict = {}
    command_dict = {}
    
    for i in range(this_battle.terrain):
        shuffle(terrain_effect_list)
        terrain_dict.update({f"{i + 1} - {terrain_effect_list[i].name}":terrain_effect_list[i].effect})

    for spell in realm_spells:
        spell_dict.update({spell.name:spell.effect})
    
    for command in realm_commands:
        command_dict.update({command.name:command.effect})

    battle_specific_rules = this_battle.battle_plan.battle_specific_rules
    if battle_specific_rules:
        reg = r'[A-Z ]+:'
        results = re.findall(reg, battle_specific_rules)
        fixed_specific_rules = battle_specific_rules
        for result in results:
            result = result.lstrip()
            fixed_specific_rules = fixed_specific_rules.replace(result, f"<br><b>{result}</b>")
    context = {
       'Battle': this_battle,
       'SpecificRules': fixed_specific_rules,
       'Spells': spell_dict,
       'CommandAbilities': command_dict,
       'TerrainEffects': terrain_dict,
    }
    return render(request, 'battle_manager/battle.html', context)

   




    