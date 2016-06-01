# 升级到Flask 0.11要注意哪些问题

前天微信推送里提到了Flask已经更新至0.11版，今天我们就具体来介绍下升级到新版本需要注意的一些事。

首先，说明下这个版本的由来。Flask很早以前就已经发布了0.10版，用在生产环境也没有啥问题。0.10版本之后，开发团队原定是要发布1.0版的，不过考虑到时间间隔实在是太长，所以额外再推出一个0.11版，缩减了一些要在1.0版推出的变化，降低过度的成本。

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

The behavior of error handlers was changed. The precedence of handlers used to be based on the decoration/call order of errorhandler() and register_error_handler(), respectively. Now the inheritance hierarchy takes precedence and handlers for more specific exception classes are executed instead of more general ones. See Error handlers for specifics.

Trying to register a handler on an instance now raises ValueError.

Note

There used to be a logic error allowing you to register handlers only for exception instances. This was unintended and plain wrong, and therefore was replaced with the intended behavior of registering handlers only using exception classes and HTTP error codes.

最重要的两个变化放到最后。

### flask cli

Added flask and the flask.cli module to start the local debug server through the click CLI system. This is recommended over the old flask.run() method as it works faster and more reliable due to a different design and also replaces Flask-Script.

![flask cli](http://ww1.sinaimg.cn/mw690/006faQNTgw1f4g4ebldxhj30vm0muwkz.jpg)

After installation of Flask you will now find a flask script installed into your virtualenv. If you don’t want to install Flask or you have a special use-case you can also use python -m flask to accomplish exactly the same.

The way this script works is by providing access to all the commands on your Flask application’s Flask.cli instance as well as some built-in commands that are always there. Flask extensions can also register more commands there if they desire so.

### 模块导入

flask.ext is now deprecated

Extension imports of the form flask.ext.foo are deprecated, you should use flask_foo.


from flask.ext import foo => import flask_foo as foo
from flask.ext.foo import bam => from flask_foo import bam
import flask.ext.foo => We'd have to rewrite any reference to flask.ext.foo in the code further below. If that's too hard, just skip those and show a warning.


The old form still works, but Flask will issue a flask.exthook.ExtDeprecationWarning for each extension you import the old way. We also provide a migration utility called flask-ext-migrate that is supposed to automatically rewrite your imports for this.
