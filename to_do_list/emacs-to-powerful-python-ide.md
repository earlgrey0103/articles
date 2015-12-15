# Emacs：最好的Python编辑器？

> 本文是[realpython.com](https://realpython.com/blog/python/emacs-the-best-python-editor/)继《将Sublime Text 3打造为Python全栈开发环境及》和[《Vim与Python真乃天作之合》](http://codingpy.com/article/vim-and-python-match-in-heaven/)，又一篇关于如何配置Python IDE的文章。这一次，主角变成了与Vim同样享有神器之称的Emacs编辑器。译者之前没有接触过Emacs，但是看完这篇文章之后，觉得与Vim和Sublime Text 3相比，最出彩的一个地方就是可以和IPython与Jupyter Notebook进行集成。按照本文的介绍配置完之后，确实会让Emacs成为一个异常强大的Python IDE。

> 本文作者是Kyle Purdon​，是Bitly公司的一名应用开发工程师。译文链接：[http://codingpy.com/article/emacs-the-best-python-editor/](http://codingpy.com/article/emacs-the-best-python-editor/)。译文如存在问题，可以通过网站评论区或微信公众号“编程派”指出，谢谢支持！

## 安装与基础

### 安装
Emacs安装不是本文的重点，因此，这里推荐大家参考[ErgoEmacs](http://ergoemacs.org/)网站提供的[安装指南](http://ergoemacs.org/emacs/which_emacs.html)，完成在Linux、Mac或Windows平台的基本安装。安装完成之后，打开应用，你就会看到默认设置下地Emacs界面。

![Emacs编辑器默认页面](https://realpython.com/images/blog_images/emacs/emacs-fresh-launch.png)

### Emacs基础
同样，本文也不会过多介绍Emacs使用的基础知识。学习Emacs最容易的方法，就是通过其自带的教程。本文介绍的内容并不要求你知道如何使用Emacs；相反，本文的每一部分讲述的都是你学习基础知识后可以使用的。

你可以使用方向键将光标移动到标有“Emacs Tutorial”字样的地方，然后按回车键，就可以打开自带教程。然后，你将会看到下面这段话：

    Emacs commands generally involve the CONTROL key (sometimes labeled
    CTRL or CTL) or the META key (sometimes labeled EDIT or ALT).  Rather than
    write that in full each time, we'll use the following abbreviations:

     C-<chr>  means hold the CONTROL key while typing the character <chr>
        Thus, C-f would be: hold the CONTROL key and type f.
     M-<chr>  means hold the META or EDIT or ALT key down while typing <chr>.
        If there is no META, EDIT or ALT key, instead press and release the
        ESC key and then type <chr>.  We write <ESC> for the ESC key.

接下来，本文还会继续出现类似`C-x C-s`等按键命令。这些命令表示，要同时按下Control键和x键，然后再同时按下Control和s键。这正是使用Emacs编辑器的基本形式。了解更多基础知识，你可以学习自带教程或者GNU网站提供的这个教程[Guided Tour of Emacs](http://www.gnu.org/software/emacs/tour/)。

### 配置与插件包（packages）

Emacs的好处之一，就是配置简单。Emacs配置的核心则是初始化文件（Initialization File）—— `init.el`。

在Unix环境下，这个文件应该放置在`$HOME/.emacs.d/init.el`路径。

    $ touch ~/.emacs.d/init.el

同时，在Windows平台，如果没有设置`HOME`环境变量，该文件应该放置在`C:/.emacs.d/init.el`路径。

> 本文将会与大家分享许多配置示例。那么如果你想继续跟随本文进行配置的话，请先创建init文件。如果不想的话，可以在结语部分直接查看最终的完整init文件。

插件包（packages）可以对Emacs进行自定义，需要从不同的代码仓库获取。其中，最主要的Emacs插件包仓库是`MELPA`仓库。本文中提到的所有插件包都将从该仓库获取并安装。

### 样式（主题&更多）

首先，下面是一个插件包安装示例代码，其中安装了一个主题插件。

    ;; init.el --- Emacs configuration

    ;; INSTALL PACKAGES
    ;; --------------------------------------

    (require 'package)

    (add-to-list 'package-archives
           '("melpa" . "http://melpa.org/packages/") t)

    (package-initialize)
    (when (not package-archive-contents)
      (package-refresh-contents))

    (defvar myPackages
      '(better-defaults
        material-theme))

    (mapc #'(lambda (package)
        (unless (package-installed-p package)
          (package-install package)))
          myPackages)

    ;; BASIC CUSTOMIZATION
    ;; --------------------------------------

    (setq inhibit-startup-message t) ;; hide the startup message
    (load-theme 'material t) ;; load material theme
    (global-linum-mode t) ;; enable line numbers globally

    ;; init.el ends here

配置示例代码的第一部分是`;; INSTALL PACKAGES`，安装了`better-defaults`和`material-theme`共两个插件包。`better-defaults`插件集合了一系列对Emacs默认配置的修改，为我们开始进一步自定义奠定了良好的基础。`material-theme`插件则提供了一组自定义的样式。

> 主题插件中，我个人更喜欢的就是这个`material-theme`插件，所以本文中我们将一直使用这个插件。

第二部分则是`;; BASIC CUSTOMIZATION`（基本自定义）。

1. 禁用启动消息（即显示所有教程信息的页面）。在你更熟悉Emacs之前，你可以不禁用。
2. 加载`material`主题。
3. 启用全局显示行号

全局启用意味着这个功能对于Emacs打开的所有缓冲区（buffers）都适用。所以，如果你打开了Python文件、markdown文件或者是纯文本文件，它们都将显示行号。你还可以根据不同的模式（mode）启用不同的功能，——例如，python模式、markdown模式和纯文本模式。稍后我们将Emacs配置为Python IDE时还会讲到。

现在我们已经有了一个完整的基础配置文件，可以重启Emacs，观察变化。如果你将`init.el`文件放在了正确地路径中，Emacs将会自动加载该文件。

另外，你也可以在命令行输入`emacs -q --load <path to init.el>`命令，启动Emacs。配置文件加载完成后，我们之前见到的Emacs窗口会变得更好看：

![完成基础配置的Emacs界面](https://realpython.com/images/blog_images/emacs/emacs-themed.png)

下面这张图展示了一些Emacs本身自带的基础功能——包括简单的文件检索和Split Layouts。

![Emacs基本功能：文件检索和Split Layout](https://realpython.com/images/blog_images/emacs/emacs-simple-features.png)

我最喜欢的一个Emacs基础功能，就是可以进行快速的递归文本检索（recursive grep search）—— `M-x rgrep`。举个例子，假如你想在某个文件夹下以`.md`为扩展名的文件中，查找所有出现过`python`一词的段落：

![Emacs Grep检索](https://realpython.com/images/blog_images/emacs/emacs-rgrep.gif)

完成基础配置之后，我们可以开始将Emacs配置为Python开发环境啦！

## Elpy ——Python开发

Emacs自带的python模式（python.el）支持缩进和语法高亮功能。。但是如果要与专门针对Python设计的IDE竞争的话，我们肯定还需要添加更多的功能。`elpy`（Emacs Lisp Python Environment）插件可以说为我们提供了Python开发环境所需要的几乎全部功能，包括：

- 自动缩进
- 语法高亮
- 自动补全
- 语法检查
- REPL集成
- 虚拟环境支持，以及
- 更多其他功能

要想安装并启用`elpy`插件，我们需要进行一些配置，并使用你自己喜欢的方式（例如，`pip`或`conda`）安装`flake8`和`jedi`这两个Python工具包。

下面的配置可以安装`elpy`插件包：

    (defvar myPackages
      '(better-defaults
        elpy ;; add the elpy package
        material-theme))

现在我们这样启用这个插件：

    (elpy-enable)

完成上面的配置之后，我们可以重启Emacs，并打开一个Python文件，就可以查看新的配置是否生效。

![安装并启用了elpy插件的Emacs](https://realpython.com/images/blog_images/emacs/emacs-elpy-basic.png)

上面这幅图中显示了以下几种功能：

- 自动缩进
- 语法高亮
- 语法检查（第三行的错误提示）
- 自动补全（第九行显示的列表方法）

另外，假设我们想要运行这个脚本。在Python自带的IDLE或Sublime Text中，你可以点击一个运行当前脚本的按钮。Emacs编辑器也是一样，不过我们只需要Python缓冲区按下`C-c C-c`即可。

![Emacs elpy执行Python脚本](https://realpython.com/images/blog_images/emacs/emacs-elpy-execute.png)

通常，我们会希望运行一个虚拟环境，然后再使用虚拟环境中安装的工具包来执行代码。要想在Emacs中使用虚拟环境，我们需要输入`M-x pyvenv-activate`，然后根据提示操作。输入`M-x pyvenv-deactivate`就可以关闭虚拟环境。Elpy插件还提供了调试虚拟环境、处理elpy插件可能出现的问题的接口。输入`M-x elpy-config`，就会出现下面的信息，其中包含了有价值的调试信息。

![emacs elpy配置](https://realpython.com/images/blog_images/emacs/emacs-elpy-config.png)

到这里，我们已经介绍完在Emacs中实现Python IDE基础功能的方法。接下来，我们来进一步完善Emacs的配置。

## 额外的Python功能

除了上面介绍的基本IDE功能之外，Emacs还针对Python语言提供了一些额外的功能。在这一部分，我们无法介绍全部的额外功能，但是肯定会涉及PEP8、IPython/Jupyter集成。不过在此之前，我们要快速梳理一下语法检查配置。

### 更好的语法检查（Flycheck v. Flymake）

默认情况下，安装了Elpy插件的Emacs提供一个名叫`Flymake`的语法检查插件。但是，我们还可以选择另外一个名叫`Flycheck`的插件，后者支持实时语法检查。幸运地是，从`Flymake`切换至`Flycheck`非常简单：

    (defvar myPackages
      '(better-defaults
        elpy
        flycheck ;; add the flycheck package
        material-theme))

以及

    (when (require 'flycheck nil t)
      (setq elpy-modules (delq 'elpy-module-flymake elpy-modules))
      (add-hook 'elpy-mode-hook 'flycheck-mode))

现在，我们就可以在编辑Python代码的同时，获得实时代码检查反馈了：

![emacs flycheck实时代码检查](https://realpython.com/images/blog_images/emacs/emacs-elpy-flycheck.gif)

### 遵循PEP8规范

不管你喜不喜欢，PEP8都不会消失。如果你想遵循PEP8标准的全部或部分规范，你大概希望能够实现自动化合规。`autopep8`插件就是解决之道。这个插件与Emacs无缝集成，因此当你保存文件时——`C-x C-s`——autopep8插件就会自动格式化代码，并纠正所有不符合PEP8标准的错误（排除你不希望检查的错误）。

首先，你需要通过你喜欢的方式安装`autopep8`这个Python工具包，然后添加下面的Emacs配置代码：

    (defvar myPackages
      '(better-defaults
        elpy
        flycheck
        material-theme
        py-autopep8)) ;; add the autopep8 package
以及

    (require 'py-autopep8)
    (add-hook 'elpy-mode-hook 'py-autopep8-enable-on-save)

现在我们保存Python示例文件，Autopep8插件就会自动纠正出现的错误：

![emacs elpy autopep8自动纠正错误](https://realpython.com/images/blog_images/emacs/emacs-elpy-autopep8.gif)

### IPython/Jupyter集成

接下来这个功能尤其强大：将Emacs与IPython REPL和Jupyter Notebooks集成。首先，我们将Emacs中标准的Python REPL集成替换为IPython版本:

    (elpy-use-ipython)

现在如果我们按下`C-c C-c`再次运行Python代码，我们使用的将是IPython REPL：

![emacs elpy ipython repl集成](https://realpython.com/images/blog_images/emacs/emacs-elpy-ipython.png)

尽管做到目前这样已经非常有用了，但是真正的神奇之处还在Emacs与Jupyter notebook之间的集成。这里，我们假设你已经知道如何启动Jupyter Notebook服务器。要实现前面提到的集成，我们只需要再添加一些配置即可：

    (defvar myPackages
      '(better-defaults
        ein ;; add the ein package (Emacs ipython notebook)
        elpy
        flycheck
        material-theme
        py-autopep8))

Jupyter提供的notebook网络接口很好，但是要求我们离开Emacs编辑器才能使用：

![jupter web界面](https://realpython.com/images/blog_images/emacs/jupyter-web.png)

不过，我们可以通过在Emacs中直接连接notebook服务器，并与服务器进行直接交互的方式，就可以完成网络接口所提供的功能。

![emacs jupter界面](https://realpython.com/images/blog_images/emacs/emacs-elpy-jupyter.gif)

## 其他Emacs功能

前面我们已经介绍了所有Python IDE应具备的基础功能（以及一些非常棒的额外功能），但是还有一些功能也是IDE需要支持的。首先就是git集成。

### Git集成（Magit）

[Magit](http://magit.vc/)是MELPA仓库中非常受欢迎的一个插件包，几乎每一个使用Git的Emacs用户都会安装这个插件。这个插件极其强大，功能也特别全面，超出了本文的范围。不过还好[Mastering Emacs网站](https://www.masteringemacs.org/)上有[一篇介绍Magit的好文](https://www.masteringemacs.org/article/introduction-magit-emacs-mode-git)。下面这张图就摘自Mastering Emacs网站的那篇文章，展示了Emacs中git集成的效果：

![mastering emacs magit插件演示](https://realpython.com/images/blog_images/emacs/masteringemacs-magit.png)

### 其他Emacs模式

与使用只针对Python的IDE相比，使用Emacs的一大好处就是它还能够支持除Python外的其他语言。工作的时候，我通常要使用Python、Golang、JavaScript、Markdown、JSON以及其他语言。因此，只使用Emacs编辑器并且完美支持所有这些语言将会大大提高工作效率。Emacs编辑器支持以下语言：

- Python
- Golang
- Ruby
- Puppet
- Markdown
- Dockerfile
- YAML
- Web (HTML/JS/CSS)
- SASS
- NginX Config
- SQL

### 在终端使用Emacs按键组合

学会使用Emacs之后，你会希望在其他地方也能够使用Emacs按键组合。只需要在bash提示符之后输入`set -o emacs`即可实现。但是，Emacs的一个强大之处就是你可以在终端下以headless模式运行Emacs编辑器。这也是我本人的默认终端环境。要开启headless模式，只需要输入`emacs -nw`即可。

## 结语

正如你所见，Emacs明显是最好的编辑器。老实说，市面上还有其他很好的Python IDE可供选择，但是我会毫不犹豫地推荐你学习Vim或Emacs，因为基于这两个编辑器配置的开发环境无疑是功能最为多样化的。最后，为大家提供本文中完整的Emacs配置：

    ;; init.el --- Emacs configuration

    ;; INSTALL PACKAGES
    ;; --------------------------------------

    (require 'package)

    (add-to-list 'package-archives
           '("melpa" . "http://melpa.org/packages/") t)

    (package-initialize)
    (when (not package-archive-contents)
      (package-refresh-contents))

    (defvar myPackages
      '(better-defaults
        ein
        elpy
        flycheck
        material-theme
        py-autopep8))

    (mapc #'(lambda (package)
        (unless (package-installed-p package)
          (package-install package)))
          myPackages)

    ;; BASIC CUSTOMIZATION
    ;; --------------------------------------

    (setq inhibit-startup-message t) ;; hide the startup message
    (load-theme 'material t) ;; load material theme
    (global-linum-mode t) ;; enable line numbers globally

    ;; PYTHON CONFIGURATION
    ;; --------------------------------------

    (elpy-enable)
    (elpy-use-ipython)

    ;; use flycheck not flymake with elpy
    (when (require 'flycheck nil t)
      (setq elpy-modules (delq 'elpy-module-flymake elpy-modules))
      (add-hook 'elpy-mode-hook 'flycheck-mode))

    ;; enable autopep8 formatting on save
    (require 'py-autopep8)
    (add-hook 'elpy-mode-hook 'py-autopep8-enable-on-save)

    ;; init.el ends here

希望这些配置能够激起你学习并使用Emacs的热情！

