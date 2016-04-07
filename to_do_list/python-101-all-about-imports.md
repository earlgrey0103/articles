# 关于import你应该知道的一切（一）

> 本文首发于微信公众号“编程派”。微信搜索“编程派”，获取更多Python编程教程和精彩资源吧！

原文：[Python 101 - All about imports](http://www.blog.pythonlibrary.org/2016/03/01/python-101-all-about-imports/)

作为一名新手Python程序员，你首先学习的内容之一就是如何导入其他模块或包。但是，我注意到甚至那些许多年来不时使用Python的人，也不是都知道Python的导入机制是多么的灵活。在本文中，我们将探讨以下话题：

- 常规导入（regular imports）
- 使用from语句
- 相对导入（relative imports）
- 可选导入（optional imports）
- 本地导入（local imports）
- 导入注意事项

## 常规导入

常规导入应该是最常使用的导入方式，大概是这样的：

    import sys

你只需要使用`import`一词，然后指定你希望导入的模块或包即可。通过这种方式导入的好处是可以一次性导入多个包或模块：

    import os, sys, time

虽然这节省了空间，但是这违背了Python风格指南。Python风格指南建议将每个导入语句单独成行。

有时在导入模块时，你想要重命名这个模块。这个功能很容易实现：

    import sys as system
 
    print(system.platform)

上面的代码将我们导入的`sys`模块重命名为`system`。我们可以按照和以前一样的方式调用模块的方法，但是可以用一个新的模块名。也有某些子模块必须要使用点标记法才能导入。

    import urllib.error

这个情况不常见，但是知道总比不知道好。

## 使用from语句

很多时候你只想要导入一个模块或库中的某个部分。我们来看看在Python中如何实现这点：


    from functools import lru_cache

上面这行代码可以让你直接调用`lru_cache`。如果你按照正常的方式导入`functools`，那么你就必须像这样调用`lru_cache`：

    functools.lru_cache(*args)

根据你实际的使用场景，上面的做法可能是更好的。在复杂的代码库中，能够看出某个函数是从哪里导入的这点很有用的。不过，如果你的代码维护的很好，模块化程度高，那么只从某个模块中导入一部分内容也是非常方便和简洁的。

当然，你还可以使用from方法导入模块的全部内容，就像这样：

    from os import *

这种做法在少数情况下是挺方便的，但是这样也会打乱你的命名空间。问题在于，你可能定义了一个与导入模块中名称相同的变量或函数，这时如果你试图使用`os`模块中的同名变量或函数，实际使用的将是你自己定义的内容。因此，你最后会碰到一个相当让人困惑的逻辑错误。标准库中我唯一推荐全盘导入的模块只有Tkinter。

如果你正好要写自己的模块或包，有人会建议你在`__init__.py`文件中导入所有内容，让模块或者包使用起来更方便。我个人更喜欢显示地导入，而非隐式地导入。

你也可以采取折中方案，从一个包中导入多个项：

    from os import path, walk, unlink
    from os import uname, remove

在上述代码中，我们从`os`模块中导入了5个函数。你可能注意到了，我们是通过多次从同一个模块中导入实现的。当然，如果你愿意的话，你也可以使用圆括号一次性导入多个项：

    from os import (path, walk, unlink, uname, 
                    remove, rename)

这是一个有用的技巧，不过你也可以换一种方式：

    from os import path, walk, unlink, uname, \
                    remove, rename

上面的反斜杠是Python中的续行符，告诉解释器这行代码延续至下一行。

## 相对导入

PEP 328介绍了引入相对导入的原因，以及选择了哪种语法。具体来说，是使用句点来决定如何相对导入其他包或模块。这么做的原因是为了避免偶然情况下导入标准库中的模块产生冲突。这里我们以PEP 328中给出的文件夹结构为例，看看相对导入是如何工作的：

    my_package/
        __init__.py
        subpackage1/
            __init__.py
            module_x.py
            module_y.py
        subpackage2/
            __init__.py
            module_z.py
        module_a.py

在本地磁盘上找个地方创建上述文件和文件夹。在顶层的`__init__.py`文件中，键入下面的代码：

    from . import subpackage1
    from . import subpackage2

接下来进入`subpackage1`文件夹，编辑其中的`__init__.py`文件，键入下面的内容：

    from . import module_x
    from . import module_y

现在编辑`module_x.py`文件，键入下面的代码：

    from .module_y import spam as ham
     
    def main():
        ham()

最后编辑`module_y.py`文件，输入以下代码：

    def spam():
        print('spam ' * 3)

打开终端，然后`cd`至`my_package`包所在的文件夹，但不要进入`mu_package`。在这个文件夹下运行Python解释器。我使用的是IPython，因为它的自动补全功能非常方便：

    In [1]: import my_package
     
    In [2]: my_package.subpackage1.module_x
    Out[2]: <module 'my_package.subpackage1.module_x' from 'my_package/subpackage1/module_x.py'>
     
    In [3]: my_package.subpackage1.module_x.main()
    spam spam spam


Relative imports are great for creating code that you turn into packages. If you have created a lot of code that is related, then this is probably the way to go. You will find that relative imports are used in many popular packages on the Python Packages Index (PyPI). Also note that if you need to go more than one level, you can just use additional periods. However, according to PEP 328, you really shouldn’t go above two.

Also note that if you were to add an “if __name__ == ‘__main__’” portion to the module_x.py and tried to run it, you would end up with a rather confusing error. Let’s edit the file and give it a try!

from . module_y import spam as ham
 
def main():
    ham()
 
if __name__ == '__main__':
    # This won't work!
    main()
Now navigate into the subpackage1 folder in your terminal and run the following command:


python module_x.py

You should see the following error on your screen for Python 2:

Traceback (most recent call last):
  File "module_x.py", line 1, in <module>
    from . module_y import spam as ham
ValueError: Attempted relative import in non-package
And if you tried to run it with Python 3, you’d get this:

Traceback (most recent call last):
  File "module_x.py", line 1, in <module>
    from . module_y import spam as ham
SystemError: Parent module '' not loaded, cannot perform relative import
What this means is that module_x.py is a module inside of a package and you’re trying to run it as a script, which is incompatible with relative imports.

If you’d like to use this module in your code, you will have to add it to Python’s import search path. The easiest way to do that is as follows:

import sys
sys.path.append('/path/to/folder/containing/my_package')
import my_package
Note that you want the path to the folder right above my_package, not my_package itself. The reason is that my_package is THE package, so if you append that, you’ll have issues using the package. Let’s move on to optional imports!


## 可选导入

Optional imports are used when you have a preferred module or package that you want to use, but you also want a fallback in case it doesn’t exist. You might use optional imports to support multiple versions of software or for speed ups, for example. Here’s an example from the package github2 that demonstrates how you might use optional imports to support different versions of Python:

try:
    # For Python 3
    from http.client import responses
except ImportError:  # For Python 2.5-2.7
    try:
        from httplib import responses  # NOQA
    except ImportError:  # For Python 2.4
        from BaseHTTPServer import BaseHTTPRequestHandler as _BHRH
        responses = dict([(k, v[0]) for k, v in _BHRH.responses.items()])
The lxml package also makes use of optional imports:

try:
    from urlparse import urljoin
    from urllib2 import urlopen
except ImportError:
    # Python 3
    from urllib.parse import urljoin
    from urllib.request import urlopen
As you can see, it’s used all the time to great effect and is a handy tool to add to your repertoire.

Local imports
A local import is when you import a module into local scope. When you do your imports at the top of your Python script file, that is importing the module into your global scope, which means that any functions or methods that follow will be able to use it. Let’s look at how importing into a local scope works:

import sys  # global scope
 
def square_root(a):
    # This import is into the square_root functions local scope
    import math
    return math.sqrt(a)
 
def my_pow(base_num, power):
    return math.pow(base_num, power)
 
if __name__ == '__main__':
    print(square_root(49))
    print(my_pow(2, 3))
Here we import the sys module into the global scope, but we don’t actually use it. Then in the square_root function we import Python’s math module into the function’s local scope, which means that the math module can only be used inside of the square_root function. IF we try to use it in the my_pow function, we will receive a NameError. Go ahead and try running the code to see this in action!

One of the benefits of using local scope is that you might be using a module that takes a long time to load. If so, it might make sense to put it into a function that is called rarely rather than your module’s global scope. It really depends on what you want to do. Frankly, I’ve almost never used imports into the local scope, mostly because it can be hard to tell what’s going on if the imports are scattered all over the module. Conventionally, all imports should be at the top of the module after all.

Import Pitfalls
There are some very common import pitfalls that programmers fall into. We’ll go over the two most common here:

Circular imports
Shadowed imports
Let’s start by looking at circular imports

Circular imports

Circular imports happen when you create two modules that import each other. Let’s look at an example as that will make it quite clear what I’m referring to. Put the following code into a module called a.py

# a.py
import b
 
def a_test():
    print("in a_test")
    b.b_test()
 
a_test()
Then create another module in the same folder as the one above and name it b.py

import a
 
def b_test():
    print('In test_b"')
    a.a_test()
 
b_test()
If you run either of these modules, you should receive an AttributeError. This happens because both modules are attempting to import each other. Basically what’s happening here is that module a is trying to import module b, but it can’t do that because module b is attempting to import module a which is already being executed. I’ve read about some hacky workarounds but in general you should just refactor your code to prevent this kind of thing from happening

Shadowed imports

Shadow imports (AKA name masking) happen when the programmer creates a module with the same name as a Python module. Let’s create a contrived example! In this case, create a file named math.py and put the following code inside it:

import math
 
def square_root(number):
    return math.sqrt(number)
 
square_root(72)
Now open a terminal and try running this code. When I tried this, I got the following traceback:

Traceback (most recent call last):
  File "math.py", line 1, in <module>
    import math
  File "/Users/michael/Desktop/math.py", line 6, in <module>
    square_root(72)
  File "/Users/michael/Desktop/math.py", line 4, in square_root
    return math.sqrt(number)
AttributeError: module 'math' has no attribute 'sqrt'
What happened here? Well when you run this code, the first place Python looks for a module called “math” is in the currently running script’s folder. In this case, it finds the module we’re running and tries to use that. But our module doesn’t have a function or attribute called sqrt, so an AttributeError is raised.

Wrapping Up
We’ve covered a lot of ground in this article and there’s still a lot more to learn about Python’s importing system. There’s PEP 302 which covers import hooks and allows you to do some really cool things, like import directly from github. There’s also Python’s importlib which is well worth taking a look at. Get out there and start digging in the source code to learn about even more neat tricks. Happy coding!

Related Reading
Import traps
Circular imports in Python 2 and Python 3
Stackoverflow – Python relative imports for the billionth time