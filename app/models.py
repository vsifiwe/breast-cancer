from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Account(models.Model):
    email = models.CharField(max_length = 200, unique=True)
    password = models.CharField(max_length = 200)
    type = models.CharField(max_length = 50)

    def __str__(self):
        return self.email

class Prediction(models.Model):
    owner = models.ForeignKey(Account, on_delete=CASCADE)
    prediction = models.CharField(max_length=200)
    accuracy = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.owner.email + self.prediction
