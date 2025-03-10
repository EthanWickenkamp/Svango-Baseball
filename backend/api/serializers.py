from rest_framework import serializers
from .models import Item, Team, Game, Player, GameStat, AtBat

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class GameStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameStat
        fields = '__all__'

class AtBatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtBat
        fields = '__all__'
