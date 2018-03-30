from django.views.generic import DetailView, ListView 
from portfolio.models import Portfolio 

import logging

# Global constant
ITEMS_PER_PAGE = 1

log = logging.getLogger('django.debug')

class PortfolioListView(ListView):
    context_object_name = "context_portfolio_list" 
    model = Portfolio 
    template_name = "portfolio/portfolio-list.html"
    paginate_by = ITEMS_PER_PAGE 

    def get_queryset(self):
        queryset = Portfolio.objects.all()
        return queryset

class PortfolioDetailView(DetailView):
    template_name = "portfolio/portfolio-item.html"
