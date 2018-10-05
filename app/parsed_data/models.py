from datetime import timezone

from django.db import models



class WebtoonData(models.Model):
    title = models.CharField(max_length=200)
    url_img_thumbnail = models.URLField()
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class EpisodeData(models.Model):
    title = models.CharField(max_length=200)
    url_img_thumbnail = models.URLField()
    rating = models.CharField(max_length=200)
    created_date = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.title
