from django.shortcuts import render, redirect
from .models import Articles, Category


def index(request):
    return render(request, 'main/index.html')


def articles(request):
    article = Articles.objects.all()
    is_published = Articles.objects.filter(is_published=True)
    context = {
        'articles': article,
        'title': 'Список статей',
        'is_published': is_published,
        }
    return render(request, 'main/articles.html', context)


def get_category(request, category_id):
    articles = Articles.objects.filter(category_id=category_id)
    category = Category.objects.get(id=category_id)
    is_published = Articles.objects.filter(category_id=category_id, is_published=True)
    context = {
        'articles': articles,
        'category': category,
        'title': 'Список статей',
        'is_published': is_published,
    }
    return render(request, 'main/category.html', context)


def view_article(request, articles_id):
    article_item = Articles.objects.get(id=articles_id)
    context = {
        'article_item': article_item,
    }
    return render(request, 'main/article.html', context)
