from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 1,
            'title': 'The matrix',
            'year': 1999,
            'genre': 'Sci-fi'
        },
        {
            'id': 2,
            'title': 'The mick',
            'year': 2009,
            'genre': 'Comedy'
        },
        {
            'id': 3,
            'title': 'The third brigade',
            'year': 2006,
            'genre': 'Action'
        }
    ]
}


def movies(request):
    return render(request, 'movies/movies.html', data)


def home(request):
    return HttpResponse("Homepage")
