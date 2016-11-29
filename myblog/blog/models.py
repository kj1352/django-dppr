from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=30, default="Dr.Pavagada Prakash Rao")
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Shop(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=30, default="Dr.Pavagada Prakash Rao")
    price = models.CharField(max_length=6)
    book_id = models.CharField(max_length=20)
    img_id = models.CharField(max_length=1000, null=True)
    publications = models.CharField(max_length=100)
    published_date = models.DateField()


    def __str__(self):
        return self.title

class Calender(models.Model):
    event_name = models.CharField(max_length=500)
    event_type = models.CharField(max_length=100)
    timing = models.DateTimeField()
    venue = models.CharField(max_length=200)
    address = models.TextField(max_length=400)

    def __str__(self):
        return self.event_name
