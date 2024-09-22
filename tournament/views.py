from django.shortcuts import render
from django.views.generic import ListView, DetailView

from tournament.models import Player, Team, GameSession, League


def index(request):
    """View function for the home page of the site."""

    num_players = Player.objects.count()
    num_teams = Team.objects.count()
    num_game_sessions = GameSession.objects.count()
    num_leagues = League.objects.count()

    context = {
        "num_players": num_players,
        "num_teams": num_teams,
        "num_game_sessions": num_game_sessions,
        "num_leagues": num_leagues,
    }

    return render(request, "tournament/index.html", context=context)


class LeagueListView(ListView):
    model = League
    context_object_name = "league_list"
    paginate_by = 5


class TeamListView(ListView):
    model = Team
    context_object_name = "team_list"
    paginate_by = 5
    queryset = Team.objects.select_related("league")


class TeamDetailView(DetailView):
    model = Team


class GameSessionListView(ListView):
    model = GameSession
    context_object_name = "game_session_list"
    template_name = "tournament/game_session_list.html"
    paginate_by = 5
    queryset = GameSession.objects.select_related("team", "player")

class GameSessionDetailView(DetailView):
    model = GameSession
    template_name = "tournament/game_session_detail.html"
    context_object_name = "game_session"


class PlayerListView(ListView):
    model = Player
    context_object_name = "player_list"
    paginate_by = 5


class PlayerDetailView(DetailView):
    model = Player

