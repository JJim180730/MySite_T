from django.urls import path

from . import views

app_name = "polls" #application namespace
urlpatterns = [
#     #orignal URL patterns
#     # ex: /polls/
#     path("", views.index, name="index"),
#     # ex: /polls/5/
#     # the 'name' value as called by the {% url %} template tag
#     path("<int:question_id>/",views.detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),


    # Convert the URLconf.
    # Delete some of the old, unneeded views.
    # Introduce new views based on Django’s generic views.
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

]