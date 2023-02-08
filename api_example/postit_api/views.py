from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from .models import *
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .serializers import *

class AlbumList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        reviews = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if reviews.exists():
            return super().delete(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima trinti svetimų pranešimų!')

    def put(self, request, *args, **kwargs):
        reviews = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if reviews.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Negalima koreguoti svetimų pranešimų!')

class AlbumReviewLikeCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
        serializer_class = AlbumReviewLikeSerializer
        permission_classes = [permissions.IsAuthenticated]

        def get_queryset(self):
            user = self.request.user
            review = AlbumReview.objects.get(pk=self.kwargs['pk'])
            return AlbumReviewLike.objects.filter(review=review, user=user)

        def perform_create(self, serializer):
            if self.get_queryset().exists():
                raise ValidationError('Jūs jau palikote patiktuką šiam pranešimui!')
            else:
                review = AlbumReview.objects.get(pk=self.kwargs['pk'])
                serializer.save(user=self.request.user, review=review)

        def delete(self, request, *args, **kwargs):
            if self.get_queryset().exists():
                self.get_queryset().delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                raise ValidationError('Jūs nepalikote patiktuko po šiuo pranešimu!')