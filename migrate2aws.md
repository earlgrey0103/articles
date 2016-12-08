# 网站迁移到AWS or 腾讯云

1.1 云服务选择
  - CVM
  - COS

1.2 CVM 配置
  - SSH 登陆
  - 添加 user 及 权限
  - 禁用 root 及密码登陆
  - SSH config
  - zsh


2. 搭建私有 Git Server

原因：下载 github 比较慢，私有

var/wwww/codingpy.com

  - Gitolite3
  - 库和用户权限管理
  一个用户
  - git post reiceive

3. 迁移数据库
  - 安装数据库
  - 数据库配置
  - 备份数据库到本地
  - 上传到新服务器
  - pg 命令
  - 查询确认

4. 应用环境配置
  - Python 3
  - Nginx uWSGI
  - Redis


5. 集成 COS
  - COS SDK
  - Restful API
  - 签名算法生成

6. 后续配置
  - CDN
  - SSL 证书
  - Let's Encrypt：https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04
  - CVM 镜像
  - 域名转入


## SSH 到 EC2

chmod 400 mykey.pem # change key file permission

cp path_to_mykey.pem ~/.ssh/
vim ~/.ssh/config

```
Host codingpy_aws
Hostname ec2-54-214-212-10.us-west-2.compute.amazonaws.com
User ec2-user
IdentityFile ~/.ssh/mykey.pem
ControlPersist 1h
```

## 服务器配置

禁用 root登陆
增加 sudo 用户

### root 下增加 sudo 用户

adduser earlgrey

install sudo package

```
apt-get update
apt-get install sudo
usermod -a -G sudo earlgrey
```

### add to group www-data

ec2:
sudo groupadd www-data
sudo usermod -a -G www-data ec2-user

new user

adduser -G usergroup, group2 username

To assign a primary group to an user:

$ usermod -g primarygroupname username
To assign secondary groups to an user:

$ usermod -G secondarygroupname username
From man-page:

...
-g (primary group assigned to the users)
-G (Other groups the user belongs to)
...

existing user

usermod -G www-data username

%sudo	ALL=(ALL) NOPASSWD:ALL


To best share with multiple users who should be able to write in /var/www, it should be assigned a common group. For example the default group for web content on Ubuntu and Debian is www-data. Make sure all the users who need write access to /var/www are in this group.

sudo chgrp -R www-data /var/www
sudo chmod -R g+rwx /var/www

Additionally, you should make the directory and all directories below its "set GID", so that all new files and directories created under /var/www are owned by the www-data group.

sudo find /var/www -type d -exec chmod 2775 {} \;

Find all files in /var/www and add read and write , execute permission for owner and group:

sudo find /var/www -type f -exec chmod ug+rwx {} \;

You might have to log out and log back in to be able to make changes if you're editing permission for your own account.


还是 sudo chmod -R 775 'your directory'？
chmod u=rwx,g=rx,o=    | chmod 750 | For executables by group only

- http://superuser.com/questions/19318/how-can-i-give-write-access-of-a-folder-to-all-users-in-linux/19333#19333
- http://blog.superuser.com/2011/04/22/linux-permissions-demystified/

### SSH PUBLIC KEY

KEY for git

KEY for sudo login

`ssh-keygen -t rsa`

### 为用户配置 SSH 访问


```
scp /tmp/pubkey.pub server:/tmp/pubkey.pub
ssh server
mkdir /home/username/.ssh
cat /tmp/pubkey.pub ~/.ssh/authorized_keys
```


https://www.digitalocean.com/community/tutorials/initial-server-setup-with-debian-8

### 禁用 root 登陆

禁用密码登陆
开启防火墙

修改密码：

root 下 passwd username

## 安装 oh-my-zsh

aws 下报错 complete:13: command not found: compdef

解决：chmod a-r /etc/profile.d/aws-cli.sh

https://github.com/robbyrussell/oh-my-zsh/issues/4771

## 搭建 Git 服务器

### 创建用户

centos: sudo adduser --system  -c 'git version control' -p WYJA3rCAcY9Mdw -m -d /home/git git 

debian: sudo adduser --system --shell /usr/bin/zsh --gecos 'git version control' --group --disabled-password --home /home/git git

sudo cp .zshrc /home/git/.zshrc

### 生成 SSH Key Pair：

sudo su - git
gl-setup /tmp/aws_tokyo.pub

克隆仓库：git clone git@aws_tokyo:gitolite-admin.git

`ssh-keygen -t rsa`

cp ~/.ssh/git_rsa.pub /tmp/git_rsa.pub 

Host myshortname realname.example.com
    HostName realname.example.com
    IdentityFile ~/.ssh/realname_rsa # private key for realname
    User remoteusername

Host myother realname2.example.org
    HostName realname2.example.org
    IdentityFile ~/.ssh/realname2_rsa
    User remoteusername



上传私钥：

rsync -avr /tmp/aws_tokyo.pub -e "ssh -i ~/.ssh/aws_tokyo.pem" ec2-user@aws_tokyo:/tmp/aws_tokyo.pub

cat /tmp/aws_tokyo.pub >> ~/.ssh/authorized_keys

yum install git gitolite


### git post-receive

Git repositories have a folder called 'hooks'. This folder contains some sample files for possible actions that you can hook and perform custom actions set by you.

Git documentation define three possible server hooks: 'pre-receive', 'post-receive' and 'update'. 'Pre-receive' is executed as soon as the server receives a 'push', 'update' is similar but it executes once for each branch, and 'post-receive' is executed when a 'push' is completely finished and it's the one we are interested in.

In our repository if you type:

ls
You will see a few files and folders, including the 'hooks' folder. So let's go to 'hooks' folder:

cd hooks
Now, create the file 'post-receive' by typing:

cat > post-receive
When you execute this command, you will have a blank line indicating that everything you type will be saved to this file. So let's type:

#!/bin/sh
git --work-tree=/var/www/domain.com --git-dir=/var/repo/site.git checkout -f

When you finish typing, press 'control-d' to save. In order to execute the file, we need to set the proper permissions using:

chmod +x post-receive
You can see on the documentation that 'git-dir' is the path to the repository. With 'work-tree', you can define a different path to where your files will actually be transferred to.

The 'post-receive' file will be looked into every time a push is completed and it's saying that your files need to be in /var/www/domain.com.

https://www.digitalocean.com/community/tutorials/how-to-set-up-automatic-deployment-with-git-with-a-vps

### 参考：

- https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-git-server-on-a-vps
- https://dericteong.wordpress.com/2013/06/12/setup-git-server-in-amazon-ec2/
- http://gitolite.com/gitolite/install.html#qi
- https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server

## using gitolite

每次新加一个repo时，要在gitolite conf中添加设置，配置权限

## 应用环境配置

sudo apt-get install python3 python3-pip python3-dev
sudo pip3 install virtualenv

cd /var/www/
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate

解决报错，包缺失：

sudo apt-get install libjpeg62-turbo-dev

systemd unit file:

systemctl status <service-name>


this works

uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi


### 加入环境变量

vim .zshrc


图片和静态文件保存至 S3 Bucket
https://flask-s3.readthedocs.io/en/latest/


## 迁移数据库

1. 数据库备份
2. 数据库安装

sudo apt-get install postgresql-9.4 postgresql-server-dev-9.4
sudo apt-get install redis-server

sudo su - postgres
createuser --interactive

createdb earlgrey

change user password

ALTER USER "user_name" WITH PASSWORD 'new_password';


https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-9-4-on-debian-8


3. 数据库迁移

ssh production
pg_dump -C -Fp -f dump.sql -U postgres some_database_name
scp dump.sql development:（scp username@remote:/file/to/send /where/to/put）
rm dump.sql
ssh development
psql -U earlgrey -f dump.sql

4. 数据库查询

确认迁移成功

select id, title from articles where title like 'Python%';

5. 加入环境变量

.envs

https://technet.microsoft.com/en-us/library/bb264565(v=sql.90).aspx

http://stackoverflow.com/questions/1237725/copying-postgresql-database-to-another-server

Database Migration From Postgresql to Mongodb
https://www.vishnu-tech.com/2015/11/database-migration-from-postgresql-to-mongodb/

## 静态文件

上传文件夹

scp -r ~/path/to/foler/ server:/path/to/save/



## NGINX

apt-get install nginx

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04

## CDN


## 域名转入

