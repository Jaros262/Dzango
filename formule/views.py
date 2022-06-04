from django.views.generic import ListView, DetailView
from django.shortcuts import render

from django.http import HttpResponse

from formule.models import Sesion, Team, Grand_prix, Racer, Nationality

def index(request):
    team = Team.objects.all()
    sesion = Sesion.objects.all()
    racer = Racer.objects.all()
    nation = Nationality.objects.all()
    grandPrix = Grand_prix.objects.all()
    context = {
        'team' : team,
        'sesion' : sesion,
        'racer' : racer,
        'nation' : nation,
        'grandPrix' : grandPrix
    }
    return render(request, 'index.html', context=context)

class racerListView(ListView):
    model = Racer
    context_object_name = 'racer'
    template_name = "list.html"

class racerDetailView(DetailView):
    model = Racer
    context_object_name = 'racer_detail'
    template_name = "detail.html"

class nationsListView(ListView):
    model = Nationality
    context_object_name = 'nations'
    template_name = "nations.html"

class nationsDetailView(DetailView):
    model = Nationality
    context_object_name = 'nation_detail'
    template_name = "detail_nations.html"