from django.conf.urls import include
from django.conf.urls import url
from homepage.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name = 'homepage'),
]
