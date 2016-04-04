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

Depending on what you’re doing, the above might actually be a good thing. In complex code bases, it’s quite nice to know where something has been imported from. However, if your code is well maintained and modularized properly, importing just a portion from the module can be quite handy and more succinct.

Of course you can also use the from method to import everything, like so:

from os import *
This is handy in rare circumstances, but it can also really mess up your namespace. The problem is that you might define your own function or a top level variable that has the same name as one of the items you imported and if you try to use the one from the os module, it will use yours instead. So you end up with a rather confusing logic error. The Tkinter module is really the only one in the standard library that I’ve seen recommended to be imported in total.

If you happen to write your own module or package, some people recommend importing everything in your __init__.py to make your module or package easier to use. Personally I prefer explicit to implicit, but to each their own.

You can also meet somewhere in the middle by importing multiple items from a package:

from os import path, walk, unlink
from os import uname, remove
In the code above, we import five functions from the os module. You will also note that we can do so by importing from the same module multiple times. If you would rather, you can also use parentheses to import lots of items:

from os import (path, walk, unlink, uname, 
                remove, rename)
This is useful technique, but you can do it another way too:

from os import path, walk, unlink, uname, \
                remove, rename
The backslash you see above is Python’s line continuation character, which tells Python that this line of code continues on the following line.

Relative imports
PEP 328 describes how relative imports came about and what specific syntax was chosen. The idea behind it was to use periods to determine how to relatively import other packages / modules. The reason was to prevent the accidental shadowing of standard library modules. Let’s use the example folder structure that PEP 328 suggests and see if we can get it to work:

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
Create the files and folders above somewhere on your hard drive. In the top-level __init__.py, put the following code in place:

from . import subpackage1
from . import subpackage2
Next navigate down in subpackage1 and edit its __init__.py to have the following contents:

from . import module_x
from . import module_y
Now edit module_x.py such that is has the following code:

from .module_y import spam as ham
 
def main():
    ham()
Finally edit module_y.py to match this:

def spam():
    print('spam ' * 3)
Open a terminal and cd to the folder that has my_package, but not into my_package. Run the Python interpreter in this folder. I’m using iPython below mainly because its auto-completion is so handy:

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

Optional imports
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