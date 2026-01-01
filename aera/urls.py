from django.urls import path
from . import views

app_name="aera"

urlpatterns = [
    path("", views.index, name="aera_home"),
]
