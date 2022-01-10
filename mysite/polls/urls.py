from django.urls import path

from . import views
# Здесь расположены пути и паттерны путей к страницам
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'), # путь на страницу index
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # путь на страницу detail
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # и так далее
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]