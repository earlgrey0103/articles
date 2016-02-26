# pgcli v0.20.1 Bug修复版发布

编程派消息，`Pgcli`是一个针对Postgres数据库的命令行操作界面，具备自动补全与语法高亮功能。11月8日，开发者在项目主页发布了该工具的最新Bug修复版。用户可以通过下面的命令安装最新版本：

    :::bash
    $ pip install -U pgcli

此版本修复了在Windows平台启动pgcli时崩溃的问题。

**主要特性如下**：

Pgcli基于prompt_toolkit编写而来；
自动完成键入 SQL关键字以及数据库列表；
使用Pygments语法高亮显示；
Smart-completion(默认启用)上下文；
SELECT * FROM <tab> 只显示table名；
SELECT * FROM users WHERE <tab> 只显示column名；
在配置文件中自动创建~/.pglirc；
支持psql back-sla；

更多详情，可以查看[项目主页](http://pgcli.com/index)。

## 具体用法

    :::bash
    $ pgcli --help
    Usage: pgcli [OPTIONS] [DATABASE] [USERNAME]
    
    Options:
      -h, --host TEXT     Host address of the postgres database.
      -p, --port INTEGER  Port number at which the postgres instance is listening.
      -U, --user TEXT     User name to connect to the postgres database.
      -W, --password      Force password prompt.
      -w, --no-password   Never prompt for password.
      -v, --version       Version of pgcli.
      -d, --dbname TEXT   database name to connect to.
      --pgclirc TEXT      Location of pgclirc file.
      --help              Show this message and exit.

## 示例

    :::bash
    $ pgcli local_database
    
    $ pgcli postgres://amjith:passw0rd@example.com:5432/app_db
    
    $ pgcli -h localhost -p 5432 -U amjith app_db

![pgcli autocompletion example](http://cms.csdnimg.cn/article/201501/08/54adf5db6017c.jpg)

