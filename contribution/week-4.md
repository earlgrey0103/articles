# Django学习与实战（四）：基于类的通用视图详解

关键词：django学习, django实战, django类视图, listview视图, detailview视图, 编程派

> 本文由编程派与Django学习小组合作发布，首发于**编程派**微信公众号：编程派（微信号：codingpy）是一个专注Python编程的公众号，每天更新有关Python的国外教程和优质书籍等精选干货，欢迎关注。

通过三周的时间我们开发了一个简单的个人 Blog，教程地址：

**第一周**：[Django学习与实战（一） —— 编写博客的 Model 和首页面](http://blog.codingpy.com/article/writing-your-own-blog-with-django/)

**第二周**：[Django学习与实战（二） —— 博客详情页面和分类页面](http://blog.codingpy.com/article/writing-your-own-blog-with-django-part-two/)

**第三周**：[Django学习与实战（三） —— 文章列表分页和代码语法高亮](http://blog.codingpy.com/article/writing-your-own-blog-with-django-part-three/)


有朋友反映说对于 Django 的 class-based-view（基于类的通用视图）还有很多不明白的地方，因此接下来我们会出一系列文章讲解几个常用的基于类的视图的用法，并在适当的源码层面下讲解其机理和如何按照我们的需要拓展它。

本教程首先介绍两个 Blog 项目中遇到的通用视图：**ListView** 和 **DetailView**。从名字我们可以对其功能略窥一二，**ListView** 用于 List（列出）一系列 Model （比如文章列表），**DetailView** 获取某个 Model（比如某篇文章）以展示其细节。

## ListView

在开发一个网站时，我们常常需要获取存储在数据库中的某个 Model 的列表，比如 Blog 要获取文章（Article）列表以显示到首页，通常我们都会写如下的视图函数来满足我们的需求：

```python
def index(request):
    """
    获取 Article 列表以渲染首页模板
    """
    article_list = Article.objects.all() # 获取文章列表
    category_list = Category.objects.all() # 获取分类列表
    context = { 'article_list' : article_list , 'category_list' : category_list }
    return render_to_response('blog/index.html',context)
```

当然这仅仅是一个最为基本的视图函数的例子，Django 开发者发现，如果项目里有大量的视图都是实现类似于上面这种获取存储在数据库中的某个 Model 的列表的功能的话，会不断地重复书写诸如下面的代码：

```python
article_list = Article.objects.all()
context = { 'article_list' : article_list }
return render_to_response('blog/index.html',context)
```

就是不断地获取 Model 列表然后渲染模板文件，Django 说写多了开发人员就觉得无聊了，那我们何不把这些逻辑抽象出来放到一个类里？于是 Django 帮我们写好了一个类，专门用于处理上面的情况，这就是 **ListView**，将上面的视图函数转写成类视图如下：

```python
class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.all()
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
```

首先看看 get_queryset 方法，它完成的功能和 article_list = Article.objects.all() 这句代码类似，获取某个 Model 的列表（这里是文章列表），同时我们加入了自己的逻辑，即对 article_lis
t 中的各个 article 进行了 markdwon 拓展，假如仅仅只需要获取 article_list ，则甚至可以不用复写 get_queryset 方法，只需指定一个 model 属性，告诉 Django 去获取哪个 model 的列表就可以了，像这样：

```python
class IndexView(ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"
    model = Article

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
```

第二个复写的方法是 get_context_data 方法，这个方法是用来给传递到模板文件的上下文对象（context）添加额外的内容的（context 的概念在前面的教程中已有介绍，如果这里不懂的话我再简单解释一下，我们在模板文件中会使用 {{ }} 这样的标签来包裹模板变量，这些变量哪里来的？就是视图函数通过 context 传递到模板的）。我们这里因为首页需要显示分类信息，因此我们把 category_list 通过 get_context_data 方法加入了 context 对象，视图函数再帮我们把 context 传递给模板。return super(IndexView, self).get_context_data(**kwargs) 语句的作用是添加了 category_list 到上下文中，还要把默认的一些上下文变量也返回给视图函数，以便其后续处理。

现在有了 model 列表，context，按照视图函数的逻辑应该是把这些传递给模板了，ListView 通过指定 template_name 属性来指定需要渲染的模板，而 context_object_name 是给 get_queryset 方法返回的 model 列表重新命名的，因为默认返回的 model 列表其名字是 object_list，为了可读性，我们可以通过 context_object_name 来重新指定，例如我们这里指定为 article_list。

return render_to_response('blog/index.html',context) 的功能在 ListView 中 Django 已经默认帮我们做了，翻看其源代码就会知道：

```python
... 省略其他代码
def render_to_response(self, context, **response_kwargs):
        """
        Returns a response, using the `response_class` for this
        view, with a template rendered with the given context.

        If any keyword arguments are provided, they will be
        passed to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
... 省略其他代码
```

如果你改变渲染模板的一些行为，通过复写 render_to_response 方法即可。

以上方法在类视图调用 as_view() 方法后会被自动调用。

**ListView 总结**：

- ListView 主要用在获取某个 model 列表中
- 通过 template_name 属性来指定需要渲染的模板，通过 context_object_name 属性来指定获取的 model 列表的名字，否则只能通过默认的 object_list 获取
- 复写 get_queryset 方法以增加获取 model 列表的其他逻辑
- 复写 get_context_data 方法来为上下文对象添加额外的变量以便在模板中访问

## DetailView

前面的 ListView 用于获取某个 model 的列表，获取的是一系列对象，但获取单个 mdoel 对象也是很常见的，比如 Blog 里点击某篇文章后进入文章的详情页，这里获取的就是点击这篇文章。我们通常会写如下视图函数：

```python
def detail(request,article_id):
    article = get_object_or_404(Article,pk=article_id)
    context = { 'article' : article }
    return render_to_response('blog/detail.html',context)
```

同样的，如果这种需求多的话，开发人员就需要枯燥而乏味地大量重复写 article = get_object_or_404(Article,pk=article_id) 这样的句子，Django 通过 DetailView 来把这种逻辑抽象出来，把上面的视图函数转成类视图：

```python
class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks'], )
        return obj
```

model 属性告诉 Django 是获取哪个 model 对应的单个对象，template_name，context_object_name 属性和 ListView 中是一样的作用，pk_url_kwarg 相当于视图函数中的 article_id 参数，已告诉 Django 获取的是 id 为多少的 model 实例。

get_object 方法默认情况下获取 id 为pk_url_kwarg 的对象，如果需要在获取过程中对获取的对象做一些处理，比如对文章做 markdown 拓展，通过复写 get_object 即可实现。

之后的处理就和 ListView 类似了，已经实现了 render_to_response 方法来渲染模板。

以上方法在类视图调用 as_view() 方法后会被自动调用。

**DetailView 总结**

- DetailView主要用在获取某个 model 的单个对象中
- 通过 template_name 属性来指定需要渲染的模板，通过 context_object_name 属性来指定获取的 model 对象的名字，否则只能通过默认的 object 获取
- 复写 get_object 方法以增加获取单个 model 对象的其他逻辑
- 复写 get_context_data 方法来为上下文对象添加额外的变量以便在模板中访问

## 使用类的通用视图的好处

通过上面的例子你可能并未体会到使用类的通用视图的好处，毕竟我们写的基于函数的视图似乎代码量更短，但这仅仅是因为例子简单而已。同时别忘了，类是可以被继承的，假如我们已经写好了一个基于类的通用视图，要对其拓展功能，只需继承原本这个类视图即可，而如果写的是函数呢？拓展性就没有这么灵活，可能需要使用到装饰器等高级技巧，或甚至不得不重复一段代码到新拓展的视图函数中。但本质上而言，基于类的通用视图依然是一个视图函数，因为最终调用时我们会通过 genericview.as_view() 方法把类视图转换成一般的视图，url 配置是这样的：

```python
url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
```

因此，基于类的视图并非什么新的东西，只是为了方便而对一般的视图另一种形式的改写而已，理解了一般的视图写法后，通过阅读其官方文档和类视图的源码，很快就能掌握如何写好类视图了。以下就给出其参考资料：

- [类视图的官方文档](https://docs.djangoproject.com/en/1.9/topics/class-based-views/)
- [类视图的官方文档中文翻译版（可能不全）](http://python.usyiyi.cn/django/topics/class-based-views/index.html)
- 类视图的源代码位于 django/views/generic 目录下


## Django学习小组简介

**django学习小组**是一个促进 django 新手互相学习、互相帮助的组织。小组在一边学习 django 的同时将一起完成几个项目，包括：

- **一个简单的 django 博客**，用于发布小组每周的学习和开发文档；
- **django中国社区**，为国内的 django 开发者们提供一个长期维护的 django 社区；

上面所说的这个社区类似于 segmentfault 和 stackoverflow ，但更加专注（只专注于 django 开发的问题）。更多的信息请关注我们的 [github 组织](https://github.com/djangoStudyTeam/DjangoBlog)，本教程项目的相关源代码也已上传到 github 上。

同时，你也可以加入我们的邮件列表 [django_study@groups.163.com](mailto:django_study@groups.163.com) ，随时关注我们的动态。我们会将每周的详细开发文档和代码通过邮件列表发出。如有任何建议，欢迎提 Issue，欢迎 fork，pr，当然也别忘了 star 哦！

