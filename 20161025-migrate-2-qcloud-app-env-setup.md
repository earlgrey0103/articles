# 上云连载5：使用 Nginx + uWSGI 部署 Flask 应用

title:上云连载5：在 CVM 上使用 Nginx + uWSGI 部署 Flask 应用
slug: deploy-flask-app-on-cvm-with-nginx-uwsgi
keywords: nginx flask, uwsgi flask, uwsgi nginx, python 应用部署, flask 部署, web app 部署, uwsgi 配置, 

***

本文是「上云连载」系列第五篇，将以编程派网站为例，介绍如何在[腾讯云 CVM](https://www.qcloud.com/product/cvm.html) 上部署 Flask 应用。具体来说，是如何在 Debian 8 系统下使用 uWSGI 和 Nginx 部署一个 Flask 应用，其中 Nginx 的作用是前端反向代理。

我在这里列出的是部署编程派网站时的大致操作步骤，仅供大家参考。

## 准备工作

在开始之前，你应该已经[创建了一个腾讯云 CVM 实例](https://buy.qcloud.com/cvm)（Debian 8 操作系统），或者是其他任意云服务器，并按照[上云连载2](http://codingpy.com/article/migrate-to-qcloud-cvm-setup/) 中所述配置好了一个非 root 用户。该用户应该具备 sudo 权限。

## 获取应用代码库

首先你应该有一个可以运行的 Flask 应用。当然，你也可以用[编程派网站的代码库](https://github.com/bingjin/codingpy)做演示。

我在部署时，将应用代码放置在了 /var/www/ 目录下。输入如下命令创建该目录：

```
mkdir -p /var/www
```

可以直接从 Github 上克隆应用代码库：

```
cd /var/www
git clone https://github.com/bingjin/codingpy.git
```

也可以通过[上云连载3](http://codingpy.com/article/migrate-to-qcloud-git-server/)中搭建的 Git 服务器获取。

为了避免每次都要登陆服务器上手动拉取，我们在中央代码库中设置 post-receive 钩子（hook）。每次本地推送新的更新到服务器后，会自动更新目标代码库的代码。

> 在不需要多人合作的前提下，不必搭建 Git 服务器。

不过要先手动在 /var/www/ 下创建一个工作目录：

```
cd /var/www && mkdir codingpy
```

然后进入 codingpy.git 目录下的 hooks 目录，创建 post-receive 文件：

```
sudo su - git
cd repositories/codingpy.git/hooks/
vim post-receive
```

我使用了 [https://gist.github.com/thomasfr/9691385](https://gist.github.com/thomasfr/9691385) 中提供的方案，你也可以根据应用的实际情况进行修改。

保存 post-receive 文件后，执行：

```
chmod +x post-receive
```

之后，每次本地推送更新时，/var/www/codingpy/ 目录下的文件也会自动更新。

## 安装所需组件

编程派的 Flask 应用使用的是 Python 3，采用 Nignx 作为反向代理服务器，redis 用来做缓存。我们使用 apt-get 命令进行安装：

```
sudo apt-get install python3-pip python3-dev nginx redis
```

python3-pip 将安装 pip 包管理器，用于管理 Flask 应用的依赖包。在安装 python3-pip 时会自动安装 Python 3。python3-dev 将用于构建 uWSGI 包。

如果你的应用时基于 Python 2 的，请执行：

```
sudo apt-get install python-pip python-dev nginx redis
```

## 新建虚拟环境

如果只在生产服务器上部署一个 Python/Flask 应用的话，不使用虚拟环境也无所谓。但是最佳实践是将网站应用的环境与系统环境隔离开来，考虑到以后可以在 CVM 上部署其他的应用，推荐创建使用 virtualenv 一个单独的虚拟环境用于部署。

> virtualenv 包的使用说明：[virtualenv](http://codingpy.com/article/virtualenv-must-have-tool-for-python-development/)

首先，使用 pip3 安装 virtualenv 包。

```
pip3 install virtualenv
```

然后

```
cd /var/www
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
```

-p 选项指定虚拟环境中的 Python 版本。

virtualenv 适用于 Python 2 和 3。如果是在 Python 3 下，你还可以使用自带的 pyvenv 包快速创建一个虚拟环境，不需另外再安装 virtualenv。

## 安装应用依赖

上一节最后一步操作将激活新建的虚拟环境。我们进入项目文件目录，并通过 requirements.txt 文件安装应用的全部依赖。

```
(venv) cd codingpy
(venv) pip install -r requirements.txt
```

在安装过程中，Pillow、psycopg2、gevent 等库可能会报错，这是因为 Debian 系统还缺乏构建这些包所需的组件。你可以按照报错提示安装相应的资源包。

```
sudo apt-get install libjpeg8-dev postgrseql-server-dev-9.4
```

如果出现了其他的报错，建议多多利用搜索引擎查找解决方案。

## 测试 uWSGI

安装完依赖包之后，由于我们打算通过 uWSGI 来部署 Flask 应用，还需要在项目目录下创建一个文件作为应用的入口。该文件将告诉 uWSGI 服务器如何与应用进行交互。

我们将该文件命名为 wsgi.py：

```
(venv) $ vim /var/www/codingpy/wsgi.py 
```

这里提供一个最简单的示例：

```python
from manage import app

if __name__ == "__main__":
    app.run()
```

接下来，通过如下命令测试 uWSGI 服务器是否运行正常：

```
(venv) $ uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
```

打开浏览器，输入服务器的 IP 地址，指定访问端口为 5000：

```
http://server_domain_or_IP:5000
```

这时你应该能够看到应用的界面。

## 配置 uWSGI 

刚才已经测试 uWSGI 能够正常运行我们的 Flask 应用，不过运行方式并不适合长期使用。我们可以创建一个 uWSGI 配置文件，指定所需的运行选项。

将该文件放在项目的根目录下，命名为 codingpy.ini 。

```
vim /var/www/codingpy/codingpy.ini
```

文件的第一行应为 `[uwsgi]` ，这样 uWSGI 将应用文件中的配置。指定模块名为 `wsgi.py` ，省略后缀，并注明模块中的可调用对象的名称为 `app`：

```
[uwsgi]
module = wsgi:app
```

然后，让 uWSGI 以 master 模式启动，生成 5 个工作者进程来处理请求；我还开启了 gevent 模式，设置了线程数等选项：

```
master = true
processes = 5
threads = 100
gevent = 100
async = 100
```

在测试 uWSGI 时，我们将应用暴露在了 5000 端口上。但是，我们打算用 Nginx 来处理实际的客户端请求，Nginx 再将请求传递至 uWSGI。由于 Nginx 和 uWSGI 均运行在同一台机器上，更好的方式是使用 Unix 套接字，因为安全性更高，速度也更快。我们将套接字命名为 codingpy.sock，并把文件放置在 /var/tmp/ 目录下。

另外，还要修改套接字上的权限。由于我们后面将向 Nginx 用户组赋予 uWSGI 进程的所有权，因此要确保套接字所属的用户组可以对其进行读写操作。添加 `vaccum` 选项，指定进程终止时清除套接字。

```
socket = /tmp/codingpy.sock
chmod-socket = 660
vacuum = true
```

接下来，还要设置 `die-on-term` 选项。init 系统和 uWSGI 对进程信号 SIGNTERM 的解释不同，会执行不同的操作。这样设置之后，可以确保二者执行相同的行为。

```
die-on-term = true
```

在实际运行过程中，我的 Flask 应用无法正确获取环境变量，因此选择通过 uWSGI 配置传入。我将所有环境变量放置在了根目录下的 .envs 文件中，然后通过如下设置在 uWSGI 启动时导入： 

```
for-readline = .envs
  env = %(_)
endfor =
```

配置完选项之后，保存文件并退出。

## 创建 systemd Unit 文件

Debian 8 和 Ubuntu 16.04 中， systemd 已经成为了默认的 init 系统。我们将创建一个 systemd unit 文件，使得服务器启动时自动启动 uWSGI 和 Flask 应用。

在 /etc/systemd/system 目录下创建一个后缀为 .service 的文件：

```
sudo vim /etc/systemd/system/codingpy.service
```

首先，配置 `[Unit]` 部分，指定元数据和依赖。我们设置服务的说明，告知 init  系统在满足网络条件后才启动该服务。

```
[Unit]
Description=uWSGI instance to serve codingpy.com
After=network.target
```

然后，配置 `[Service]` 部分，指定进程所属的用户和用户组。由于我们创建的日常用户 earlgrey 拥有相关文件的所有权，因此将其设置为进程的所有者。另外，将所属用户组设置为 www-data，这样 Nginx 就可以和 uWSGI 进程进行通信。

接下来，完成工作目录映射，设置好环境变量，告知 init 系统 uWSGI 进程的可执行文件的路径。然后指定启动服务的命令。Systemd 要求指定 uWSGI 可执行文件的完整路径。

```
[Service]
User=earlgrey
Group=www-data
WorkingDirectory=/home/earlgrey/codingpy
Environment="PATH=/var/www/venv/bin"
ExecStart=/var/www/venv/bin/uwsgi --ini codingpy.ini
```

最后，添加 `[Install]` 部分。这将告知 systemd 在服务启动时将其链接到哪个服务。我们要在多用户系统启动运行时启动该服务：

```
[Install]
WantedBy=multi-user.target
```

保存并关闭该文件。我们现在可以启动创建好的服务，并设置为服务器启动时运行：

```
sudo systemctl start codingpy
sudo systemctl enable codingpy
```

## 配置 Nginx

完成上一节的配置之后，uWSGI 服务器应该已经正常运行了，并等待处理指定套接字上的请求。现在，我们需要配置 Nginx，使用 uwsgi 协议将网络请求转发到该套接字上。

首先，在 Nginx 的 `sites-available` 目录下创建一个新的服务器模块配置文件。将其命名为 codingpy，与其他地方的名称保持一致：

```
sudo vim /etc/nginx/sites-available/codingpy
```

输入如下配置，让 Nignx 监听默认的 80 端口，并使用这个 server block 处理针对服务器域名或 IP 地址的请求：

```
server {
    listen 80;
    server_name codingpy.com, www.codingpy.com;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/var/www/codingpy/codingpy.sock;
    }
}
```

其中的 location block 匹配所有满足要求的请求。`uswgi_params` 中包含了部分需要的 uWSGI 参数。然后使用 `uwsgi_pass` 指令将请求转发到定义好的套接字上。

Nginx 的设置就是这些。保存并关闭文件。为了让刚才的配置生效，将上面的文件链接到 `sites-enabled` 目录：

```
sudo ln -s /etc/nginx/sites-available/codingpy /etc/nginx/sites-enabled
```

接着通过如下命令测试文件配置的语法是否有问题：

```
sudo nginx -t
```

如果输出中没有显示存在问题，我们就可以重启 Nginx 进程，读取新的服务器配置：

```
sudo systemctl restart nginx
```

现在你就可以用浏览器打开服务器的网址或域名，查看 Flask 应用是否正常响应请求：

```
http://server_domain_or_IP
```

## 结语

在本文中，我们创建了一个用于运行 Flask 应用的虚拟环境，并配置了 uWSGI 服务器与 Flask 应用进行交互。然后，我们创建了 systemd 服务文件，在服务器启动时自动运行应用服务器。我们还配置了 Nginx 转发网络请求至应用服务器。

你可以参考本文中的大致步骤，来部署你自己的 Flask 应用。

在之后的文章中，我将介绍如何为编程派网站接入 CDN 等腾讯云服务。
