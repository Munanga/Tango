from django.urls import path
from rango import views

app_name = "tango"

urlpatterns = [
    path('',views.index,name="index"),
]