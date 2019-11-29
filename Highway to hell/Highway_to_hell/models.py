from django.db import models

# Create your models here.


class Highway(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserWant(models.Model):
    startDate = models.DateTimeField()
    start_point = models.CharField(max_length=30)
    finish_point = models.CharField(max_length=30)