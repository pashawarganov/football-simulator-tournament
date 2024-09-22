from django.urls import path

from tournament.views import (
    index,
    TeamListView,
    TeamDetailView,
    LeagueListView,
    PlayerListView,
    PlayerDetailView,
    GameSessionListView,
    GameSessionDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("leagues/", LeagueListView.as_view(), name="league-list"),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("teams/<int:pk>", TeamDetailView.as_view(), name="team-detail"),
    path("players/", PlayerListView.as_view(), name="player-list"),
    path("players/<int:pk>", PlayerDetailView.as_view(), name="player-detail"),
    path("game-sessions/", GameSessionListView.as_view(), name="game-session-list"),
    path("game-sessions/<int:pk>", GameSessionDetailView.as_view(), name="game-session-detail"),
]

app_name = 'tournament'
