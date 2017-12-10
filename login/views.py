from django.shortcuts import render
#from django.views.generic import ListView
from django.views.generic.base import TemplateView



# Create your views here.
#class LoginAccountPageView(ListView):
class LoginAccountPageView(TemplateView):
    template_name = "login/login-account.html"
