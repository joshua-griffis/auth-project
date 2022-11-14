from app.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", root),
    path("admin/", admin.site.urls),
]
