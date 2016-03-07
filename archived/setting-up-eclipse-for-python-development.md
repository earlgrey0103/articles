# 在Eclipse上配置Python开发环境

关键词：Python IDE, Python eclipse ide, pydev eclipse, PyDev安装教程, Eclipse安装教程, Python开发环境

> 本文首发于[微信公众号“编程派”](http://mp.weixin.qq.com/s?__biz=MzAwNDc0MTUxMw==&mid=401789732&idx=2&sn=a5b9e63ff23ed20e70a70f8b66c6b210#rd)。微信搜索“编程派”，获取更多Python编程教程和精彩资源吧！

Eclipse是著名的跨平台集成开发环境（IDE），最初主要用来Java语言开发。但是我们通过安装不同的插件Eclipse可以支持不同的计算机语言。比如说，我们可以通过安装PyDev插件，使Eclipse成为一个非常优秀的Python IDE。本文的主题，就是如何在Eclipse上安装PyDev插件，配置Python开发环境。

> 声明：小编之前也没有使用过PyDev，因此可能介绍的并不太全面。本文是应一位关注公号的朋友要求所写，希望能够有所帮助！

***

## 什么是PyDev？

PyDev 这个强大插件是2003年时Fabio Zadrozny领导开发的，目的是使得用户可以完全利用 Eclipse 来进行 Python 应用程序的开发和调试。

而PyDev 插件的出现也的确方便了众多的 Python 开发人员。它提供了一些很好的功能，如：语法错误提示、代码分析、代码浏览、Quick Outline、Globals Browser、Hierarchy View、运行和调试等等。而其中，最受开发者推崇的功能就是调试器。如果你在调试方面做得很差，那么这个功能肯定能够帮到你！

![PyDev：鼠标悬浮在一个类上时会自动显示该类的定义](http://ww4.sinaimg.cn/mw690/006faQNTgw1f1mc36g55zj30ik09sq4k.jpg)

<p style="text-align:center">PyDev：鼠标悬浮在一个类上时会自动显示该类的定义</p>

![PyDev：代码分析](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1mt3cwfssj30m20ifaep.jpg)

<p style="text-align:center">PyDev：代码分析</p>

它还可以让你选择Python、Jython和IronPython等不同的Python实现进行编程。

总的来说，基于 Eclipse 平台，PyDev拥有诸多强大的功能，可定制性强，同时也非常易于使用。

***

## 如何安装Eclipse？

这里推荐安装Eclipse IDE for Java Developers，方便以后学习Java。

安装过程其实非常简单明了，只需要前往[这个下载地址](https://www.eclipse.org/downloads/)下载对应的系统安装包。

有一个需要注意的问题，即Eclipse要求系统上已经安装了相应的Java SDK。小编电脑上之前已经安装过JVM 1.6，但是这次安装过程中还是报错了，因为版本低于要求。

![安装Eclipse时出错，JVM必须>= 1.7](http://ww4.sinaimg.cn/mw690/006faQNTgw1f1mc31cklbj30ne08ejsr.jpg)

<p style="text-align:center">安装Eclipse时出错，JVM必须>= 1.7</p>

## 安装Java SDK

那么要解决这个问题，我们只需要安装或更新到所要求的JVM即可。据说对于El Capitan版本，苹果已经不再提供自己的JDK了，所以Mac用户必须前往[Oracle的相关页面](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)下载。

![安装最新的Java SDK: JVM](http://ww1.sinaimg.cn/mw690/006faQNTgw1f1mc344tkej30ts0hs10r.jpg)

## 安装PyDev

在安装PyDev之前，我们首先需要在Eclipse中设置pydev官网提供的软件更新站点。在Mac版本中，我们前往Preferences -> Install / Update下即可设置。按照下图操作即可。

![添加Update Site](http://ww1.sinaimg.cn/mw690/006faQNTgw1f1mc32jozwj30ye0k0afh.jpg)

添加完更新站点之后，我们在Help菜单下找到Install New Software。

![Help菜单下选择Install New Software](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1mc32t1fij315e0koqas.jpg)

然后在界面中Work with后的输入框中，输入pydev，编辑器会自动提示可供选择更新的站点，按下回车之后就会出现可以安装的PyDev插件啦。

![搜索PyDev插件](http://ww4.sinaimg.cn/mw690/006faQNTgw1f1mu8z0jjbj31ca0laq83.jpg)

接下来按照提示安装即可。

![PyDev安装过程](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1mc33stpsj315y0hwaf8.jpg)

安装成功后，需要重启。

![安装PyDev插件成功后，需要重启。](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1mc34tp3cj30tk088mys.jpg)

然后选择Perspective。依次点击菜单，Windows -> Perspective -> Other...。选中列表中的PyDev，即可将Eclipse界面更改为PyDev配置的样式。

![开启PyDev Perspective](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1mc351oolj30py0dgwgs.jpg)

接下来，我们就可以在Eclipse中编写Python程序啦。

## 小结

由于基于Eclipse的原因，PyDev算是一个非常强大的Python IDE。在PyCharm没有推出免费版之前，是许多开发者的首选工具。当然，对于经常需要进行Java 开发或者C/C++开发的人来说，也是非常好的选择。

在安装好PyDev之后，还有许多值得深入研究的配置，例如我们如何在PyDev中使用virtualenv。这些就留给大家自己去探索吧。

## 参考资料

- http://www.pydev.org/manual_101_install.html
- http://www.cnblogs.com/Bonker/p/3584707.html
- http://www.crifan.com/eclipse_install_plugin_pydev/
- http://ntraft.com/eclipse-with-pydev-and-virtualenv/
- https://www.londonappdeveloper.com/virtualenv-with-eclipse-with-pydev-on-windows-10/
- https://www.londonappdeveloper.com/setting-up-your-windows-10-system-for-python-development-pydev-eclipse-python/
- http://www.ibm.com/developerworks/cn/opensource/os-cn-ecl-pydev/