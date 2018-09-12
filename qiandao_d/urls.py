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
from qian.models import data,log_a
from django.contrib import admin
from django.urls import path
from django.urls import include, path
import requests,json,uuid
import datetime
#log.objects.all().delete()


class qian:
    def __init__(self):
        self.data=data.objects.all()
    def qian(self):
       try:
        for i in self.data:
            if i.fk=='GET':            
              if i.cookie=='null':
               print('没cookie')
               a=requests.get(i.url,data=i.data,headers=eval(i.header))              
              else:
               print('有cookie')
               a=requests.get(i.url,data=i.data,cookies=eval(i.cookie),headers=eval(i.header))
              
              try:
                   print(json.loads(a.text))
                   b=log_a.objects.create(user=uuid.uuid1(),name=i.name,username=i.user,data=str(a.json()),time= datetime.datetime.now())
               
              except:
                   print(a.text)
                   b=log_a.objects.create(user=uuid.uuid1(),name=i.name,username=i.user,data=str(a.text),time= datetime.datetime.now())
             
            elif i.fk=='POST':
              if i.cookie=='null':
               print('没cookie')
               a=requests.post(i.url,data=i.data,headers=eval(i.header))              
              else:
               print('有cookie')
               a=requests.post(i.url,data=i.data,cookies=eval(i.cookie),headers=eval(i.header))
              
              try:
                   print(json.loads(a.text))
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

schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("00:00").do(job)
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
