from django.shortcuts import render
from homework.models import Movie, PersonMovie
# Create your views here.

def show_movies(request):
    movies = Movie.objects.all().order_by("year")
    return render(request, 'movies.html', {"movies":movies})

def show_movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    actorsMovies = PersonMovie.objects.filter(movie = movie)
    return render(request, 'movie_detail.html', {"movie": movie, 'sttaring':actorsMovies})
