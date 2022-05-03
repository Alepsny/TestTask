from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='home'),
    path('articles/', views.articles, name='articles'),
    path('article/<int:articles_id>', view_article, name='view_article'),
    path('category/<int:category_id>/', get_category, name='category')
]
