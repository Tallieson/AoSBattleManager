from django.contrib import admin
from .models import User, Realm, RealmFeature, CommandAbility, Spell, TerrainFeature, AdditionalRule, BattlePlan, BattleType, Source, Battle, Post

# Register your models here.
admin.site.register(User)
admin.site.register(Realm)
admin.site.register(RealmFeature)
admin.site.register(CommandAbility)
admin.site.register(Spell)
admin.site.register(TerrainFeature)
admin.site.register(AdditionalRule)
admin.site.register(BattlePlan)
admin.site.register(BattleType)
admin.site.register(Source)
admin.site.register(Battle)
admin.site.register(Post)