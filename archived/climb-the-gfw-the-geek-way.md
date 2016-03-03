# 瞭望墙外世界的各种姿势

> 本文由[EarlGrey@编程派](http://codingpy.com)独家整理，首发于微信公众号“编程派”。微信搜索“编程派”，跟我一起学Python。

编程派的网站部署在[DigitalOcean](https://m.do.co/c/70fd6733d655)的纽约节点，与国内有些地区的网络相性较差，因此不时有朋友反映网站打不开的问题。当初选择节点时，并没有仔细测试各个节点对国内的访问速度，现在考虑是不是要切换到新加坡节点。成功切换后情况应该会好一些吧。

在切换节点之前，和大家分享一个曲线救国的方案，即使用Shadowsocks搭建代理服务。本文除了推荐购买付费VPS搭建服务之外，还会分享如何在Koding、Heroku等免费平台搭建服务，让大家可以不用花一分钱就轻松飞跃长城。

有了这个梯子之后，你不仅可以毫无障碍地浏览编程派网站，还可以惬意地在Twitter上勾搭知名Python开发者。

## 什么是Shadowsocks？

Shadowsocks是一个轻量级的代理服务，可以说就是一把瑞士军刀，轻巧方便，功能却非常强大。

这么多年的翻墙经历中，先后使用过免费VPN、GoAgent、付费VPN红杏等工具，但是哪一个都没有Shadowsocks用的爽。目前，我自己就是在网站服务器上搭建了一个Shadowsocks代理服务。

它在广大翻墙群众中非常流行，有许多基于shadowsocks搭建的付费VPN服务，用它在自己服务器上搭建代理的朋友则是更多。其影响力之大，以至于官方都坐不住了，向原作者clowwindy施加压力，使得作者删除了在Github上的代码库。

不过这丝毫没有影响shadowsocks的继续传播，目前已经衍生出了无数版本的代理服务。

## Shadowsocks背后的原理

Shadowsocks实质上也是一种socks5代理服务，类似于ssh代理。这部分介绍其背后实现的原理，引用了[一位网友对此的解释](http://vc2tea.com/whats-shadowsocks/)，适合帮助非专业人士理解。（不感兴趣的朋友，可以直接跳过此节）

简单来说，Shadowsocks是将原来 ssh 创建的 Socks5 协议拆开成 server 端和 client 端，所以下面这个原理图基本上和利用 ssh tunnel 大致类似。

![Shadowsocks及其背后的原理](http://ww2.sinaimg.cn/mw690/006faQNTgw1f1itwk8p4bj30j808x0ty.jpg)

具体通信步骤如下：

1. 客户端发出的请求基于 Socks5 协议跟 ss-local 端进行通讯，由于这个 ss-local 一般是本机或路由器或局域网的其他机器，不经过 GFW，所以解决了上面被 GFW 通过特征分析进行干扰的问题； 
2. ss-local 和 ss-server 两端通过多种可选的加密方法进行通讯，经过 GFW 的时候是常规的TCP包，没有明显的特征码而且 GFW 也无法对通讯数据进行解密; 
3. ss-server 将收到的加密数据进行解密，还原原来的请求，再发送到用户需要访问的服务，获取响应原路返回。

了解背后的原理后，说不定你也可以自己实现Shadowsocks哦！O(∩_∩)O~

## 搞定服务器

首先，这个服务端所在的服务器必须在墙外。要是在墙内，你还翻个什么墙啊！

这里推荐几个选择：

- DigitalOcean：有优惠券可以使用，也可以点击[我的推广链接](https://m.do.co/c/70fd6733d655)。
- Vultr：目前他们家在搞活动（好像一直都有），[可以两个月内使用50美元](https://www.vultr.com/register/?register_promo=50for60)。注册后验证信用卡时，会扣除2.5美元的费用，但是后续会返还信用卡。需要注意的时，这50每月必须在两个月内用掉，否则就没有了。
- Amazon Web Services：AWS为新注册用户提供了免费12个月的使用套餐，可以免费启动虚拟机、存储文件或启动网站或应用程序。这里也需要验证信用卡，扣除费用为不固定，有1美元的，也有2美元的。
- Koding：允许建立一个免费的虚拟机，配置如下:1 Core、1GB RAM、3GB Total Disk。
- Heroku：Heroku是可支持多种编程语言的PAAS平台，可以在上面申请免费空间，部署免费应用。

可以说，你至少可以两个月免费使用代理服务，快乐地翻墙。

## 安装服务端

DO、Vultr、AWS、Koding等服务器上shadowsocks服务端的安装方法类似，Heroku平台则有较大区别，这里推荐[mrluanma](https://github.com/mrluanma/)开源的专用工具。

### 安装Shadowsocks

首先用 apt-get 命令安装 pip 和 m2crypto

	apt-get install python-pip python-m2crypto

然后用 pip 安装 shadowsocks

	pip install shadowsocks

### 单用户配置

	$ vi  /etc/shadowsocks.json

写入如下配置:

	{
	    "server":"0.0.0.0",
	    "server_port":443,
	    "local_address": "127.0.0.1",
	    "local_port":1080,
	    "password":"mypassword",
	    "timeout":300,
	    "method":"aes-256-cfb",
	    "fast_open": false,
	    "workers": 1
	}

各字段的含义:

server: 服务器 IP (IPv4/IPv6)，注意这也将是服务端监听的 IP 地址
server_port: 服务器端口
local_port: 本地端端口
password: 用来加密的密码
timeout: 超时时间（秒）
method: 加密方法，可选择 “bf-cfb”, “aes-256-cfb”, “des-cfb”, “rc4″, 等等。默认是一种不安全的加密，推荐用 “aes-256-cfb”

### 多用户多端口配置

{
    "server":"0.0.0.0",
    "local_address":"127.0.0.1",
    "local_port":1080,
    "port_password":{
         "8989":"password0",
         "9001":"password1",
         "9002":"password2",
         "9003":"password3",
         "9004":"password4"
    },
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}

### Koding平台注意事项

在Koding上，服务器IP地址只能是 0.0.0.0，否则会遇到 socket.error: [Errno 99] Cannot assign requested address 错误。

### 启动服务端

安装配置完成之后，就是在服务器上运行 Shadowsocks，命令如下：

	ssserver -c /etc/shadowsocks.json

## Heroku上安装服务端

以下是在Heroku上安装shadowsocks的详细过程，之前你需要注册Heroku平台账号，并在本地安装Heroku Toolbelt、NodeJS。

输入账号密码登陆：

	heroku login

创建应用，如：

	heroku create appname

下载Shadowsocks的Heroku专版，准备应用程序：

	git clone https://github.com/mrluanma/shadowsocks-heroku.git
	cd shadowsocks-heroku
	git init
	git commit -m "init"

添加remote：

	heroku git:remote -a appname

推送至Heroku：

	git push heroku master

设置加密方法和密码，如：

	heroku config:set METHOD=rc4 KEY=PASSWORD

加密方法推荐rc4和aes-256-cfb：

	heroku config:set METHOD=加密方法 KEY=密码

运行代理服务，如：
	
	node local.js -s appname.herokuapp.com -l 1080 -m rc4 -k PASSWORD

这样就可以通过设置Firefox或Chrome浏览器的插件翻墙了。将浏览器的代理设置为 SOCKS v5，地址为127.0.0.1，端口为1080。Chrome 浏览器建议使用 SwitchySharp 插件

## 客户端设置

### Windows

1.下载一个Shadowsocks的客户端程序。下载地址：http://t.cn/RLcp1EX。不需要安装，解压后即可使用。
2.运行解压后文件夹中的“shadowsocks.exe”
3.右下角找到程序图标，右键图标，“服务器”--“编辑服务器”，如下图，设置好shadowsocks的账号信息，点确定；

![编辑shadowsocks服务器](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1ix5d823gj30d608o0tt.jpg)

4.再次右键程序图标，勾选“启用系统代理“。

![再次右键程序图标，勾选“启用系统代理“](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1ix5ddet9j306h06xt96.jpg)

5.接下来，可以在Chrome中直接打开Youtube测试下效果。

### Mac

下载完Mac客户端后，具体设置与Windows平台下的操作类似。

### iOS

直接在Appstore搜索下载Shadowsocks，app打开后就是一个浏览器，内置了公共服务器，但是一般情况下，公共服务器不稳定，基本没啥用的。这时你就可以设置自己的服务器了。设置方法和Windows版一样。相比Android版，iOS版只支持浏览器。

当然，你可以搭建 Strongswan，实现在 iOS 上连接 VPN。具体流程请参考：[http://www.jianshu.com/p/2f51144c35c9](http://www.jianshu.com/p/2f51144c35c9)。

### Android

安卓下的Shadowsocks软件名称为“影梭”（ 百度网盘），下载后无需root，设置好服务器和帐号信息后即可直接使用。与iOS版本不同，android版是以VPN的方式运行的，也就是说不仅支持浏览器，而且支持其他App，简直好用到没人性。

![Android系统下影梭设置方法](http://ww1.sinaimg.cn/mw690/006faQNTgw1f1ix5e9gaoj30f00qoabo.jpg)

## 下一步

有了海外VPS之后，仅仅用于翻墙可能有点太浪费了。你还可以用它做下载站，中转YouTube的视频；或是直接在上面搭建自己的网站，就像我一样。O(∩_∩)O~

## 参考资料：

- [如何在 VPS 上搭建 VPN 来翻墙](http://www.jianshu.com/p/2f51144c35c9)
- [AWS上搭建免费每个月15G的shadowsocks](http://blog.xuanzhangjiong.xyz/2016/01/21/AWS%E4%B8%8A%E6%90%AD%E5%BB%BA%E5%85%8D%E8%B4%B9%E6%AF%8F%E4%B8%AA%E6%9C%8815G%E7%9A%84shadowsocks/)
- [一键在各个平台下安装Shadowsocks服务的脚本](https://github.com/teddysun/shadowsocks_install)
- [在Heroku上搭建Shadowsocks](http://sjnote.com/blog/2014/10/25/Running-Shadowsocks-On-Heroku.html)
- [在Koding上搭建Shadowsocks](http://www.isaced.com/post-262.html)
- [PC/MAC/Android等设备上使用客户端的方法](http://www.jianshu.com/p/d948f2e88866)
