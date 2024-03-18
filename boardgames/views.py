from django.shortcuts import render, redirect
from .models import BoardGame, Gamer

def game_list(request):
    games = BoardGame.objects.all()
    return render(request, 'boardgames/game_list.html', {'games': games})

def borrow_game(request, game_id):
    user = request.user
    gamer = Gamer.objects.get(user=user)
    game = BoardGame.objects.get(id=game_id)

    if gamer.borrowed_games.count() < gamer.max_borrowed_games:
        if game.borrowers.filter(id=user.id).exists():
            return render(request, 'boardgames/borrow_error.html', {'game': game})
        else:
            gamer.borrowed_games.add(game)
            return redirect('boardgames:game_list')
    else:
        return render(request, 'boardgames/borrow_error.html', {'game': game})

# Add views for adding, editing, and deleting games