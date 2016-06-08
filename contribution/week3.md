# Django博客开发实战：文章列表分页和代码语法高亮

关键词：django博客开发实战, django学习教程, django列表分页, django语法高亮, web开发教程

> **摘要：**前两期教程我们实现了博客的 Model 部分，以及 Blog 的首页视图 IndexView，详情页面 DetailView，以及分类页面 CategoryView，前两期教程链接请戳：
>
> [Django 学习小组：博客开发实战第一周教程 —— 编写博客的 Model 与首页面](http://codingpy.com/article/writing-your-own-blog-with-django/)
>
> [Django 学习小组：博客开发实战第二周教程 —— 博客详情页面和分类页面](http://codingpy.com/article/writing-your-own-blog-with-django-part-two/)

本周我们将继续完善我们的个人博客，来实现分页和代码高亮的功能。

***

## 实现文章列表分页功能

我们的数据库中会有越来越多的文章，把它们全部用一个列表显示在首页好像不太合适，如果显示一定数量的文章，比如8篇，这就需要用到分页功能。

Django提供了一些类来帮助你管理分页的数据 -- 也就是说，数据被分在不同页面中，并带有“上一页/下一页”标签。这些类位于`django/core/paginator.py`中。

文章过多，为了提高用户体验，一次只展示部分文章，为用户提供一个分页功能，就像下面这样：

![分页效果图](http://7xq740.com1.z0.glb.clouddn.com/%E5%88%86%E9%A1%B5%E6%95%88%E6%9E%9C%E5%9B%BE.png)

比较完善的分页效果，应该是这样的：

- 用户在哪一页，则当前页号高亮以提示用户所在位置，比如上图显示用户正处在第二页。
- 当用户所处的位置还有上一页时，显示上一页按钮；当还有下一页时，显示下一页按钮，否则不显示。
- 当分页较多时，总是显示当前页及其前几页和后几页的页码（教程中使用的是两页），其他页码用省略号代替。
- 总是显示第一页和最后一页的页码。

### 模板标签

关于分页需要使用到的的 API ，Django 官方文档对此有十分详细的介绍，它还给出了一个完整示例，读懂它的代码后仿照它即可实现基本的分页功能。请参考[官方文档对于分页的示例](https://docs.djangoproject.com/en/1.9/topics/pagination/)，如果你不习惯英文的话，也可以参照网友的翻译版本[Django 中文文档：分页](http://python.usyiyi.cn/django/topics/pagination.html)。下面就根据官方的示例来实现我们的需求。

尽管可以把分页逻辑直接写在视图内，但是为了通用性，我们使用一点点 Django 更加高级的技巧——模板标签（TemplateTags）。分页功能的实现有很多第三方 APP 可以直接使用，但是为了学习 Django 的知识，所以我们自己实现一个。这些第三方 APP 基本都是使用的模板标签，因此这可能是一种比较好的实践。

为了使用模板标签，Django 要求我们先建立一个 templatetags 文件夹，并在里面加上  `__init__.py`文件以指示 python 这是一个模块（python 把含有该问价的文件夹当做一个模块，具体请参考任何一个关于 python 模块的教程）。并且 templatetags 文件夹和你的 model.py，views.py 文件是同级的，也就是说你的目录结构看起来应该是这样：

```python
polls/
    __init__.py
    models.py
    templatetags/
        __init__.py
        poll_extras.py
    views.py
```

（这个目录结构引自官方文档，关于详细的模板标签的介绍请参考官方文档：[custom template tags](https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/)，不一定全部读懂，但还是推荐花几十分钟扫一遍明白其大致说了什么）。

在 templatetags 目录下建立一个 paginate_tags .py 文件，准备工作做完，结合 Django 的模板系统，我们来看看该如何编写我们的程序。

### 如何编写分页代码

首先来回顾一下 Django 的模板系统是如何工作的，回想一下视图函数的工作流程，视图函数接收一个 Http 请求，经过一系列处理，通常情况下其会渲染某个模板文件，把模板文件中的一些用 {{ }} 包裹的变量替换成从该视图函数中相应变量的值。事实上在此过程中 Django 悄悄帮我们做了一些事情，它把视图函数中的变量的值封装在了一个 Context （一般翻译成上下文）对象中，只要模板文件中的变量在 Context 中有对应的值，它就会被相应的值替换。

因此，我们的程序可以这样做：首先把取到的文章列表（官方术语是一个 queryset）分页，用户请求第几页，我们就把第几页的文章列表传递给模板文件；另外还要根据上面的需求传递页码值给模板文件，这样只要把模板文件中的变量替换成我们传递过去的值，那么就达到本文开篇处那样的分页显示效果了。

```python
paginate.py

from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# 这是分页功能涉及的一些类和异常，官方文档对此有详细介绍。当然从命名也可以直接看出它们的用途：Paginator（分页），PageNotAnInteger（页码不是一个整数异常），EmptyPage（空的页码号异常）

register = template.Library()
# 这是定义模板标签要用到的

@register.simple_tag(takes_context=True)
# 这个装饰器表明这个函数是一个模板标签，takes_context = True 表示接收上下文对象，就是前面所说的封装了各种变量的 Context 对象。
def paginate(context, object_list, page_count):
    # context是Context 对象，object_list是你要分页的对象，page_count表示每页的数量

    left = 3 # 当前页码左边显示几个页码号 -1，比如3就显示2个
    right = 3 # 当前页码右边显示几个页码号 -1

    paginator = Paginator(object_list, page_count) # 通过object_list分页对象
    page = context['request'].GET.get('page') # 从 Http 请求中获取用户请求的页码号

    try:
        object_list = paginator.page(page) # 根据页码号获取第几页的数据
        context['current_page'] = int(page) # 把当前页封装进context（上下文）中
        pages = get_left(context['current_page'], left, paginator.num_pages) + get_right(context['current_page'], right, paginator.num_pages)
        # 调用了两个辅助函数，根据当前页得到了左右的页码号，比如设置成获取左右两边2个页码号，那么假如当前页是5，则 pages = [3,4,5,6,7],当然一些细节需要处理，比如如果当前页是2，那么获取的是pages = [1,2,3,4]

    except PageNotAnInteger:
        # 异常处理，如果用户传递的page值不是整数，则把第一页的值返回给他
        object_list = paginator.page(1)
        context['current_page'] = 1 # 当前页是1
        pages = get_right(context['current_page'], right, paginator.num_pages)
    except EmptyPage:
        # 如果用户传递的 page 值是一个空值，那么把最后一页的值返回给他
        object_list = paginator.page(paginator.num_pages)
        context['current_page'] = paginator.num_pages # 当前页是最后一页，num_pages的值是总分页数
        pages = get_left(context['current_page'], left, paginator.num_pages)

    context['article_list'] = object_list # 把获取到的分页的数据封装到上下文中
    context['pages'] = pages # 把页码号列表封装进去
    context['last_page'] = paginator.num_pages # 最后一页的页码号
    context['first_page'] = 1 # 第一页的页码号为1
    try:
        # 获取 pages 列表第一个值和最后一个值，主要用于在是否该插入省略号的判断，在模板文件中将会体会到它的用处。注意这里可能产生异常，因为pages可能是一个空列表，比如本身只有一个分页，那么pages就为空，因为我们永远不会获取页码为1的页码号（至少有1页，1的页码号已经固定写在模板文件中）
        context['pages_first'] = pages[0]
        context['pages_last'] = pages[-1] + 1
        # +1的原因是为了方便判断，在模板文件中将会体会到其作用。

    except IndexError:
        context['pages_first'] = 1 # 发生异常说明只有1页
        context['pages_last'] = 2 # 1 + 1 后的值

    return ''  # 必须加这个，否则首页会显示个None


def get_left(current_page, left, num_pages):
    """
    辅助函数，获取当前页码的值得左边两个页码值，要注意一些细节，比如不够两个那么最左取到2，为了方便处理，包含当前页码值，比如当前页码值为5，那么pages = [3,4,5]
    """
    if current_page == 1:
        return []
    elif current_page == num_pages:
        l = [i - 1 for i in range(current_page, current_page - left, -1) if i - 1 > 1]
        l.sort()
        return l
    l = [i for i in range(current_page, current_page - left, -1) if i > 1]
    l.sort()
    return l


def get_right(current_page, right, num_pages):
    """
    辅助函数，获取当前页码的值得右边两个页码值，要注意一些细节，比如不够两个那么最右取到最大页码值。不包含当前页码值。比如当前页码值为5，那么pages = [6,7]
    """
    if current_page == num_pages:
        return []
    return [i + 1 for i in range(current_page, current_page + right - 1) if i < num_pages - 1]
```

首先让我们来看看整个分页程序的执行过程，模板标签本质上来说就是一个 python 函数而已，只是该函数可以被用在 Django 的模板系统里面。函数就是接受参数，返回一个值。例如我们这里定义的 `def paginate(context, object_list, page_count):` 分页函数，它接收了这么一些参数，经过各种处理，最终返回了 None 。

### 模板文件编写

接下来把需要变量值都添加到上下文了，看看我们的模板文件该怎么写：

```html
templates/blog/pagination.html

<div id="pagenavi" class="noselect">
    {% if article_list.has_previous %} # 判断是否还有上一页，有的话要显示一个上一页按钮
        <a class="previous-page" href="?page={{ article_list.previous_page_number }}">
            <span class="icon-previous"></span>上一页
        </a>
    {% endif %}

    # 页码号为1永远显示
    {% if first_page == current_page %} # 当前页就是第一页
        <span class="first-page current">1</span>
    {% else %} # 否则的话，第一页是可以点击的，点击后通过?page=1的形式把页码号传递给视图函数
        <a href="?page=1" class="first-page">1</a>
    {% endif %}

    {% if pages_first > 2 %} # 2以前的页码号要被显示成省略号了
        <span>...</span>
    {% endif %}

    {% for page in pages %} # 通过for循环把pages中的值显示出来
        {% if page == current_page %} # 是否当前页，按钮会显示不同的样式
            <span class="current">{{ page }}</span>
        {% else %}
            <a href="?page={{ page }}">{{ page }}</a>
        {% endif %}
    {% endfor %}

  	# pages最后一个值+1的值小于最大页码号，说明有页码号需要被省略号替换
    {% if pages_last < last_page %}
        <span>...</span>
    {% endif %}

  	# 永远显示最后一页的页码号，如果只有一页则前面已经显示了1就不用再显示了
    {% if last_page != 1 %}
        {% if last_page == current_page %}
            <span class="current">{{ last_page }}</span>
        {% else %}
            <a href="?page={{ last_page }}">{{ last_page }}</a>
        {% endif %}
    {% endif %}

    # 还有下一页，则显示一个下一页按钮
    {% if article_list.has_next %}
        <a class="next-page" href="?page={{ article_list.next_page_number }}">
            下一页<span class="icon-next"></span>
        </a>
    {% endif %}
</div>
```

至此代码部分编写完了，看看如何使用这个模板标签吧，比如我们要在首页对文章列表进行分页：

```html
templates/blog/index.html

{% load paginate_tags %} # 首先必须通过load模板标签载入分页标签
{% paginate article_list 7 %} 把文章列表传给paginate函数，每页分7个，context上下文则自动被传入，无需显示指定

{% for article in article_list %}
    # display the article information
{% endfor %}

{% include 'blog/pagination.html' %}
# 这里用到一个 include 技巧，把pagination的模板代码写在单独的pagination.html文件中，这样哪里需要用到哪里就 include 进来就行，提高代码的复用性。
```

至此，整个分页功能就完成了，看看效果：

![文章分页演示](http://7xq740.com1.z0.glb.clouddn.com/%E6%96%87%E7%AB%A0%E5%88%86%E9%A1%B5%E6%BC%94%E7%A4%BA.png)

## 支持 fetch code 与代码高亮

### fetch code

我们的博客文章是支持 markdown 语法标记的（使用的是 markdown2 第三方 app），markdown 比较常用的两个特性是 fetch code 和语法高亮。由于我们目前没有对博客文章的 markdown 标记做任何拓展，因此要标记一段代码，我们必须在每行代码前缩进 4 个空格，这很不方便。而 fetch code 可以让我们在写文章时只按照下面的输入就可以标记一段代码，相比每行缩进四个空格要方便很多：

```python
def test_function():
    print('fectch code like this!')
```

下面来拓展它。很简单，把用 markdown 标记的语句拓展一下，在 Views.py 中找到 IndexView，其中有一句代码的作用是来 markdown 我们的博客文章的：

```python
for article in article_list:
    article.body = markdown2.markdown(article.body, )
```

将 markdown 函数拓展一下，传入如下参数即可：

``` python
for article in article_list:
    article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
```

这样，每次要输入一段代码时，按照上面的语法输入就可以了，比如我输入下面的代码段：


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

来看看效果：

![fech code](http://7xq740.com1.z0.glb.clouddn.com/fetch_code%E6%BC%94%E7%A4%BA%E5%9B%BE.png)

此外别忘了把其他做了 markdown 标记的地方也做相应拓展，目前我们一共有三处：IndexView，DetailView，CategoryView。

### 代码高亮

现在输入代码方便了，但是美中不足的是代码只有一种颜色，我们想要代码高亮，需要使用到 Pygments 包。先安装它：pip install pygments，安装好后别忘了添加到 settings.py 中：

```python
settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'markdown2',
    'pygments', # 添加进来
]
```

pygments 的工作原理是把代码切分成一个个单词，然后为这些单词添加 css 样式，不同的词应用不同的样式，这样就实现了代码颜色的区分，即高亮了语法，因此我们要引入一些 css 样式文件。在我们的 [GitHub](https://github.com/djangoStudyTeam/DjangoBlog/tree/feature/blog/static/blog/css) 项目的 [DjangoBlog](https://github.com/djangoStudyTeam/DjangoBlog/tree/feature)/[blog](https://github.com/djangoStudyTeam/DjangoBlog/tree/feature/blog)/[static](https://github.com/djangoStudyTeam/DjangoBlog/tree/feature/blog/static)/**blog**/css 目录下有相应的文件，拷贝下来添加到你的项目相同目录下就可以了。之后在模板中引入样式文件：

```html
templates/base.html

<head>
    <meta charset="UTF-8">
    <title>Myblog</title>
    ...
    <link rel="stylesheet" href="{% static 'blog/css/pygments/github.css' %}">
    引入上面的样式文件,当然里面有很多样式文件，喜欢哪个引哪个，比如我引的是github风格的语法高亮
    ...
</head>
```

看看效果：

![代码高亮](http://7xq740.com1.z0.glb.clouddn.com/%E4%BB%A3%E7%A0%81%E9%AB%98%E4%BA%AE.png)

这里比较麻烦的是必须指定代码对应的语言，有人说 pygments 可以自动识别语言的，但是我目前的测试来看似乎没有效果。目前没有找到设置方法，如有知道的朋友请告知。

整个完整的 Blog 项目代码请访问我们的 [GitHub 组织仓库](https://github.com/djangoStudyTeam/DjangoBlog)获取。

声明：本教程只是演示如何实现分页和 markdown 语法高亮功能，在细节上处理上还有很多需要斟酌的地方，如果您有更好的实现方式或者实践经验，恳请传授我们。如果您对本教程有任何不清晰的地方或者其他意见和建议，请及时通过邮件列表或者 [GitHub Issue](https://github.com/djangoStudyTeam/DjangoBlog/issues) 或者评论留言反馈给我们。您的反馈和建议是我们持续改善本教程的最佳方式。

## 接下来做什么？

个人博客功能逐步完善，接下来的教程我们将继续实现个人博客常带的功能：**标签云**和**文章归档**，敬请期待下一期教程。如果你还有其他想实现的功能，也请告诉我们，我们会在教程中陆续实现。

## Django学习小组简介

**django学习小组**是一个促进 django 新手互相学习、互相帮助的组织。

小组在一边学习 django 的同时将一起完成几个项目，包括：

- **一个简单的 django 博客**，用于发布小组每周的学习和开发文档；
- **django中国社区**，为国内的 django 开发者们提供一个长期维护的 django 社区；

上面所说的这个社区类似于 segmentfault 和 stackoverflow ，但更加专注（只专注于 django 开发的问题）。

目前小组正在完成第一个项目，本文即是该项目第三周的相关文档。

更多的信息请关注我们的 [github 组织](https://github.com/djangoStudyTeam/DjangoBlog)，本教程项目的相关源代码也已上传到 github 上。

同时，你也可以加入我们的邮件列表 [django_study@groups.163.com](mailto:django_study@groups.163.com) ，随时关注我们的动态。我们会将每周的详细开发文档和代码通过邮件列表发出。

如有任何建议，欢迎提 Issue，欢迎 fork，pr，当然也别忘了 star 哦！

