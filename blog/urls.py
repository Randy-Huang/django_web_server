from blog.views import ArticleListView
from django.conf.urls import include
from django.conf.urls import url

app_name = 'blog'
urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='blog-list')
    #url(r'^articles/([0-9]{8})', ,name='article')
    #url(r'^', ,name='category')
]
