from django import forms
from django.contrib.auth.forms import UserCreationForm

from tournament.models import Player


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


class PlayerCreationForm(UserCreationForm):
    class Meta:
        model = Player
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
        )


class PlayerScoreUpdateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["score", "points"]
