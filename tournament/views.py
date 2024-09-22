from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from tournament.forms import (
    LeagueSearchForm,
    TeamSearchForm,
    GameSessionSearchForm,
    PlayerSearchForm,
    PlayerCreationForm,
    PlayerScoreUpdateForm
)
from tournament.models import Player, Team, GameSession, League


def index(request):
    """View function for the home page of the site."""

    num_players = Player.objects.count()
    num_teams = Team.objects.count()
    num_game_sessions = GameSession.objects.count()
    num_leagues = League.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_players": num_players,
        "num_teams": num_teams,
        "num_game_sessions": num_game_sessions,
        "num_leagues": num_leagues,
        "num_visits": num_visits,
    }

    return render(request, "tournament/index.html", context=context)


class LeagueListView(ListView):
    model = League
    context_object_name = "league_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.session.get("name", "")
        context["search_form"] = LeagueSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        form = LeagueSearchForm(self.request.GET)
        self.queryset = League.objects.all()
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return self.queryset


class LeagueCreationView(CreateView):
    model = League
    fields = "__all__"
    success_url = reverse_lazy("tournament:league-list")


class LeagueUpdateView(UpdateView):
    model = League
    fields = "__all__"
    success_url = reverse_lazy("tournament:league-list")


class LeagueDeleteView(DeleteView):
    model = League
    success_url = reverse_lazy("tournament:league-list")


class TeamListView(ListView):
    model = Team
    context_object_name = "team_list"
    paginate_by = 5
    queryset = Team.objects.select_related("league")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.session.get("name", "")
        context["search_form"] = TeamSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        form = TeamSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return self.queryset


class TeamDetailView(DetailView):
    model = Team


class TeamCreationView(CreateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("tournament:team-list")


class TeamUpdateView(UpdateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("tournament:team-list")


class TeamDeleteView(DeleteView):
    model = Team
    success_url = reverse_lazy("tournament:team-list")


class GameSessionListView(ListView):
    model = GameSession
    context_object_name = "game_session_list"
    template_name = "tournament/game_session_list.html"
    paginate_by = 5
    queryset = GameSession.objects.select_related("team", "player")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        date = self.request.session.get("date", "")
        context["search_form"] = GameSessionSearchForm(
            initial={"date": date}
        )
        return context

    def get_queryset(self):
        form = GameSessionSearchForm(self.request.GET)
        if form.is_valid():
            date = form.cleaned_data["date"]
            if date:
                return self.queryset.filter(
                    date=date
                )
        return self.queryset

class GameSessionDetailView(DetailView):
    model = GameSession
    template_name = "tournament/game_session_detail.html"
    context_object_name = "game_session"


class GameSessionCreationView(CreateView):
    model = GameSession
    fields = "__all__"
    template_name = "tournament/game_session_form.html"
    success_url = reverse_lazy("tournament:game-session-list")


class GameSessionUpdateView(UpdateView):
    model = GameSession
    fields = "__all__"
    template_name = "tournament/game_session_form.html"
    success_url = reverse_lazy("tournament:game-session-list")


class GameSessionDeleteView(DeleteView):
    model = GameSession
    template_name = "tournament/game_session_confirm_delete.html"
    success_url = reverse_lazy("tournament:game-session-list")


class PlayerListView(ListView):
    model = Player
    context_object_name = "player_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.session.get("username", "")
        context["search_form"] = PlayerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        form = PlayerSearchForm(self.request.GET)
        self.queryset = Player.objects.all()
        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return self.queryset


class PlayerDetailView(DetailView):
    model = Player


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerCreationForm
    success_url = reverse_lazy("tournament:player-list")


class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerScoreUpdateForm
    success_url = reverse_lazy("tournament:player-list")


class PlayerDeleteView(DeleteView):
    model = Player
    success_url = reverse_lazy("tournament:player-list")
