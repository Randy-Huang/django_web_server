from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView 
from oauth2client.contrib.django_util import decorators 
from user_agents import parse

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

@decorators.oauth_required
def get_profile_required(request):
    resp, content = request.oauth.http.request('https://www.googleapis.com/auth/analytics.readonly')
    return HttpResponse(content)

@decorators.oauth_enabled
def get_profile_optional(request):
    if request.oauth.has_credentials():
        return HttpResponse('User email: {}'.format(request.oauth.credentials.id_token['email']))
    else:
        return HttpResponse('Here is an OAuth Authorize link:<a href="{}">Authorize</a>'.format(request.oauth.get_authorize_redirect()))
