from django.urls import path
from . import views

urlpatterns=[
    path('',views.MoviesList.as_view())
]