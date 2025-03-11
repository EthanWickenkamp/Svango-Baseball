from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import viewsets
from .models import Item, Team, Game, Player, GameStat, AtBat
from .serializers import ItemSerializer, TeamSerializer, GameSerializer, PlayerSerializer, GameStatSerializer, AtBatSerializer

# Create your views here.
@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, API is working!"})



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_queryset(self):
        queryset = Player.objects.all()
        team_param = self.request.query_params.get('team')

        if team_param == 'null':  # Allows fetching free agents
            queryset = queryset.filter(team__isnull=True)
        elif team_param is not None:
            queryset = queryset.filter(team=team_param)

        return queryset

class GameStatViewSet(viewsets.ModelViewSet):
    queryset = GameStat.objects.all()
    serializer_class = GameStatSerializer

class AtBatViewSet(viewsets.ModelViewSet):
    queryset = AtBat.objects.all()
    serializer_class = AtBatSerializer

    def get_queryset(self):
        queryset = AtBat.objects.all()
        game_id = self.request.query_params.get('game')
        if game_id:
            queryset = queryset.filter(game_id=game_id)
        return queryset




