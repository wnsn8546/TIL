from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def index(request):

    articles = Article.objects.order_by('-pk')

    page = request.GET.get("page")
    articles_all = Article.objects.all()
    paginator = Paginator(articles_all, 4)
    posts = paginator.get_page(page)


    context = {
        'articles': articles,
        "posts": posts,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':

        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)

def detail(request, pk):

    article = Article.objects.get(pk=pk)

    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':

        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():

            article_form.save()
            return redirect('articles:detail', article.pk)

    else:

        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)

def search(request):
    search_keyword = request.GET.get('search_keyword','')

    if search_keyword:
        articles = Article.objects.filter(Q(title__icontains = search_keyword) | Q(content__icontains = search_keyword))
        print(articles)
    else:
        print('검색결과가 없습니다.')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/search.html', context)

def test(request):
    board_list = Article.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(board_list, '10')
    page_obj = paginator.page(page)
    return render(request, 'articles/test.html', {'page_obj':page_obj}) 

def categories(request):
    page = int(request.GET.get("page"))
    articles_all = Article.objects.all()
    paginator = Paginator(articles_all, 3)
    posts = paginator.get_page(page)

    return render(
        request,
        "articles/categories.html",
        {
            "posts": posts,
        },
    )