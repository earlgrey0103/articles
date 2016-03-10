# 你能打败这个简易版的AlphaGo吗？

关键词：python 围棋程序, AlphaGo围棋, GoGui围棋界面, Python编译为C++, Python教程, 终端游戏

> 本文首发于[微信公众号号“编程派”](http://mp.weixin.qq.com/s?__biz=MzAwNDc0MTUxMw==&mid=401852723&idx=1&sn=1f3a2e70130e040ce9e4732937854af9#rd)。微信搜索“编程派”，获取更多Python编程一手教程及优质资源吧。

这个题目是不是有点标题党？其实也不算。AlphaGo将深度学习和蒙特卡罗树搜索二者结合起来，而本文要介绍的围棋程序只使用了这种蒙特卡罗树搜索算法之一的UTC算法（upper confidence bounds applied to trees），可以说是超级简易版的AlphaGo了。

> 有关蒙特卡罗树搜索，请看另一篇：AlphaGo背后的搜索算法：蒙特卡罗树搜索。

这个围棋程序的名字叫Disco，是使用Python语言实现的。作者是shedskin库的作者Mark Dufour。shedskin又是什么？shedskin是一个将Python翻译成C++代码的专门库，只是似乎在Github上的关注度并不太高。这个程序也被作者用作shedskin的示例之一，因为据说编译成C++代码之后，执行效率比原来提升了6-75倍（这是在黑Python吗）。

和Disco下围棋，或许会让你有种极客范的感觉。因为你可以直接在终端里玩，大概是下面这样的：

![命令行中的围棋程序](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1qr3msjbxj309v0973yv.jpg)

注意，轮到你落子的时候，你应该类似这样输入要下哪：2 5。

有没有兴趣玩一下这个游戏？也可以按照下面的步骤，将程序接入图形化的围棋界面哦。

***

## 获取源码

我们首先获取Disco的源代码。

- 克隆[shedskin的代码库](https://github.com/shedskin/shedskin)，在examples文件夹下找到go.py文件。
- [前往我的百度网盘下载](http://pan.baidu.com/s/1qXdb9Is)。

## 安装GoGui

GoGui是一款开源软件，提供了围棋对弈的界面，但是不自带围棋算法。GoGui支持通过命令行命令直接与围棋引擎对话，而且保存当前棋局之后还可以切换围棋程序。

你可以前往[SourceForge](http://gogui.sourceforge.net/)下载该程序。

## 添加Disco程序

安装好GoGui之后，我们首先要做的就是添加Disco程序，因为我们前面讲到GoGui是不自带围棋算法的。具体步骤见下。

### 添加新程序

![GoGUI创建新程序](http://ww4.sinaimg.cn/mw690/006faQNTgw1f1qr4wpbdnj30dc0aymyu.jpg)

### 配置命令及工作目录

![GoGUI创建新程序：配置命令及工作目录](http://ww2.sinaimg.cn/mw690/006faQNTgw1f1qr4whsopj30dc0axtad.jpg)

## 开始玩游戏

在开始进行人机大战之前，你需要将棋盘设置为9x9大小。毕竟咱们用的围棋程序是个超级简易版的AlphaGo嘛，应付不了19x19的完整棋盘。

然后，在Program菜单下选择Attach -> 1.Disco。这样就将我们的围棋程序与GoGui成功连接起来了。

![GoGUI：attach program](http://ww2.sinaimg.cn/mw690/006faQNTgw1f1qr4w5lxnj30dc0b040a.jpg)

最后，选择让Disco执黑先行。为什么？因为程序就是这么设计的。

![GoGUI：将棋盘设置为9x9，并让程序执黑先行](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1qr4vqjrnj30dc0axjt5.jpg)

小编和Disco下了几步（因为以前学的都忘了），发现每一步Disco至少要思考近40秒。

## 加速Python程序

既然作者都说了编译成C++代码后能够极大提高性能，岂有不尝试的道理。

我们先安装shedskin。切换到shedskin目录下之后，输入下面的安装命令：

	sudo python setup.py install

注意，shedskin目前只支持Python 2。

然后切换到examples目录下，运行下面的命令：

	shedskin -e go.py

如果出现Template Not Found这个错误，不要惊慌。这好像是目前版本的一个小bug。小编准备去提个issue。

解决办法很简单，只需要将代码库中shedskin目录下的templates文件夹，复制到 Python 2的site-packages/shedskin目录即可。

	cp -r shedskin/templates/ /usr/local/lib/python2.7/dist-packages/shedskin/

根据你自己的环境修改相应的代码哦。

可是执行`shedskin -e go.py`成功之后，却没办法接着执行make命令！！这个问题不知道如何解决。因为已经按照文档中所说按照libgc-dev等库。

后来只能找来Nuitka，这也是个将Python代码编译成C++的第三方库。编译了一个go.exe（在Windows 10下无法执行。。。），在Ubuntu下执行，感觉上也没有快多少。

![执行Nuitka编译后生成的exe文件](http://ww1.sinaimg.cn/mw690/006faQNTgw1f1rhkuz1vnj30i90bc0vn.jpg)