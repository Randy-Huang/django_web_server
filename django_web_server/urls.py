"""django_web_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from django_web_server.views import TemplateErrorView404
import os

# project site root
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

# for ssl file from sslforfree.com
urlpatterns += [
    url(r'^.well-known/acme-challenge/(?P<path>.*)$', serve, {
        'document_root': os.path.join(settings.STATIC_ROOT, 'ssl/'), 
    }),
]

# homepage app
urlpatterns += [
    # Notice the expression does not end in $, 
    # that happens at the myapp/url.py level
    url(r'^', include('homepage.urls', namespace='homepage', app_name='homepage')),
]

# login app
urlpatterns += [
    url(r'^login/', include('login.urls', namespace='login', app_name='login')),
]

# blog app
urlpatterns += [
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# custom error view
handler404 = TemplateErrorView404.as_view()

