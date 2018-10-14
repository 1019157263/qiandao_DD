from django.urls import path
from . import views
app_name = 'qian'

urlpatterns=[
path('',views.index,name='index'),
path('login/',views.login,name='login'),
path('sign/',views.sign,name='sign'),
]