# Mac OS X系统中如何安装Python

关键词：Mac OS X 安装Python, Python安装方法, Python更新, Mac Python更新版本, Python源代码安装, 常见的Python安装方法

与其他开源软件一样，在Mac OS X平台上安装Python有多种方法。笔者觉得有必要将一些最简单的方式记录下来，其中包括：

- Homebrew
- 安装文件（packaged binaries）
- 源代码安装

上面是一般安装Python时最常见得几种方法，每一种都有各自的优势，下面我会详细介绍。

大部分情况下，安装Python 2和Python 3的过程还是略有不同，虽然大致差不多。因此，在安装时要注意自己需要的是哪个版本。

还要提醒大家注意的是，Mac OS X(10.8+)系统中已经预先安装了Python 2.7，所以下面的操作提示只有在你需要更新版本或者寻找更好地软件管理方式时才有用（比如说Homebrew）。

## 通过Homebrew安装

首先，如果你还不知道什么是[Homebrew](http://brew.sh/)，而你用的又是Mac OS X系统，那么建议你先了解一下Homebrew。据其官网介绍，Homebrew是“OS X平台所欠缺的包管理器”。笔者认为，这个介绍一点都不为过。

![Homebrew官网截图](http://ww1.sinaimg.cn/large/006faQNTjw1f0dsc7kx0jj30jg09kt9x.jpg)

Homebrew可以让你通过命令行快速安装、更新、删除软件包，有点类似Ubuntu系统下的`apt-get`。这样，你安装各种软件时就会容易得多。例如，笔者就是通过homebrew安装了下面这些软件：android-sdk、go、mongodb、sqlite、git、imagemagick、lua和python3。

要安装Homebrew，只需跟着其网站的介绍操作即可。

既然你已经了解并安装了Homebrew，我们接下来就可以开始安装Python了。你可以通过Homebrew安装不同版本的Python，包括2.7.x和3.5.x。

安装Python 2.7的话，请输入：

	:::emacs
	$ brew install python

如果你选择使用Python 3，只需要将`python`替换成`python3`即可。想查看可以安装哪些Python版本的话，可以通过下面的命令在Homebrew上搜索：

	:::emacs
	$ brew search python

这个命令会列出可以安装的全部Python版本。

## 通过安装包安装

如果你想更新至最新的2.7.x或3.x版本，你可以直接从[Python官网](https://www.python.org/downloads/mac-osx/)下载二进制安装文件。

![Python官网下载页面](http://ww2.sinaimg.cn/large/006faQNTjw1f0dscdc8x1j30jg0clgn3.jpg)

点击上面的链接，然后选择需要的版本。Python 2和3的最新版本就在页面的顶部。选择好Python版本之后，你就能看到针对不同操作系统的安装包下载链接了。

我建议你下载相应系统的安装器，因为它会处理好所有的安装事宜，只需要确保下载了自己电脑CPU架构（32位或64位）对应的文件即可。笔者下载的则是Mac OS X 64位/32位安装器。

双击安装器之后，只要按照提示操作，就可以顺利安装Python。

## 从源码安装Python

最后一种，也是最少见的安装方式，就是从源码安装Python。大部分人都不会这样做，因为已经有现成的安装文件了。这种方法也只有在你真的需要自定义一些Python设置时，才会选择的安装方式。因为你在编译Python安装程序之前，可以进行部分设置。

下面就是从源码安装Python的相应步骤：

	:::emacs
	curl -OL http://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz  
	tar xzvf Python-2.7.11.tgz  
	cd Python-2.7.11  
	./configure --prefix=/usr/local --enable-shared
	make  
	make install  

安装时，请确保版本号与你希望使用的版本保持一致。

上面的操作同样也适用于从源码安装Python 3，只需要替换版本号即可。

**欢迎大家扫描下方二维码关注我的公众号“编程派”，谢谢支持！**

<p style="text-align:center">
    <img src="http://codingpy.com/static/images/wechat-of-codingpy.jpg" alt="编程派的微信公众号二维码" style="width:215px;height:215px">
</p>