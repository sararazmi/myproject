from django.shortcuts import render
from .models import Board

def home(request):
    result = Board.objects.all()
    boards_names = list()
    return render(request, 'home.html', {'x': result , 'y':'sara'})



def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})


