# Django博客开发实战：开篇

> 这个公号开通已经大半年的时间了，之前推送了许多有关Python核心知识的内容，现在或许是时候发布一些 Web 开发相关的文章了，主要涉及 Flask 和 Django 这两个框架。其中，针对 Django 框架，编程派将与“Django学习小组”合作，首发 Django 博客开发实战等系列内容，也就是今天这篇的由来；针对 Flask 框架，上周收到了 Millyn 同学的投稿，会分三部分放出。以后日常推送的内容，也会逐步往这方面靠拢。

## Django开发环境搭建

django 的开发环境搭建以及如何创建工程在网上有大量的博客和教程介绍，在此不再重复说明。但是我们认为最好的参考资料，还是Django官方的入门 Tutorials ，即[官方文档](https://docs.djangoproject.com/en/1.9/)的 **First steps** 部分的六个 **部分**。当然如果你不喜欢英文，可以看网友的翻译版本：[Django1.8.2中文文档](http://python.usyiyi.cn/django/index.html)的**入门**部分。

要开始 Django 开发，你需要掌握以下知识：

- 如何创建 Django 工程，并了解 Django 默认的工程目录结构
- 如何创建 Django APP
- 理解 Django 的 MTV 模式，学会编写 Model、View、Template
- Django 如何处理静态文件，即各种 CSS，JS，以及图片文件等

## Django应用是如何工作的？

先看一张流程图，再来逐步讲解其过程：

![django 工作流](http://7xq740.com1.z0.glb.clouddn.com/u=3965620747,3597889975&fm=21&gp=0.jpg)

1：用户通过浏览器输入相应的 URL 发起 HTTP请求（一般是 GET/POST）

2：django 接收到请求，检测 urls.py 文件，找到和用户输入的 URL 相匹配的项，并调用该 URL 对应的视图函数（view）。例如，通常来说 urls.py 文件里的代码是这样的：

```python
url(r'^homepage/$', views.home_page)
```

则当用户输入的 URL 为 www.某个网址.com/homepage 时，django 检测到该 URL 与上面的代码匹配，于是调用后面的 ``views.home_page`` 视图函数，把相应的请求交给该视图函数处理。

3：视图函数被调用后，可能会访问数据库（Model）去查询用户想要请求的数据，并加载模板文件（Template），渲染完数据后打包成 ``HttpResponse`` 返回给浏览器（Http协议）

大致工作流程就是这样，从流程可以看出，我们需要做的就是：

- 编写相应的 url
- 编写数据库（Model）
- 编写处理 Http 请求的视图函数（View）
- 编写需要渲染的模板（Template）

这就是 Django 开发的最主要工作，下面遵循这样的开发流程开始编写我们的博客吧。

## 编写 Model

Model 对应数据库，我们编写的是一个 Blog 应用，因此数据库中应该存放 Blog 下的文章（Aticle），文章由标题（title）、正文（body）、发布时间（publised_time）等组成。

先看 django 是如何定义数据库的，之后再逐行解释代码（假设你已经对 django 的工程目录结构了解了，我们一般把 Model 定义在 ``models.py`` 文件中）：

``models.py``：

```python
from django.db import models
# 和 model 相关的一些API定义在 django.db.models 模块中

class Article(models.Model):
    """
    所有的 model 必须继承自django.db.models
    类 Aticle 即表示 Blog 的文章，一个类被 diango 映射成数据库中对应的一个表，表名即类名
    类的属性（field），比如下面的 title、body 等对应着数据库表的属性列
    """
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    # 在 status 时说明

    title = models.CharField('标题', max_length=70)
    # 文章标题，CharField 表示对应数据库中表的列是用来存字符串的，'标题'是一个位置参数
    #（verbose_name），主要用于 django 的后台系统，不多做介绍。max_length 表示能存储的字符串	# 的最大长度

    body = models.TextField('正文')
    # 文章正文，TextField 用来存储大文本字符

    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    # 文章创建时间，DateTimeField用于存储时间，设定auto_now_add参数为真，则在文章被创建时会自 	   # 动添加创建时间

    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    # 文章最后一次编辑时间，auto_now=True表示每次修改文章时自动添加修改的时间

    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    # STATUS_CHOICES，field 的 choices 参数需要的值，choices选项会使该field在被渲染成form时	  	  # 被渲染为一个select组件，这里我定义了两个状态，一个是Draft（草稿），一个是Published（已发	  # 布），select组件会有两个选项：Draft 和 Published。但是存储在数据库中的值分别				# 是'd'和'p'，这就是 choices的作用。

    abstract = models.CharField('摘要', max_length=54, blank=True, null=True,
                                help_text="可选，如若为空将摘取正文的前54个字符")
    # 文章摘要，help_text 在该 field 被渲染成 form 是显示帮助信息

    views = models.PositiveIntegerField('浏览量', default=0)
    # 阅览量，PositiveIntegerField存储非负整数

    likes = models.PositiveIntegerField('点赞数', default=0)
    # 点赞数

    topped = models.BooleanField('置顶', default=False)
    # 是否置顶，BooleanField 存储布尔值（True或者False），默认（default）为False

    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)
	# 文章的分类，ForeignKey即数据库中的外键。外键的定义是：如果数据库中某个表的列的值是另外一
    # 个表的主键。外键定义了一个一对多的关系，这里即一篇文章对应一个分类，而一个分类下可能有多篇	   # 文章。详情参考django官方文档关于ForeinKey的说明，on_delete=models.SET_NULL表示删除某个	# 分类（category）后该分类下所有的Article的外键设为null（空）

    def __str__(self):
        # 主要用于交互解释器显示表示该类的字符串
        return self.title

    class Meta:
        # Meta 包含一系列选项，这里的 ordering 表示排序，- 号表示逆序。即当从数据库中取出文章		# 时，其是按文章最后一次修改时间逆序排列的。
        ordering = ['-last_modified_time']


class Category(models.Model):
    """
    另外一个表，存储文章的分类信息
    """
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name
```

由上可见，设计数据库结构就是编写 models，数据库中每一个实体对应的表在 django 中对应着 ``models.py`` 中的一个类，类的属性对应着数据库表的属性列。

model 定义完毕后，运行以下命令即可生成相应的数据库：

`python manage.py makemigrations`

`python manage.py migrate`

你可以打开相应的数据库文件，看看里面生成的表结构，加深理解。

以上的代码中涉及到一些 django 相关的概念，分别给出以下参考资料供学习：

- Django 模型层（model）的概论：[官方文档](https://docs.djangoproject.com/en/1.9/topics/db/models/)、[中文翻译文档](http://python.usyiyi.cn/django/topics/db/models.html)
- 类中各属性（field）：[官方文档对 django 提供的各 field 的介绍](https://docs.djangoproject.com/en/1.9/ref/models/fields/)、[相应的中文文档](http://python.usyiyi.cn/django/ref/models/fields.html)
- ForeinKey（一对多），还有 ManyToMany（多对多）、OneToOne（一对一）的介绍：[官方文档对外关系的介绍](https://docs.djangoproject.com/en/1.9/topics/db/models/#relationships)

## 编写 View

上面已经介绍了 django 应用的工作流程，数据库建立完毕后需要编写视图函数（view）来处理 Http 请求。

同样先来看 django 的视图代码是如何写的。我们现在要设计的是一个首页的视图函数，即用户进入我们的 博客首页后，我们需要把数据库中存储的文章的相关信息取出来展示给用户看：

```python
from blog.models import Article
from blog.models import Category
from django.views.generic import ListView
import markdown2

class IndexView(ListView):
    """
    首页视图,继承自ListVIew，用于展示从数据库中获取的文章列表
    """

    template_name = "blog/index.html"
    # template_name属性用于指定使用哪个模板进行渲染

    context_object_name = "article_list"
    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）

    def get_queryset(self):
        """
    	过滤数据，获取所有已发布文章，并且将内容转成markdown形式
    	"""
        article_list = Article.objects.filter(status='p')
        # 获取数据库中的所有已发布的文章，即filter(过滤)状态为'p'(已发布)的文章。
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
            # 将markdown标记的文本转为html文本
        return article_list

    def get_context_data(self, **kwargs):
   	 	# 增加额外的数据，这里返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
```

你可能觉得奇怪，既然是视图函数，为什么不是用 def 来定义，而是写成一个类？

这里涉及到 django 关于类的通用视图的概念：参考[类的通用视图](https://docs.djangoproject.com/en/1.9/topics/class-based-views/)。我们通过调用 ``as_view`` 方法会将该类视图转为一般的视图，这在 url 部分会介绍。

这个视图的工作流程如下：首先接受来自用户的 Http 请求，然后从数据库中获取到已经发布的文章列表：`article_list = Article.objects.filter(status='p')`，并转换 markdown 语法标记，再加载模板文件：`template_name = "blog/index.html"`，将模板中的变量用相应数据库中的数据替换后返回给浏览器。这样，用户就看到了从数据库中被取出，然后被渲染后的文章列表了。

## 编写 Template

template 稍微麻烦一点，因为涉及到 html 的相关知识。如果你没有学过 html ，可能会有些看不懂，因此推荐学习一下，这里有很棒的教程：[w3school 的 html 教程](http://www.w3school.com.cn/html/index.asp)供学习使用。

这里只介绍一点点本项目涉及的模板相关知识，其实 django 文档的入门教程的六个部分中涵盖的点已经足以对付此简单的博客项目了。

- 模板标签，用 ``{% %}`` 表示，一些常用的有 ``{% for %}`` 循环标签，``{% if %}`` 判断标签等。
- 模板变量，用 ``{{ variable }}`` 表示，模板渲染指的是这些变量会被数据库中相应的值代替，例如`article_list = Article.objects.filter(status='p')`，从数据库中取出了已发布的文章列表，赋给了 article_list 变量。如果模板文件中有如下代码：

``` python
{% for article in article_list %}
	{{article.title}}
```

那么渲染时就会循环渲染 n 篇文章，并且 `{{article.title}}` 也会被存储在数据库中文章的标题取代。

更多详细的资料，请参考[官方文档关于 template 的介绍](https://docs.djangoproject.com/en/1.9/topics/templates/)，或者[中文文档](http://python.usyiyi.cn/django/topics/templates.html)

## 编写 URL

写好了数据库、视图和模板，现在就是当用户在浏览器输入 url 访问我们的博客时，要告诉 django 哪个 url 的请求对应哪个视图函数来处理，通过 ``urls.py`` 来指定：

``urls.py``：

```python
urlpatterns = [
    ...
    url(r'^blog/', views.IndexView.as_view()),
    # 首页调用IndexView
    ...
]
```

至此，Blog 应用的首页算是完成了，当用户访问我们的主页就可以看到文章列表了：

![django blog homepage](http://7xq740.com1.z0.glb.clouddn.com/django-blog%E5%B1%95%E7%A4%BA%E5%9B%BE.png)

## 结束语

本节是 django blog 项目的开篇，是 **django 学习小组**的集体学习成果。**django学习小组**是一个促进 django 新手互相学习、互相帮助的组织。

小组在一边学习 django 的同时将一起完成几个项目，包括：

- **一个简单的 django 博客**，用于发布小组每周的学习和开发文档；
- **django中国社区**，为国内的 django 开发者们提供一个长期维护的 django 社区；

上面所说的这个社区类似于 segmentfault 和 stackoverflow ，但更加专注（只专注于 django 开发的问题）。

目前小组正在完成第一个项目，本文即是该项目第一周的相关文档。

更多的信息请关注我们的 [github 组织首页](https://github.com/djangoStudyTeam/DjangoBlog)，本教程项目的相关源代码也已上传到 github 上。

同时，你也可以加入我们的邮件列表 [django_study@groups.163.com](mailto:django_study@groups.163.com) ，随时关注我们的动态。我们会将每周的详细开发文档和代码通过邮件列表发出。

如有任何建议，欢迎提 issue，欢迎 fork，pr，当然也别忘了 star 哦！
