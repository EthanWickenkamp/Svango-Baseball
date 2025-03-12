from django.utils.timezone import now
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from .models import Item, Team, Game, Player, GameStat, AtBat
from .serializers import ItemSerializer, TeamSerializer, GameSerializer, PlayerSerializer, GameStatSerializer, AtBatSerializer

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    def get_queryset(self):
        queryset = Player.objects.all()
        team_param = self.request.query_params.get('team')

        if team_param == "null":
            return queryset.filter(team__isnull=True)
        elif team_param is not None:
            return queryset.filter(team=team_param)
        return queryset 

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameStatViewSet(viewsets.ModelViewSet):
    queryset = GameStat.objects.all()
    serializer_class = GameStatSerializer

class AtBatViewSet(viewsets.ModelViewSet):
    queryset = AtBat.objects.all()
    serializer_class = AtBatSerializer


@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, API is working!"})

# @csrf_exempt
# @api_view(["POST"])
# def start_game(request):
#     """
#     Creates a new game if one doesn't already exist today for the same teams.
#     Also creates GameStat entries for selected players.
#     """
#     home_team_id = request.data.get("home_team_id")
#     away_team_id = request.data.get("away_team_id")
#     selected_player_ids = request.data.get("players", [])

#     if not home_team_id or not away_team_id or not selected_player_ids:
#         return Response({"error": "Home team, away team, and players are required"}, status=400)

#     try:
#         home_team = Team.objects.get(id=home_team_id)
#         away_team = Team.objects.get(id=away_team_id)
#     except Team.DoesNotExist:
#         return Response({"error": "Invalid team IDs"}, status=400)

#     today = now().date()
#     game, created = Game.objects.get_or_create(
#         home_team=home_team,
#         away_team=away_team,
#         game_date=today
#     )

#     # Create GameStat entries for selected players
#     for player_id in selected_player_ids:
#         try:
#             player = Player.objects.get(id=player_id)
#             GameStat.objects.get_or_create(player=player, game=game, team=player.team)
#         except Player.DoesNotExist:
#             continue  # Skip invalid players

#     return Response({"game_id": game.id, "message": "Game started successfully"}, status=201)

@api_view(['GET', 'POST'])  # Temporarily allow GET for testing
def start_game(request):
    if request.method == "GET":
        return Response({"message": "GET request successful! API is correctly mapped."}, status=200)

    if request.method == "POST":
        return Response({"message": "Game Started!"}, status=201)

    return Response({"error": "Method Not Allowed"}, status=405)