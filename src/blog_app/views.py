from turtle import position
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView,ListView
from blog_app.models import Article


def ArticleList(request):

    articles = Article.objects.all()

    if request.toolbar and request.toolbar.edit_mode_active:
        menu = request.toolbar.get_or_create_menu('article_list_menu','Articles')
        menu.add_modal_item('Add new article',url="%s" % (reverse('admin:blog_app_article_add')))

    return render(request,'article_list.html',{
        'object_list':articles,
    })

def ArticleDetail(request,slug):

    article = Article.objects.get(slug=slug)

    if request.toolbar and request.toolbar.edit_mode_active:
        menu = request.toolbar.get_or_create_menu('article_detail_menu',article.slug)
        menu.add_modal_item('Edit Article',url=(reverse('admin:blog_app_article_change',args=[article.pk])))

    return render(request,'article_detail.html',{
        'article':article,
    })

