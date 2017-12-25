from blog.models import Article
from blog.models import Category
from blog.models import Tag
from django.shortcuts import render
from django.views.generic import ListView 
from django.views.generic import DetailView

# Global constant
ITEMS_PER_PAGE = 10

# Create your views here.
class ArticleListView(ListView):
    context_object_name = "article_list" 
    model = Article
    template_name = "blog/blog-list.html"
    paginate_by = ITEMS_PER_PAGE 

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(ArticleListView, self).get_context_data(**kwargs)   

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/blog-article.html"
    pk_article = 'article_name'
    context_object_name = 'context_article'
    
    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(ArticleDetailView, self).get_context_data(**kwargs)   

    def get_object(self):
        obj = super(ArticleDetailView, self).get_object
        return obj

class CategoryView(ListView):
    model = Article
    template_name = ""
    pass

class TagView(ListView):
    model = Article
    template_name = ""
    pass

