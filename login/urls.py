from django.conf.urls import include
from django.conf.urls import url
from login.views import LoginAccountPageView

app_name = 'homepage'
urlpatterns = [
    url(r'^$', LoginAccountPageView.as_view(), name='login-account'),
]
