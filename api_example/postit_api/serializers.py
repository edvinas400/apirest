from rest_framework import serializers
from .models import *


class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.StringRelatedField(many=True)
    reviews = serializers.StringRelatedField(many=True)
    band = serializers.StringRelatedField(many=False)
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['id', 'band', 'name', 'songs', 'review_count', 'reviews']

    def get_review_count(self, obj):
        return AlbumReview.objects.filter(album=obj).count()


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    album = serializers.SlugRelatedField(queryset=Album.objects.all(), slug_field='name')
    likes = serializers.SerializerMethodField()

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'likes', 'album', 'content', 'score']

    def get_likes(self, review):
        return AlbumReviewLike.objects.filter(review=review).count()


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumReviewLike
        fields = ['id']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user