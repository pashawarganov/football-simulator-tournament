from django.urls import path

from tournament.views import (
    index,
    TeamListView,
    TeamDetailView,
    TeamCreationView,
    TeamUpdateView,
    TeamDeleteView,
    LeagueListView,
    LeagueCreationView,
    LeagueUpdateView,
    LeagueDeleteView,
    PlayerListView,
    PlayerDetailView,
    PlayerCreateView,
    PlayerUpdateView,
    PlayerDeleteView,
    GameSessionListView,
    GameSessionDetailView,
    GameSessionCreationView,
    GameSessionUpdateView,
    GameSessionDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("leagues/", LeagueListView.as_view(), name="league-list"),
    path("leagues/create/", LeagueCreationView.as_view(), name="league-create"),
    path("leagues/<int:pk>/update/", LeagueUpdateView.as_view(), name="league-update"),
    path("leagues/<int:pk>/delete/", LeagueDeleteView.as_view(), name="league-delete"),

    path("teams/", TeamListView.as_view(), name="team-list"),
    path("teams/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("teams/create/", TeamCreationView.as_view(), name="team-create"),
    path("teams/<int:pk>/update/", TeamUpdateView.as_view(), name="team-update"),
    path("teams/<int:pk>/delete/", TeamDeleteView.as_view(), name="team-delete"),

    path("players/", PlayerListView.as_view(), name="player-list"),
    path("players/<int:pk>/", PlayerDetailView.as_view(), name="player-detail"),
    path("players/create/", PlayerCreateView.as_view(), name="player-create"),
    path("players/<int:pk>/update/", PlayerUpdateView.as_view(), name="player-update"),
    path("players/<int:pk>/delete/", PlayerDeleteView.as_view(), name="player-delete"),

    path("game-sessions/", GameSessionListView.as_view(), name="game-session-list"),
    path("game-sessions/<int:pk>/", GameSessionDetailView.as_view(), name="game-session-detail"),
    path("game-sessions/create/", GameSessionCreationView.as_view(), name="game-session-create"),
    path("game-sessions/<int:pk>/update/", GameSessionUpdateView.as_view(), name="game-session-update"),
    path("game-sessions/<int:pk>/delete/", GameSessionDeleteView.as_view(), name="game-session-delete"),
]

app_name = 'tournament'
