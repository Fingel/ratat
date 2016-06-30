from rest_framework import serializers

from ratat.players.models import Race, Dass, Character


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'


class DassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dass
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'name', 'race', 'dass', 'frc_bns', 'sta_bns',
            'agi_bns', 'wit_bns', 'per_bns', 'lck_bns',
            'frc', 'sta', 'agi', 'wit', 'per', 'lck'
        )
