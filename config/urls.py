from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        route="admin/",
        view=admin.site.urls,
        name="admin",
    ),
    path(
        route="user/",
        view=include("user_api.urls"),
        name="user",
    ),
]