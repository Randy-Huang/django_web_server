from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from user_agents import parse

import blog.views as blog
import logging

# Create your views here.
log = logging.getLogger('django.debug')

# waitting to use class-based replace to showHomepage()
class HomePageView(TemplateView):
    template_name = "homepage/index.html"

    '''def get(self, request, *args, **kwargs):
        #contect = super(HomePageView, self).get_context_data(**kwargs)

        ua_string = request.META.get('HTTP_USER_AGENT')
        user_agent = parse(ua_string)

        log.debug(user_agent.is_mobile)
        return render(request, 'homepage/index.html', {'user_agent': user_agent})
'''
