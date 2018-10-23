from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import data,user
# Create your views here.
from . import HttpPars
import json,datetime
#print(HttpPars.HttpPars(a).Pars())
#from django.core.urlresolvers import reverse
from hashlib import sha1


def jia_mi(str):
    sh = sha1()
    sh.update(str.encode())
    return sh.hexdigest()



def index(request):
     #return HttpResponse('666')
     if request.method=='GET':
          #
           #print([[o for o in i] for i in user.objects.all()])
           try:
            get_username = request.COOKIES['username']
            get_lianjie = request.COOKIES['lianjie']
            print(get_lianjie)
            get_lij=user.objects.get(username=get_username).lijie
            if get_lianjie==get_lij:
                print('验证成功')
                print(get_username)
                return render(request, 'qian/index.html')
            else:
                return HttpResponse('<h1>:)  非法请求<br></h1>')
           except:
               return HttpResponse('<h1>:)  会话过期，请先登陆<br></h1>')
     if request.method=='POST':
           name=request.POST['name']      
           http=request.POST['http']
           # open('xx.txt','w').write(http)
           # print(http)
           try:
             dict=HttpPars.HttpPars(str(http)).Pars()
          # print(dict)
             x=json.dumps(dict, ensure_ascii=False,sort_keys=True, indent=4, separators=(',', ': '))       
             print(x)
             get_username = request.COOKIES['username']
             b=data.objects.create(user=user.objects.get(username=get_username),name=name,fk=dict['fk'],url=dict['url'],cookie='null',header=dict['header'],data=dict['data'])

             return HttpResponse('<h1>:)  添加成功<br></h1>'+x)
           except:
             return HttpResponse('<h1>:)  添加失败<br></h1>')


def sign(request):
    # return HttpResponse('666')
    if request.method == 'GET':
        return render(request, 'qian/sign.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        email=request.POST['email']
        #print(username,password)
        try:
          user.objects.create(username=username,pwd=password,email=email,time= datetime.datetime.now(),lijie='null')
          return HttpResponse(str({'info':'sign is ok'}))
        except BaseException as e:
          ex={'info':str(e),'type':username}
          return HttpResponse(str(ex))
def login(request):
    # return HttpResponse('666')
    if request.method == 'GET':

        #get_username=request.COOKIES['username']
        #print(get_username)
        return render(request, 'qian/admin.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        print(username,password)
        try:
            pwd = user.objects.get(username=username).pwd
        except:
            ex = {'info': '验证失败，用户名或密码错误', 'type': username}
            return HttpResponse(ex)
        if password == pwd:
           # a=render(request, 'qian/c.html')
            ex={'info':'验证成功','type':username}
            a=HttpResponse(str(ex))
            print(66666)
            jia=jia_mi(datetime.datetime.now().strftime('%Y-%m-%d'))
           # md5=str(genearteMD5(str(datetime.datetime.now().strftime('%Y-%m-%d'))))
            a.set_cookie('username', username, max_age=100)
            a.set_cookie('lianjie',jia, max_age=100)
            user.objects.filter(username=username).update(lijie=jia)
            return a
        else:
            ex={'info':'验证失败，用户名或密码错误','type':username}
            return HttpResponse(str(ex))


