# 选择最好的Python集成开发环境（IDE）

关键词：Python开发环境, Python编程开发工具, Python教程, PyCharm特点, WingIDE, Komodo IED, Eric IDE, eclipise pdev, python iep ide

- 原文：[http://pedrokroger.net/choosing-best-python-ide/](http://pedrokroger.net/choosing-best-python-ide/)
- 本文由[EarlGrey@编程派](http://codingpy.com)原创编译，首发于微信公众号“编程派”。微信搜索“编程派”，跟我一起学Python。

In this article I’ll review six Python IDEs. I’m mainly interested in IDEs that are cross-platform and have strong web development support (Django, HTML templates, JavaScript, etc). Because of this, well-regarded IDEs like PyScripter and Python Tools for Visual Studio are out since they are Windows-only. The Python website maintains a full list of Python IDEs.

PyCharm

PyCharm is one of the most popular Python IDEs and deservedly so. It’s packed with features such as incredible code completion, code analysis, code navigation, top-notch Django, JavaScript, HTML, and CSS support, great debugger, and much more.

pycharm

I wrote extensively about it before, so I won’t be a bore and repeat it here. The TL;DR is “PyCharm is a great Python IDE and you should definitely check it out”.

PyCharm main shortcomings is that it can be slow and its UI looks non-native in most platforms. In all fairness, PyCharm has come a long way in terms of UI and font rendering. The following is a screenshot of PyCharm, TextMate, and Emacs, respectively. I think PyCharm compares positively with TextMate:

pycharm-font

Sometimes PyCharm does feel slow, but it’s improving in each version. The current version feels much faster than the first version. In fact, it’s a no brainer if you consider that PyCharm gives you top-notch completion, code analysis and code navigation. As a comparison, Emacs starts much faster in my computer, but completion with ropemacs is way slower and less accurate than PyCharm’s.

PyCharm has great support and bugs are fixed regularly. It has good documentation, although I wish the on-line documentation had a more modern look with shallower structure. For example, the subsection “Version Control with PyCharm” is subdivided in eight subsections that are small enough to fit in one larger and easily scrollable page. Also, it would be nice to have the documentation as a PDF file.

pycharm-documentation

WingIDE

WingIDE is a solid IDE from Wingware that has been in development since 1999. It has many advanced features such as a first-rate debugger, code intelligence, and it can be extended in Python.

WingIDE’s debugger is super powerful and allows you to set breakpoints, step through code, inspect data, debug remotely, and debug Django templates. It has support for matplotlib where the plots are updated automatically.

wingide

For web development, WingIDE supports Django, Plone, Pyramid, Google App Engine and many others.

My main criticism is that the GUI, although responsive, is unattractive, old-fashioned, and quirky.

For instance, you can’t just open an existing directory like you can with PyCharm or TextMate; you need to create a new project (Project→New Project). But WingIDE doesn’t ask for the project’s name. The project will receive a default name and you can rename it if you want (Project→Save Project). Now you can add files or an existing directory (Project→Add Existing Directory).

And when you add a directory, it’s added to the Project pane folded (that is, the files and subdirectories are hidden) by default:

image

I hate being persnickety, but the first time I imported a Django project I was staring at the screen wondering what went wrong since nothing happened. After a while a noticed the small change in the left corner.

In general you can’t discover much from the UI. There’s no explicit support for Virtualenv; we need to select the Python binary in Project→Project Properties. This is not a big deal, but if we need to set a Django Settings module we need to type it in a text box, instead of just selecting the file directly with a file dialog. And, as we all know, it’s easy to make mistakes when typing. For example, in the following screenshot the value for DJANGO_SETTINGS_MODULE is wrong. After trying to run the code I realized that it should be ${DJANGO_SITENAME}.project.settings.

image

We can see the lack of discoverability in setting custom hotkeys as well. In order to (re-)bind a command we need to check the list of commands in the manual and type it in the text box (it has completion). Again, it’s not a huge deal, but it’s nice when you can accomplish things without leaving the IDE.

wing-custom-keys

Hopefully, Wingware is aware (no pun intended) of these shortcomings and seems to be working to fix them (not needing X11 to run it on the Mac is a step on the right direction).

If you are trying WingIDE, my advice is to stick to it for a while. They UI may seen a little off at first, but it has many useful and powerful features underneath and a great support for web and scientific programming.

PyDev

PyDev is a Python IDE for Eclipse with Django support, code completion, code analysis, navigation, remote debugging, interactive console and much more. You can install it as a plugin for Eclipse or by installing LiClipse, an advanced Eclipse distribution.

eclipse-debug

Eclipse seems to be one of those things that people either love or hate. It has good ideas and even Emacs creator Richard Stallman was impressed by it. However, sometimes things in Eclipse are unnecessarily complicated. For instance, the way it imports code in a project is just moronic. I find that I need to search or look up the documentation to accomplish even the simplest task such as changing the text font. This is not PyDev’s fault and, if anything, PyDev maintainer Fabio Zadrozny deserves big kudos for making it bearable to work with Python in Eclipse.

LiClipse adds support not only for Python, but for related languages such as CoffeScript, JavaScript, Django Templates, and much more. My main criticism is that it needs more and better documentation.

If you are already sold (or stuck 😉 on the Eclipse platform, PyDev is for you. If you want to try it out but has never used Eclipse before, I suggest you get a book to get acquainted with the Eclipse way of doing things.

Komodo IDE

Komodo is an IDE for dynamic languages such as Python, PHP and Ruby. The new version has many improvements such as code refactoring, multiple selections, better UI interface, open fast dialog, and much more.

komodo

Komodo IDE is pleasant and its configurations are easy to find and change. I like the editor and font rendering. Although the new version claims to have better OS X support, it doesn’t support the cocoa textbox shortcuts by default (such as Control-A and Control-E). It doesn’t have direct support for Virtualenv, but you can pick the Python interpreter in Project→Properties.

It has some support for Django, such as syntax highlighting and code completion for templates. (Although I couldn’t get it to work properly. Other people seem to be having problems with completion as well.)

It’s a good IDE if you deal with multiple languages and don’t do much web programming. Otherwise I think PyCharm, WingIDE, and PyDev are way ahead for a more reasonable price.

Eric

Eric is an open-source IDE for Python and Ruby with the ugliest mascot I have ever seen. It scares the bejesus out of me!



It toke me a while to install it as it has zero installation instructions. I tried to install Eric 5 (for Python 3) but after failing I decided to install Eric 4 (for Python 2) instead. I followed this receipt as a guide. I installed the dependencies with homebrew and ran the install.py script:

brew install qt pyqt qscintilla2
export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
sudo python install.py
Eric has a nice collection of features such as Python and Ruby debugger, code coverage, automatic code checking, Python and Ruby shell, class browser, and others. And it has features for collaborative editing (thanks to jgmitzen for pointing that out). However, to me, Eric seems more like an editor with some IDE features rather than a full-fledged IDE (not that there’s anything wrong with that).(I take that back, Eric is a full-fledged IDE, that was the caffeine talking ;-)) However, its documentation is sparse and consists of a couple of technical reports.

Eric is being actively maintained (a new version for both Eric 4 and 5 was released a few days ago) but its lack of support for Django and web programming means that I’ll pass.

IEP

IEP is an Interactive Editor for Python and not really an IDE. It may be useful for people looking for a Matlab replacement. It supports multiple Python shells simultaneously and you can program GUI toolkits such as PySide, PyQt4, wx, fltk, GTK, and Tk interactively.

iep

It’s open source and written in pure Python 3. Although it’s not a complete Python IDE, I’d love to see this level of interactivity in the other IDEs.

Conclusion

If you are looking for a full-fledged and cross-platform IDE, PyCharm, WingIDE, and PyDev are really your best choices.

Both PyCharm and WingIDE are well-priced and have personal and academic licenses, plus free licenses for classroom use and open source developers. PyDev is free and a LiClipse license is $50, which is a no-brainer if you need to work with Eclipse.

My IDE of choice is PyCharm. It is very good already and because its developers keep improving it, I have no doubt PyCharm is going to be even better in the future.

You can’t go wrong with WingIDE as well. It has outstanding features and a remarkable debugger. WingIDE developer’s know it needs some UI improvement and keep launching new versions.

I have a lot of respect for PyDev’s developer, but I can’t really stomach Eclipse; maybe it’s me. If you are into Eclipse, you should check LiClipse out as it will do a lot for you out-of-the-box.