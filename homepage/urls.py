from django.conf.urls import include
from django.conf.urls import url
from homepage.views import HomePageView, AboutMeView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name = 'homepage'),
    url(r'^about-me$', AboutMeView.as_view(), name = 'about-me'),
]
