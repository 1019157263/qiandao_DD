#  签到api详细文档
----------
##  0.后端介绍
开发语言：python
web框架：django

####运行步骤：
1. 下载python3.x
2. 安装django，在cmd运行 `pip install django` 
```
pip install django
```
3.cd进工程目录
输入：`python manage.py runserver 0.0.0.0:8000` 

4.进入：`127.0.0.1:8000/admin` 进入站点后台管理


| 请求参数 | 类型 |
|:----------:|:----------:|
|  用户名   | test01 |
| 密码 | root |

----------




##  1.注册接口
```
调用地址：http://127.0.0.1:8000/qain/sign/

请求方式：POST

返回类型：JSON

```
| 请求参数 | 类型 | 是否必须 | 描述 |
|:----------:|:----------:|:----------:|:----------:|
|   username         |   str   |      必须      |    用户名        |
|      pwd      |      str      |     必须      |      密码      |
|       email     |   str         |      必须      |    邮箱        |

注册成功返回：
```
{'info':'sign is ok'}
```
注册失败返回：
```
{'info':失败原因,'type':username}
```

----------




## 2.登录接口
```
调用地址：http://127.0.0.1:8000/qain/login/

请求方式：POST

返回类型：JSON
```
| 请求参数 | 类型 | 是否必须 | 描述 |
|:----------:|:----------:|:----------:|:----------:|
|   username         |   str   |      必须      |    用户名        |
|      pwd      |      str      |     必须      |      密码      |

登录成功返回：
```
{'info':'验证成功','type':username}
```
登录失败返回：
```
ex={'info':'验证失败，用户名或密码错误','type':username}
```

----------



## 3.http报文解析接口
```
调用地址：http://127.0.0.1:8000/qain/

请求方式：POST

返回类型：JSON
```
| 请求参数 | 类型 | 是否必须 | 描述 |
|:----------:|:----------:|:----------:|:----------:|
|   name         |   str   |      必须      |    任务名称        |
|      http      |      str      |     必须      |      任务的http报文      |

添加成功返回：
```
{ "data": XXX, "fk": XXX, "header": XXX, "info": "提交成功", "url": XXX, "username": XXX }
```
添加失败返回：
```
{'info': '添加失败', 'type': '请仔细阅读使用说明书'}
```

----------




## 4.信息接口
```
restful API
```




## 5.任务列表接口:
```
resrful API
```

