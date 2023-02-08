from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    name = models.CharField(verbose_name="band name", max_length=150)

    def __str__(self):
        return f"{self.name}"

    def __repr__ (self):
        return f"{self.name}"


class Album(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    name = models.CharField(max_length=150)
    duration = models.IntegerField('Song duration in seconds',default=0)
    def __str__(self):
        return f"{self.name}"

class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="reviews")
    content = models.TextField(max_length=1000)
    score = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))))
    def __str__(self):
        return f"{self.score}, {self.content}"


class AlbumReviewComment(models.Model):
    content = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.created}"
    class Meta:
        ordering = ['-created']


class AlbumReviewLike(models.Model):
    review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
