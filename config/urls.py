from app.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", root, name="root"),
    path("creating", create, name="create"),
    path("randomize", randomize, name="random"),
    path("update_char/<char_id>", update, name="update_char"),
    path("delete/<char_id>", delete, name="delete_char"),
    path("sign_up", sign_up, name="sign"), 
    path("login", login_user, name="login"),
    path('logout', logout_user, name="logout"),
    path("admin/", admin.site.urls),
]
