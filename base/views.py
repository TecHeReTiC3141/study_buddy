from django.shortcuts import render
from .models import Room


def home(request):

    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    r = Room.objects.get(id=pk)

    print(r)
    context = {'room': r}
    return render(request, 'base/room.html', context)
