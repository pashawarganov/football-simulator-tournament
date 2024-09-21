from django.shortcuts import render

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
