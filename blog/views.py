from blog.models import Article
from blog.models import Category
from blog.models import Tag
from django.shortcuts import render
from django.views.generic import ListView 
from django.views.generic import DetailView

# Global constant
ITEMS_PER_PAGE = 1

# Create your views here.
class ArticleListView(ListView):
    context_object_name = "context_article_list" 
    model = Article
    template_name = "blog/blog-list.html"
    paginate_by = ITEMS_PER_PAGE 

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['article_list'] = Article.objects.all()
        kwargs['browse_type'] = self.request.GET.get('browse')
        return super(ArticleListView, self).get_context_data(**kwargs)   

    def get_queryset(self):
        queryset = Article.objects.all()
        if self.request.GET.get('browse'):
            res = self.request.GET.get('browse')
            if res == 'Tag':
                queryset = Tag.objects.all()
            elif res == 'Category':
                queryset = Category.objects.all()
            else:
                queryset = Article.objects.all()
        return queryset 

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

