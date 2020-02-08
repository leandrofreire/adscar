from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from campanhas.models import Campanha


def index(request):
    campanhas = Campanha.objects.all()
    context = {'campanhas': campanhas}
    return render(request, 'campanhas/index.html', context)


def landing(request):
    return render(request, 'campanhas/landing.html')
