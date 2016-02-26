Google's Python Class

- Overview: https://developers.google.com/edu/python/
- Set Up:https://developers.google.com/edu/python/set-up

## 概述

欢迎来到谷歌的Python公开课。这是一门免费课程，目标受众是希望学习Python语言、有一定编程经验的人。这门课程包括了书面学习材料、课程视频和大量的代码练习。谷歌公司内部培训使用的就是这些材料。一开始的练习只涉及基础的Python概念，例如字符串（string）和列表（list），随着课程逐渐深入，后面的练习则需要编写处理文本文件、处理进程和http连接的完整程序。虽然本门课程在设计时，针对的是那些具备一些其他编程语言经验的人，但是你只需要知道什么是“变量”或“if语句”即可。你不一定要成为专家程序员才能学习这门课。

在开始学习之前，简单介绍下本门课的结构。“Python安装”一节介绍的是如何在本地机器上安装Python，“Python简介”一节会对Python语言进行简要的介绍，然后从“Python字符串”一节开始，我们就开始学习编程材料，这节的最后会提供第一个编程练习的链接。每一个书面章节之后，都会提供相应章节材料的编程练习链接。课程视频与书面材料是同步的，首先会简单介绍Python语言，然后讲解字符串，接着做第一个练习，等等。在谷歌，这些材料支撑了为期两天的培训课程，所以课程视频也分为第一天和第二天两个部分。

这些材料是Nick Parlante在谷歌的engEDU小组工作时编写的。我要感谢在谷歌时的同事John Cox、Steve Glassman,、Piotr Kaminksi和Antoine Picard的帮助。最后，还要感谢谷歌和我的上司Maggie Johnson将这些材料以Creative Commons Attribution 2.5协议免费分享在互联网上——欢迎大家分享！

## Python安装

这节介绍的是如何在电脑上安装、配置Python，这样你才能运行、编辑Python程序。你可以在开始学习课程之前完成这项工作，也可以留到有了一定的了解、想动手编写代码的时候再进行。谷歌的Python公开课使用的是简单、标准的Python安装环境，尽管有更加复杂的安装方法。Python是免费、开源的编程语言，官网python.org提供了所有系统环境下的安装文件。在本课中，我们希望你安装的Python支持以下两点操作即可：

- 运行已有的Python程序，例如`hello.py`。
- 以互动模式（interactive mode）运行Python解释器，支持直接在解释器中编码。

在课程视频中，你会看到本课中会大量进行上面的操作，而你要解决课程中的代码练习的话，也必须要能够做上面的操作。

### 下载谷歌Python公开课的代码练习

首先，我们下载`goole-python-exercises.zip`文件，并将其解压至方便查找的地方。解压后的`google-python-exercises`文件夹中，包含了许多不同的Python代码练习题。其中，有一个名为`hello.py`的简单Python文件，接下来你可以运行该文件，验证下电脑上是否成功安装了Python。下面是在Windows系统和其他操作系统中安装Python的指南：

### 在Linux、Mac OS X等系统中安装Python

除了Windows之外的大部分操作系统都默认安装了Python。要检查系统中是否已经安装了Python，可以打开命令行（一般来说，指的就是运行“Terminal”程序），然后`cd`至`google-python-exercies`目录下。接下来，按照下面的操作，试着运行`hello.py`程序（你需要输入粗体部分的代码）：

	~/google-python-exercises$ python hello.py
	Hello World
	~/google-python-exercises$ python hello.py Alice
	Hello Alice

如果系统没有安装Python，请前往[Python.org的下载页面](http://python.org/download)。如果想以交互模式运行Python，只需要在终端输入“python”即可：

	~/google-python-exercises$ **python**
	Python 2.5.2 (r252:60911, Feb 22 2008, 07:57:53) 
	[GCC 4.0.1 (Apple Computer, Inc. build 5363)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 1 + 1
	2
	>>> **你可以在这里输入表达式...按`ctrl-d`退出**

在本课中，你需要2.4或之后的Python版本，目前或许最好不要使用3.x版本。

### 执行位（可选步骤）

上面的命令式运行Python程序最简单的方式。如果一个`.py`文件上设置了“执行位”（Execute Bit）的话，那不需要先输入“python”就可以直接通过文件名运行。你可以像下面这样，使用`chmod`命令来设置执行位：

	~/google-python-exercises$ chmod +x hello.py
	~/google-python-exercises$ ./hello.py   ## now can run it as ./hello.py
	Hello World

> 译者注：在`.py`文件的顶部添加 !# usr/bin/python也可以实现这个效果。

### Windows系统下安装Python

在Windows系统下，基本的Python安装还是比较容易的：

- 前往[python.org的下载页面](http://www.python.org/download/)，选择一个Python版本下载。只要版本在2.4或以上，在学习本门课时就不会出现问题。现在，最好还是避免使用3.x版本。
- 运行Python安装器，选择默认设置即可。这会在根目录下安装Python，并配置一些必要的文件关联。

安装完Python之后，打开命令提示符（附件 > 命令提示符，或在`run`对话框中输入`cmd`）。`cd`至`google-python-exercises`目录中（即`google-python-exercises.zip`文件解压后的目录）。在命令提示符中输入`python hello.py`之后，你应该可以看到`hello.py`这个Python程序的运行结果（你需要输入的部分以粗体显示）：

	C:\google-python-exercises> python hello.py
	Hello World
	C:\google-python-exercises> python hello.py Alice
	Hello Alice

如果结果与上面的相同，那么证明你成功安装了Python。否则，请查阅[Python Windows FAQ](http://www.python.org/doc/faq/windows/)寻求帮助。

如果想以互动模式运行Python解释器，可以从开始菜单中选择Run...命令，然后输入`python`——系统会在新窗口中以互动模式启动Python。在Windows系统下，按`Ctrl-Z`退出（其他操作系统下，按`Ctrl-D`退出）。

在课程视频中，我们一般使用`./hello.py`这样的命令运行Python程序。但是在Windows系统下，通过`python hello.py`这样形式的代码运行起来最简单。

### 编辑Python程序（适用于所有操作系统）

一个Python程序就是一个你可以直接编辑的文本文件。如果你按照之前的要求进行了操作，那么现在应该已经打开了一个命令行，在命令行中你可以输入`python hello.py Alice`进行代码练习。另外，你可以按向上的箭头键回忆之前输入过的命令，这样你不需要重新输入，就可以轻松运行之前的命令了。

你需要一个支持代码缩进等功能的文本编辑器。

网上有许多免费的工具可供选择：

- Windows系统 —— 不要使用**记事本**或**写字板**。可以试试免费得Notepad++或者JEdit。
- Mac系统 —— 自带的TextEdit也行，但功能不强大。可以试试免费得TextWrangler或JEdit。
- Linux —— 任何unix系统的文本编辑器都行，或者也可以尝试上面提到的JEdit。

> 译者注：
Sublime Text 3
Vim
Emacs

### 编辑器配置

在编辑Python程序时，我们建议你在按下tab键时，让编辑器插入空格符，而不是制表符。这门课中所有的Python文件都使用2个空格作为缩进，另一个常见的选择是4个空格。如果编辑器支持按return键后自动缩进，那就更好了。我们还建议在保存文件时，按照unix的规范创建新行作为行结束符（unix line-ending convention），因为我们的代码文件就是这样设置的。如果运行`hello.py`时出现了`Unknown option:-`这个错误，那么这个文件的行结束符可能存在问题。下面是一些常见编辑器中针对Python所做的一些设置，让编辑器正确处理tab和行结束符。

- Windows Notepad++ —— Tabs：Settings > Preferences > Edit Components > Tab settings； 自动缩进：Settings > Preferences > MISC；行结束符：Format > Convert, 设置为Unix。
- JEdit（任何系统）—— 行结束符：状态栏上的'U' 'W' 'M'字样，将其设置为'U'。
- Windows记事本或写字本 —— 不建议使用。
- Mac TextWrangler —— Tabs：
- Mac TextEdit —— 不建议使用。
- Unix pico —— Tabs: Esc-q toggles tab mode, Esc-i to turns on auto-indent mode
- Unix emacs —— Tabs: manually set tabs-inserts-spaces mode: M-x set-variable(return) indent-tabs-mode(return) nil

### 检查编辑效果

用你选择的编辑器，打开`hello.py`程序试试编辑效果。将代码中的“Hello"修改为“Howdy”（你现在还不需求明白里面的其他代码...稍后会在课程中进行解释）。编辑完之后保存，然后运行程序查看新的输出结果。你可以试着在源代码中那个`print`语句下面，再加上一条`print 'yay'`，两者使用同样地缩进。接下来再次运行程序，看看你的编辑是否成功生效。在本课中，我们希望你保持一个编辑/运行的工作流，这可以让你轻松地在代码编辑和程序运行之间进行切换。

### 快速Python编写风格（Quick Python Style）

Python的优势之一，就是可以在输入一段代码之后，快速输出代码运行的记过。在本课中，我们希望你能够做到这样：使用文本编辑器编辑当前的file.py文件，在另一个命令行窗口中，按向上箭头键运行file.py文件，查看运行结果。（抛开教学理念不谈，解释器对于进行一些小实验非常有用，你在之后的课程中就可以看到。但是，为了方便学员编辑代码，编码练习是以Python文件的形式呈现的。由于编写Python程序才是本课的终极目标，因此我想最好大家一直以脚本模式运行Python，解释器用来做些小实验就好了。）
