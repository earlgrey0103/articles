# 升级到Flask 0.11要注意哪些问题

关键词：flask最新版, flask新特性, flask升级, flask开发, flask文档

URL：flask-just-upgraded-to-0.11

前天微信推送里提到了Flask已经更新至0.11版，今天我们就具体来介绍下升级到新版本需要注意的一些事。

首先，说明下这个版本的由来。Flask很早以前就已经发布了0.10版，用在生产环境也没有啥问题。0.10版本之后，开发团队原定是要发布1.0版的，不过考虑到时间间隔实在是太长，所以额外再推出一个0.11版，缩减了一些要在1.0版推出的变化，降低过渡的难度。

为了查看新版本的特性，我们先升级Flask。方法很简单，如下所示：

``pip install -U flask``

## 有哪些变化？

Flask官方文档的变更日志中，提到了一共33处变化。我这里选择性地列出几个比较重大的变化，更详细的内容[请看文档](http://flask.pocoo.org/docs/0.11/changelog/#version-0-11)。

### 调试

新版本中移除了Flask应用中的 debug_log_format 属性，这意味着如果没有启用调试，那么Flask会默认记录日志，日志记录格式是硬编码在框架中的。不过开发者可以通过新增的 LOGGER_HANDLER_POLICY 配置键停用默认的日志记录程序，从而使用自定义的日志记录器。

### 模板

除了在调试模式之外，不会再自动重载模板。可以通过新增的 TEMPLATES_AUTO_RELOADT 配置键进行配置。

render_template_string()函数改为默认自动对模板变量进行自动转义，与 render_template() 的行为更加一致。

### 错误处理

在Flask中，一般推荐按如下方式注册错误处理程序：

```python
@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!'
```

在0.11版之前，如果在一个函数上装饰多个错误程序，那么各自的优先级是按照装饰/调用顺序处理。现在则改为按照异常的继承层级，意味着针对更加具体异常的处理程序会优先执行，而不再执行针对更普遍异常的程序。

另外，直接在应用实例上注册处理程序会报ValueError。

***

最重要的两个变化放到最后。

### flask cli

最新的版本集成了Armin自己开发的 click 库，提供了 flask 命令行命令和 flask.cli模块，用于开启本地调试服务器。相对于过去使用 flask.run()方法，使用 flask 命令更快更可靠，而且可以替代 Flask-Script 第三方扩展。

在虚拟环境中安装Flask后，就可以直接在命令行使用 flask 命令。

![flask cli](http://ww1.sinaimg.cn/mw690/006faQNTgw1f4g4ebldxhj30vm0muwkz.jpg)

### 模块导入

新版中弃用了以 flask.ext 形式导入扩展模块，应该改用 flask_foo。

如果你仍使用原来的形式，Flask 会对每个这样导入的扩展报 flask.exthook.ExtDeprecationWarning 警示。为了便利开发者，Flask团队提供了一个叫做 flask-ext-migrate 的迁移工具，可以自动改写导入语句。

举例来看具体变化：

```python
from flask.ext import foo => import flask_foo as foo
from flask.ext.foo import bam => from flask_foo import bam
import flask.ext.foo => import flask_foo
```

