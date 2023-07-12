from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Python'},
    {'id': 2, 'name': 'JS'},
    {'id': 3, 'name': 'C++'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):

    r = None
    for i in rooms:
        if i['id'] == int(pk):
            r = i
            break

    print(r)
    context = {'room': r}
    return render(request, 'base/room.html', context)
