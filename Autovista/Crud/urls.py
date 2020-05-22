from django.urls import path, include
from . import views

urlpatterns = [
 path('leads/',views.index,name="lead"),
]