# 比迅雷还要快的视频下载利器You-Get

关键词：you-get, youtube 视频下载, 视频网站视频下载, 网络视频下载, Python 视频下载, 轻松下载网络视频

URL：using-you-get-to-download-videos

现在在线视频超火爆，可是我还是更倾向于将视频下载至本地后观看，原因之一是受不了播放时的卡顿，还有一个原因就是保存文件以备以后观摩，比如说视频教程。其实，这样也是可以省流量的！(因为后续看的时候就不花流量啦)

但是有些视频网站不希望你直接下载视频文件，因为网站自身流量就少了，广告没法放了嘛！所以，这些网站的技术人员设置了重重障碍，找到网络视频的真实文件地址是极其困难的。

你可以学些前端知识，通过 Chrome 审查元素来进行嗅探视频地址，也可以在看视频之前清除 Cookies ，然后看一遍视频再找到视频文件。甚至，你会装一个迅雷浏览器扩展插件之类的，直接右键嗅探视频地址，或者求助一些在线视频提取的网站。

但是这些似乎都有点太麻烦了，我们不如考虑使用Python写的视频下载利器[You-Get](https://you-get.org/)，它已经帮你解决了寻找下载地址的问题。

## 什么是You-Get？

You-Get 是一个轻量级的命令行程序，可以让我们便利地下载网络视频。据[官网文档介绍](https://github.com/soimort/you-get/wiki/%E4%B8%AD%E6%96%87%E8%AF%B4%E6%98%8E)，它主要有以下几个功用：

- 下载流行网站的音视频，例如YouTube、Youku,、Niconico以及更多。
- 于您心仪的媒体播放器中观看在线视频，脱离浏览器与广告
- 下载您喜欢网页上的图片
- 下载任何非HTML内容，例如二进制文件

## 如何安装

在安装You-Get之前，请先确保你的本地系统已经具备了以下依赖：

- [Python3](https://www.python.org/downloads/)
- [FFmpeg](https://www.ffmpeg.org/) (强烈推荐) 或 [Libav](https://libav.org/)

如果你用的是OS X系统，可以参考下[这篇文章](http://codingpy.com/article/install-python-on-mac-os-x/)。

安装好依赖后，我推荐使用 ``pip`` 安装You-Get的最新版：

``pip install you-get``

如果你用的是Windows系统，那么推荐安装预编译好的安装包，可以[从这个地址下载](https://github.com/soimort/you-get/releases/latest)。

## 如何使用

使用方法很简单，只需要输入 ``you-get 视频URL（自行替换）`` 即可。比如我早上随机下载了B站的一个动画视频，具体效果如下图所示：

![You-Get下载B站视频](http://ww4.sinaimg.cn/mw690/006faQNTjw1f43wirz3amj30vk0caaew.jpg)

下载速度满速哦！比我之前用迅雷下载视频的速度快多了。

如上面第一部分所讲的那样，You-Get还支持直接在终端观看视频、下载网页图片等功能。这里就需要[参照官网文档去设置](https://you-get.org/)了。

据官方介绍，You-Get支持下载包括Youtube在内的70余家视频网站，其中还有有丰富技术视频教程的Khan Academy、InfoQ。

当然，具体哪些可用就需要自己亲自去测试了。


 