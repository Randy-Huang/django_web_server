from blog.views import ArticleListView
from blog.views import ArticleDetailView
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='blog-list'),
#    url(r'^articles/(?P<article_name>(?!.*[\W]))/$', ArticleDetailView.as_view(), name='article'),
    url(r'^articles/(?P<article_name>[-\w]+)/$', ArticleDetailView.as_view(), name='article'),
#    url(r'^articles/(?P<article_id>\d+)$', ArticleDetailView.as_view(), name='article'),

#    url(r'^categorys/(?P<tag>(?!.*[\W]))/$', CategoryView.as_view, name='categorys'),
#    url(r'^tags/(?P<tag>(?!.*[\W]))/$', TagView.as_view, name='tags'),
]
