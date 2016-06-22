# 打造属于自己的个性化终端

关键词：个性化终端, 终端模拟器, 自定义终端, 编程派,

URL: customize-your-terminal

我们在《硅谷码农是这样秀逼格、撩妹子的！》一文中看到了许多程序员提升逼格的方法，其中“打造个性化终端”或许可以算是实现最快、成本最低的招数了。这也是我们今天分享的主题，具体来说是使用Zsh + Oh my Zsh。

## 选择正确的终端

各个平台系统自带的终端好像都不是很好用，功能不全，因此在开始使用Zsh之前，我们需要先找到一个好用的终端。

对于OS X用户，我推荐使用[iTerm2](https://www.iterm2.com/)替代系统自带的终端。iTerm2提供了许多自带终端中没有的特性，包括分屏、自定义配色方案、粘贴历史、热键配置等。你使用终端的机会越多、使用的越熟练，就会发现这些功能非常有用。

![iTerm2截图](http://ww2.sinaimg.cn/mw690/006faQNTgw1f54cqtzz8gj30m808o74u.jpg)

Windows平台内置了PowerShell，但是和广泛用于网站托管的UNIX服务器接口存在很大不同。因此，最好使用能提供类似UNIX命令行体验的终端。

这里我推荐[Cmder](http://cmder.net/)，它自带了Git集成、自定义的提示符和配色方案等功能，对于大多数开发者来说已经足够了。但可惜的是，Cmder并不支持Zsh。

![Cmder截图](http://ww3.sinaimg.cn/mw690/006faQNTgw1f54cqt37hjj311y0kcq7c.jpg)

## 安装Zsh + Oh My Zsh

不管是在服务器还是本机上打开终端，默认都会运行名叫 Bash 的 shell，它是目前最为流行的 shell，几乎每个基于UNIX的系统都支持。但是也存在其他的 Bash 替代方案，能帮助开发者更方便快捷地使用终端。

其中之一就是Z shell，也被称为Zsh。我们还将一起使用名叫[Oh-My-Zsh](http://ohmyz.sh/)的Zsh配置管理框架。

Oh-My-Zsh的安装非常简单，只需在命令行输入以下命令并重启即可：

``curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh``

如果之前为切换shell，请先运行：

``chsh -s $(which zsh)``

## ZSH主题

Oh-My-Zsh提供了140多个主题可选择，我自己目前使用的是默认主题，具体效果如下：

![Oh-My-Zsh默认主题](http://ww1.sinaimg.cn/mw690/006faQNTgw1f54cqu2fa8j30wk0p0my7.jpg)

有很多开发者选择使用[名为agnoster的主题](https://github.com/fcamblor/oh-my-zsh-agnoster-fcamblor)，具体效果如下：

![Oh-My-Zsh主题agnoster](https://cloud.githubusercontent.com/assets/2618447/6316862/70f58fb6-ba03-11e4-82c9-c083bf9a6574.png)

其具体安装方法为：

1. 下载下来之后解压，然后到目录里面运行install文件，就可以将主题安装到~/.oh-my-zsh/themes目录下

2. cd切换到用户根目录，打开.zshrc文件，然后将ZSH_THEME后面的字段改为agnoster即可。

如果显示存在问题，那么说明你需要安装[Vim-Powerline相关字体](https://github.com/powerline/fonts)。

***

到目前为止，我们算是做了一些终端的“面子”工程。Zsh其实还提供了很多插件，有兴趣的朋友可以自行探索。


