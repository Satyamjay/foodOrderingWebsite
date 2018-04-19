from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'signup/', views.signup_page, name='signup'),
    url(r'login/', views.login_page, name='login'),
]