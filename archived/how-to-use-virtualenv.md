# Python开发神器之一：virtualenv

关键词：python开发神器, python虚拟环境, virtualenv, virtualenvwrapper, 第三方包冲突, 依赖管理, python项目开发

URL：virtualenv-must-have-tool-for-python-development

Python 的第三方包成千上万，在一个 Python 环境下开发时间越久、安装依赖越多，就越容易出现依赖包冲突的问题。为了解决这个问题，开发者们开发出了 virtualenv，可以搭建虚拟且独立的 Python 环境。这样就可以使每个项目环境与其他项目独立开来，保持环境的干净，解决包冲突问题。

## 安装 virtualenv

[virtualenv](https://virtualenv.pypa.io/en/stable/)是一个第三方包，是管理虚拟环境的常用方法之一。此外，Python 3 中还自带了虚拟环境管理包。

我们可以用``easy_install``或者``pip``安装。

``pip install virtualenv``

## 基本用法

### 创建项目的虚拟环境

```
$ cd my_project_folder
$ virtualenv venv # venv 可替换为别的虚拟环境名称
```

执行后，在本地会生成一个与虚拟环境同名的文件夹，包含 Python 可执行文件和 pip 库的拷贝，可用于安装其他包。

但是默认情况下，虚拟环境中不会包含也无法使用系统环境的global site-packages。比如系统环境里安装了 requests 模块，在虚拟环境里``import requests``会提示``ImportError``。如果想使用系统环境的第三方软件包，可以在创建虚拟环境时使用参数``–system-site-packages``。

``virtualenv --system-site-packages venv``

另外，你还可以自己指定虚拟环境所使用的 Python 版本，但前提是系统中已经安装了该版本：

``virtualenv -p /usr/bin/python2.7 venv``


### 使用虚拟环境

进入虚拟环境目录，启动虚拟环境。

```
cd venv
source bin/activate # Windows 系统下运行 Scripts\
python -V
```

如果未对命令行进行个性化，此时命令行前面应该会多出一个括号，括号里为虚拟环境的名称。启动虚拟环境后安装的所有模块都会安装到该虚拟环境目录里。

退出虚拟环境：

``deactivate``

如果项目开发完成后想删除虚拟环境，直接删除虚拟环境目录即可。

## 使用virtualenvwrapper

上述 virtualenv 的操作其实已经够简单了，但对于开发者来说还是不够简便，所以便有了 virtualenvwrapper。这是 virtualenv 的扩展工具，提供了一系列命令行命令，可以方便地创建、删除、复制、切换不同的虚拟环境。同时，使用该扩展后，所有虚拟环境都会被放置在同一个目录下。

### 安装virtualenvwrapper

``pip install virtualenvwrapper``

### 设置环境变量

把下面两行添加到``~/.bashrc``（或者``~/.zshrc``）里。

```shell
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
   export WORKON_HOME=$HOME/.virtualenvs 
   source /usr/local/bin/virtualenvwrapper.sh
fi
```

其中，.virtualenvs 是可以自定义的虚拟环境管理目录。

然后执行：``source ~/.bashrc``，就可以使用 virtualenvwrapper 了。Windows 平台的安装过程，请参考[官方文档](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)。

### 使用方法

创建虚拟环境：

``mkvirtualenv venv``

注意：mkvirtualenv 也可以使用 virtualenv 的参数，比如 –python 来指定 Python 版本。创建虚拟环境后，会自动切换到此虚拟环境里。虚拟环境目录都在 WORKON_HOME 里。

其他命令如下：

```
lsvirtualenv -b # 列出虚拟环境

workon [虚拟环境名称] # 切换虚拟环境

lssitepackages # 查看环境里安装了哪些包

cdvirtualenv [子目录名] # 进入当前环境的目录

cpvirtualenv [source] [dest] # 复制虚拟环境

deactivate # 退出虚拟环境

rmvirtualenv [虚拟环境名称] # 删除虚拟环境
```

## 参考链接：

1. http://rickgray.me/2015/05/02/use-vitualenv-to-build-your-python-virtualenv.html
2. http://snailvfx.github.io/2016/05/11/virtualenv/
