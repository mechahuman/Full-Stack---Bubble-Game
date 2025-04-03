from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=100, unique=True)
    highscore = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.username}: {self.highscore}"