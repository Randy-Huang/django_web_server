from django.conf.urls import include
from django.conf.urls import url
from login.views import LoginView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login-account'),
]
