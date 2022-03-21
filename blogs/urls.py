from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    LatestArticlesList,
    article_heart,
    article_happy,
    article_like,
    )

urlpatterns = [
    path('<int:pk>/heart/', article_heart),
    path('<int:pk>/happy/', article_happy),
    path('<int:pk>/like/', article_like),
    path('latest-articles/', LatestArticlesList.as_view()),
    path('', ArticleListView.as_view()),
    path('<slug:article_slug>/', ArticleDetailView.as_view()),
]