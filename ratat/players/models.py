from django.db import models
from django.contrib.auth.models import User


class Race(models.Model):
    name = models.CharField(max_length=255)
    frc = models.IntegerField()
    sta = models.IntegerField()
    agi = models.IntegerField()
    wit = models.IntegerField()
    per = models.IntegerField()
    lck = models.IntegerField()

    def __str__(self):
        return self.name


class Dass(models.Model):
    name = models.CharField(max_length=255)
    frc = models.IntegerField()
    sta = models.IntegerField()
    agi = models.IntegerField()
    wit = models.IntegerField()
    per = models.IntegerField()
    lck = models.IntegerField()

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    race = models.OneToOneField(Race)
    dass = models.OneToOneField(Dass)
    frc_bns = models.IntegerField()
    sta_bns = models.IntegerField()
    agi_bns = models.IntegerField()
    wit_bns = models.IntegerField()
    per_bns = models.IntegerField()
    lck_bns = models.IntegerField()

    @property
    def frc(self):
        return self.race.frc + self.dass.frc + self.frc_bns

    @property
    def sta(self):
        return self.race.sta + self.dass.sta + self.sta_bns

    @property
    def agi(self):
        return self.race.agi + self.dass.agi + self.agi_bns

    @property
    def wit(self):
        return self.race.wit + self.dass.wit + self.wit_bns

    @property
    def per(self):
        return self.race.per + self.dass.per + self.per_bns

    @property
    def lck(self):
        return self.race.lck + self.dass.lck + self.lck_bns

    def __str__(self):
        return self.name
