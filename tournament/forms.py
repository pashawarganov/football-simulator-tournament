from django import forms

from tournament.models import Team, League, Player, GameSession


class LeagueSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name..."
            }
        ),
    )


class TeamSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name..."
            }
        ),
    )


class PlayerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username..."
            }
        ),
    )


class GameSessionSearchForm(forms.Form):
    date = forms.DateField(
        required=False,
        label="",
        widget=forms.DateInput(
            attrs={
                "placeholder": "Search by date...",
                "type": "date",
            }
        ),
        input_formats=["%Y-%m-%d"]
    )
