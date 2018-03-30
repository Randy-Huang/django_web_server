from django.conf.urls import include
from django.conf.urls import url
from portfolio.views import PortfolioListView, PortfolioDetailView

urlpatterns = [
    url(r'^$', PortfolioListView.as_view(), name = 'portfolio-list'),
    #url(r'^portfolio/(?P<portfolio-item-name>[-\w]+)/$', PortfolioDetailView.as_view(), name='portfolio-item'),
]
