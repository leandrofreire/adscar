from django.urls import path

from . import views

app_name = 'campanhas'

urlpatterns = [
    path('', views.index, name='index'),
    path('landing', views.landing, name='landing'),
]