from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    # View de detalhes
    path('<int:question_id>/', views.detail, name='detail'),
    # View de resultados das pesquisas
    path('<int:question_id>/results/', views.results, name='results'),
    # View dos votos
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
