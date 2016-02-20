# bpython：功能强大的Python shell

关键词：bpython, Python替代shell, 自动缩进Python终端, 语法高亮shell

Python是一个非常实用、流行的解释型编程语言，其优势之一就是可以借助其交互的shell进行探索式地编程。你可以试着输入一些代码，然后马上获得解释器的反馈，而不必专门写一个脚本。但是Python自带的shell也有一些局限性，例如无法自动补全、不能高亮语法等。

好在强大的Python社区对默认shell进行了扩展，开发了许多漂亮的Python shell。每一个都提供了一个极好的交互性的Python 体验。今天我就为大家介绍其中较为优秀的一款 — bpython。

## bpython简介

bpython是一个不错的Python解释器的界面，开发者的目的是提供给用户所有的内置功能，很像现在的IDE（集成开发环境），但是将这些功能封装在在一个简单，轻量级的包里，可以在终端窗口里面运行。

bpython并不追求创造任何新的或者开创性的东西。相反，它聚集了一些简洁的理念，关注于实用性和操作性。

## 如何安装

bpython最新版本是0.15。有四种安装方式：

- 官网下载最新版本的tarball：http://bpython-interpreter.org/releases/
- 克隆bpython的Git仓库：git clone https://github.com/bpython/bpython/
- 通过pip安装：pip install bpython
- 通过系统自带的包管理器：apt-get install bpython

想让bpython正常运行的话，还需要安装以下依赖包：

Pygments
requests
curtsies >= 0.1.18,< 0.2
greenlet
urwid (for bpython-urwid only)

## 具体功能

功能十分丰富，具体包括：

- 内置的语法高亮 – 使用Pygments排版你敲出的代码，并合理配色
- 根据你的行为，显示自动补全的建议
- 为任何Python函数列出所期望的参数 – 可以显示你调用的任何函数的参数列表
- “Rewind”功能会调出内存里的最后一行代码并重新执行
- 可以将你输入的代码送到pastebin
- 可以将你输入的代码保存到一个文件
- 自动缩进
- 支持Python 3


## bpython演示视频

<div id="mod_tenvideo_flash_player_1453169798053"><embed wmode="direct" flashvars="vid=a1302hzyak9&amp;tpid=0&amp;showend=1&amp;showcfg=1&amp;searchbar=1&amp;pic=http://shp.qpic.cn/qqvideo_ori/0/a1302hzyak9_496_280/0&amp;skin=http://imgcache.qq.com/minivideo_v1/vd/res/skins/TencentPlayerMiniSkin.swf&amp;shownext=1&amp;list=2&amp;autoplay=0" src="http://imgcache.qq.com/tencentvideo_v1/player/TPout.swf?max_age=86400&amp;v=20140714" quality="high" name="tenvideo_flash_player_1453169798053" id="tenvideo_flash_player_1453169798053" bgcolor="#000000" width="670px" height="502px" align="middle" allowscriptaccess="always" allowfullscreen="true" type="application/x-shockwave-flash" pluginspage="http://get.adobe.com/cn/flashplayer/"></div>

## 类似的Python shell

除了bpython之外，还有IPython、ptpython和dreampie等三个类似的Python shell。以后再给大家详细介绍。

**欢迎大家扫描下方二维码关注我的公众号“编程派”，谢谢支持！**

<p style="text-align:center">
    <img src="http://codingpy.com/static/images/wechat-of-codingpy.jpg" alt="编程派的微信公众号二维码" style="width:215px;height:215px">
</p>
