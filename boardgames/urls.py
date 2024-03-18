from django.urls import path
from . import views

app_name = 'boardgames'

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('borrow/<int:game_id>/', views.borrow_game, name='borrow_game'),
    # Add URLs for other views
]