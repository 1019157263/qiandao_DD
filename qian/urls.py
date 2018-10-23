from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter,url
from django.views.generic import TemplateView
from django.urls import include


app_name = 'qian'

user_list=views.UserViewSet.as_view({'get':'list','post':'create'})
user_detail=views.UserViewSet.as_view({'get':'retrieve'})


urlpatterns=[
path('',views.index,name='index'),
path('login/',views.login,name='login'),
path('sign/',views.sign,name='sign'),
url('user/', user_list),
url(r'user_detail/id/(?P<pk>)*', user_detail),
#url('user_detail/id/<str:pk>', user_detail),
]