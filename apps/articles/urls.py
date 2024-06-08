from django.urls import path
from . import views
from .views import home_view

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('boxing/', views.boxing_articles, name='boxing_articles'),
    path('mma/', views.mma_articles, name='mma_articles'),
    path('golf/', views.golf_articles, name='golf_articles'),
    path('football/', views.football_articles, name='football_articles'),
    path('basketball/', views.basketball_articles, name='basketball_articles'),
    path('hockey/', views.hockey_articles, name='hockey_articles'),
    path('tennis/', views.tennis_articles, name='tennis_articles'),
    path('formula1/', views.formula1_articles, name='formula1_articles'),
    path('poker/', views.poker_articles, name='poker_articles'),
    path('athletics/', views.athletics_articles, name='athletics_articles'),
    path('swimming/', views.swimming_articles, name='swimming_articles'),
    path('cycling/', views.cycling_articles, name='cycling_articles'),
    path('volleyball/', views.volleyball_articles, name='volleyball_articles'),
    path('snooker/', views.snooker_articles, name='snooker_articles'),
    path('cybersports/', views.cybersports_articles, name='cybersports_articles'),
    path('olympic_sports/', views.olympic_sports_articles, name='olympic_sports_articles'),
    path('other_sports/', views.other_sports_articles, name='other_sports_articles'),
    path('category/<str:category>/', views.category_articles, name='category_articles'),
    path('', home_view, name='home'),
    path('search/', views.search_view, name='search'),
    path('search_results/', views.search_results_view, name='search_results'),
    path('<int:article_id>/save/', views.save_article, name='save_article'),
]




