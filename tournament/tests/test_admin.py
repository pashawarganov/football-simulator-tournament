from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin",
        )
        self.client.force_login(self.admin_user)
        self.player = get_user_model().objects.create_user(
            username="bob123",
            password="test123",
            score=4,
            points=1
        )

    def test_player_score_and_points_listed(self):
        url = reverse("admin:tournament_player_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.player.score)
        self.assertContains(response, self.player.points)

    def test_player_detail_score_and_points_listed(self):
        url = reverse("admin:tournament_player_change", args=[self.player.pk])
        response = self.client.get(url)
        self.assertContains(response, self.player.score)
        self.assertContains(response, self.player.points)
