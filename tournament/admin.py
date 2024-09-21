from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tournament.models import League, Player, Team, GameSession


admin.site.register(League)
admin.site.register(Team)
admin.site.register(GameSession)

@admin.register(Player)
class PlayerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("points", "score")


