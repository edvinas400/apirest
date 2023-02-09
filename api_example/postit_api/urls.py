from django.urls import path
from . import views

urlpatterns = [
    path('albums', views.AlbumList.as_view()),
    path('reviews', views.AlbumReviewList.as_view()),
    path('reviews/<int:pk>', views.AlbumReviewDetail.as_view()),
    path('reviews/<int:pk>/like', views.AlbumReviewLikeCreate.as_view()),
    path('signup', views.UserCreate.as_view()),
]