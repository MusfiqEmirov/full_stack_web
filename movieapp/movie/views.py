from datetime import date
from django.shortcuts import render, get_object_or_404
from movie.models import Movie


data = {

    "sliders":[
        {
            "slider_image":"slider1.jpg",
            "sliderUrl":"filmin-adi-1"
        },
        {
            "slider_image":"slider2.jpg",
            "sliderUrl":"filmin-adi-2"
        },
        {
            "slider_image":"slider3.jpg",
            "sliderUrl":"filmin-adi-3"
        }

    ]
}

def index(request):
    movies = Movie.objects.filter(is_active=True, is_home=True)
    sliders = data["sliders"]
    return render(request,'index.html',{
        "movies":movies,
        "sliders":sliders
    })

def movies(request):
    movies = Movie.objects.all()
    return render(request,"movies.html", {
        "movies":movies
    })


def movie_details(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    return render(request, "movies-detalis.html",{
        "movie": movie,
        "genres": movie.genres.all(),
        "people": movie.people.all(),
        "videos": movie.video_set.all()
    })