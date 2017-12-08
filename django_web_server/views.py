from django.views.generic.base import TemplateView

import logging

# for showing error page
class TemplateErrorView404(TemplateView):
    template_name = "error/error-404.html"


