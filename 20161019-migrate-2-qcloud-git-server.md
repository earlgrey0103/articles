# 上云连载3：搭建私有可协作的 Git 服务器

slug: migrate-to-qcloud-git-server
keywords: 私人 Git 服务器, git 仓库管理, gitolite, 腾讯云 CVM, ssh 密钥对

***

本文是「上云连载」系列的第三篇，将介绍如何在[腾讯云 CVM](https://www.qcloud.com/product/cvm.html) 上搭建一个私有可协作的 Git 服务器。文中操作也适用于其他云服务商提供的服务器资源，具体配置时请注意操作系统的异同。

## 为什么？

搭建私有 Git 服务器，对于个人部署 Web 应用来说并不是必须的，你完全可以跳过这一步骤，使用 Github 管理自己的应用仓库。

这次回迁过程中选择自己搭建，一是出于练习的目的，二是发现国内拉取 Github 仓库速度较慢。这点大家在使用各种国外资源库时想必都有体会。

另外，如果你是一名移动开发者，而且应用收费的话，使用私有 Git 服务器可以很好地保护你的代码。

## Gitolite

能够托管 Git 仓库的软件有很多，如 Gitosis、GitList、Gitlab 等，其中不少还有比较好看的图形界面。但在本文中，我们选择的是一个图形界面的项目：Gitolite。

Gitolite 可以帮助你管理对私有 Git 服务器的访问权限，有如下特点：

- 服务器上只有一个 Unix 用户
- 允许多个 gitolite 用户访问
  - 这些 gitolite 用户不是服务器上的真实用户
  - 因此没有 shell 权限
- 管理各个仓库的访问权限
- 无需 root 即可安装
- 通过 sshd 进行用户验证

## 安装 Gitolite

上一篇的最后，我们在安装 oh-my-zsh 时已经安装了 Git。接下来只要安装 Gitolite 即可。

在 Debian 8 系统上，键入如下命令：

`sudo apt-get install gitolite3`

在安装过程中，它会要求你选择用来管理 Gitolite 的公钥地址。我们暂时不做选择。

接下来，我们将创建一个系统级别用户，专门用来管理 gitolite。该用户的名称可以设置为 git，方便协作者记忆。我们不设置密码，这样就只能使用 `su` 命令来访问 git 用户。

`sudo adduser --system --shell /usr/bin/zsh --gecos 'git version control' --group --disabled-password --home /home/git git`

我喜欢给新用户也使用 zsh，接着把管理用户 earlgrey 中的 .zshrc 设置复制到 git 用户。

`sudo cp .zshrc /home/git/.zshrc`

## 配置密钥对

在本地电脑上生成一个用于管理 Gitolite 的 SSH 密钥对，你可以继续使用上一篇中生成的密钥对，但推荐单独生成一个。生成密钥对时，注意更改保存地址和文件名称，不要覆盖之前的密钥对。

假设最终生成的密钥对名称为 `git_rsa`，我们可以这样将公钥复制到 Git 服务器：

`scp ~/.ssh/git_rsa.pub earlgrey@qcloud-cvm-ip:/tmp/git-admin.pub`

## 配置 Gitolite

接下来，我们以普通用户登录服务器。再通过 `su` 命令登录 git 用户，使用刚才复制的公钥来初始化 Gitolite。

```
sudo su - git
gitolite setup -pk /tmp/git-admin.pub
```

## 管理 Gitolite

下面可以回到本地，开始管理 Gitolite。这主要是通过修改 gitolite-admin 仓库来实现。

首先，我们从刚配置好的 Git 服务器上克隆该库到本地：

`git clone git@qcloud-cvm-ip:gitolite-admin`

这会在当前目录下创建一个叫做 `gitolite-admin` 的目录。我们可以通过修改该目录下的文件，对服务器的访问策略做出修改。

### 添加新用户

为了与同事或其他人员进行写作，我们需要给项目添加新用户。为此，就需要他们提供公钥。Gitolite 会将用户名与同名的公钥关联起来。假设我们要添加一个名为 `pythontg` 的用户。

在本地机器上，我们切换到 `gitolite-admin` 目录，看看目录下都有些什么文件：

```
cd gitolite-admin
ls
```

输出结果显示，目录中共有两个文件夹：`conf` 和 `keydir`。`keydir` 就是用于保存用户公钥的。

我们将从 `pythontg` 用户那里得到的公钥，复制到该目录下：

`cp /path/to/pythontg/public/key.pub ~/gitolite-admin/keydir/pythontg.pub`

然后将新文件添加到 git，并提交更改：

```
git add keydir/pythontg.pub
git commit -m 'New user pythontg added'
git push
```

### 配置权限

完成上面的操作之后，你可能会看到下面这样的警告信息：

```
remote: 
remote:         ***** WARNING *****
remote:         the following users (pubkey files in parens) do not appear in the config file:
remote: pythontg(pythontg.pub)
```

该信息表示新用户没有在配置文件中出现。这意味着，虽然 Gitolite 已经知道新建了这么一个用户，但是还没有为新用户创建任何权限。

编辑 `~/gitolite-admin/conf/gitolite.conf` 文件，并为其创建一个新仓库：

```
repo    gitolite-admin
        RW+     =   git-admin

repo    testing
        RW+     =   @all

repo	pythontg
		RW+ 	= 	pythontg
```

Gitolite 使用 repo 关键词 + 仓库名，指定 git 仓库。并在下方编辑权限类型，以及拥有权限的用户。

@all 是用户组的名称，这里是一个特殊的用户组，表示所有的 gitolite 用户。

权限的定义如下：

- R 表示只读
- RW 表示可读或推送更改，但不能删除 git ref
- RW+ 表示可读、可写，而且可以删除 git ref

推送修改后，我们就成功为新用户创建了一个仓库，并赋予了充足的权限。

用户 `pythontg` 可以这样在本地克隆该库：

`git clone git@qcloud-cvm-ip:pythontg`

## 纯粹个人使用的 Git 服务器

到此为止，我们已经完成了 Gitolite 的配置，拥有了一个可供多名用户协作的私有 Git 服务器。我们按照上面的类似步骤，将应用的代码库添加到 Gitolite，并推送到服务器上。

如果你只想要一个供个人使用的 Git 服务器，那么只需要在拥有 SSH 登陆权限的账户下创建一个裸仓库（bare repository）即可。

```
mkdir -p /var/repo
sudo chmod 700 /var/repo
cd /var/repo
git init --bare codingpy.git
```

然后在本地机器上，进入你已有的应用目录。如果已经有本地 Git 仓库，可以修改 remote 设置：

`git remote set-url origin earlgrey@qcloud-cvm-ip:/var/repo/codingpy.git`

如果是一个新仓库，可以这样操作：

`git init && git remote add origin earlgrey@qcloud-cvm-ip:/var/repo/codingpy.git`

上述命令中的用户名、IP 地址及仓库地址，请根据自身的情况修改。

## 结语

到目前为止，Git 服务器的配置就完成了。参考上述操作，我将编程派网站的仓库放置到了新的服务器上，再也不用忍受慢速 Git 拉取了。

## 参考：

- https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-git-server-on-a-vps
- https://dericteong.wordpress.com/2013/06/12/setup-git-server-in-amazon-ec2/
- http://gitolite.com/gitolite/install.html#qi
- https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server
