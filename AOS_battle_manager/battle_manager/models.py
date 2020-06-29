from django.db import models

# Create your models here.
class Realm(models.Model):
    name = models.CharField(max_length=200)


class Spell(models.Model):
    name = models.CharField(max_length=200)
    effect = models.CharField(max_length=1000)
    realm_specific = models.BooleanField
    specific_realm_id = models.IntegerField
    battle_specific = models.BooleanField
    specific_battle_id = models.IntegerField

class CommandAbility(models.Model):
    name = models.CharField(max_length=200)
    effect = models.CharField(max_length=1000)
    realm_specific = models.BooleanField
    specific_realm_id = models.IntegerField
    battle_specific = models.BooleanField
    specific_battle_id = models.IntegerField

class RealmFeature(models.Model):
    name = models.CharField(max_length=200)
    effect = models.CharField(max_length=1000)
    realm_specific = models.BooleanField
    specific_realm_id = models.IntegerField
    battle_specific = models.BooleanField
    specific_battle_id = models.IntegerField

class TerrainFeature(models.Model):
    name = models.CharField(max_length=200)
    effect = models.CharField(max_length=1000)
    realm_spell = models.BooleanField
    specific_realm_id = models.IntegerField
    battle_specific = models.BooleanField
    specific_battle_id = models.IntegerField

class AdditionalRules(models.Model):
    name = models.CharField(max_length=200)
    effect = models.CharField(max_length=1000)

class BattlePlans(models.Model):
    name = models.CharField(max_length=200)
    aditional_rules = models.ManyToManyField(AdditionalRules)

