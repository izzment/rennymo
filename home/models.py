from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Tag(models.Model):
    caption = models.CharField(max_length=10)

    def __str__(self):
        return self.caption


class Event(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    date = models.DateField()
    description = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

