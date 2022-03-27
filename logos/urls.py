from django.urls import path

from . import views

urlpatterns = [
    path('', views.LogoListView.as_view()),
]