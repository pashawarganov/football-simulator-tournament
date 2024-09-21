from django.urls import path

from tournament.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = 'tournament'
