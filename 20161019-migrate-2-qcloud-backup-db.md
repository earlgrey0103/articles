# 上云连载4：数据库备份与恢复

slug: migrate-to-qcloud-backup-and-restore-database
keywords：数据库备份, 数据库恢复, postgresql 数据库备份, python postgresql 教程, Python 数据库教程

***

本文是「上云连载」第四篇，在开始部署 Flask 应用环境之前，我们先把原先服务器上的数据库备份导出，并在腾讯云 CVM 上完成数据库恢复工作。

由于我在开发「编程派」网站时使用的是 PostgreSQL，因此本文所说的数据库备份和恢复操作，均是针对 PostgreSQL 而言的。如果你使用的是其他类型数据库，请参考相关的文档。

## 数据库备份

PostgreSQL 号称是世界上最先进的开源数据库。从我对国外 Python 社区有限的了解来看，国外 Python 开发者对该数据库非常推崇，PyCon US 上经常请这方面的专家来普及数据库使用知识。我记得当初选择 PostgreSQL 也是因为听了某个演讲说 Python 和 PostgreSQL 二者如何契合。

有关 PostgreSQL 的具体介绍，请见[官方文档](https://www.postgresql.org/docs/manuals/)。我们接下来通过 SSH 登陆到旧服务器，然后在用户根目录下使用 `pg_dump` 命令备份数据库： 

```sh
pg_dump -C -Fp -f dump.sql -U postgres some_database_name
```

有关 [pg_dump](https://www.postgresql.org/docs/current/static/app-pgdump.html) 命令的详情，[请看文档](https://www.postgresql.org/docs/current/static/app-pgdump.html)。我这里对上述命令做个简单解释。

pg_dump 是一个用于备份数据库的工具命令，即使当前数据库存在连接的情况下也没有问题，不会阻塞其他用户访问。不过这个命令一次只能备份一个数据库，如果想备份所有数据库共有的全局对象，则需要使用 pg_dumpall 命令。

在这里，pg_dump 命令生成的是一个名为 dump.sql 的脚本文件。

 * -C 选项表示在输出的脚本中，一开始会是创建并重连到数据库的命令。
 * -F 选项指定输出的格式，后面跟着的 p 表示输出纯文本 SQL 脚本文件，也是默认选项。
 * -f 表示将输出发送至指定的文件。
 * -U 表示以什么用户名连接到要备份的数据库

接下来，我们通过 `scp` 命令将服务器上的 dump.sql 文件保存至本地：

```
scp username@old-server:dump.sql /path/to/save/dump.sql
```

## 数据库恢复

数据库的恢复也非常简单，同样只需要执行一个命令即可。但是在此之前，我们先安装并配置好 PostgeSQL 。

scp dump.sql development:（scp username@remote:/file/to/send /where/to/put）

### 安装及配置

在 Debian 系统下，请使用如下命令安装 PostgreSQL：

```sh
sudo apt-get install postgresql-9.4
```

安装完成后，默认会新建一个名为 postgres 的系统用户，用于管理 PostgreSQL 数据库。我们不打算直接用该账号，而是创建一个自己常用的。这里，我按如下操作创建一个名为 earlgrey 的 psotgresql 账号。

```sh
sudo su - postgres
createuser --interactive
```

根据提示输入用户名，并选择合适的账户类型。我创建的是一个和 postgres 同级别的账号。然后创建一个和新账号同名的数据库：

```
createdb earlgrey
```

这样，即使在登陆为 earlgrey 账户时，也可以使用 psql 命令进行 PostgreSQL 命令行。

进入命令行后，根据需要修改该账号的密码。

```
ALTER USER "earlgrey" WITH PASSWORD 'new_password';
```

### 数据库恢复

数据库的安装和配置基本完成了，接下来我们把本文第一步中备份好的 dump.sql 文件上传至 CVM 上。

```
scp /path/to/dump.sql qcloud:/path/to/dump.sql
```

注意，这里我使用的是第二篇中配置好的服务器别名，[具体请参考这里](http://codingpy.com/article/migrate-to-qcloud-cvm-setup/)。

最后，执行下面这条命令：

```
psql -U earlgrey -f dump.sql
```

-U 和 -f 选项的功能应该是不言自明的，具体请参考[官方文档](https://www.postgresql.org/docs/devel/static/app-psql.html)。执行该命令后，你应该会在终端看到一系列输出，实际上是 psql 在执行 dump.sql 文件中的一系列命令，即创建数据库并写入数据。

### 确认恢复

为了确认数据库恢复成功，我们以 earlgrey 账户连接到新创建的数据库 codingpy。

```
\c codingpy
```

然后执行 SQL 查询语句：

```sql
SELECT id, title FROM articles WHERE title LIKE 'Python%';
```

![SQL 查询语句结果](http://ww2.sinaimg.cn/large/801b780agw1f93571szlcj21680vcqep.jpg)

## 结语

本文中，我们完成了对编程派网站文章数据的备份和恢复。在将要部署的 Flask 应用中，我们可以通过该 URI 访问并连接到恢复后的数据库：

```
postgresql://earlgrey:new_password@localhost/codingpy
```

## 参考资料

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-9-4-on-debian-8
https://technet.microsoft.com/en-us/library/bb264565(v=sql.90).aspx

http://stackoverflow.com/questions/1237725/copying-postgresql-database-to-another-server

Database Migration From Postgresql to Mongodb
https://www.vishnu-tech.com/2015/11/database-migration-from-postgresql-to-mongodb/