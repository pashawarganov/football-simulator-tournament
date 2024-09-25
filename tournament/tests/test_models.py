from django.test import TestCase
from django.contrib.auth import get_user_model

from tournament.models import League, Team, GameSession


class ModelsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="1qazxcde3",
        )
        self.league = League.objects.create(
            name="Test League",
            country="USA",
        )
        self.team = Team.objects.create(
            name="Test Team",
            league=self.league,
            rating=8
        )
        self.game_session = GameSession.objects.create(
            player=self.user,
            team=self.team,
            score=4,
            last_stage="final",
            win=True
        )

    def test_player_str(self):
        self.assertEqual(
            str(self.user),
            f"{self.user.username} "
            f"({self.user.first_name} {self.user.last_name})"
        )

    def test_league_str(self):
        self.assertEqual(
            str(self.league),
            f"{self.league.name} ({self.league.country})"
        )

    def test_team_str(self):
        self.assertEqual(
            str(self.team),
            self.team.name
        )

    def test_game_session_str(self):
        self.assertEqual(
            str(self.game_session),
            f"{self.game_session.player.username} - "
            f"{self.game_session.team.name} ({self.game_session.date})"
        )
