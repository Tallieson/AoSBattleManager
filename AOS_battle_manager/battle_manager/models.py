from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class AdditionalRule(models.Model):
    name = models.CharField(max_length=50)
    effect = models.CharField(max_length=1000)
    custom = models.BooleanField(default=False)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class BattleType(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class BattlePlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, null=True)
    setup = models.CharField(max_length=1000, default="Enter setup info")
    victory = models.CharField(max_length=1000, default="Enter victory info")
    aditional_rules = models.ManyToManyField(AdditionalRule)
    battle_type = models.OneToOneField(BattleType, on_delete=models.CASCADE, null=True)
    custom = models.BooleanField(default=False)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    deployment_map = models.ImageField(upload_to='', default='no-image-found.png')

    def __str__(self):
        return self.name

class Realm(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Spell(models.Model):
    name = models.CharField(max_length=50)
    effect = models.CharField(max_length=1000)
    realm_specific = models.BooleanField(default=False)
    specific_realm_id = models.ForeignKey(Realm, on_delete=models.CASCADE, null=True)
    battle_specific = models.BooleanField(default=False)
    specific_battle_id = models.ForeignKey(BattlePlan, on_delete=models.CASCADE, null=True)
    custom = models.BooleanField(default=False)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class CommandAbility(models.Model):
    name = models.CharField(max_length=50)
    effect = models.CharField(max_length=1000)
    realm_specific = models.BooleanField(default=False)
    specific_realm_id = models.ForeignKey(Realm, on_delete=models.CASCADE, null=True)
    battle_specific = models.BooleanField(default=False)
    specific_battle_id = models.ForeignKey(BattlePlan, on_delete=models.CASCADE, null=True)
    custom = models.BooleanField(default=False)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class RealmFeature(models.Model):
    name = models.CharField(max_length=50)
    effect = models.CharField(max_length=1000)
    realm_specific = models.BooleanField(default=False)
    specific_realm_id = models.ForeignKey(Realm, on_delete=models.CASCADE, null=True)
    battle_specific = models.BooleanField(default=False)
    specific_battle_id = models.ForeignKey(BattlePlan, on_delete=models.CASCADE, null=True)
    custom = models.BooleanField(default=False)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class TerrainFeature(models.Model):
    name = models.CharField(max_length=50)
    effect = models.CharField(max_length=1000)
    realm_spell = models.BooleanField(default=False)
    specific_realm_id = models.ForeignKey(Realm, on_delete=models.CASCADE, null=True)
    battle_specific = models.BooleanField(default=False)
    specific_battle_id = models.ForeignKey(BattlePlan, on_delete=models.CASCADE, null=True)
    custom = models.BooleanField(default=False)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name




