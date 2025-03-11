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
    players = PlayerSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = '__all__'


class AtBatSerializer(serializers.ModelSerializer):
    player = serializers.SerializerMethodField()

    class Meta:
        model = AtBat
        fields = '__all__'

    def get_player(self, obj):
        return obj.gamestat.player.name


class GameStatSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    team = serializers.SerializerMethodField()
    atbats = AtBatSerializer(many=True, source="atbat")

    class Meta:
        model = GameStat
        fields = '__all__'

    def get_team(self, obj):
        return obj.player.team.name


class GameSerializer(serializers.ModelSerializer):
    home_team = TeamSerializer(read_only=True)
    away_team = TeamSerializer(read_only=True)
    winner = serializers.ReadOnlyField()
    gamestats = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = '__all__'

    def get_gamestats(self, obj):
        return GameStatSerializer(obj.gamestat.all(), many=True).data
