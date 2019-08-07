from django.shortcuts import render
from football.models import Teams
# Create your views here.

def show_table(request):
    teams = Teams.objects.all().order_by('-points')
    return render(request, 'show_teams.html', {'teams':teams})