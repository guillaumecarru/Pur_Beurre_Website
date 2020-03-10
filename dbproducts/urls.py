from django.urls import path, re_path

from . import views

urlpatterns = [
    path("research_substitute/", views.research_substitute, name="research_substitute"),
    path("details/<int:product_id>/", views.detail, name="detail"),
    re_path(r'^ajax_calls/search/', views.autocompleteModel),
]
