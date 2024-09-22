from django.urls import path

from tournament.views import (
    index,
    TeamListView,
    LeagueListView,
    PlayerListView,
    PlayerDetailView,
    GameSessionListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("leagues/", LeagueListView.as_view(), name="league-list"),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("players/", PlayerListView.as_view(), name="player-list"),
    path("players/<int:pk>", PlayerDetailView.as_view(), name="player-detail"),
    path("game-sessions/", GameSessionListView.as_view(), name="game-session-list"),
]

app_name = 'tournament'
