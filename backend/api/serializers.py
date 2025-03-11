from rest_framework import serializers
from .models import Item, Team, Game, Player, GameStat, AtBat

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'



class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    #nest players in team api response very RESTful less calls
    players = PlayerSerializer(many=True)
    class Meta:
        model = Team
        fields = '__all__'

class AtBatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtBat
        fields = ['inning', 'outcome']

class GameSerializer(serializers.ModelSerializer):
    home_team = TeamSerializer()  # Fully serialize home team
    away_team = TeamSerializer()  # Fully serialize away team
    winner = serializers.ReadOnlyField()
    class Meta:
        model = Game
        fields = '__all__'



class GameStatSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    game = GameSerializer()
    atbats = AtBatSerializer(many=True, read_only=True)
    class Meta:
        model = GameStat
        fields = '__all__'