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


| 用户名 | 密码 |
|:----------:|:----------:|
| test01| root |

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




## 4.用户信息接口
### 4.1获取用户列表
```
调用地址：http://127.0.0.1:8000/qian/api/UserViewSet/

请求方式：GET

返回类型：JSON

```
成功返回：
```
[
    {
        "username": "admin",
        "email": "1019157263@qq.com",
        "lijie": "131a316a82e93a0a4aba4e779e91e5a9a55d6179",
        "time": "2018-09-11T15:29:00"
    },
   ...
    {
        "username": "222",
        "email": "1019157263@qq.com",
        "lijie": "null",
        "time": "2018-01-01T00:00:00"
    }
]
```
失败返回：
```
{
    "detail": "未找到。"
}
```

### 4.2增加用户
```
调用地址：http://127.0.0.1:8000/qian/api/UserViewSet/

请求方式：POST

返回类型：JSON

```

| 请求参数 | 类型 | 是否必须 | 描述 |
|:----------:|:----------:|:----------:|:----------:|
|   username         |   str   |      必须      |    --        |
|      email      |      str      |     必须      |      --      |
|      time      |      str      |     必须      |      --      |
|      lijie      |      str      |     必须      |      --      |



成功返回：
```
{
    "username": "用户名",
    "email": "密码",
    "lijie": "lijie",
    "time": "2011-10-01T11:01:00"
}
```
失败返回：
```
{
    "detail": "未找到。"
}
```


### 删除用户

```
调用地址：http://127.0.0.1:8000/qian/api/UserViewSet/{id}/

请求方式：DELETE

返回类型：JSON
```

#### 修改用户

```
调用地址：http://127.0.0.1:8000/qian/api/UserViewSet/{id}/

请求方式：PUT

返回类型：JSON
```

| 请求参数 | 类型 | 是否必须 | 描述 |
|:----------:|:----------:|:----------:|:----------:|
|   username         |   str   |      必须      |    --        |
|      email      |      str      |     必须      |      --      |
|      time      |      str      |     必须      |      --      |
|      lijie      |      str      |     必须      |      --      |

#### 查询用户

```
调用地址：http://127.0.0.1:8000/qian/api/UserViewSet/{id}/

请求方式：GET

返回类型：JSON
```


## 4.任务数据接口
### 4.1获取任务列表
```
调用地址：http://127.0.0.1:8000/qian/api/DataViewSet/

请求方式：GET

返回类型：JSON

```
成功返回：
```
[
    {
        "user": "admin",
        "name": "MIUI",
        "fk": "GET",
        "url": "xxx",
        "cookie": "xxx",
		"header": "xxx",
		"data": ""
    },
...
,
]
```
失败返回：
```
{
    "detail": "未找到。"
}
```

### 4.2增加任务
```
调用地址：http://127.0.0.1:8000/qian/api/DataViewSet/

请求方式：POST

返回类型：JSON

```

| 请求参数 | 类型 | 是否必须 | 描述 |
|:----------:|:----------:|:----------:|:----------:|
|   user         |   str   |      必须      |    用户名        |
|      name      |      str      |     必须      |      任务名称      |
|      fk      |      str      |     必须      |      请求方式      |
|      url      |      str      |     必须      |      --      |
|      cookie      |      str      |     必须      |      --      |
|      header      |      str      |     必须      |      --      |
|      data      |      str      |     选填      |      --      |



成功返回：
```
{
数据
}
```
失败返回：
```
{
    "detail": "未找到。"
}
```


### 删除任务

```
调用地址：http://127.0.0.1:8000/qian/api/DataViewSet/{id}/

请求方式：DELETE

返回类型：JSON
```

#### 修改任务

```
调用地址：http://127.0.0.1:8000/qian/api/DataViewSet/{id}/

请求方式：PUT

返回类型：JSON
```

| 请求参数 | 类型 | 是否必须 | 描述 |
|:----------:|:----------:|:----------:|:----------:|
|   username         |   str   |      必须      |    --        |
|      email      |      str      |     必须      |      --      |
|      time      |      str      |     必须      |      --      |
|      lijie      |      str      |     必须      |      --      |

#### 查询任务

```
调用地址：http://127.0.0.1:8000/qian/api/UserViewSet/{id}/

请求方式：GET

返回类型：JSON
```
