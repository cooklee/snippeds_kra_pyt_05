"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from homework import views as homework_views
from exercises import views as exercise_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path("movies/", homework_views.show_movies),
    path("movie_detail/<int:id>", homework_views.show_movie_detail),
    path("show_band/<int:id>", exercise_views.show_band),
    path("tm/", exercise_views.tabliczka_mnozenia),
    path("przywitanie/", exercise_views.imie),
    path('temp/', exercise_views.temp),
    path('show_session/', exercise_views.show_session),
    path('set_session/', exercise_views.set_session),
    path('del_session/', exercise_views.del_session),
    path('del_session/', exercise_views.del_session),
    path('edit_person/<int:id>', homework_views.edit_person),
    path('edit_movie/<int:id>', homework_views.edit_movie)
]
