> http://www.toptal.com/python/top-10-mistakes-that-python-programmers-make

Common Mistake #1: Misusing expressions as defaults for function arguments
## 常见错误1：错误地将表达式作为函数的默认参数

Python allows you to specify that a function argument is optional by providing a default value for it. While this is a great feature of the language, it can lead to some confusion when the default value is mutable. For example, consider this Python function definition:

在Python中，我们可以通过提供一个默认值，使得某个函数的参数成为可选项。虽然这是Python语言中很好地一个特性，但是当默认值是可变类型时，也会导致一些令人困惑的情况发生。例如，下面这个Python函数的定义就存在这个问题：

	>>> def foo(bar=[]):        # bar是可选参数，如果没有提供则默认为[]，
	...    bar.append("baz")    # 但是稍后我们会看到这行代码会出现问题。
	...    return bar

A common mistake is to think that the optional argument will be set to the specified default expression each time the function is called without supplying a value for the optional argument. In the above code, for example, one might expect that calling foo() repeatedly (i.e., without specifying a bar argument) would always return 'baz', since the assumption would be that each time foo() is called (without a bar argument specified) bar is set to [] (i.e., a new empty list).

Python程序员常犯的一个错误，就是想当然地认为在每次调用函数时，如果没有为可选参数提供值，那么这个可选参数就会被设置为指定的默认值。在上面的代码中，你们可能觉得重复调用foo()函数应该会一直返回'baz'，因为你们默认每次foo()函数调用时（没有指定`bar`变量的值），`bar`变量都被设置为[]（也就是，一个新的空列表）。

But let’s look at what actually happens when you do this:

但是，重复调用这段代码的实际输出结果却是这样的：

	>>> foo()
	["baz"]
	>>> foo()
	["baz", "baz"]
	>>> foo()
	["baz", "baz", "baz"]

Huh? Why did it keep appending the default value of "baz" to an existing list each time foo() was called, rather than creating a new list each time?

很奇怪吧？为什么每次调用`foo()`函数时，都会把"baz"这个默认值添加到已有的列表中，而不是重新创建一个新列表呢？

The more advanced Python programming answer is that the default value for a function argument is only evaluated once, at the time that the function is defined. Thus, the bar argument is initialized to its default (i.e., an empty list) only when foo() is first defined, but then calls to foo() (i.e., without a bar argument specified) will continue to use the same list to which bar was originally initialized.

答案就是，函数参数的默认值在Python中只会被执行一次，也就是定义该函数的时候。因此，只有当`foo()`函数被定义时，`bar`参数才被初始化为其默认值（也就是，一个空列表），但是之后的`foo()`函数调用时，都会继续使用`bar`参数原先初始化的那个列表。

FYI, a common workaround for this is as follows:

当然，一个常见的解决办法就是：

	>>> def foo(bar=None):
	...    if bar is None:		# or if not bar:
	...        bar = []
	...    bar.append("baz")
	...    return bar
	...
	>>> foo()
	["baz"]
	>>> foo()
	["baz"]
	>>> foo()
	["baz"]

## 常见问题2：错误地使用类变量
Common Mistake #2: Using class variables incorrectly

我们来看下面这个例子：
Consider the following example:

  >>> class A(object):
  ...     x = 1
  ...
  >>> class B(A):
  ...     pass
  ...
  >>> class C(A):
  ...     pass
  ...
  >>> print A.x, B.x, C.x
  1 1 1

这个结果很正常。
Makes sense.

  >>> B.x = 2
  >>> print A.x, B.x, C.x
  1 2 1

嗯，这次也没有问题。
Yup, again as expected.

  >>> A.x = 3
  >>> print A.x, B.x, C.x
  3 2 3

到底怎么回事？我们改变的只是`A.x`，为什么`C.x`值却跟着变了？

What the $%#!&?? We only changed A.x. Why did C.x change too?

在Python语言中，类变量是作为字典来处理的，并且遵循Method Resolution Order(MRO)。因此，在上面的代码中，由于类C中并没有`x`这个属性，解释器将会查找它的基类（base class，尽管Python支持多重继承，但是在这个例子中，C的基类只有A）。换句话说，C并不没有独立于A、属于自己的`x`属性。所以，引用`C.x`实际上就是引用`A.x`。这也导致了Python代码中出现的这个问题。

In Python, class variables are internally handled as dictionaries and follow what is often referred to as Method Resolution Order (MRO). So in the above code, since the attribute x is not found in class C, it will be looked up in its base classes (only A in the above example, although Python supports multiple inheritance). In other words, C doesn’t have its own x property, independent of A. Thus, references to C.x are in fact references to A.x. This causes a Python problem unless it’s handled properly. Learn more aout class attributes in Python.

## 常见错误3：错误地制定异常代码块（exception block）的参数
Common Mistake #3: Specifying parameters incorrectly for an exception block

假设你写了下面这段代码：
Suppose you have the following code:

  >>> try:
  ...     l = ["a", "b"]
  ...     int(l[2])
  ... except ValueError, IndexError:  # To catch both exceptions, right?
  ...     pass
  ...
  Traceback (most recent call last):
    File "<stdin>", line 3, in <module>
  IndexError: list index out of range

这段代码的问题在于，`except`语句并不支持以这种方式指定异常。而在Python 2.x中，需要使用`e`将异常绑定值可选的第二个参数中，才能进一步查看异常的情况。因此，在上述代码中，`except`语句并没有捕获IndexError异常；相反出现的异常被绑定到了一个名为`IndexError`的参数中。

The problem here is that the except statement does not take a list of exceptions specified in this manner. Rather, In Python 2.x, the syntax except Exception, e is used to bind the exception to the optional second parameter specified (in this case e), in order to make it available for further inspection. As a result, in the above code, the IndexError exception is not being caught by the except statement; rather, the exception instead ends up being bound to a parameter named IndexError.

在`except`语句中正确捕获多个异常的正确方法，则是将第一个参数指定为元组，然后在元组中写下希望捕获的异常类型。另外，为了提高可移植性，请使用`as`关键词，Python 2和Python 3均支持这种用法。

The proper way to catch multiple exceptions in an except statement is to specify the first parameter as a tuple containing all exceptions to be caught. Also, for maximum portability, use the as keyword, since that syntax is supported by both Python 2 and Python 3:

  >>> try:
  ...     l = ["a", "b"]
  ...     int(l[2])
  ... except (ValueError, IndexError) as e:  
  ...     pass
  ...
  >>>

## 常见错误4：错误理解Python中的作用域规则
Common Mistake #4: Misunderstanding Python scope rules

Python中作用域的生效顺序基于所谓的`LEGD`原则，也就是“本地、外围、全局、内建”（Local，Enclosing，Global，Builtin）。看上去是不是很简单？不过，事实上这个原则的生效方式还是有着一些特殊之处，说到这点，我们就不得不提下面这个常见的Python难题。假设有下面这段代码：

Python scope resolution is based on what is known as the LEGB rule, which is shorthand for Local, Enclosing, Global, Built-in. Seems straightforward enough, right? Well, actually, there are some subtleties to the way this works in Python, which brings us to the common more advanced Python programming problem below. Consider the following:

  >>> x = 10
  >>> def foo():
  ...     x += 1
  ...     print x
  ...
  >>> foo()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 2, in foo
  UnboundLocalError: local variable 'x' referenced before assignment

出了什么问题？
What’s the problem?

上述错误的出现，原因在于当你在某个作用域内为变量赋值时，该变量被Python解释器自动认为是该作用域的本地变量，并会取代任何外部作用域中相同名称的变量。

The above error occurs because, when you make an assignment to a variable in a scope, that variable is automatically considered by Python to be local to that scope and shadows any similarly named variable in any outer scope.

正是因为这样，才会出现一开始好好的代码，在某个函数内部添加了一个赋值语句之后却出现了`UnboundLocalError`，难怪会让许多人吃惊。

Many are thereby surprised to get an UnboundLocalError in previously working code when it is modified by adding an assignment statement somewhere in the body of a function. (You can read more about this here.)

在使用列表时，Python程序员尤其容易陷入这个圈套。

It is particularly common for this to trip up developers when using lists. 

请看下面这个代码示例：
Consider the following example:

  >>> lst = [1, 2, 3]
  >>> def foo1():
  ...     lst.append(5)   # This works ok...
  ...
  >>> foo1()
  >>> lst
  [1, 2, 3, 5]

  >>> lst = [1, 2, 3]
  >>> def foo2():
  ...     lst += [5]      # ... but this bombs!
  ...
  >>> foo2()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 2, in foo
  UnboundLocalError: local variable 'lst' referenced before assignment

呃？为什么函数`foo1`运行正常，`foo2`却出现了错误？

Huh? Why did foo2 bomb while foo1 ran fine?

答案与上一个示例相同，但是却更加难捉摸清楚。`foo1`函数并没有为`lst`变量进行赋值，但是`foo2`却有赋值。我们知道，`lst += [5]`只是`lst = lst + [5]`的简写，从中我们就可以看出，`foo2`函数在尝试为`lst`赋值（因此，被Python解释器认为是函数本地作用域的变量）。但是，我们希望为`lst`赋的值却又是基于`lst`变量本身（这时，也被认为是函数本地作用域内的变量），也就是说该变量还没有被定义。这才出现了错误。

The answer is the same as in the prior example problem, but is admittedly more subtle. foo1 is not making an assignment to lst, whereas foo2 is. Remembering that lst += [5] is really just shorthand for lst = lst + [5], we see that we are attempting to assign a value to lst (therefore presumed by Python to be in the local scope). However, the value we are looking to assign to lst is based on lst itself (again, now presumed to be in the local scope), which has not yet been defined. Boom.

## 常见错误5：在遍历列表时更改列表
Common Mistake #5: Modifying a list while iterating over it

下面这段代码的问题应该算是十分明显：
The problem with the following code should be fairly obvious:

  >>> odd = lambda x : bool(x % 2)
  >>> numbers = [n for n in range(10)]
  >>> for i in range(len(numbers)):
  ...     if odd(numbers[i]):
  ...         del numbers[i]  # BAD: Deleting item from a list while iterating over it
  ...
  Traceback (most recent call last):
    	  File "<stdin>", line 2, in <module>
  IndexError: list index out of range

Deleting an item from a list or array while iterating over it is a Python problem that is well known to any experienced software developer. But while the example above may be fairly obvious, even advanced developers can be unintentionally bitten by this in code that is much more complex.

Fortunately, Python incorporates a number of elegant programming paradigms which, when used properly, can result in significantly simplified and streamlined code. A side benefit of this is that simpler code is less likely to be bitten by the accidental-deletion-of-a-list-item-while-iterating-over-it bug. One such paradigm is that of list comprehensions. Moreover, list comprehensions are particularly useful for avoiding this specific problem, as shown by this alternate implementation of the above code which works perfectly:

>>> odd = lambda x : bool(x % 2)
>>> numbers = [n for n in range(10)]
>>> numbers[:] = [n for n in numbers if not odd(n)]  # ahh, the beauty of it all
>>> numbers
[0, 2, 4, 6, 8]

Common Mistake #6: Confusing how Python binds variables in closures

Considering the following example:

>>> def create_multipliers():
...     return [lambda x : i * x for i in range(5)]
>>> for multiplier in create_multipliers():
...     print multiplier(2)
...
You might expect the following output:

0
2
4
6
8

But you actually get:

8
8
8
8
8
Surprise!

This happens due to Python’s late binding behavior which says that the values of variables used in closures are looked up at the time the inner function is called. So in the above code, whenever any of the returned functions are called, the value of i is looked up in the surrounding scope at the time it is called (and by then, the loop has completed, so i has already been assigned its final value of 4).

The solution to this common Python problem is a bit of a hack:

>>> def create_multipliers():
...     return [lambda x, i=i : i * x for i in range(5)]
...
>>> for multiplier in create_multipliers():
...     print multiplier(2)
...
0
2
4
6
8
Voilà! We are taking advantage of default arguments here to generate anonymous functions in order to achieve the desired behavior. Some would call this elegant. Some would call it subtle. Some hate it. But if you’re a Python developer, it’s important to understand in any case.

Common Mistake #7: Creating circular module dependencies

Let’s say you have two files, a.py and b.py, each of which imports the other, as follows:

In a.py:

import b

def f():
    return b.x
	
print f()
And in b.py:

import a

x = 1

def g():
    print a.f()
First, let’s try importing a.py:

>>> import a
1
Worked just fine. Perhaps that surprises you. After all, we do have a circular import here which presumably should be a problem, shouldn’t it?

The answer is that the mere presence of a circular import is not in and of itself a problem in Python. If a module has already been imported, Python is smart enough not to try to re-import it. However, depending on the point at which each module is attempting to access functions or variables defined in the other, you may indeed run into problems.

So returning to our example, when we imported a.py, it had no problem importing b.py, since b.py does not require anything from a.py to be defined at the time it is imported. The only reference in b.py to a is the call to a.f(). But that call is in g() and nothing in a.py or b.py invokes g(). So life is good.

But what happens if we attempt to import b.py (without having previously imported a.py, that is):

>>> import b
Traceback (most recent call last):
  	  File "<stdin>", line 1, in <module>
  	  File "b.py", line 1, in <module>
    import a
  	  File "a.py", line 6, in <module>
	print f()
  	  File "a.py", line 4, in f
	return b.x
AttributeError: 'module' object has no attribute 'x'
Uh-oh. That’s not good! The problem here is that, in the process of importing b.py, it attempts to import a.py, which in turn calls f(), which attempts to access b.x. But b.x has not yet been defined. Hence the AttributeError exception.

At least one solution to this is quite trivial. Simply modify b.py to import a.py within g():

x = 1

def g():
    import a	# This will be evaluated only when g() is called
    print a.f()
No when we import it, everything is fine:

>>> import b
>>> b.g()
1	# Printed a first time since module 'a' calls 'print f()' at the end
1	# Printed a second time, this one is our call to 'g'
Common Mistake #8: Name clashing with Python Standard Library modules

One of the beauties of Python is the wealth of library modules that it comes with “out of the box”. But as a result, if you’re not consciously avoiding it, it’s not that difficult to run into a name clash between the name of one of your modules and a module with the same name in the standard library that ships with Python (for example, you might have a module named email.py in your code, which would be in conflict with the standard library module of the same name).

This can lead to gnarly problems, such as importing another library which in turns tries to import the Python Standard Library version of a module but, since you have a module with the same name, the other package mistakenly imports your version instead of the one within the Python Standard Library. This is where bad Python errors happen.

Care should therefore be exercised to avoid using the same names as those in the Python Standard Library modules. It’s way easier for you to change the name of a module within your package than it is to file a Python Enhancement Proposal (PEP) to request a name change upstream and to try and get that approved.

Common Mistake #9: Failing to address differences between Python 2 and Python 3

Consider the following file foo.py:

import sys

def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)

def bad():
    e = None
    try:
        bar(int(sys.argv[1]))
    except KeyError as e:
        print('key error')
    except ValueError as e:
        print('value error')
    print(e)

bad()
On Python 2, this runs fine:

$ python foo.py 1
key error
1
$ python foo.py 2
value error
2
But now let’s give it a whirl on Python 3:

$ python3 foo.py 1
key error
Traceback (most recent call last):
  File "foo.py", line 19, in <module>
    bad()
  File "foo.py", line 17, in bad
    print(e)
UnboundLocalError: local variable 'e' referenced before assignment
What has just happened here? The “problem” is that, in Python 3, the exception object is not accessible beyond the scope of the except block. (The reason for this is that, otherwise, it would keep a reference cycle with the stack frame in memory until the garbage collector runs and purges the references from memory. More technical detail about this is available here).

One way to avoid this issue is to maintain a reference to the exception object outside the scope of the except block so that it remains accessible. Here’s a version of the previous example that uses this technique, thereby yielding code that is both Python 2 and Python 3 friendly:

import sys

def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)

def good():
    exception = None
    try:
        bar(int(sys.argv[1]))
    except KeyError as e:
        exception = e
        print('key error')
    except ValueError as e:
        exception = e
        print('value error')
    print(exception)

good()
Running this on Py3k:

$ python3 foo.py 1
key error
1
$ python3 foo.py 2
value error
2
Yippee!

(Incidentally, our Python Hiring Guide discusses a number of other important differences to be aware of when migrating code from Python 2 to Python 3.)

Common Mistake #10: Misusing the __del__ method

Let’s say you had this in a file called mod.py:

import foo

class Bar(object):
   	    ...
    def __del__(self):
        foo.cleanup(self.myhandle)
And you then tried to do this from another_mod.py:

import mod
mybar = mod.Bar()
You’d get an ugly AttributeError exception.

Why? Because, as reported here, when the interpreter shuts down, the module’s global variables are all set to None. As a result, in the above example, at the point that __del__ is invoked, the name foo has already been set to None.

A solution to this somewhat more advanced Python programming problem would be to use atexit.register() instead. That way, when your program is finished executing (when exiting normally, that is), your registered handlers are kicked off before the interpreter is shut down.

With that understanding, a fix for the above mod.py code might then look something like this:

import foo
import atexit

def cleanup(handle):
    foo.cleanup(handle)


class Bar(object):
    def __init__(self):
        ...
        atexit.register(cleanup, self.myhandle)
This implementation provides a clean and reliable way of calling any needed cleanup functionality upon normal program termination. Obviously, it’s up to foo.cleanup to decide what to do with the object bound to the name self.myhandle, but you get the idea.

Wrap-up

Python is a powerful and flexible language with many mechanisms and paradigms that can greatly improve productivity. As with any software tool or language, though, having a limited understanding or appreciation of its capabilities can sometimes be more of an impediment than a benefit, leaving one in the proverbial state of “knowing enough to be dangerous”.

Familiarizing oneself with the key nuances of Python, such as (but by no means limited to) the moderately advanced programming problems raised in this article, will help optimize use of the language while avoiding some of its more common errors.