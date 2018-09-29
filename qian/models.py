from django.db import models

# Create your models here.


class user(models.Model):
    username = models.CharField(max_length=200,primary_key=True)
    pwd = models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    time=models.DateTimeField('date published')
    lijie=models.CharField(max_length=500)
    class Meta:
        #末尾不加s
        verbose_name_plural='用户'
    def __str__(self):
        return self.username
  
class data(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)#miui
    fk = models.CharField(max_length=200)#get or post
    url = models.CharField(max_length=500)#url
    cookie = models.TextField()
    header = models.TextField()
    data=models.TextField(blank=True)
    class Meta:
        #末尾不加s
        verbose_name_plural='签到任务'

    
    def __str__(self):
        return self.name
    
class log_a(models.Model):
    user = models.CharField(max_length=200,primary_key=True)
    username=models.CharField(max_length=200)
    data = models.TextField()
    name=models.CharField(max_length=200)
    time=models.DateTimeField('date published')
    class Meta:
        #末尾不加s
        verbose_name_plural='日志'
    
    def __str__(self):
        return self.username
