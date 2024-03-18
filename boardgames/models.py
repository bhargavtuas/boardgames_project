from django.db import models
from django.contrib.auth.models import User

class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Gamer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    borrowed_games = models.ManyToManyField(BoardGame, related_name='borrowers')
    max_borrowed_games = 3

    def __str__(self):
        return self.user.username

class GameLoan(models.Model):
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gamer.user.username} borrowed {self.board_game.name}"