from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/star/', views.logo_star),
    path('', views.LogoListView.as_view()),
]