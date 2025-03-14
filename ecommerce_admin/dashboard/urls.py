from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="dashboard"),
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
]
