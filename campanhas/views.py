from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from campanhas.models import Campanha


def index(request):
    campanhas = Campanha.objects.order_by('-titulo_campanha')[:5]
    context = {'campanhas': campanhas}
    return render(request, 'campanhas/index.html', context)
