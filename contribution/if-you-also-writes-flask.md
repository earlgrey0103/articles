# 如果你也想写Flask

关键词：flask web开发, Python web 开发, flask博客开发, flask微框架

URL：if-you-also-want-to-write-flask

***

上次我在编程派发表了[一篇关于如何备份文件至七牛的文章](http://codingpy.com/article/how-to-backup-server-data-using-python-and-qiniu/)，不说好坏，文章发表出去之后我思考了很多，最重要的一点是：如果我是读者，我会愿意阅读完整这篇文章吗？

如果自己是读者该怎样去文章，我是为了什么去读文章，读文章之后我能获得什么？解决现有的问题？还是照搬一些代码到自己的程序上？我们到底为什么要写代码和阅读？我最近一直在思考这些问题。

所以，今天我想以一个全新的视角去写一篇文章，也许会不成功。但我想尝试一下不同的写作视角。

本文的标题是《如果你也在写Flask》。顾名思义，这是一篇关于Flask开发的文章。本文将包含但不限于以下内容：

- Flask是什么
- 使用Flask制作自己的博客
- 扩展性到底在哪里
- 从0到1该如何学习

## Flask是什么

Flask是由Python语言编写开发而成的`轻量级`Web服务框架，Flask是由Armin Ronacher制造的一个愚人节玩笑而发展至今。关于Flask更多权威的介绍请访问Wiki浏览-[点击访问][1]。

> EarlGrey：我在这篇文章 >>> [这可能是开发者社区最成功的愚人节玩笑](http://codingpy.com/article/april-fools-joke-became-flask/) 中较为详细地介绍了Flask背后的由来。

### 我心中的Flask是什么

Flask的快捷轻便可扩展性高的优点，可供于我想到什么去开发什么的想法，我不用考虑太多。只用想现在我可能想要做一个什么了，那么Flask就可以做到。Flask拥有太多扩展包，你只需要了解这些扩展包的使用方法就可以做到很多你意想不到的功能。

Flask是基于Python所编写的快捷Web框架，那出现一个疑问了，Flask和Python到底有多大的关联？这是一个很深入的问题，而我的理解是Flask即Python，Python非Flask，而我也不会去解释为什么。因为这是每个人的看法，我不想每位看文章的朋友因为阅读了我的文章就给思维上了个锁，我发现太多文章都时读者在阅读的过程中把思维给锁住了，这非常影响阅读者的思考。

当然，我并不是说Flask不可以构建大型项目，而大型项目的构建准备工作需要的更多，这些并不在本文的讨论范围之内。以后如果有时间可以跟大家再来探讨“该怎样去思考构建大型项目”。

**现在，请思考你对于Flask的理解是？**

## 使用Flask开发自己的博客

本章可能会遇到很多困难，在实际操作过程当中如果遇到问题，建议使用Google去搜索问题，搜索时注意关键词的使用可以有助你更好寻找到问题的答案，例如搜索“Flask-Login 文档”，“Flask-SQLalchemy 字段说明”等等……又或者给我发mail或者去sf.gg问一下问题，发问时请不要用一些愚蠢的提问方式例如“请问我这里是哪里错了？”，“这个错误该如何解决？”，我们应在标题写入对问题的精要部分，使得为你解决问题的人们更有兴致的帮助你。

这里我推荐一本书[学会提问][2]，如果你有时间可以下载到Kindle或者手机阅读，你当然可以作为厕所读物。慢慢看，细细品。

好了，进入正题，构建Flask-Blog的流程分为以下步骤：

1. 搭建Flask开发环境 / *完全说明*
2. 思考数据库模型 / *完全说明*
3. 编写逻辑代码 / *完全说明*
4. 测试、完善 / *简单描述*
5. 部署到公网服务器 / *简单描述*
6. 开始扩展你的Blog程序/ *自己完成*

所有步骤的注明，会和本文密切相关。我希望读者们可以边看边互动，这样才会有学习的意义。

### 搭建Flask开发环境

无论你是使用Linux，Mac，Windows搭建环境都是很轻松的，阅读[官方文档][3]就能做到环境的部署这里我在说明一遍。

#### 安装virtualenv

Linux and Mac：

```
sudo pip install virtualenv
```

Windows:

首先需要把Python根目录下的Script目录指定到系统PATH内，然后执行。最重要的是，你需要在windows下安装GIT，利用Git bash来代替原始CMD。

```
easy_install pip  #安装pip
pip install virtualenv
```

#### 创建项目文件夹

Mac、Linux

```
mkdir -p ~/Document/flask-bb & cd ~/Document/flask-bb #创建文件夹并移动到文件夹
virtualenv venv #创建virtualenv独立环境
```

Windows

在你想要的盘符创建一个文件夹名为flask-bb，路径中不要带中文。

```
在项目文件夹内右击选择Git Bash Here
virtualenv venv #创建virtualenv独立环境
```

#### 使用virtualenv

Mac、Linux在项目目录下输入

```
. venv/bin/activate #注意前面有个 . 并空格
终端会进入virtualenv环境,并在提示符最前面加入(venv)
```

Windows系统下，同样在项目文件夹内打开Git Bash

```bash
. venv/Script/activate #注意 . 和空格
```

现在我们已经成功的部署并使用到了virtualenv环境，至于virtualenv到底有什么用呢？它其实就是一个便捷的Python虚拟环境，因为Flask的特性，每个项目里都会有不同扩展包来扩展项目本身。为了洁癖精神，不把每一个使用的扩展包都安装到**根Python环境**里。所以我们进行了一个小型的虚拟Python环境，让这些**针对于**当前项目的Flask扩展包得以应用安装。

提示：**virtualenv**不仅仅不适用于Flask，还可以是任何Python的开发环境，只要你有需求。你可以针对你不同的项目设定不同的virtualenv环境。

#### 你需要一个数据库

在本文中，我选择使用Mysql作为数据库，虽然sqlite更简单，可随意创建文件，有了问题直接删除。但为了我们在本地开发和实际部署在生产保持数据库的一致，所以在本地和服务器上都使用Mysql，而基于Mysql的GUI管理软件也有很多，大家自行搜索一下就可以在自己的系统环境中安装好Mysql。

本次我使用的是Mysql 5.6版本，并创建一个数据库编码格式为`utf8mb4`默认排序规则为`utf8mb4_bin`的数据库表。建议创建一个新的账户来管理此数据库表。

#### 运行Flask

部署好Flask环境后，我们需要怎样去运用它呢？

首先我们需要安装Flask。进入virtualenv环境后，运行如下命令：

```bash
pip install flask   #安装Flask
pip install flask-script    #安装Flask-Script 来代替原生启动管理
pip install flask-SQLAlchemy    #安装Flask-SQLAlchemy来管理数据库
pip install mysql-python    #安装mysql-python驱动数据库
```
接下来要特别注意，对于我们现在所需求的FlaskBlog的全部功能的代码都可以写到一个.py文件里，但我非常不推荐这样（我相信也没人会推荐这么做）。如果这样写非常不便于扩展功能面，本文全部描述的功能虽然仅限于非常基础的内容，但想要扩展是非常容易的，而把整个项目的文件及文件夹规划好了，更便于我们后期再次扩展开发时的效率！

以下文章所有文件，我会基于根目录来标注文件路径。

例如：

`/config.py`则在项目目录根上。

`/app/main.py`则在项目目录创建一个app的文件夹下创建main.py

开始编写吧！

`/config.py`

```python
# -*- coding=utf-8 -*-

'''
要注意的是，这里可以写入多个配置，就仿照DevelopmentConfig这个类一样，继承Config类即可。
并在最下方的Config字典里添加对应的key:value。
'''

class Config:
    SECRET_KEY = '' #填入密钥
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        _handler = RotatingFileHandler(
            'app.log', maxBytes=10000, backupCount=1)
        _handler.setLevel(logging.WARNING)
        app.logger.addHandler(_handler)

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://flask:flask@127.0.0.1/flask_dev'
    #SQLALCHEMY链接数据库都是以URI方式格式为'mysql://账户名:密码@地址/数据库表名'


config = {
    'default': DevelopmentConfig
}

```

`/manage.py`：


```python
# -*- coding=utf-8 -*-
from app import create_app, db
from flask.ext.script import Manager, Shell

app = create_app('default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
```

`/app/__init__.py`

```python
# -*- coding=utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
```

`/app/main/__init__.py`


```python
# -*- coding=utf-8 -*-
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
```

`/app/errors.py #创建该文件`

`/app/views.py`

```python
# -*- coding=utf-8 -*-
from . import main


@main.route('/')
def index():
	return 'Hello World'
```

现在，在项目根目录下执行`python manage.py runserver`即可成功运行Flask，并访问127.0.0.1:5000。

![Flask项目运行示意图](http://i3.buimg.com/d079646404d6f729.png)

好了，我们完成了第一步，在第一步中我们使用Flask的特性[蓝图][7]实现模块化应用，例如我们刚创建的蓝图``main``就作为我们展示模块，当有访客浏览我们Blog的时候都是``main``在工作，而我们在后台编写文章时就不能使用该蓝图了，应该创建一个新的如``admin``来模块化运行。蓝图有很多特性，可以点击上方的链接浏览官方蓝图文档来让自己更了解蓝图的特性。

***

### 思考数据库模型

####开始想象

为什么这一段我要让大家开始想象数据库模型，无论你是否有过开发经验，对数据库的了解或对任何的了解。你在一开始都要定义数据库模型，现在我们就开始想象一下到底需要哪些数据库模型。

Blog都有哪些内容？**站点名字、介绍、文章标题、内容、分类、评论、标签。**嗯，还得带个用户。~~要不然怎么识别自己是管理员呢？总不能输入一个通用密码登入吧？对这里提醒了我们，一个人的Blog到底需不需要所谓的“管理员账户”既然只有我们知道管理员地址，也只有我一个人发表文章，为什么我们还需要用户呢？我们形成一个专有密码不就可以作为后台登入的钥匙了吗？也许这会降低所谓的安全性，但我认为是一个非常好的想法。你既然都是一个人写了，干嘛不要更简单点的登入模式？

如删除线内容一样，我在写文章的时候最初考虑的是用一个简单的一串密钥密码来验证后台管理，但我在写的过程当中考虑到了为了能在本文中对于用户登入注册这一块产生一块小的思考点，会使读者在后期自己开发时有更好的思维方向。

OK，我来一点一点解释需求的字段到底该不该保留。站点名字和介绍我们可以写在Base.html模板里把，文章标题、分类、内容、标签是需要的，但评论是否需要吗？现在有很多评论系统，国内的[多说][6]，国外的[Disqus][5]都可以引用到Blog里作为评论，那我是个懒人不想写标签这一块的字段，就留给你们最后去自己思考怎么写吧。

按我上面所说的，我们定义一个极简Blog大概就需要3张表“文章表”、“分类表”、“用户表”用来储存标题、内容、分类然后进行关联，而登入我们使用flask-login扩展来帮助我们完成自己定义好模型即可，评论用第三方扩展来处理，标签自己想办法。

注：不要被我的思维而定死了，请尽情想象，如果手边有笔纸我建议你写下来。并用关联线去自由的关联你想要产生出关系的数据库字段。

文章表

| 字段名| 属性| 说明|
|:---|---:|---:|
|id|数字|主键字段，自增|
|title|文本|标题字段|
|body|多行文本|内容字段|
|create_time|时间|创建文章时间|
|user_id|数字|关联用户表主键ID|
|category_id|数字|关联分类表主键ID|

分类表

| 字段名| 属性| 说明|
|:---|---:|---:|
|id|数字|主键字段，自增|
|name|文本|分类名字|

用户表

| 字段名| 属性| 说明|
|:---|---:|---:|
|id|数字|主键字段，自增|
|username|string|用户名字段|
|password|string|密码字段|
|real_name|string|真实姓名|

在三个表之间我们有两个一对多的关系，也就是一（分类）对多（文章）。现在再想想有什么更好的点子？或者你需要的字段更多？这些你都可以尽可能的发挥自己的想象及联合你本身实际的需求来增减。

那么我们把字段定出来了，怎么写到Flask生成数据库呢？

`/app/models.py`

```python
# -*- coding=utf-8 -*-
from . import db
from datetime import datetime


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    titile = db.Column(db.String(64), unique=True)
    body = db.Column(db.Text)
    create_time = db.Column(db.DATETIME, default=datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Category(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    articles = db.relationship('Article', backref='category')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    real_name = db.Column(db.String(64), unique=True)
    articles = db.relationship('Article', backref='user')
```

我写了三个类，分别为文章、分类、用户，其中有两条一对多的关系。
关于一对多、多对多的关系详细解释可以去[官方文档][8]进行查阅了解。
接下来我们来把我们定义好的数据库表写入到数据库。

**pip安装**

```
pip install flask-migrate #使用migrate来管理升级迁移数据库
```

**编辑 /manage.py**

```python
# -*- coding=utf-8 -*-
from app import create_app, db
from app.models import Article , Category , User  #注册数据库模型
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand   #载入migrate扩展

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)  #注册migrate到flask


manager.add_command('db', MigrateCommand)   #在终端环境下添加一个db命令

if __name__ == '__main__':
    manager.run()
```

接下来,我们到终端里依次输入

```
python manage.py db init
python manage.py db migrate -m "first init db"
python manage.py db upgrade
'''
单项目内只需要第一次执行db init，如果你在未来的日子里需要修改models.py并使其生效，只需要在改过models.py后执行指令的后面2步即可。
'''
```

现在你用任何一个可视化或终端去检查一下mysql数据库是否成功创建了数据库表。

顺带我解释一下unique、primary_key、default这些关键字：

**unique**是否允许重复，如果为True则在该表内不允许该字段用重复的数据出现。
**primary_key**是否为主键
**default**默认值

到这里，我们已经完成了两项任务。从中我们学习到了如何用virtualenv来部署flask环境，学习到了蓝图模块及设计数据库。我希望到这里你的数据库跟我设计的不一样，实例代码只是为了完成演示步骤。而在阅读的你，我希望你真的能够通过自己的想象去扩建一些字段，并自己理解字段中一些关键词的意义。

***

### 编写逻辑代码
设想一下，我们大概需要哪些逻辑代码，呐我想想。

1. 文章展示页
2. 文章详情页
3. 后台登入
4. 增、改、删文章、分类

在这里我只提供增、删的代码块，改这个代码块作为练习题由读者自己完成。

喏，这些应该就差不多了吧。
一步一步来，按道理我们应该先写后台。有后台，就应该有注册和登入，那注册开放了，怎么去解决任何人都可以注册的问题呢？有2种办法。

1. 拥有注册码的才可以注册（你可以在文件内自定一串随机码作为注册码）

2. 你可以完成注册后，注释掉注册逻辑代码。

当然这里我推荐第一种啦，因为比较简单，而且如果你想和你的朋友一起写这个博客，就不需要那么麻烦。只需要在告诉他你的注册码是多少就行了。

写好了后台之后，我们就应该要能增、改、删文章或者分类，我们来一步一步设计我们所需求的功能。

#### 编写后台模块

`pip安装`

```
pip install flask-wtf   #安装flask-wtf表单快速渲染生成
pip install WTForms-SQLAlchemy #安装flask-wtf-sqlalchemy用于通过数据库数据返回生成表单内容
pip install flask-bootstrap #安装flask-bootstrap，快速渲染bootstrap样式页面。
pip install flask-login #安装flask-login 用于登入及权限管理的扩展
```

`修改-> /app/__init__.py`

```python
# -*- coding=utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap   #引入Flask-Bootstrap
from flask.ext.login import LoginManager    #引入Flask-Login
from config import config

db = SQLAlchemy()   #实例化对象
bootstrap = Bootstrap() #实例化对象
login_manager = LoginManager()  #实例化对象
login_manager.session_protection = 'strong' #设置flask-login session等级
login_manager.login_view = 'admin.login'    #如果未登入转跳到指定方法
login_manager.login_message = u'请登入账号再进行下一步操作!' #未登入提示语

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    '''
    载入一个名为'admin'的蓝图作为后台管理模块
    '''

    return app
```

`新建-> /app/admin/__init__.py`

```python
# -*- coding=utf-8 -*-
from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views, errors
'''
前面我们载入了一个名为admin的蓝图模块
在这里我们需要构建这个模块
'''
```

`新建-> /app/admin/forms.py`

```python
# -*- coding=utf-8 -*-
from flask.ext.wtf import Form
from ..models import Category
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import Required, length, Regexp, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class LoginForm(Form):
    username = StringField(u'帐号', validators=[Required(), length(6, 64)])
    password = PasswordField(u'密码', validators=[Required()])
    submit = SubmitField(u'登入')


class RegistrationForm(Form):
    username = StringField(u'用户名', validators=[Required(), length(6, 18), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, u'用户名只允许字母',u'用户名不允许特殊符号')])
    password = PasswordField(
        u'密码', validators=[Required(), EqualTo('password2', message=u'密码错误提示1')])
    password2 = PasswordField(u'重复密码', validators=[Required()])
    real_name = StringField(u'昵称', validators=[Required()])
    registerkey = StringField(u'注册码', validators=[Required()])
    submit = SubmitField(u'注册')


class PostArticleForm(Form):
    title = StringField(u'标题', validators=[Required(), length(6, 64)])
    body = TextAreaField(u'内容')
    category_id = QuerySelectField(u'分类', query_factory=lambda: Category.query.all(
    ), get_pk=lambda a: str(a.id), get_label=lambda a: a.name)
    submit = SubmitField(u'发布')


class PostCategoryForm(Form):
    name = StringField(u'分类名', validators=[Required(), length(6, 64)])
    submit = SubmitField(u'发布')
```
forms.py里构建表单内容，然后在前端渲染时直接调用对应form即可快速生成表单内容。

在`PostArticleForm`表单里我们更引入了wtf-sqlalchemy的特性，通过查找数据库内容来生成对应的select表单。


* `修改-> /app/models.py`*

```python
# -*- coding=utf-8 -*-
from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash  # 引入密码加密 验证方法
from flask.ext.login import UserMixin  # 引入flask-login用户模型继承类方法


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    body = db.Column(db.Text)
    create_time = db.Column(db.DATETIME, default=datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Category(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    articles = db.relationship('Article', backref='category')


class User(UserMixin, db.Model):
    # 在使用Flask-Login作为登入功能时,在user模型要继承UserMimix类.
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    real_name = db.Column(db.String(64), unique=True)
    articles = db.relationship('Article', backref='user')

    @property
    def password(self):
        raise AttributeError(u'密码属性不正确')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        # 增加password会通过generate_password_hash方法来加密储存

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
        # 在登入时,我们需要验证明文密码是否和加密密码所吻合


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

`新建-> /app/admin/views.py`

编写路由视图代码块，包括登入、注册、增删文章、分类业务。

```python
# -*- coding=utf-8 -*-
from . import admin
from flask import render_template, flash, redirect, url_for, request
from flask.ext.login import login_required, current_user, login_user, logout_user
from forms import LoginForm, RegistrationForm, PostArticleForm, PostCategoryForm
from ..models import User, Article, Category
from .. import db


@admin.route('/')
def index():
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('admin.index'))
        flash(u'用户密码不正确')
    return render_template('admin/login.html', form=form)


@admin.route('/register', methods=['GET', 'POST'])
def register():
    register_key = 'zhucema'
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.registerkey.data != register_key:
            flash(u'注册码不符,请返回重试.')
            return redirect(url_for('admin.register'))
        else:
            if form.password.data != form.password2.data:
                flash(u'两次输入密码不一')
                return redirect(url_for('admin.register'))
            else:
                user = User(username=form.username.data, password=form.password.data, real_name=form.real_name.data)
                db.session.add(user)
                flash(u'您已经注册成功')
                return redirect(url_for('admin.login'))
    return render_template('admin/register.html', form=form)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'您已经登出了系统')
    return redirect(url_for('main.index'))


@admin.route('/article', methods=['GET', 'POST'])
@login_required
def article():
    form = PostArticleForm()
    alist = Article.query.all()
    if form.validate_on_submit():
        acticle = Article(title=form.title.data, body=form.body.data, category_id=str(form.category_id.data.id),
                          user_id=current_user.id)
        db.session.add(acticle)
        flash(u'文章添加成功')
        redirect(url_for('admin.index'))
    return render_template('admin/article.html', form=form, list=alist)


@admin.route('/article/del', methods=['GET'])
@login_required
def article_del():
    if request.args.get('id') is not None and request.args.get('a') == 'del':
        x = Article.query.filter_by(id=request.args.get('id')).first()
        if x is not None:
            db.session.delete(x)
            db.session.commit()
            flash(u'已经删除' + x.title)
            return redirect(url_for('admin.article'))
        flash(u'请检查输入')
        return redirect(url_for('admin.article'))


@admin.route('/category', methods=['GET', 'POST'])
def category():
    clist = Category.query.all()
    form = PostCategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        flash(u'分类添加成功')
        return redirect(url_for('admin.index'))
    return render_template('admin/category.html', form=form, list=clist)


@admin.route('/category/del', methods=['GET'])
@login_required
def category_del():
    if request.args.get('id') is not None and request.args.get('a') == 'del':
        x = Category.query.filter_by(id=request.args.get('id')).first()
        if x is not None:
            db.session.delete(x)
            db.session.commit()
            flash(u'已经删除' + x.name)
            return redirect(url_for('admin.category'))
        flash(u'请检查输入')
        return redirect(url_for('admin.category'))
```

`新建-> /app/templates/base.html`

定义基础模板，从后我们所有的渲染模板都会基于基础模板来继续渲染出内容页面。

```html
{% extends "bootstrap/base.html" %}

{% block title %} Flask-Blog{% endblock %}
{% block navbar %}
    <div class="navbar navbar-inverse" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle"
                        data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/">Blog</a>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="{{ url_for('main.index') }}">首页</a></li>
                    {% if current_user.is_authenticated %}
                        <li><a href="{{ url_for('admin.index') }}">后台首页</a></li>
                        <li><a href="{{ url_for('admin.article') }}">文章</a></li>
                        <li><a href="{{ url_for('admin.category') }}">分类</a></li>
                    {% endif %}
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    {% if current_user.is_authenticated %}
                        <li><a href="{{ url_for('admin.logout') }}">登出</a></li>
                    {% else %}
                        <li><a href="{{ url_for('admin.register') }}">注册</a></li>
                        <li><a href="{{ url_for('admin.login') }}">登入</a></li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </div>
{% endblock %}

{% block content %}
    <div class="container">
        {% for message in get_flashed_messages() %}
            <div class="alert alert-warning">
                <button type="button" class="close" data-dismiss="alert">&times;</button>
                {{ message }}
            </div>
        {% endfor %}
        {% block page_content %}
        {% endblock %}
    </div>
{% endblock %}
```

在base.html里，运用到了jinja模板引擎的if语法，并检测用户是否登入。如果登入则显示后台管理链接。并判断状态显示注册、登入还是登出。


`新建-> /app/templates/admin/register.html`

前端注册页面直接继承base.html，并在base.html的原有基础上增加渲染表单，我们在register视图里返回结果时，增加了注册表单的返回，所以在前端页面直接使用flask-wtf特性渲染出来即可使用。

```html
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}


{% block page_content %}
    <div class="col-md-6">
        <h1>注册账户</h1>
        <hr>
        {{ wtf.quick_form(form) }}
    </div>
    <div class="col-md-6">
    </div>
{% endblock %}
```

`新建-> /app/templates/admin/login.html`

```html
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}


{% block page_content %}
    <div class="col-md-6">
        <h1>登入博客</h1>
        <hr>
        {{ wtf.quick_form(form) }}
    </div>
    <div class="col-md-6">
    </div>
{% endblock %}
```

`新建-> /app/templates/admin/index.html`

```html
{% extends 'base.html' %}
{% block page_content %}
    {% if current_user.is_authenticated %}
        <p>感谢登入</p>
    {% else %}
        您还没有登入,请点击 <a href="{{ url_for('admin.login') }}">登入</a>
    {% endif %}
{% endblock %}
```

`新建-> /app/templates/admin/article.html`

新建文章时左侧为表单界面，右侧为已发表文章表格，可以在表格内点击链接删除该文章。

```html
{% extends 'base.html' %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block page_content %}
    <div class="col-md-6">
        {{ wtf.quick_form(form) }}
    </div>
    <div class="col-md-6">
        <table class="table">
            <thead>
            <tr>
                <th>文章编号</th>
                <th>文章标题</th>
                <th>操作</th>
            </tr>
            </thead>
            <tbody>
            {% for foo in list %}
                <tr>
                    <td>{{ foo.id }}</td>
                    <th>{{ foo.title }}</th>
                    <td><a href="{{ url_for('admin.article_del',id=foo.id,a='del') }}">删除</a></td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    </div>
{% endblock %}
```

`新建-> /app/templates/admin/category.html`

```html
{% extends 'base.html' %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block page_content %}
    <div class="col-md-6">
        {{ wtf.quick_form(form) }}
    </div>
    <div class="col-md-6">
        <table class="table">
            <thead>
            <tr>
                <th>文章编号</th>
                <th>文章标题</th>
                <th>操作</th>
            </tr>
            </thead>
            <tbody>
            {% for foo in list %}
                <tr>
                    <td>{{ foo.id }}</td>
                    <th>{{ foo.title }}</th>
                    <td><a href="{{ url_for('admin.article_del',id=foo.id,a='del') }}">删除</a></td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    </div>
{% endblock %}
```

至此，后台功能模块全部制作完成。

如果你现在运行Flask服务器，你访问127.0.0.1:5000/admin时就可以看到一个提示，提示未登入。接下来您可以去注册，注册时需要填写正确的注册码，否则注册会不成功。

我没有描写关于修改部分，而且介于目前网络流行以markdown的格式去编写文章，在该程序中我也没有引入Markdown作为编辑器，这些都可以作为读者自己的练习题。我相信，只要细心阅读本文章及本文章代码的读者朋友们配合搜索引擎及书籍都可以自己把编辑及Markdown功能写入到后台模块里。我写本片文章是为了让大家对于Flask做博客有一定了解，其实也就是让大家对于Flask的整个项目构造方法及sql增、删、减作一个了解。真正的网站程序还有很多很多需要大家去自己去研究的地方。

在我编写的代码里，有很多是重复代码及无效代码。我希望大家在编写时能尽量优化代码结构，而不是直接复制粘贴我的代码。需要读者去阅读我的代码，我为什么这么写，那我这么写的作用在哪里。明白代码的意义之后，开始思考我用什么更好的代码来代替现有的代码行才是读者朋友们该去思考的问题。

写到这时，我依然在考虑要不要继续编写博客文章的展示部分。

我个人认为是没有必要写的，因为我在写后端模块时所使用的代码行已经完全的表达了如何从数据库读取数据及渲染到前端页面。完全可以依靠上面的代码逻辑改改参数和对象作为文章的展示逻辑代码。

最终我还是决定，写吧，反正也没多少了。

***

#### 编写前台模块

前台显示文章这一块非常非常的简单。我是希望各位直接略过我这一部分，自己去思考一下该怎么写。

`编辑-> /app/main/views.py`

```python
# -*- coding=utf-8 -*-
from flask import render_template, redirect, url_for, flash, request
from . import main
from ..models import Article


@main.route('/')
def index():
    a = Article.query.all()
    return render_template('index.html', list=a)


@main.route('/read/', methods=['GET'])
def read():
    a = Article.query.filter_by(id=request.args.get('id')).first()
    if a is not None:
        return render_template('read.html', a=a)
    flash(u'未找到相关文章')
    return redirect(url_for('main.index'))
```

↑创建2个路由视图，首页和详细页。

`创建-> /app/templates/index.html`

```html
{% extends 'base.html' %}
{% block page_content %}
    <div class="col-md-8">
        {% for foo in list %}
            <div class="act">
                <h3><a href="{{ url_for('main.read' , id=foo.id) }}">{{ foo.title }}</a></h3>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

↓在文章详细页表里，需要注意的是我是如何通过数据库关联取得到分类名的，我们的数据库里文章表对应的条目内分类只是一个ID，而我们要通过这个分类ID获取分类的name，怎么做？看下面的代码关键部分。

`创建-> /app/templates/read.html`

```html
{% extends 'base.html' %}
{% block page_content %}
    <div class="container">
        <div class="col-md-12">
            <h2>{{ a.title }}</h2>
            <hr>
            <p>{{ a.create_time }} | {{ a.category.name }}</p>
            {{ a.body }}
        </div>
    </div>
{% endblock %}
```
到此，一个非常简单的Blog已经编写完成。

接下来的文章里，不会再包含任何代码块的展示。

至于代码块会不会有BUG，写的好不好，在下面的测试及完善章节里讨论。

###测试和完善都是什么

####测试

其实Flask还有单元测试的方法，我没有去描述。因为这些不在本文的讨论范围里，我只是陈述如何去写一个Blog而已。

那么如何测试我们的写的Blog呢？运行服务器，去注册账号，写文章发布你会发现有问题，为什么？因为你没有填分类。那么分类是不是一定要写？Models.py里是怎么定义文章表里的分类字段？Flask会不会报错？？这些都是要你去测试并修复的代码问题。我说过，我如果写教程一定不会写最完美的代码出来，因为这样就没有意思了，当然我认为也并不存在最完美的代码，而只有适时的代码。我只想在本文里所有的代码给与读者的感觉是比较好理解的。不写过多复杂的代码，去避免读者无谓的复制粘贴。

####完善

这个Blog需要完善的地方实在是太多太多了，你可以完善Markdown编辑器、前端样式、文章编辑、分类名修改功能、引入第三方评论系统等等…………我非常欢迎如果有读者看我的文章时，一遍看一遍自己思考编写一个Blog，直至到最后发现有了问题要和我探讨，那么请给我发Mail。我会很热情的回复你的问题，共同探讨。
现在那你会说哎，作者你这个坑，你写的我都懂，那你就告诉我了现在我要去引入一个Markdown编辑器到后台，我哪里懂？其实很简单，你去搜索一下关键词，例如‘Flask-Markdown’ 、 ‘Flask使用Markdown’等等关键词找网络博主们写的文章或者问答。

不要告诉我你不会使用搜索引擎，这些问题你就算不会翻墙用百度都能解决。更何况用Google？


### 部署到公网服务器

部署到公网服务器的方法有很多，当然你需要一台VPS。腾讯云、阿里云各种云或者BAE，SAE这种应用商店。

我不知各位是否对Http服务器有一定了解如果不了解就去了解一下Nginx，你可以直接用Flask-script的管理启动服务器，然后用Nginx去监听本地端口映射到外网访问。也可以用wsgi[服务器网关接口][9]去部署Flask Web程序。

这一块，我只做提示，不做教程。各位自行Google、百度查阅方法。

### 扩展你的Blog

最后一章，终于快写完了。这是我第一次写这么长篇幅的文章。

自己很感谢自己能够坚持下来，也很感谢我在群内聊天时大家给出的鼓励和支持。

在最后一章，我会说的比较啰嗦。这也是整篇文章的核心所在。

前面所有的代码逻辑，我都是为了给大家心里种下一个模子，而Blog只是一个最基本的网络程序，还有很多很多需要大家去了解的地方。

那么，我们到底该如何扩展我们的Blog？

我给各位打个比喻，例如我现在想要做一个会员系统，包含更详细的会员资料，拿目前的程序来修改可不可以？
我的回答是绝对可以，我们这么考虑，详细会员资料就是一个名为**info**的表，而会员还是保持**user**表。我们去掉文章及分类表的模型，只保留**user info**并对user和info编写一对一关系，每一个info表关联一个user.id。每次查询时只需要传入user.id然后由user.id关联查询对应的info表，从而输出用户的详细资料。

这只是非常简单的一个比喻，对于数据库关联方面的扩展。

那我们继续来设想，还能怎么做？

再来一个栗子，我公司最近要求我写一个内部OA系统，要求员工可以在网站内在线请假，那么我的用户系统就是引用的上面我所说的栗子。

而用户请假这个业务该怎么去编写代码？首先我们来理解一下，在现实生活中，纸质的请假条就是作于请假的数据。那么我们要存在网上，请假条就应该是一个数据库表，而数据库表里的字段就应该是请假条需要填写的内容，例如**请假时间、回岗时间、请假类别、请假人、创建时间、假条状态、审批人、审批时间**这么些字段，而请假人及审批人的信息我们就可以关联user.id来进行关联查询，假条状态我们应该是以数字来代替，例如默认是0（待审核）、1（通过）、2（否决）。

请假类别也是数字来代替1（事假）、2（婚假）、3（工伤）、4（产假）、5（病假）等等……我们设定好了字段，在来考虑他该怎样去产生一个请假条。设想写请假条跟在后台写博客是不是一个道理呢？只是展示的位置不同而已，博客是在前台可以展示给任何人浏览，而请假条必须要有一定权限（主管或经理职位）级别的用户在后台的审批界面查看。那么我们是不是可以对我们刚才设计出来的models从而设计一个forms？

接下来在前端渲染出Form，并加上一些访问权限，有账户的才能访问，无账户的则不能访问该页面。这个业务流程就完成一半了呢？还差审批，我们知道审批肯定是有一定权限的人才可以去做到。那我们修改user表里增加一个Permission（权限）字段，并设定好字权限等级，例如1（普通）、2（主管）、3（经理）、4（总裁），2能审批1、3能审批2和1、4能审批3、2、1。在用户访问路由时直接检查用户权限，达到权限范围的才可以进行访问。是不是整套流程就清晰了。

这些就叫我所谓的扩展，因为这个Blog只是展示了最基本的sql数据的增、删过程。不同的网站只是对于数据库的字段有不同的设定，而针对你自己所需求的内容。你要最早考虑的是数据库模型，这也是为什么本文中我们在部署好Flask开发环境后，我们第一件事情就是做的思考数据库模型的原因了。

我相信，在本文发表后的不久。会有不少读者能够做出属于自己的Flask-Blog。

感谢你们的阅读，谢谢！

Millyn
2016-05-11 下午3：55
millyn.network#gmail.com
本文只授权于编程派及本人博客、微信发表。
其他网站、微信号请勿转载！

 [1]:https://zh.wikipedia.org/wiki/Flask
 [2]:https://book.douban.com/subject/20428922/
 [3]:http://www.pythondoc.com/flask/index.html
 [4]:https://book.douban.com/subject/25814739/
 [5]:https://disqus.com/
 [6]:http://duoshuo.com/
 [7]:http://www.pythondoc.com/flask/blueprints.html
 [8]:http://www.pythondoc.com/flask-sqlalchemy/models.html#one-to-many
 [9]:https://zh.wikipedia.org/zh/Web%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BD%91%E5%85%B3%E6%8E%A5%E5%8F%A3
