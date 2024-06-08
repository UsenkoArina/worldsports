from django.urls import path
from.import views
from .views import login, logout
from django.conf import settings
from django.conf.urls.static import static
from .views import profile_info

app_name = 'accounts'

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
    path('profileInfo/', views.profile_info, name='profileInfo'),
    path('saved-articles/', views.saved_articles, name='saved_articles'),
    path('favorites/', views.favorites_articles, name='favorites_articles'),
    path('commented-articles/', views.commented_articles, name='commented_articles'),
]
