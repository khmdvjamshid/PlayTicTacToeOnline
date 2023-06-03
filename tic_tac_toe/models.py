from django.db import models

# Create your models here.
class GameState(models.Model):
    state = models.CharField(max_length=9)
    

class WinState(models.Model):
    symbol = models.CharField(max_length=1)


class UserSymbol(models.Model):
    User_s = models.CharField(max_length=1)