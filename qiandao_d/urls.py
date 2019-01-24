"""qiandao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# -*- coding:utf-8 -*-
#from Ding import *
import schedule
import time
import threading
from qian.models import data,log_a,user
from django.contrib import admin
from django.urls import path
from django.urls import include, path
import requests,json,uuid
import datetime
from django.conf.urls import url, include
from rest_framework import routers
from qian import views

# user_list=views.UserViewSet.as_view({'get':'list','post':'create'})
# user_detail=views.UserViewSet.as_view({'get':'retrieve'})
# #log.objects.all().delete()


class qian:
    def __init__(self):
        self.data=data.objects.all()
    def qian(self):
       try:
        for i in self.data:
            if i.fk=='GET':            
              if i.cookie=='null':
               print(f'[任务名]{i.name}[{i.fk}]-,没cookie')
               a=requests.get(i.url,data=i.data,headers=eval(i.header))              
              else:
               print(f'[任务名]{i.name}[{i.fk}]-有cookie')
               a=requests.get(i.url,data=i.data,cookies=eval(i.cookie),headers=eval(i.header))
              
              try:
                   print(f'[任务返回]{json.loads(a.text)}')
                   b=log_a.objects.create(user=uuid.uuid1(),name=i.name,username=i.user,data=str(a.json()),time= datetime.datetime.now())
               
              except:
                   print(a.text)
                   b=log_a.objects.create(user=uuid.uuid1(),name=i.name,username=i.user,data=str(a.text),time= datetime.datetime.now())
             
            elif i.fk=='POST':
              if i.cookie=='null':

               print(f'[任务名]{i.name}[{i.fk}]-没cookie')
               print(f'[数据]{i.data}')
               a=requests.post(i.url,headers=eval(i.header)) 
			   
              else:
               print(f'[任务名]{i.name}[{i.fk}]-有cookie')
               print(f'[数据]{i.data}')
               a=requests.post(i.url,data=i.data,cookies=eval(i.cookie),headers=eval(i.header))
              
              try:
                   print(f'[任务返回]{json.loads(a.text)}')
                   b=log_a.objects.create(user=uuid.uuid1(),name=i.name,username=i.user,data=str(a.json()),time= datetime.datetime.now())
               
              except:
                   print(a.text)
                   b=log_a.objects.create(user=uuid.uuid1(),name=i.name,username=i.user,data=str(a.text),time= datetime.datetime.now())
             
            
                #未完              
       except:
         print('错误')    
def job():
    print("I'm working...")
    a=qian()
    a.qian()
pz=user.objects.get(username='配置文件')
print(pz.lijie)
if eval(pz.lijie)['type']=='001':
	schedule.every(0.1).minutes.do(job)
	print('[时间]10秒')
#schedule.every().hour.do(job)
else:
	schedule.every().day.at("00:00").do(job)
	print('[时间]00：00点')
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

def xxx():
    while True:
        schedule.run_pending()
        time.sleep(1)
      
t =threading.Thread(target=xxx)
t.start()



urlpatterns = [
    path('admin/', admin.site.urls),
     path('qian/', include('qian.urls')),

]
