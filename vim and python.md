# Vim与Python真乃天作之和
> 本文由编程派-EarlGrey翻译，原文出自[realpython](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/)，是Vim的爱好者专门针对利用Sublime Text 3设置Python IDE一文所写。译者本人也是依照Sublime Text那篇文章配置的开发环境，但一直对Vim作为神器的美名非常仰慕，又看到了一篇这么全面的配置文章，觉得有必要翻译过来与大家分享，想必可以省却很多自己研究如何配置的时间。

我注意到，有人在realpython.com宣扬[Sublime Text 3](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/)。作为公司的资深开发人员（呃，也就是老古董），我觉得有义务介绍一个**真正**的的Python开发环境给大家——我要推荐的当然就是Vim了。不错，Vim编辑器无处不在，速度快，从来不会崩溃。并且它能做任何事情！

不过，不利之处也有，就是Vim配置起来很让人头疼。但是，别担心，**本文将告诉你如何配置一个强大的Vim环境，专门用于天天捣鼓Python开发。**

下面是最终效果预览。

![Vim as Python IDE](https://realpython.com/images/blog_images/vim/vim-ide.png)

> 如果想充分地利用好本文，你应该对如何使用Vim和它的命令模式至少有一个基本的了解。如果你是初学者，你可以通过[vim-adventure](http://vim-adventures.com/)或者[openvim](http://www.openvim.com/)网站学习。在继续阅读本文之前，请花点时间浏览那两个网站的内容。

## 安装
因为许多Unix衍生系统已经预装了Vim，我们首先要确认编辑器是否成功安装：

    :::shell
    vim --version

如果已经安装了，你应该看到下面的文字：

    :::shell
    VIM - Vi IMproved 7.3 (2010 Aug 15, compiled Nov  5 2014 21:00:28)
    Compiled by root@apple.com
    Normal version without GUI.  Features included (+) or not (-):
    -arabic +autocmd -balloon_eval -browse +builtin_terms +byte_offset +cindent
    -clientserver -clipboard +cmdline_compl +cmdline_hist +cmdline_info +comments
    -conceal +cryptv +cscope +cursorbind +cursorshape +dialog_con +diff +digraphs
    -dnd -ebcdic -emacs_tags +eval +ex_extra +extra_search -farsi +file_in_path
    +find_in_path +float +folding -footer +fork() -gettext -hangul_input +iconv
    +insert_expand +jumplist -keymap -langmap +libcall +linebreak +lispindent
    +listcmds +localmap -lua +menu +mksession +modify_fname +mouse -mouseshape
    -mouse_dec -mouse_gpm -mouse_jsbterm -mouse_netterm -mouse_sysmouse
    +mouse_xterm +multi_byte +multi_lang -mzscheme +netbeans_intg -osfiletype
    +path_extra -perl +persistent_undo +postscript +printer -profile +python/dyn
    -python3 +quickfix +reltime -rightleft +ruby/dyn +scrollbind +signs
    +smartindent -sniff +startuptime +statusline -sun_workshop +syntax +tag_binary
    +tag_old_static -tag_any_white -tcl +terminfo +termresponse +textobjects +title
     -toolbar +user_commands +vertsplit +virtualedit +visual +visualextra +viminfo
    +vreplace +wildignore +wildmenu +windows +writebackup -X11 -xfontset -xim -xsmp
     -xterm_clipboard -xterm_save
       system vimrc file: "$VIM/vimrc"
         user vimrc file: "$HOME/.vimrc"
          user exrc file: "$HOME/.exrc"
      fall-back for $VIM: "/usr/share/vim"
    Compilation: gcc -c -I. -D_FORTIFY_SOURCE=0 -Iproto -DHAVE_CONFIG_H -arch i386 -arch x86_64 -g -Os -pipe
    Linking: gcc -arch i386 -arch x86_64 -o vim -lncurses

在这一步，你要确保符合以下两点要求：
1. Vim编辑版本应该大于7.3。
2. 支持Python语言。在所选编辑器的功能中，确保你看到了`+python`。

如果满足上述要求，接下来可以安装[Vim扩展](https://www.codingpy.com/article/vim-setup-for-fullstack-python-development#vim-extensions)了。如果不满足，则需要[安装/升级](http://www.vim.org/download.php)。

### OS X
如果没有[Homebrew](http://brew.sh/)，建议马上安装，并运行：

    :::shell
    brew update
    brew install vim

### Unix衍生系统
Debian或Ubuntu系统，可以使用下面的代码：

    :::shell
    sudo apt-get remove vim-tiny
    apt-get update
    apt-get install vim

如果是其他版本的Linux系统，请查阅相应版本包管理器的文档。不清楚的话，可以先阅读这篇文章：[安装Vim](http://oss.sgi.com/LDP/HOWTO/Vim-HOWTO/introduction.html)

### Windows
Windows系统下安装Vim有很多种方法。请查阅[官方文档](http://www.vim.org/download.php#pc)。

## 验证安装

确保你已经安装了7.3版本以上、支持Python的Vim编辑器。你可以再次运行`vim --version`进行确认。如果你想知道Vim中使用的Python版本，你可以在编辑器中运行`:python import sys; print(sys.version)`。

    :::shell
    2.7.6 (default, Sep  9 2014, 15:04:36)
    [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)]

这行命令会输出你的编辑器当前的Python版本。如果报错，那么你的编辑器就不支持Python语言，需要重装或重新编译。

Vim编辑器安装完成后，我们来看看如何将其设置为Python开发的强大环境。

## Vim扩展
Vim本身能够满足开发人员的很多需求，但是它的可扩展性也极强，并且已经有一些杀手级的扩展，可以让Vim拥有“现代”集成开发环境的特性。所以，你所需要的第一件东西就是一个号的扩展管理器。

> Vim的扩展通常也被成为bundle或[插件](http://vimdoc.sourceforge.net/htmldoc/usr_05.html#plugin)。

### Vundle

Vim有多个扩展管理器，但是我们强烈推荐[Vundle](https://github.com/gmarik/Vundle.vim)。你可以把它想象成Vim的pip。有了Vundle，安装和更新包这种事情不费吹灰之力。

我们现在来安装Vundle：

    :::shell
    git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

该命令将下载Vundle插件管理器，并将它放置在你的Vim编辑器bundles文件夹中。现在，你可以通过.vimrc[配置文件](https://github.com/amix/vimrc)来管理所有扩展了。

将配置文件添加到你的用户的home文件夹中：

    :::shell
    touch ~/.vimrc

接下来，把下来的Vundle配置添加到配置文件的顶部：
    
    :::shell
    set nocompatible              " required
    filetype off                  " required

    " set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()

    " alternatively, pass a path where Vundle should install plugins
    "call vundle#begin('~/some/path/here')

    " let Vundle manage Vundle, required
    Plugin 'gmarik/Vundle.vim'

    " Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)


    " All of your Plugins must be added before the following line
    call vundle#end()            " required
    filetype plugin indent on    " required

这样，你就完成了使用Vundle前的设置。之后，你就可以在配置文件中添加希望安装的插件，然后打开Vim编辑器，运行下面的命令：

    :::shell
    :PluginInstall

这个命令告诉Vundle施展它的魔法——自动下载所有的插件，并为你进行安装和更新。

![vim PluginInstall image](https://realpython.com/images/blog_images/vim/vim-plugininstall.png)

> 对于Windows用户，请查阅[Windows安装指南](https://github.com/gmarik/Vundle.vim/wiki/Vundle-for-Windows)。

## 开始打造IDE吧

本文不可能列举Vim的全部功能，只能快速介绍一些Vim自带的强大功能，它们对于Python开发来说是非常有用的。

### 扔掉鼠标

或许，Vim编辑器*最重要*的功能就是它不要求使用鼠标（除了GUI版本外）。一开始，你可能会觉得这是个非常糟糕的做法，但是只要你投入时间——是的，这很花时间——学习[快捷组合键](http://stackoverflow.com/a/5400978/1799408)，就可以大幅提升工作流的速度。

### 分割布局（Split Layouts）

![Split layout of vim](https://realpython.com/images/blog_images/vim/split-layouts.png)

使用`:sv <filename>`命令打开一个文件，你可以纵向分割布局（新文件会在当前文件下方界面打开），使用相反的命令`:vs <filename>`， 你可以得到横向分割布局（新文件会在当前文件右侧界面打开）。

你还可以嵌套分割布局，所以你可以在分割布局内容再进行分割，纵向或横向都可以，直到你满意为止。众所周知，我们开发时经常需要同时查看多个文件。

**专业贴士**：记得在输入完`:sv`后，利用tab补全功能，快速查找文件。
**专业贴士**：你还可以指定屏幕上可以进行分割布局的区域，只要在`.vimrc`文件中添加下面的语句即可：

    :::shell
    set splitbelow
    set splitright

**专业贴士**：想要不使用鼠标就切换分割布局吗？只要将下面的语句添加到`.vimrc`文件中，你就可以通过快捷组合键进行切换。

    :::shell
    "split navigations
    nnoremap <C-J> <C-W><C-J>
    nnoremap <C-K> <C-W><C-K>
    nnoremap <C-L> <C-W><C-L>
    nnoremap <C-H> <C-W><C-H>

组合快捷键：
- `Ctrl-j` 切换到下方的分割窗口
- `Ctrl-k` 切换到上方的分割窗口
- `Ctrl-l` 切换到右侧的分割窗口
- `Ctrl-h` 切换到左侧的分割窗口

换句话说, 按`Ctrl`+Vim的标准移动键，就可以切换到指定窗口。

> 等等，`nnoremap`是什么意思？——简单来说，`nnoremap`将一个组合快捷键映射为另一个快捷键。`no`部门，指的是在Vim的正常模式下重新映射，而不是可视模式下。

### Buffers

### Code Folding

### Python Identation

### 标示不必要的空白字符

### 支持UTF-8编码

### 自动补全

### 支持Virtualenv虚拟环境

### 语法检查/高亮

### 配色方案

### 文件浏览

### 超级搜索

### 显示行号

### Git集成

### Powerline状态栏

### 系统剪贴板

### Shell开启Vim编辑模式

## 结语

## 资源


