# Django学习与实战（四）：标签云与文章归档

> 本文首发于**编程派**微信公众号：编程派（微信号：codingpy）是一个专注Python编程的公众号，每天更新有关Python与编程的教程和资源等精选内容，欢迎关注。

通过前四周的时间我们开发了一个简单的个人 Blog，教程地址，本周我们将实现 blog 的标签云和文章按时间自动归档功能。

之前四周的教程链接如下：

**第一周**：[Django学习与实战（一）：编写博客的 Model 和首页面](http://blog.codingpy.com/article/writing-your-own-blog-with-django/)

**第二周**：[Django学习与实战（二）：博客详情页面和分类页面](http://blog.codingpy.com/article/writing-your-own-blog-with-django-part-two/)

**第三周**：[Django学习与实战（三）：文章列表分页和代码语法高亮](http://blog.codingpy.com/article/writing-your-own-blog-with-django-part-three/)

**第四周**：[Django学习与实战（四）：基于类的通用视图详解](http://blog.codingpy.com/article/writing-your-own-blog-with-django-part-four/)

标签云与文章归档在 Blog 中也是比较常见的功能，标签云显示每篇文章的标签，文章归档显示某个时间段内的发表的文章，就像这样：

![标签云](http://7xq740.com1.z0.glb.clouddn.com/%E6%A0%87%E7%AD%BE%E4%BA%91%E6%BC%94%E7%A4%BA.png)

![文章归档](http://7xq740.com1.z0.glb.clouddn.com/%E6%96%87%E7%AB%A0%E5%BD%92%E6%A1%A3%E6%BC%94%E7%A4%BA.png)

下面我们来为我们的 Blog 添加类似的功能，最终会为我们的个人 blog 实现类似于下面这样的效果：

![整体效果展示](http://7xq740.com1.z0.glb.clouddn.com/%E6%A0%87%E7%AD%BE%E4%BA%91%E6%96%87%E7%AB%A0%E5%BD%92%E6%A1%A3%E6%95%B4%E4%BD%93%E6%95%88%E6%9E%9C%E5%B1%95%E7%A4%BA.png)

## 标签云

标签有点类似于分类，只是分类由于是多对一的关系（我们规定一篇文章只有一个分类，而一个分类下可以有多篇文章），因此在我们的 model 中使用的是 ForeignKeyField 。我们规定一篇文章可以打多个标签，并且一个标签下可能会有多篇文章，是多对多的关系，因此需要使用到 ManyToManyField，其它的实现则和 Category（分类）十分相似。首先修改我们的 model 文件，为标签（tag）新建一个数据库 model，并在文章（Article）中指定它们多对多的关系：

```python
blog/models.py

class Article(models.Model):
    """
    文章model中添加tag关系
    """
    ...
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)
    ...

class Tag(models.Model):
    """
    tag(标签)对应的数据库model
    """
    name = models.CharField('标签名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name
```

类似于 CategoryView，点击某个标签可以获取该标签下的全部文章，对应的视图函数：

```python
blog/views.py

class TagView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        """
        根据指定的标签获取该标签下的全部文章
        """
        article_list = Article.objects.filter(tags=self.kwargs['tag_id'], status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(TagView, self).get_context_data(**kwargs)
```

模板文件稍微小变了一下，添加了显示标签的区域（由于模板文件代码比较多，具体请参见 [github](https://github.com/djangoStudyTeam/DjangoBlog) 项目中 blog/templates/blog/index.html 下的模板文件）。

同时 IndexView 里也别忘了把 tag 加到 context 中，以便在模板中渲染显示：

```python
blog/views.py

class IndexView(ListView):
    ...
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['date_archive'] = Article.objects.archive()
        # tag_list 加入 context 里：
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
```

配置好 url ：

```python
blog/urls.py

url(r'^tag/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
```



## 文章归档

文章归档方面，我们实现下面的需求：

在首页会显示已发表文章对应的年份列表，点击相应年份会展开该年年份下对应的月份列表，像这样：

![blog 文章归档演示](http://7xq740.com1.z0.glb.clouddn.com/blog%E5%BD%92%E6%A1%A3%E6%BC%94%E7%A4%BA2.png)

实现思路大概如下：Django 的 ORM 为我们提供一个 datetimes 函数 （ [datetimes 函数用法](https://docs.djangoproject.com/en/1.9/ref/models/querysets/#datetimes) ），可以选出数据库中某个 model 对应的全部已去重的时间，并且可以任意指定精度。例如，我们想选出全部文章对应的发表时间，精确到月份：

```python
date_list = Article.objects.datetimes('created_time', 'month', order='DESC')
```

created_time 是 Article model 中文章发表时间，对应的是 DatetimeField( datetimes 函数也只能用于DatetimeField )，month 即精确到月，精确到年指定为 year，天则指定为 day 即可。DESC 表示降序排列，默认是升序排列。

例如有如下的一系列发表时间：

2009-01-02
2009-01-05
2009-02-02
2010-05-04
2011-06-04
2011-06-07

则得到的结果将是精确到月份去重后的结果：

2009-01
2009-02
2010-05
2011-06

这正是我们期望的结果。

以这个函数为基础，接下来我们使用 Django 的一点高级技巧（自定义 Manager）来实现完整的功能。

什么是 Manager（管理器）？Manager 可以看成是一个 model 的管理器，很多从数据库中获取 model 数据的方法都定义在这个类里，比如我们经常用的 `Article.objects.all()`，`Article.objects.filter()`，这里的 objects 就是一个 Manager 的实例，django 为每一个 model 都指定了一个默认的 Manager ，名字叫做 objects。但现在 Manager 中一些默认的方法无法满足我们的需求了，因此我们拓展一下 Manager 的功能，为其添加一个归档（archive）方法，拓展一个类的最佳方式就是继承它：

```python
blog/models.py

class ArticleManage(models.Manager):
    """
    继承自默认的 Manager ，为其添加一个自定义的 archive 方法
    """
    def archive(self):
        date_list = Article.objects.datetimes('created_time', 'month', order='DESC')
        # 获取到降序排列的精确到月份且已去重的文章发表时间列表
        # 并把列表转为一个字典，字典的键为年份，值为该年份下对应的月份列表
        date_dict = defaultdict(list)
        for d in date_list:
            date_dict[d.year].append(d.month)
        # 模板不支持defaultdict，因此我们把它转换成一个二级列表，由于字典转换后无序，因此重新降序排序
        return sorted(date_dict.items(), reverse=True)
```

自定义了 Manger 后需要在 model 中显示地指定它：

```python
blog/models.py

class Article(models.model):
    ...
    # 仍然使用默认的 objects 作为 manager 的名字
    objects = ArticleManager()
    ...
```

现在在视图函数中就可以调用了：

```python
blog/views.py

class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        # 调用 archive 方法，把获取的时间列表插入到 context 上下文中以便在模板中渲染
        kwargs['date_archive'] = Article.objects.archive()
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)

```

现在我们的时间归档列表格式是这样的：

[(2012,[09,02,01]),(2011,[12,10,06,01]),...]

因此在模板中我们可以这样循环以实现我们预初的设计：

```python
{% for year,month_list in date_archive %}
	{{year}} 年
    {% for month in month_list %}
    	{{month}}月
```

使用一些 bootstrap 的组件即可实现上图一样的效果了。


完整的模板请参考[ github](https://github.com/djangoStudyTeam/DjangoBlog) 的 blog/templates/blog/index.html 模板文件。

最后一件事就是实现点击相应的时间后显示该时间下的全部已发表文章列表了，实现思路即通过 url 把对应的年份和月份传给视图函数，视图函数通过年份和月份过滤所需文章，然后再模板渲染即可，实现和 category 与 tag 的方式十分类似：

```python
blog/views.py

class ArchiveView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        # 接收从url传递的year和month参数，转为int类型
        year = int(self.kwargs['year'])
        month = int(self.kwargs['month'])
        # 按照year和month过滤文章
        article_list = Article.objects.filter(created_time__year=year, created_time__month=month)
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(ArchiveView, self).get_context_data(**kwargs)
```

url：

```python
blog/urls.py

url(r'^archive/(?P<year>\d+)/(?P<month>\d+)$', views.ArchiveView.as_view(), name='archive'),
```

templates:

```html
blog/index.html

# 详细请参阅 github 上的模板文件完整代码
{% for year,month_list in date_archive %}
	{{year}} 年
    {% for month in month_list %}
    	<a href="{% url 'blog:archive' year month %}"><p>{{ month }} 月</p></a>
```



## 接下来做什么？

我们的个人 blog 基本已经成型了！首页展示文章列表、标签云、文章归档、分类，文章 markdown 语法标记，代码高亮显示，利用 django 后台，我们可以使用它来写 blog 文章了，你可以先尝试着找一个部署教程把 blog 部署上线。当然我们接下来也会出如何部署的教程，敬请期待。下一周我们将实现评论功能，允许用户对我们发表的文章进行评论。为了学习，我们将不使用第三方 app，而是重新发明轮子。

## Django学习小组简介

**django学习小组**是一个促进 django 新手互相学习、互相帮助的组织。小组在一边学习 django 的同时将一起完成几个项目，包括：

- **一个简单的 django 博客**，用于发布小组每周的学习和开发文档；
- **django中国社区**，为国内的 django 开发者们提供一个长期维护的 django 社区；

上面所说的这个社区类似于 segmentfault 和 stackoverflow ，但更加专注（只专注于 django 开发的问题）。更多的信息请关注我们的 [github 组织](https://github.com/djangoStudyTeam/DjangoBlog)，本教程项目的相关源代码也已上传到 github 上。

同时，你也可以加入我们的邮件列表 [django_study@groups.163.com](mailto:django_study@groups.163.com) ，随时关注我们的动态。我们会将每周的详细开发文档和代码通过邮件列表发出。

如有任何建议，欢迎提 Issue，欢迎 fork，pr，当然也别忘了 star 哦！

