from django.urls import path

from familiar import views

app_name = "familiar"
urlpatterns = [
    path("familiars", views.familiars, name="familiar-list"),
]
