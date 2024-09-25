from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tournament.models import Team, League, GameSession

LEAGUE_URL = reverse("tournament:league-list")
TEAM_URL = reverse("tournament:team-list")
GAME_SESSION_URL = reverse("tournament:game-session-list")
CHOOSE_RANDOM_TEAM_URL = reverse("tournament:choose_random_team")
PLAYER_URL = reverse("tournament:player-list")


class PublicTest(TestCase):
    def test_team_login_required(self):
        response = self.client.get(TEAM_URL)
        self.assertNotEqual(200, response.status_code)

    def test_league_login_required(self):
        response = self.client.get(LEAGUE_URL)
        self.assertNotEqual(200, response.status_code)

    def test_player_login_required(self):
        response = self.client.get(PLAYER_URL)
        self.assertNotEqual(200, response.status_code)

    def test_game_session_login_required(self):
        response = self.client.get(GAME_SESSION_URL)
        self.assertNotEqual(200, response.status_code)

    def test_choose_random_team_login_required(self):
        response = self.client.get(CHOOSE_RANDOM_TEAM_URL)
        self.assertNotEqual(200, response.status_code)


class PrivateTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="bob123",
            password="1qazxcde3",
        )
        get_user_model().objects.create_user(
            username="bob1234",
            password="1qazxcde3",
        )
        self.players = get_user_model().objects.all()
        self.leagues = [
            League.objects.create(name=f"League{i}", country=f"country{i}")
            for i in range(3)
        ]
        self.teams = [
            Team.objects.create(name=f"Team{i}", league=self.leagues[0], rating=8)
            for i in range(3)
        ]
        self.game_sessions = [
            GameSession.objects.create(
                player=self.user,
                team=self.teams[0],
                score=2 + i,
                win=False,
                last_stage="final"
            )
            for i in range(3)
        ]
        self.client.force_login(self.user)

    def test_retrieve_league(self):
        response = self.client.get(LEAGUE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["league_list"]),
            list(self.leagues)
        )

    def test_retrieve_team(self):
        response = self.client.get(TEAM_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["team_list"]),
            list(self.teams)
        )

    def test_retrieve_player(self):
        response = self.client.get(PLAYER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["player_list"]),
            list(self.players)
        )

    def test_retrieve_game_session(self):
        response = self.client.get(GAME_SESSION_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["game_session_list"]),
            list(self.game_sessions)
        )


class SearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="bob123",
            password="1qazxcde3",
        )
        self.players = {
            "bob123": self.user,
            "bob1234": get_user_model().objects.create_user(
                username="bob1234",
                password="1qazxcde3",
            )
        }
        self.leagues = {
            f"League{i}": League.objects.create(name=f"League{i}", country=f"country{i}")
            for i in range(3)
        }
        self.teams = {
            f"Team{i}": Team.objects.create(name=f"Team{i}", league=self.leagues["League1"], rating=8)
            for i in range(3)
        }
        dates = [
            datetime.today().date(),
            (datetime.today() + timedelta(days=1)).date(),
            (datetime.today() + timedelta(days=2)).date()
        ]
        self.game_sessions = {
            dates[i]: GameSession.objects.create(
                player=self.user,
                team=self.teams[f"Team{i}"],
                score=2 + i,
                win=False,
                last_stage="final",
                date=dates[i]
            )
            for i in range(3)
        }
        self.client.force_login(self.user)

    def test_search_league(self):
        key = "League1"
        response = self.client.get(LEAGUE_URL, {"name" : key})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["league_list"]),
            [self.leagues[key]]
        )

    def test_search_team(self):
        key = "Team1"
        response = self.client.get(TEAM_URL, {"name" : key})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["team_list"]),
            [self.teams[key]]
        )

    # def test_search_game_session(self):
    #     key = (datetime.today()).date()
    #     print(key, self.game_sessions)
    #     response = self.client.get(GAME_SESSION_URL, {"date" : key})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(
    #         list(response.context["game_session_list"]),
    #         [self.game_sessions[key]]
    #     )

    def test_search_player(self):
        key = "bob1234"
        response = self.client.get(PLAYER_URL, {"username" : key})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["player_list"]),
            [self.players[key]]
        )
