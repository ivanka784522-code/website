from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Topic(models.Model): 
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name  

class Room (models.Model): 

    name = models.CharField(max_length=200)
    host = models.ForeignKey (User, on_delete=models.CASCADE )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    description = 
    # participants =
    updated = 
    created = 