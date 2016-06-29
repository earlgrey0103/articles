# Django学习与实战（六）：文章评论

关键词：django博客开发实战, django学习教程, django列表分页, django语法高亮, web开发教程

URL：writing-your-own-blog-with-django-part-six

> 本文首发于**编程派**微信公众号：编程派（微信号：codingpy）是一个专注Python编程的公众号，每天更新有关Python的国外教程和优质书籍等精选干货，欢迎关注。

通过前五周的时间我们开发了一个简单的个人 Blog，本周我们将实现 blog 文章的评论功能。

## 实现思路

首先需要为评论（Comment）设计一个数据库表，并编写相应的 Model，将评论与文章关联，再编写发表评论的视图，设置相应的 url 即可。

## 评论的 Model 设计

```python
blog/models.py

class BlogComment(models.Model):
    user_name = models.CharField('评论者名字', max_length=100)
    user_email = models.EmailField('评论者邮箱', max_length=255)
    body = models.TextField('评论内容')
    created_time = models.DateTimeField('评论发表时间', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]
```

参照大部分博客评论的样式，我们的 BlogComment Model 包含这些字段：

**user_name**：用户在评论前先要填写他们想使用的昵称

**user_email**：用户在评论前先要填写他们想使用的邮箱

**body**：用户提交的评论内容

**created_time**：评论提交时间

**article**：评论关联的文章，因为一个评论只能关联某一篇文章，而一篇文章下可能有多个评论，因此是一对多的关系，使用 ForeignKey

## 评论的表单

表单用来给服务器后台提交用户填写的数据，例如平时我们看到的填写登录、注册信息的页面就是一个登录、注册表单，用户填写表单信息后，点击提交按钮，表单中填写的内容就会打包发送给服务器后台。我们需要为用户填写评论设置一个表单，django 的 form 模块为我们提供了自动生成表单的功能，如果对表单不熟悉请参阅：[官方文档：表单概述](https://docs.djangoproject.com/en/1.9/topics/forms/) ，以了解基本的表单使用方法（如果你对表单感觉很陌生的话）。

下面我们使用 Django 的 ModelForm （ [django ModelForm 介绍](https://docs.djangoproject.com/en/1.9/topics/forms/modelforms/)  ）类为我们自动生成表单。首先在 blog 目录下新建一个 forms.py （和 models.py 同一目录）文件用来存放 form 的代码：

```python
blog/forms.py

from django import forms
from .models import Article, BlogComment


class BlogCommentForm(forms.ModelForm):
    class Meta:
        """指定一些 Meta 选项以改变 form 被渲染后的样式"""
        model = BlogComment # form 关联的 Model

        fields = ['user_name', 'user_email', 'body']
        # fields 表示需要渲染的字段，这里需要渲染user_name、user_email、body
        # 这样渲染后表单会有三个文本输入框，分别是输入user_name、user_email、body的输入框

        widgets = {
            # 为各个需要渲染的字段指定渲染成什么html组件，主要是为了添加css样式。
            # 例如 user_name 渲染后的html组件如下：
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">

            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入昵称",
                'aria-describedby': "sizing-addon1",
            }),
            'user_email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入邮箱",
                'aria-describedby': "sizing-addon1",
            }),
            'body': forms.Textarea(attrs={'placeholder': '我来评两句~'}),
        }
```

## 视图函数

这里我们一如既往坚持使用基于类的通用视图，由于涉及到评论表单的提交处理，因此我们使用 FormView。这里对 FormView 的使用稍作讲解。

在 Django 的基于函数的视图中，涉及表单的处理的视图其逻辑一般是这样的：

```python
def post_comment(request):
    if request.method =='POST':
    	form = BlogCommentForm(request.POST)
        if form.is_valid():
            ...
        else:
            ...
     else:
        ...
```

即，首先判断用户是否通过表单 POST 了数据过来，如果是，则根据 POST 过来的数据构建一个表单，如果数据验证合法（form.is_valid），则创建评论，否则返回表单提交页。如果没有 POST 数据，则做其他相应的事情。FormView 把这些逻辑做了整合，无需写那么多 if else 语句：

```python
blog/views.py

from django.views.generic.edit import FormView

...

class CommentPostView(FormView):
    form_class = BlogCommentForm # 指定使用的是哪个form
    template_name = 'blog/detail.html'
    # 指定评论提交成功后跳转渲染的模板文件。
    # 我们的评论表单放在detail.html中，评论成功后返回到原始提交页面。

    def form_valid(self, form):
        """提交的数据验证合法后的逻辑"""
        # 首先根据 url 传入的参数（在 self.kwargs 中）获取到被评论的文章
        target_article = get_object_or_404(Article, pk=self.kwargs['article_id'])

        # 调用ModelForm的save方法保存评论，设置commit=False则先不保存到数据库，
        # 而是返回生成的comment实例，直到真正调用save方法时才保存到数据库。
        comment = form.save(commit=False)

        # 把评论和文章关联
        comment.article = target_article
        comment.save()

        # 评论生成成功，重定向到被评论的文章页面，get_absolute_url 请看下面的讲解。
        self.success_url = target_article.get_absolute_url()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        """提交的数据验证不合法后的逻辑"""
        target_article = get_object_or_404(Article, pk=self.kwargs['article_id'])

        # 不保存评论，回到原来提交评论的文章详情页面
        return render(self.request, 'blog/detail.html', {
            'form': form,
            'article': target_article,
            'comment_list': target_article.blogcomment_set.all(),
        })
```

为了方便地重定向回原来提交评论的文章详情页面，我们为文章（Article）的模型新增一个方法：get_absolute_url，调用该方法将得到该 Article 对应的 url，例如这是文章 1 的 url：http://localhost:8000/article/1，则调用后返回 /article/1，这样调用 HttpResponseRedirect 后将返回该 url 下的文章详情页。

```python
blog/models.py

from django.core.urlresolvers import reverse

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    ...

    class Meta:
        ordering = ['-last_modified_time']

    # 新增 get_absolute_url 方法
    def get_absolute_url(self):
        # 这里 reverse 解析 blog:detail 视图函数对应的 url
        return reverse('blog:detail', kwargs={'article_id': self.pk})
```

同时为了在详情页渲染一个评论表单，稍微修改一下 ArticleDetailView 的视图函数，把评论表单 form 插入模板上下文中：

```python
blog/views.py

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks'], )
        return obj

    # 新增 form 到 context
    def get_context_data(self, **kwargs):
        kwargs['comment_list'] = self.object.blogcomment_set.all()
        kwargs['form'] = BlogCommentForm()
        return super(ArticleDetailView, self).get_context_data(**kwargs)
```



## URL 设置

```python
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
	...
    # 设置评论视图对应的 url
    url(r'^article/(?P<article_id>\d+)/comment/$', views.CommentPostView.as_view(), name='comment'),
]
```

## 设置模板文件

新增了一个 comment.html 文件以渲染评论表单和评论列表，并且修改了 detail.html 文件以在文章详情页显示评论表单和评论列表，修改了blog/tatic 下的 style.css 为评论添加样式，由于代码比较多，就不贴出来了，主要是 html 和 css 的前端相关代码，请到 [GitHub 仓库](https://github.com/djangoStudyTeam/DjangoBlog) 更新相关的模板和静态资源文件。

至此，整个评论功能的框架做好了，显示效果如下：

![评论效果演示图](http://7xq740.com1.z0.glb.clouddn.com/%E8%AF%84%E8%AE%BA%E6%BC%94%E7%A4%BA%E5%9B%BE.png)

当然这只是一个评论的框架，很多细节有待处理和完善，但无论如何，用户已经可以为我们的文章发表评论意见了。

## 前情回顾

**第一周**：[Django学习与实战（一）：编写博客的 Model 和首页面](http://codingpy.com/article/writing-your-own-blog-with-django/)

**第二周**：[Django学习与实战（二）：博客详情页面和分类页面](http://codingpy.com/article/writing-your-own-blog-with-django-part-two/)

**第三周**：[Django学习与实战（三）：文章列表分页和代码语法高亮](http://codingpy.com/article/writing-your-own-blog-with-django-part-three/)

**第四周**：[Django学习与实战（四）：基于类的通用视图详解](http://codingpy.com/article/writing-your-own-blog-with-django-part-four/)

**第五周**：[Django学习与实战（五）：标签云与文章归档](http://codingpy.com/article/writing-your-own-blog-with-django-part-five/)
