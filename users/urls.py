from django.urls import path

from . import views

urlpatterns = [
    # Create user
    path("create_user/", views.create_user, name="create_user"),
    # Modify user
    path("modify_user/", views.modify_user, name="modify_user"),
    # Delete user
    path("delete_user/", views.delete_user, name="delete_user"),
]
