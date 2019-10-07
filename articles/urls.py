from . import views
from django.conf.urls import url

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'create/', views.create_article, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='details'),
]
