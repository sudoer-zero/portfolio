from . import views
from django.urls import path


urlpatterns = [
    path(
        "",
        views.MessagePost.as_view()
    ),

    path(
        '<int:pk>/',
        views.MessageDetailView.as_view(),
        name='message_detail'
    ),
]