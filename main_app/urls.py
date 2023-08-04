from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("dogs/", views.dogs_index, name="index"),
    path("dogs/<int:dog_id>/", views.dogs_details, name="details"),
    path("dogs/create/", views.DogCreate.as_view(), name="dogs_create"),
    path("dogs/<int:pk>/update/", views.DogUpdate.as_view(), name="dogs_update"),
    path("dogs/<int:pk>/delete/", views.DogDelete.as_view(), name="dogs_delete"),
    path("dogs/<int:dog_id>/add_playdate/", views.add_playdate, name="add_playdate"),
    path("tricks/", views.TrickList.as_view(), name="tricks_index"),
    path("tricks/<int:pk>/", views.TrickDetail.as_view(), name="tricks_details"),
    path("tricks/create/", views.TrickCreate.as_view(), name="tricks_create"),
    path("tricks/<int:pk>/update/", views.TrickUpdate.as_view(), name="tricks_update"),
    path("tricks/<int:pk>/delete/", views.TrickDelete.as_view(), name="tricks_delete"),
    path(
        "dogs/<int:dog_id>/assoc_trick/<int:trick_id>/",
        views.assoc_trick,
        name="assoc_trick",
    ),
    path(
        "dogs/<int:dog_id>/unassoc_trick/<int:trick_id>/",
        views.unassoc_trick,
        name="unassoc_trick",
    ),
]
