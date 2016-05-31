#Django学习小组：Blog开发实战第二周教程
上周我们完成了博客的 Model 部分，以及 Blog 的首页视图 IndexView。

本节接上周的文档 [Django学习小组出品：一起来做一个简单的Blog第一周文档（教程）](http://www.jianshu.com/p/3bf9fb2a7e31)，我们继续给博客添加功能，以及改善前面不合理的部分。本教程将带你完成 Blog 的详情页面，即用户点击首页的文章标题或者阅读全文按钮将跳转到文章的详情页面来阅读整篇文章。其次将调整一些目录结构以使其在实践应用中更加合理。

> 提示：在阅读教程的过程中，如有任何问题请访问我们项目的 [GithHub](https://github.com/djangoStudyTeam/DjangoBlog) 或评论留言以获取帮助，本教程的相关代码已全部上传在 Github。如果你对我们的教程或者项目有任何改进建议，请您通过随时告知我们。更多交流请加入我们的邮件列表 [django_study@groups.163.com](mailto:django_study@groups.163.com)。

#重写URL
对于一个有多个 app 的项目，把所有的`urlpatterns`都放在项目的`urls.py`似乎不是一个很合适的选择，为此我们需要在`blog`文件夹下新建一个文件`urls.py`，把跟这个 app 相关的`urlpatterns`都放在这个文件里。
文件中的`urlpatterns`看不懂暂时没关系，下面很快就会介绍它。
```python
# blog/urls.py
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^blog/$', views.IndexView.as_view(), name='index'),
    url(r'^blog/article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^blog/category/(?P<cate_id>\d+)$', views.CategoryView.as_view(), name='category'),
]
# 使用(?P<>\d+)的形式捕获值给<>中得参数，比如(?P<article_id>\d+)，当访问/blog/article/3时，将会将3捕获给article_id,这个值会传到views.ArticleDetailView,这样我们就可以判断展示哪个Article了
```
然后在项目的`urls.py`中包含（include）它:
```python
# DjangoBlog/blog_project/urls.py
from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls', namespace='blog', app_name='blog'))
]
# 其中namespace参数为我们指定了命名空间，这说明这个urls.py中的url是blog app下的，这样即使不同的app下有相同url也不会冲突了。
```
这样，我们就重写了URL，看起来是不是更有条理了？
#新增文章详情页
```python
class ArticleDetailView(DetailView):
# Django有基于类的视图DetailView,用于显示一个对象的详情页，我们继承它
    model = Article
    # 指定视图获取哪个model
    
    template_name = "blog/detail.html"
    # 指定要渲染的模板文件
    
    context_object_name = "article"
    # 在模板中需要使用的上下文名字
    
    pk_url_kwarg = 'article_id'
    # 这里注意，pk_url_kwarg用于接收一个来自url中的主键，然后会根据这个主键进行查询
    # 我们之前在urlpatterns已经捕获article_id

    # 指定以上几个属性，已经能够返回一个DetailView视图了，为了让文章以markdown形式展现，我们重写get_object()方法。
    def get_object(self):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = markdown2.markdown(object.body)
        return obj
```
`get_object()`返回该视图要显示的对象。如果有设置 queryset，该queryset 将用于对象的源；否则，将使用get_queryset(). get_object()从视图的所有参数中查找`pk_url_kwarg`参数； 如果找到了这个参数，该方法使用这个参数的值执行一个基于主键的查询。

新建一个模板 detail.html 来展示我们的文章详情

```html
blog/templates/blog/detail.html

{% extends 'base.html' %}
{% block content %}
    <div id="bd" class="wrp clear-fix">
        <div id="main">
            <div id="detail-title">
                <ul id="single-nav">
               
     <li><a href="{% url 'blog:index' %}">首页</a></li>
                    <li>&gt;</li>
                    <li>
                        <ul class="post-categories">
                            <li><a href="" title=""
                                   rel="category">{{ article.category.name }}</a>
                            </li>
                        </ul>
                    </li>
                    <li>&gt;</li>
                    <li class="title-active"><a href="{% url 'blog:detail' article.pk %}"
                                                rel="bookmark">{{ article.title }}</a>
                    </li>
                </ul>
            </div>
            <div id="post-1951"
                 class="post-1951 post type-post status-publish format-standard hentry category-meida-report">
                <div class="post-hd">
                    <h1 class="title">{{ article.title }}</h1>
                </div>
                <div class="date-read">
                    <i class="icon-date"></i><span class="date">{{ article.last_modified_time|date:"Y年n月d日" }}</span>
                </div>
                <div class="post-bd">
                    {{ article.body |safe }}
                </div>
            </div>
        </div>
    </div>
    <div id="previous-next-nav">
    </div>
{% endblock %}
```
整个执行流程就是这样的：

假设用户要访问某篇文章，比如他点击了某篇文章的标题，在模板文件中（首页的模板，代码可以参见 [GitHub](https://github.com/djangoStudyTeam/DjangoBlog/blob/master/blog/templates/blog/index.html) 上的 index.html），他点击的就是这样一个标签：

```html
<h1 class="title">
  <a href="{% url 'blog:detail' article.pk %}">{{ article.title }}</a>
</h1>
```

<a> 标签是一个超链接，用户点击后会跳转到由 href 指定的 url，这里我们使用了 django 自带的模板标签 url 标签，它会自动解析 blog:detail 这个视图函数对应的 url，并且把 article.pk（文章的主键）传递给detail 视图函数 。detail 的 url 是这样定义的：

```python
url(r'^blog/article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail')
```

假设用户点击了第三篇文章，那么该 url 会被解析成：/blog/article/3，其中 3 被传递给了详情页面视图函数。

现在视图函数被调用，它首先根据传给它的参数获自动调用 get_object 方法取到文章的 model，然后根据 context_object_name = "article" 把 article 加入到上下文中（可以理解为携带着这个变量及其值并要传递给模板文件的对象，模板文件从这个对象中取出模板变量对应的值并替换。），之后渲染 template_name = "blog/detail.html" 指定的模板文件，至此用户就跳转到了文章详情页，效果如下：

![文章详情页](http://7xq740.com1.z0.glb.clouddn.com/detail.png)

#新增分类视图

点击某个分类，展示该分类下所有文章，其逻辑和首页展示全部文章列表是一样的，唯一不同的是我们获取的不是全部文章，而是该分类下的文章。代码如下：
```python
class CategoryView(ListView):
# 继承自ListView,用于展示一个列表

    template_name = "blog/index.html"
    # 指定需要渲染的模板
    
    context_object_name = "article_list"
    # 指定模板中需要使用的上下文对象的名字

    def get_queryset(self):
        #get_queryset 的作用已在第一篇中有介绍，不再赘述
        article_list = Article.objects.filter(category=self.kwargs['cate_id'],status='p')
        # 注意在url里我们捕获了分类的id作为关键字参数（cate_id）传递给了CategoryView，传递的参数在kwargs属性中获取。
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
        return article_list
    
    # 给视图增加额外的数据
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        # 增加一个category_list,用�
��在页面显示所有分类，按照名字排序
        return super(CategoryView, self).get_context_data(**kwargs)
```
这里我们复用的是主页的模板（因为展示的东西都是一样的），点击相应的分类，展示该分类下所有文章。同样别忘了如果要用户点击分类按钮跳转到分类页面的话，要指定 <a> 标签的 href 属性，善用 url 模板标签，防止硬编码 url，像这样：

```html
<li class="cat-item">
  <a href="{% url 'blog:category' category.pk %}">{{ category.name }}</a>
</li>
```

分类显示效果如下，显示分类二下的全部文章：

![分类显示效果图](http://7xq740.com1.z0.glb.clouddn.com/category.png)

# 接下来做什么？

至此，我们完成了博客的首页，详情展示页以及分类功能，基本的框架算是完成了。接下来我们会为我们的 Blog 添加更多高级的功能，包括有标签云、文章归档、文章分页等。敬请期待我们下一周的教程。如果你希望为你的 Blog 添加其他更加独特的功能，也请随时告诉我们。

# Django学习小组简介

**django学习小组**是一个促进 django 新手互相学习、互相帮助的组织。

小组在一边学习 django 的同时将一起完成几个项目，包括：

- **一个简单的 django 博客**，用于发布小组每周的学习和开发文档；
- **django中国社区**，为国内的 django 开发者们提供一个长期维护的 django 社区；

上面所说的这个社区类似于 segmentfault 和 stackoverflow ，但更加专注（只专注于 django 开发的问题）。

目前小组正在完成第一个项目，本文即是该项目第二周的相关文档。

更多的信息请关注我们的 [github 组织](https://github.com/djangoStudyTeam/DjangoBlog)，本教程项目的相关源代码也已上传到 github 上。

同时，你也可以加入我们的邮件列表 [django_study@groups.163.com](mailto:django_study@groups.163.com) ，随时关注我们的动态。我们会将每周的详细开发文档和代码通过邮件列表发出。

如有任何建议，欢迎提 issue，欢迎 fork，pr，当然也别忘了 star 哦！






