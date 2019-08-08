from django.shortcuts import render
from homework.models import Movie, PersonMovie, Person, Genre
# Create your views here.

def get_sort_by_key(id):
    temp_dict = {'1': 'rating',
     '2': '-rating',
     '3': 'year'
    }
    return temp_dict[id]

def show_movies(request):
    key = request.session.get('key', '3')
    key = request.GET.get('key', key)
    request.session['key'] = key
    movies = Movie.objects.all().order_by(get_sort_by_key(key))
    return render(request, 'movies.html', {"movies":movies})

def show_movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    actorsMovies = PersonMovie.objects.filter(movie = movie)
    return render(request, 'movie_detail.html', {"movie": movie, 'sttaring':actorsMovies})


def edit_person(request, id):
    id = request.POST.get('id', id)
    person = Person.objects.get(id=id)
    if request.method == "POST":
        person.first_name = request.POST['first_name']
        person.last_name = request.POST['last_name']
        person.save()
    return render(request, 'edit_person.html', {'person': person})

def edit_movie(request, id):
    id = request.POST.get('id', id)
    movie = Movie.objects.get(id=id)
    genre  = Genre.objects.all()

    if request.method == "POST":
        selected = request.POST.getlist('genre')
        movie.title = request.POST['title']
        movie.year = request.POST['year']
        g = Genre.objects.filter(id__in=selected)
        movie.genre.set(g)
        movie.save()
    return render(request, 'edit_movie.html', {'movie': movie, 'genre':genre})