# 重磅！Win 10更新将带来原生Bash！

关键词：bash on windows, 微软BUILD大会, Windows下使用Bash, 命令行工具, 微软年度更新, 开发者功能

作为一名程序员，你在电脑上使用最多的工具，或许除了你最喜欢的IDE和编辑器之外，就是命令行了。使用Linux和OS X作为开发环境的开发者是有福的，因为他们可以使用强大的开源命令行Bash，甚至是Zsh。

![漂亮的Bash](http://ww2.sinaimg.cn/mw690/006faQNTgw1f2fqogh56fj306e0260g4.jpg)

但是如果你买不起Mac或也没用Linux，而是苦逼地用Windows机器做开发的话，那么你能使用的命令行应该这下面这样子的。

![Windows cmd.exe](http://ww3.sinaimg.cn/mw690/006faQNTgw1f2fqog6jltj302j01q0ha.jpg)

或者是这样子。

![Powershell prompt](http://ww4.sinaimg.cn/mw690/006faQNTgw1f2fqofvkcmj303t01u0ok.jpg)

## Windows 10推新开发者功能

不过这种情况很快就会改变。3月30日（当地时间），在Windows BUILD大会上，微软公司的Kevin Gallo宣布开发者“可以在Windows上运行Unbuntu下的Bash”啦！

![bash coming to windows](http://ww3.sinaimg.cn/mw690/006faQNTgw1f2fqx9ljesj30ki0doq5v.jpg)

据介绍，这是Windows 10系统即将发布的“Anniversary”更新中将推出的一个开发者功能。通过启用该功能，你可以在Windows系统上运行原生的用户模式shell和命令行。

![Windows Anniversary Update](http://ww4.sinaimg.cn/mw690/006faQNTgw1f2fr0ao9haj31ko11sgqh.jpg)

具体情况，可以看这个视频：

<div id="mod_tenvideo_flash_player_1459387444844" class="tenvideo_player"><embed wmode="window" flashvars="vid=z0191p54cok&amp;tpid=3&amp;showend=1&amp;showcfg=1&amp;searchbar=1&amp;shownext=1&amp;list=2&amp;autoplay=1&amp;ptag=%7Cuc.manage.li.title&amp;outhost=http%3A%2F%2Fv.qq.com%2Fpage%2Fz%2Fo%2Fk%2Fz0191p54cok.html&amp;refer=http%3A%2F%2Fv.qq.com%2Fu%2Fvideos%2F&amp;openbc=0&amp;fakefull=1&amp;title=%20%E5%8F%B7%E5%A4%96%EF%BC%81Windows%E4%B8%8A%E4%B9%9F%E8%83%BD%E4%BD%BF%E7%94%A8Bash%E5%95%A6%EF%BC%81" src="http://imgcache.qq.com/tencentvideo_v1/player/TencentPlayer.swf?max_age=86400&amp;v=20140714" quality="high" name="tenvideo_flash_player_1459387444844" id="tenvideo_flash_player_1459387444844" bgcolor="#000000" width="650px" height="472px" align="middle" allowscriptaccess="always" allowfullscreen="true" type="application/x-shockwave-flash" pluginspage="http://get.adobe.com/cn/flashplayer/"></div>

## 如何开启这个功能？

完成这个更新之后，你可以前往Windows的设置，启用开发者模式并添加该功能。然后你按Windows键，然后输入bash，系统就会提示你是否从Windows商家下载安装Canonical家提供的Ubuntu。

![Installing Ubuntu on Windows](http://ww2.sinaimg.cn/mw690/006faQNTgw1f2fqsror9mj30hs05ajtc.jpg)

请注意，这不是在虚拟机中运行Ubuntu或Bash。这是Windows自身系统上运行的一个真正的原生Bash！据试用过的开发者介绍，运行速度很快。

## 这个功能可以让你做什么？

现在你可以直接在Windows上运行Bash脚本，使用Linux下的命令行工具，如sed、awk、grep。

![直接在Windows上运行Bash脚本](http://ww3.sinaimg.cn/mw690/006faQNTgw1f2frsqgbaij30j70cbgnl.jpg)

甚至，你还可以通过`apt-get`安装Ruby、Redis和Emacs等程序。

例如，可以通过`apt-get install emacs23`安装emacs：

![Emacs界面](http://ww3.sinaimg.cn/mw690/006faQNTgw1f2fqsrd7wlj30hs09atch.jpg)

注意，这是直接从Ubuntu的代码库中下载的哦！

## 注意事项

前面提到了，这是一个开发者功能，而且属于预览阶段，所以肯定存在一些缺陷和限制。据微软官方博客介绍，这是微软首次推出该技术，还属于测试阶段，会时不时出现故障。所以不要期望每个Bash脚本都能完美运行。

虽然现在你可以运行原生Bash了，但是还要特别注意，这是一个开发者工具，是为了方便你构建和编写代码的。所以，你不能将其作为一个服务器平台，用来托管网站。

此外，还要注意Bash无法和Windows应用进行交互，反之亦然。也就是说，你无法从Bash中启动记事本，或者从PowerShell中运行Bash下的Ruby。

## 参考链接

[Run Bash on Ubuntu on WIndows](https://blogs.windows.com/buildingapps/2016/03/30/run-bash-on-ubuntu-on-windows/)

[Scott Hanselman的试用情况](http://www.hanselman.com/blog/DevelopersCanRunBashShellAndUsermodeUbuntuLinuxBinariesOnWindows10.aspx)
