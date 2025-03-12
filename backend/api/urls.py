from django.urls import path, include
from .views import start_game, ItemViewSet, TeamViewSet, GameViewSet, PlayerViewSet, GameStatViewSet, AtBatViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'games', GameViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'gamestat', GameStatViewSet)
router.register(r'atbats', AtBatViewSet)

urlpatterns = [
    #path('api/games/start/', start_game, name="start-game"),
    path('', include(router.urls)),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]