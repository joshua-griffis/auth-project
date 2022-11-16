from app.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", root, name="root"),

    path("sign_up", sign_up, name="sign"), 
    path("login", login_user, name="login"),
    path('logout', logout_user, name="logout"),
    path("admin/", admin.site.urls),
]
