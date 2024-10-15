from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("all/", views.AllView.as_view(), name="all"),
    path("logout/", views.logout_view, name="logout"),

    path("login/", views.LoginV.as_view(), name="login"),

    path("statistics/", views.statisitcs, name="statistics"),
    path("question/", views.question, name="question"),

    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/frequency", views.FreqView.as_view(), name="frequency"),

    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]