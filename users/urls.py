from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_user, name="index_user"),
]
