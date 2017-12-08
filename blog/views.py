from blog.models import Article
from blog.models import Category
from blog.models import Tag
from django.shortcuts import render
from django.views.generic import ListView 
from django.views.generic import DetailView

# Create your views here.
def showBlogList(request):
    return render(request, 'blog/blog-list.html')

class ArticleListView(ListView):
    context_object_name = "article_list" 
    model = Article
    template_name = "blog/blog-list.html"

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(ArticleListView, self).get_context_data(**kwargs)   

class ArticleDetailView(DetailView):
    template_name = ""
    pass

class CategoryView(ListView):
    model = Article
    template_name = ""
    pass

class TagView(ListView):
    model = Article
    template_name = ""
    pass

