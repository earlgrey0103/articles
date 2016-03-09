# 你能打败这个简易版的AlphaGo吗？

这个题目是不是有点标题党？其实也不算。AlphaGo将深度学习和蒙特卡罗树搜索二者结合起来，而本文要介绍的围棋程序只使用了这种蒙特卡罗树搜索算法之一的UTC算法（upper confidence bounds applied to trees），可以说是超级简易版的AlphaGo了。

这个围棋程序的名字叫Disco，是使用Python语言实现的。作者是shedskin库的作者Mike Dufour。shedskin又是什么？shedskin是一个将Python翻译成C++代码的专门库，只是似乎在Github上的关注度并不太高。这个程序也被作者用作shedskin的示例之一，因为据说编译成C++代码之后，执行效率比原来提升了6-75倍（这是在黑Python吗）。

和Disco下围棋，或许会让你有种极客范的感觉。因为你可以直接在终端里玩，大概是下面这样的：

![命令行中的围棋程序](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1qr3msjbxj309v0973yv.jpg)

注意，轮到你落子的时候，你应该类似这样输入要下哪：2 5。

有没有兴趣玩一下这个游戏？也可以将程序接入图形化的围棋界面哦。

## 获取源码

- 克隆shedskin的仓库，在examples文件夹下找到go.py文件。
- [前往我的百度网盘下载](http://pan.baidu.com/s/1qXdb9Is)。

## 安装GoGUI

http://gogui.sourceforge.net/

![GoGUI创建新程序](http://ww4.sinaimg.cn/mw690/006faQNTgw1f1qr4wpbdnj30dc0aymyu.jpg)

![GoGUI创建新程序：配置命令及工作目录](http://ww2.sinaimg.cn/mw690/006faQNTgw1f1qr4whsopj30dc0axtad.jpg)

## 开始玩游戏

![GoGUI：attach program](http://ww2.sinaimg.cn/mw690/006faQNTgw1f1qr4w5lxnj30dc0b040a.jpg)

![GoGUI：将棋盘设置为9x9，并让程序执黑先行](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1qr4vqjrnj30dc0axjt5.jpg)

第一步36秒，第二步40多秒

## 加速程序

既然作者都说了编译成C++代码后能够极大提高性能，岂有不尝试的道理。

发现了最新0.9.1的bug：Template Not Found。小编准备去提个issue。

cp /site-packages/shedskin即可。

编译成功后，无法make。这个问题不知道如何解决。因为已经按照文档中所说按照libgc-dev等库。

后来又使用nuitka，这也是个将Python代码编译成C++的第三方库。编译了一个go.exe，在Ubuntu下执行，似乎也没有快多少。
