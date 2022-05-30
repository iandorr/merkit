from django.urls import include, path, re_path
from blog_app.views import ArticleList, ArticleDetail

app_name = 'blog_app'

urlpatterns = [
    #path('',ArticleListView.as_view(),name='article_list'),
    path('',ArticleList,name='article_list'),
    path('<str:slug>/',ArticleDetail,name='article_detail'),
]
