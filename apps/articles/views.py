import datetime
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CommentForm
from django.db.models import Q
from django.urls import reverse
from .models import Article, SportCategory
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def index(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.order_by('-pub_date')
    
    return render(request, 'articles/list.html', {'latest_articles_list': articles, 'sort_by': sort_by})

def detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Article not found!")
    comments = article.comment_set.all()
    # Check if the user is authenticated
    if request.user.is_authenticated:
        form = CommentForm()

        if request.method == 'POST':
            if 'like' in request.POST:
                article.like(request.user)
            elif 'unlike' in request.POST:
                article.unlike(request.user)
            else:
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.user = request.user
                    comment.article = article
                    comment.save()
                    return HttpResponseRedirect(request.path_info)
        return render(request, 'articles/detail.html', {'article': article, 'comments': comments, 'form': form})
    else:
        # If the user is not authenticated, only display comments without the form
        return render(request, 'articles/detail.html', {'article': article, 'comments': comments})

def home_view(request):
    latest_articles_list = Article.objects.order_by('-pub_date')
    return render(request, 'articles/home.html')

def category_articles(request, category_name):
    try:
        category = SportCategory.objects.get(name=category_name)
    except SportCategory.DoesNotExist:
        raise Http404("Category not found!")
    articles = Article.objects.filter(category=category)
    context = {'articles': articles}
    return render(request, 'base.html', context)

def boxing_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='BOXING').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='BOXING').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='BOXING').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='BOXING').order_by('-pub_date')
    
    return render(request, 'boxing_articles.html', {'articles': articles, 'sort_by': sort_by})

def mma_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='MMA').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='MMA').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='MMA').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='MMA').order_by('-pub_date')
    
    return render(request, 'mma_articles.html', {'articles': articles, 'sort_by': sort_by})

def golf_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='GOLF').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='GOLF').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='GOLF').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='GOLF').order_by('-pub_date')
    
    return render(request, 'golf_articles.html', {'articles': articles, 'sort_by': sort_by})

def football_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='FOOTBALL').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='FOOTBALL').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='FOOTBALL').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='FOOTBALL').order_by('-pub_date')
    
    return render(request, 'football_articles.html', {'articles': articles, 'sort_by': sort_by})

def basketball_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='BASKETBALL').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='BASKETBALL').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='BASKETBALL').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='BASKETBALL').order_by('-pub_date')
    
    return render(request, 'balsketball_articles.html', {'articles': articles, 'sort_by': sort_by})

def hockey_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='HOCKEY').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='HOCKEY').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='HOCKEY').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='HOCKEY').order_by('-pub_date')
    
    return render(request, 'hockey_articles.html', {'articles': articles, 'sort_by': sort_by})

def tennis_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='TENNIS').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='TENNIS').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='TENNIS').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='TENNIS').order_by('-pub_date')
    
    return render(request, 'tennis_articles.html', {'articles': articles, 'sort_by': sort_by})

def formula1_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='FORMULA 1').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='FORMULA 1').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='FORMULA 1').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='FORMULA 1').order_by('-pub_date')
    
    return render(request, 'formula1_articles.html', {'articles': articles, 'sort_by': sort_by})

def poker_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='POKER').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='POKER').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='POKER').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='POKER').order_by('-pub_date')
    
    return render(request, 'poker_articles.html', {'articles': articles, 'sort_by': sort_by})

def athletics_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='ATHLETICS').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='ATHLETICS').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='ATHLETICS').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='ATHLETICS').order_by('-pub_date')
    
    return render(request, 'athletics_articles.html', {'articles': articles, 'sort_by': sort_by})

def swimming_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='SWIMMING').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='SWIMMING').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='SWIMMING').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='SWIMMING').order_by('-pub_date')
    
    return render(request, 'swimming_articles.html', {'articles': articles, 'sort_by': sort_by})

def cycling_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='CYCLING').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='CYCLING').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='CYCLING').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='CYCLING').order_by('-pub_date')
    
    return render(request, 'cycling_articles.html', {'articles': articles, 'sort_by': sort_by})

def volleyball_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='VOLLEYBALL').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='VOLLEYBALL').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='VOLLEYBALL').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='VOLLEYBALL').order_by('-pub_date')
    
    return render(request, 'volleyball_articles.html', {'articles': articles, 'sort_by': sort_by})

def snooker_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='SNOOKER').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='SNOOKER').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='SNOOKER').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='SNOOKER').order_by('-pub_date')
    
    return render(request, 'snooker_articles.html', {'articles': articles, 'sort_by': sort_by})

def cybersports_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='CYBERSPORTS').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='CYBERSPORTS').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='CYBERSPORTS').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='CYBERSPORTS').order_by('-pub_date')
    
    return render(request, 'cybersports_articles.html', {'articles': articles, 'sort_by': sort_by})

def olympic_sports_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='OLYMPIC SPORTS').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='OLYMPIC SPORTS').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='OLYMPIC SPORTS').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='OLYMPIC SPORTS').order_by('-pub_date')
    
    return render(request, 'olympic_sports_articles.html', {'articles': articles, 'sort_by': sort_by})

def other_sports_articles(request):
    sort_by = request.GET.get('sort_by', 'newest')
    if sort_by == 'newest':
        articles = Article.objects.filter(category__name='OTHER SPORTS').order_by('-pub_date')
    elif sort_by == 'oldest':
        articles = Article.objects.filter(category__name='OTHER SPORTS').order_by('pub_date')
    elif sort_by == 'most_likes':
        articles = Article.objects.filter(category__name='OTHER SPORTS').annotate(num_likes=Count('likes')).order_by('-num_likes', '-pub_date')
    else:
        articles = Article.objects.filter(category__name='OTHER SPORTS').order_by('-pub_date')
    
    return render(request, 'other_sports_articles.html', {'articles': articles, 'sort_by': sort_by})

def search_view(request):
    return render(request, 'search.html')

def search_results_view(request):
    query = request.GET.get('q')
    
    if query:
        results = Article.objects.filter(Q(article_title__icontains=query) |Q(article_text__icontains=query)|Q(category__name__icontains=query)).order_by('-pub_date')
    else:
        results = []
    
    return render(request, 'search_results.html', {'query': query, 'articles': results})

@login_required
def save_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        if request.user in article.saved_by.all():
            article.saved_by.remove(request.user)
        else:
            article.saved_by.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
 
