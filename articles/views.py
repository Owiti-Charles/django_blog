from django.shortcuts import render, redirect
from .models import Article
from . import forms
from django.contrib.auth.decorators import login_required


def articles(request):
    article = Article.objects.all().order_by('date')

    return render(request, 'articles/articles.html', {'articles': article})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url='/account/login/')
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            return redirect('articles:articles')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/new_article.html', {'form': form})
