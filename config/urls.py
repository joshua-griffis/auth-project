from app.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", root),
    path("login", login, name="login"),
    path("sign_up", sign_up, name="sign"),
    path("admin/", admin.site.urls),
]
