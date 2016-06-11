# Guido老爹谈Python的未来

关键词：guido van rossum, python的未来, python语言趋势, python移动开发, Python性能提升, python开发

URL：guido-van-rossum-on-pythons-next-steps

6月初，Python之父Guido van Rossum在今天的PyCon US大会上作了名为“Python Language”的演讲。近日，他又接受了IT媒体Infoworld的采访，大谈Python的未来。我们一起来看看Guido老爹对Python的未来是怎么看的吧。

## Python在移动计算领域的应用

Guido：移动对Python来说仍是一个很难啃下来的平台，但是并没有浏览器平台的难度大，因为Python实际上是可以运行在所有品牌智能手机上的。你只需要找到懂得怎样构建移动版本Python的人就行了。

标准的CPython源代码几乎可以编译成能在安卓和苹果手机上运行的二进制文件。有很多人在朝这方面努力，不断贡献着补丁包。不过进展的速度比我希望的要慢一些。不过话又说回来，我本人并不开发移动应用，所以我没有太多自己参与的动力。但是我很乐于见到这方面的进展。

## Python替代JavaScript？

Guido：这并不是我们的目标。由于浏览器平台的结构问题，我们很难和JavaScript竞争，最多就是将Python翻译成JavaScript。不过通常情况下，翻译后的程序比Python原生程序运行的更慢，相比用JavaScript编写的同类程序则更慢。现在有人在尝试将Python翻译成JavaScript，在浏览器中运行Python。

## 对WebAssembly的看法

这可能会让在浏览器中运行Python成为可能。如果它替代了asm.js，那就基本上意味着JavaScript不再是Web平台上唯一使用的语言了，而是变成了这个类似汇编语言的东西。这和Python有点像，你编写的Python代码，其底层的Python解释器其实使用C语言编写的。在编译时，会把Python代码翻译成机器码，而这中间也涉及了某种汇编语言。

如果我们无法在浏览器中消灭JavaScript，我们或许可以让JavaScript成为任何希望在浏览器中运行语言的统一翻译对象。这样的话，或许Python和其他语言，如Ruby和PHP，就能高效地翻译成底层的JavaScript。

WebAssembly其实对Python开发者来说是个机遇。我相信以后会有一段试验期，那些更喜欢开发工具的人可以有机会探索怎样才是在WebAssembly之上运行Python的最好方法。他们试验成功并开始推广之后，我们就可以和Python开发者说，“你现在也可以用Python编写浏览器客户端app了”。但现在还不是时候。

## Python的性能提升

Guido：Python 3的性能已经跟上来了，比2012年时要快的多。另外，还有像PyPy这样的Python实现。有一些新版本的Python解释器也在试图提升速度。

其实，Python的性能并没有人们说的那样差，而且因为Python大部分是用C语言实现的，很多事情做起来可以和C语言一样快。我还是认为，Python对于大部分事情来说已经足够快了。

尽管没有往Python 3中新增特性以改善速度，但是我们已经让语言的很多方面变快了：比如，引用计数比以前快了些。主要还是优化现有的代码，但是作为用户来说，很难注意到区别。

而且如果你急需提升某个Python程序的速度，可以尝试使用PyPy。它已经足够成熟，值得尝试。

## Python为什么受欢迎？

Guido：主要是学习方便，使用方便，而且社区开放、乐于助人。

## Python的开发工作

Guido：目前，以及过去五年多时间里，主要是其他人在推动Python的发展。我偶尔进行一些指导，判断某个新想法是否值得接受，通常是设计是否要添加新语法时。在标准库开发方面，我很少干预。有时候，我也不得不让大家停止讨论，各自妥协。

我的想法是让社区能够自我延续，这样我就可以最终退休或者至少可以度个长假。我希望未来这门语言会吸收其他语言或者其他领域的新理念。

我最后想谈谈SciPy和NumPy。这两个团队正在推动使用Python替代Matlab。我们的替代方案是开源的，而且更好，他们能做到的。他们正在将Python带领到我以前从未想象过的领域。他们开发出了像Jupyter Notebooks这样的工作，可以在浏览器中使用交互式Python。

查看英文原文：[guido-van-rossum-on-pythons-next-steps](http://www.infoworld.com/article/3078633/application-development/qa-guido-van-rossum-on-pythons-next-steps.html)