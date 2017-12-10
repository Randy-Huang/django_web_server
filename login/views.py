from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
class LoginAccountPageView(ListView):
    template_name = "login/index.html"