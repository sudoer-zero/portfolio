from django.shortcuts import render

from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import api_view

from django.http import Http404

from .serializers import ArticleSerializer
from .models import Article


class ArticleListView(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleDetailView(APIView):
    def get_object(self, article_slug):
        try:
            return Article.objects.all().get(slug=article_slug)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, article_slug, format=None):
        articles = self.get_object(article_slug)
        serializer = ArticleSerializer(articles)
        return Response(serializer.data)


class LatestArticlesList(ListAPIView):
    queryset = Article.objects.all()[0:3]
    serializer_class = ArticleSerializer


@api_view(['POST'])
def article_heart(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.heart += 1
    article.save()
    data = {
        'success': True
    }
    return Response(data)


@api_view(['POST'])
def article_like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.like += 1
    article.save()
    data = {
        'success': True
    }
    return Response(data)



@api_view(['POST'])
def article_happy(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.happy += 1
    article.save()
    data = {
        'success': True
    }
    return Response(data)