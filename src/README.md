# XuBolg
### Author：Xu
## 程序结构
```
└─ blog/ ·································· 应用所在目录
   ├─ migrations/ ······································ 图片目录
   ├─ static/ ······································ 静态文件目录
   │  └─ blog/ ··································· 包括css，js，images
   ├─ templates/ ······································ html模板目录
   |  └─ blog/ ··································· blog HTML文件
   ├─ board/ ··································· 榜单页面
   │  ├─ index/ ··································· ~~引导页面~~（splash替代）
   │  ├─ common/ ··································· 通用模板
   │  ├─ item/ ···································· 电影信息页面
   │  ├─ list/ ···································· 电影列表页面
   │  ├─ profile/ ································· 个人信息页面
   │  ├─ search/ ··································· 搜索页面
   │  ├─ splash/ ··································· 滑动欢迎页面
   │  └─ logs/ ·································· 日志目录   
   ├─ admin.py ······································ 后台管理页面
   ├─ apps.py ······································ 应用注册页面
   ├─ models.py ······································ 数据库模型页面
   ├─ tests.py ······································ 测试数据页面
   ├─ urls.py ······································ URL地址映射管理页面
   └─ views.py   ···································· 视图管理页面（视图层）
└─ XuSite/ ·································· 项目所在目录
   ├─ __init__.py/ ······································ 表明是python类型，没有任何意义
   ├─ settings.py/ ······································ django项目配置文件
   ├─ urls.py/ ······································ django项目路径映射文件
   ├─ wsgi.py/ ······································ 暂时不知道是什么文件
   ├─ db.sqlite3 ······································ 项目自动生成文件
   └─ manage.py ···································· 项目运行相关
```
## 写在前面
一直都想建立一个个人网站来试试。正好现在有大把的时间可以让我来研究如何建站。
也算是学习了，莫名其妙就接触了python，然后想用python写一个web，最后选择了django这个框架。
整个程序其实早就建好了，之后有事情就有一个月的时间没有去写了。现在捡起来继续写。
买的树莓派到了之后准备部署项目上去试试看。
## 开发日志
### 2018-09-04 17:02:12
* 今天整理了一下之前做的东西，之后上传到github上。  
* 目前的进度基本框架已经完成，就是需要逻辑上的东西进行尝试了。  
* 前端框架Bootstrap也需要研究。  
### 2018-09-06 17:43:50
* 创建article.html  
* 使用普通方法实现url跳转。detailview不知道为什么跳转失败  
* views中携带的blog不能迭代。  
* 可以使用get_object_or_404指定pk之后传递数据  
* 明天应该继续完成article  
