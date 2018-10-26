from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter,url
from django.views.generic import TemplateView
from django.urls import include


app_name = 'qian'

router=DefaultRouter()
router.register(r'UserViewSet',views.UserViewSet)




urlpatterns=[
url('^api/',include(router.urls)),
path('',views.index,name='index'),
path('login/',views.login,name='login'),
path('sign/',views.sign,name='sign'),


# url('user/', user_list),
# url(r'user_detail/id/(?P<pk>)*', user_detail),
# #url('user_detail/id/<str:pk>', user_detail),
]