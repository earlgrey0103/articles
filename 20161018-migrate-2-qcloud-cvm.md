# 上云连载2：学会正确配置自己的服务器

slug:migrate-to-qcloud-cvm-setup
keywords: 腾讯云 CVM, 腾讯云服务器, Debian 系统配置, SSH 登陆配置

***

本文是「上云连载」系列的第二篇，将主要介绍如何按照自己的喜好配置云服务器，同时确保登陆方便、安全。如有不正确的地方，希望大家指正。

## 新建云服务器实例

各家云计算服务商对云服务器产品的叫法都不一样，亚马逊家的叫 EC2 （Elastic Compute Cloud），之前用的 DigitalOcean 的叫 Droplet，国内的阿里云的叫 ECS （Elastic Compute Service），腾讯云则叫 CVM （Cloud Virtual Machine）。但是本质上是类似的，都是可以按需快速部署的虚拟服务器。

这次网站回迁，我选择的是腾讯云的 CVM。在开始进行 CVM 配置之前，我们先通过腾讯云的控制台新建一个实例。

由于[之前我们领的代金券](http://www.qcloud.com/event/newusergift)只适用于包年包月类型的服务器，所以新建实例时计费模式选择为「包年包月」。对于需要长期运行的网站应用来说，包年包月的模式还是比较划算的。机型选择标准型S1中最低配的即可。

![新建云服务器实例](http://ww2.sinaimg.cn/large/801b780agw1f8xpykh30hj21kw0ybq93.jpg)

我在 DigitalOcean 时使用的服务器操作系统是 Ubuntu 14.04，但是回迁到腾讯云时我改为了 Debian 系统。二者的差异不大，以前处理 Ubuntu 系统时的操作大多也是适用的。

![新建云服务器实例](http://ww4.sinaimg.cn/large/801b780agw1f8xpyy9h5ej21kw0to78p.jpg)

选择存储与网络时，建议将系统盘选择为云硬盘，除了可以获得免费赠送的空间之外，还方便以后根据需求升级 CVM 的 CPU 和内存。其他的使用默认设置即可。 

![新建云服务器实例](http://ww3.sinaimg.cn/large/801b780agw1f8xq13eeauj21kw0x9wj4.jpg)

接下来需要设置一些 CVM 相关的信息，如主机名和登陆密码。一开始，你的账号下只有默认项目，这里我已经创建了一个叫做「编程派网站」的项目。在腾讯云中，你的所有云资源，包括云服务器、对象存储甚至是 SSH 密钥，都可以和项目关联在一起，方便对应管理。如果你发现采购的云资源在控制台看不到，可以试试切换所属的项目。

![新建云服务器实例](http://ww3.sinaimg.cn/large/801b780agw1f8xq1yqijrj21io0twdk8.jpg)

如果你不希望手动设置密码，可以选择「自动生成密码」，腾讯云会向你的注册邮箱发送相关登陆信息。安全组暂时选择为默认安全组，将暴露所有端口到公网和内网。

## root 登陆

在登陆刚启动的 CVM 实例之前，我们需要知道服务器的公网 IP，以及 root 用户的密码。如果你选择的是自动生成密码，那么请查看邮箱。接下来，我们在本地使用如下命令登陆到服务器。

`$ ssh root@qcloud-cvm-ip # 请将 qcloud-cvm-ip 替换为实际 IP `

按照提示进行操作，输入 root 用户验证所需的密码（可以从腾讯云发送的邮件中找到）。如果这是你第一次使用密码登陆服务器，登陆成功后系统还会提示你更换 root 密码。

### root 用户

root 用户是 Linux 环境下的超级管理用户，拥有非常大的权限。由于 root 用户权限过大，不建议大家日常使用 root 账号进行服务器操作。因为有可能会出现让你加班、甚至被开除的意外。

因此，我们接下来创建一个新的用户账号，在日常工作中使用。

## 创建新用户

以 root 账号登陆服务器之后，我们就可以添加以后经常使用的用户账号了。本文中，我们将创建一个名为 `earlgrey` 的新用户，你可以根据自己的情况选择合适的用户名。

`$ adduser earlgrey`

系统会要求你回答一些问题，最重要的就是设置该用户的密码。对于其他问题，并不是必须的，可以直接按回车键完成。

## 添加 root 权限

现在 `earlgrey` 用户还只是一名普通用户，不具备系统管理权限。我们需要为该用户添加 root 权限。这样，就可以在每个命令前加上 `sudo` 以管理员权限执行了。

### 安装 sudo

由于 Debian 8 系统默认没有安装 `sudo` 包，因此我们先通过 `apt-get` 安装。

首先，更新 apt 包目录：

`$ apt-get update`

然后使用下面的命令安装 `sudo`：

`$ apt-get install sudo`

现在可以使用 `sudo` 和 `visudo` 命令了。

### 赋予 sudo 权限

为了给新用户添加管理权限，我们需要把新用户添加到 `sudo` 用户组。Debian 8 系统中，属于 `sudo` 用户组的用户默认可以使用 `sudo` 命令。

在 root 用户下 ，运行如下命令，将 `earlgrey` 用户添加到 `sudo` 用户组：

`$ usermod -a -G sudo earlgrey`

上面的命令中，`-a` 选项指的是将用户添加到对应的用户组中，只能配合 `-G` 选项一起使用。`-G` 后可以指定多个用户组名称。如 `$ usermod -a -G sudo, wwww-data`。

## 添加公钥验证

推荐给新用户添加公钥验证，一来可以避免每次登陆时都要输入密码，二来需要私钥才能登陆可以提高安全性。

### 生成密钥对

如果没有现成的 SSH 密钥对（由公钥和私钥组成），很容易就可以生成。只需要在本地机器上输入如下命令即可：

`ssh-keygen` 

假如本地用户的名称为 `earlgrey`，接下来应该会看到如下输出：

```
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/earlgrey/.ssh/id_rsa):
```

如果你以前没有生成过密钥对，按回车接受默认设置即可。如果有旧的密钥对的话，这样会覆盖以前的密钥对，建议更改为别的文件名。系统还会提示输入口令（passphrase），为了简单起见，我们直接回车使用空口令。如果你输入了口令的话，那么在 SSH 登陆时，除了需要提供密钥之外，还需要输入口令才能登陆。

命令运行结束后，会在本地用户的根目录中的 `.ssh` 目录下创建一个私钥 `id_rsa` 和一个公钥 `id_rsa.pub`。记得别公开分享你自己的私钥。

### 复制公钥

赋值公钥有两种方法，一是通过 `sshh-copy-id` 脚本自动赋值到远程用户，二是手动安装。

1. ssh-copy-id 脚本

如果本地机器上安装了 `ssh-copy-id` 脚本，那么就可以使用该脚本将公钥安装到任何有登陆权限的用户。

运行该脚本，同时指定用户名和服务器的 IP 地址：

`$ ssh-copy-id earlgrey@qcloud-cvm-ip`

按提示输入登陆密码后，你刚才生成的公钥就会自动赋值到远程用户的 `.ssh/authorized_keys` 文件中。接下来就可以使用对应的私钥登陆服务器了。

2. 手动安装公钥

使用如下命令打印你刚刚生成的公钥（`id_rsa.pub`：

`$ cat ~/.ssh/id_rsa.pub`

打印出来的公钥大致应该是这样子的：

`ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBGTO0tsVejssuaYR5R3Y/i73SppJAhme1dH7W2c47d4gOqB4izP0+fRLfvbz/tnXFz4iOP/H6eCV05hqUhF+KYRxt9Y8tVMrpDZR2l75o6+xSbUOMu6xN+uVF0T9XzKcxmzTmnV7Na5up3QM3DoSRYX/EP3utr2+zAqpJIfKPLdA74w7g56oYWI9blpnpzxkEd3edVJOivUkpZ4JoenWManvIaSdMTJXMy3MtlQhva+j9CgguyVbUkdzK9KKEuah+pFZvaugtebsU+bllPTB0nlXGIJk98Ie9ZtxuY3nCKneB+KjKiXrAvXUPCI9mWkYS/1rggpFmu3HbXBnWSUdf earlgrey@Macbook Pro.local`

然后，以新用户身份登陆服务器：

`$ ssh earlgrey@qcloud-cvm-ip`

登陆成功后，应该会进入该用户的根目录。接下来创建一个叫 `.ssh` 的新目录，然后使用如下命令限制目录权限：

```sh
mkdir .ssh
chmod 700 .ssh
```

700 表示只有目录的所有者才能读、写和执行。

现在使用 Vim 文本编辑器在 `.ssh` 目录下创建一个名为 `authorized_keys` 的文件。

`$ vim .ssh/authorized_keys`

在 Vim 中按 i 进入插入模式，然后 `Ctrl + v` 粘贴之前赋值的公钥。然后按 `Esc` 回到正常模式，在英文输入法下键入 `:wq` 保存并退出文件。

并使用如下命令限制文件的权限：

`chmod 600 .ssh/authorized_keys`

600 表示文件所有者可读、可写。

之后，你就可以使用私钥验证登陆服务器了，不必重复输入密码。

## 禁用 root 登陆

在开始配置服务器的时候 ，我们提到了最好不用使用 root 账号登陆服务器。为了确保不会出现这种情况，我们可以修改 SSH daemon 的配置，禁止远程登陆值 root 账号。

以上面配置的管理员用户身份，使用 sudo 命令打开配置文件：

`$ sudo vim /etc/ssh/sshd_config`

如果想禁止远程 root 登陆，找到下面这行文本：

`PermitRootLogin yes`

将其修改为

`PermitRootLogin no`

并保存文件。由于我们已经创建了一个管理用户，而且可以视情况增加权限，禁止 root 账号登陆反而可以让服务器更加安全。

最后，只需要重启 SSH 服务即可让新配置生效。

`$ systemctl restart ssh`

## 本地配置 SSH

完成以上配置之后， 以后我们每次只需要 `ssh earlgrey@qcloud-cvm-ip` 即可登陆服务器。

不过这样还是有点麻烦，每次都得输入用户名和 IP 地址。为了进一步简化操作，我们对本地的 SSH 登陆进行配置。

打开 `~/.ssh/config` 文件，然后添加如下配置：

```
Host qcloud
Hostname qcloud-cvm-ip
User earlgrey
IdentityFile ~/.ssh/id_rsa
```

之后，只需要执行 `ssh qcloud` 即可登陆服务器。

## 安装 oh-my-zsh

到上面那步为止，CVM 基本配置完成了。

不过由于在本地用惯了 oh-my-zsh，我决定在服务器上也安装使用。

我们先登陆服务器：

`$ ssh qcloud`

然后执行

```
$ sudo apt-get install git zsh
$ sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

安装好之后，建议将服务器上的 oh-my-zsh 主题设置为不同于本地的，否则你可能分辨不出是不是在服务器上的操作。

***

「上云连载」系列的第二篇就讲到这里，大部分是比较基础的操作，比较适合新手跟着一起操作。下一篇将介绍如何在 CVM 上搭建私有可协作的 Git 服务器。

