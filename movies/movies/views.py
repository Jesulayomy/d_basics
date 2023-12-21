from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

# data = {
#     'movies': [
#         {
#             'id': 1,
#             'title': 'The matrix',
#             'year': 1999,
#             'genre': 'Sci-fi'
#         },
#         {
#             'id': 2,
#             'title': 'The mick',
#             'year': 2009,
#             'genre': 'Comedy'
#         },
#         {
#             'id': 3,
#             'title': 'The third brigade',
#             'year': 2006,
#             'genre': 'Action'
#         }
#     ]
# }


def movies(request):
    data = {'movies': Movie.objects.all()}
    return render(request, 'movies/movies.html', data)

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    genre = request.POST.get('genre')
    if title and year:
        movie = Movie(title=title, year=year, genre=genre)
        movie.save()
        return HttpResponseRedirect('/movies/')
    return render(request, 'movies/add.html')

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except Exception:
        raise Http404("Movie does not exist")
    movie.delete()

    return HttpResponseRedirect('/movies/')

def home(request):
    return HttpResponse("Homepage")
