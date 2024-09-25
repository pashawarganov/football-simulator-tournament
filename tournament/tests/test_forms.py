from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tournament.forms import PlayerCreationForm
from tournament.models import Team, League, GameSession, Player

LEAGUE_URL = reverse("tournament:league-list")
TEAM_URL = reverse("tournament:team-list")
GAME_SESSION_URL = reverse("tournament:game-session-list")
CHOOSE_RANDOM_TEAM_URL = reverse("tournament:choose_random_team")
PLAYER_URL = reverse("tournament:player-list")


class PlayerFormTests(TestCase):
    def test_player_form_is_valid(self):
        form_data = {
            "username": "bob123",
            "password1": "test123test",
            "password2": "test123test",
            "first_name": "Bob",
            "last_name": "James",
        }
        form = PlayerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
