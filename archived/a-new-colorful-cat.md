# 小技巧：多姿多彩的cat命令

关键词：cat 命令, 个性化终端, 语法高亮, pygments 包, shell 别名

URL：a-new-colorful-cat

今天和大家分享一个小技巧，可以让 cat 命令的输出变得多姿多彩。这篇可以算是[打造属于自己的个性化终端](http://codingpy.com/article/customize-your-terminal/)一文的续篇。

一般来说，我们在终端输入 ``cat some.py`` 命令之后，输出大概是下面这样的：

![一般的cat命令输出](http://ww4.sinaimg.cn/mw690/006faQNTgw1f5a2lzkosrj31900poqaf.jpg)

虽然咱们需要的功能是实现了，但是看上去没有“生机”。有没有办法让 cat 命令的输出变成下面这样：

![多姿多彩的cat命令输出](http://ww3.sinaimg.cn/mw690/006faQNTgw1f5a2m0cz0wj31bg0qgtew.jpg)

答案当然是肯定的！你也一起来试试吧。

## 实现方法

这个效果其实实现起来并不复杂。我们将用到 Pygments 库，进行实时语法高亮：

``pip install pygments``

然后，我们只要设置 shell 别名即可。如果你使用的是 bash，那么请打开 ``~/.bashrc``并加入这一行：

``alias cat='pygmentize -O style=monokai -f console256 -g'``

到这里，我们就完成了配置工作。以后，只需要输入``cat file.ext``，就会根据文件的扩展名自动进行语法高亮。

如果你不喜欢 monokai 主题，那么可以[参考该页面](http://pygments.org/demo/5387188/)选择所需的主题。


