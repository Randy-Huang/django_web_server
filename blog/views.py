from blog.models import Article, Category, Tag 
from django.conf import settings
from django.views.generic import DetailView, ListView 
from oauth2client.contrib.django_util import decorators
from pandas import DataFrame
from utility.google_analytics_api import GoogleAanalyticsService

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
        kwargs['recent_article_list'] = Article.objects.all().order_by('-created_time')[0:5]
        kwargs['browse_type'] = self.request.GET.get('browse')
        kwargs['ckeditor_folder'] = settings.CKEDITOR_UPLOAD_PATH

        # Get GA data 
        ga_data = GoogleAanalyticsService().get_ga_data(dimensions=None)
        visitors = str(ga_data['totalsForAllResults']['ga:entrances']).zfill(6)
        kwargs['visitors'] = visitors
        settings.BLOG_SETTINGS = visitors
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
    context_object_name = 'context_article'
    model = Article
    template_name = "blog/blog-article.html"
    pk_url_kwarg = 'article_name'
    
    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['recent_article_list'] = Article.objects.all().order_by('-created_time')[0:5]
        kwargs['ckeditor_folder'] = settings.CKEDITOR_UPLOAD_PATH

        # Get GA data 
        ga_data = GoogleAanalyticsService().get_ga_data(filters=self.kwargs['article_name'])
        views = ga_data['rows'][0][3]
        kwargs['visitors'] = settings.BLOG_SETTINGS
        kwargs['views'] = ga_data['rows'][0][3]

        # model operation
        article_model = Article.objects.get(unique_name=self.kwargs['article_name'])
        article_model.views = views
        article_model.save()

        context = super(ArticleDetailView, self).get_context_data(**kwargs)   
        return context 

    def get_object(self, queryset=None):

        return super(ArticleDetailView, self).get_object()

    def get(self, request, *args, **kwargs):
        return super(ArticleDetailView, self).get(request, *args, **kwargs)
