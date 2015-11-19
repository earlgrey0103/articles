# Python面试必须要看的15个问题

> 本文由EarlGrey@编程派独家编译，转载请务必注明出处。

> 原文：[Sheena@codementor](https://www.codementor.io/python/tutorial/essential-python-interview-questions)
> 译文：[编程派](http://codingpy.com/article/essential-python-interview-questions)

Introduction
## 引言

Looking for a Python job? Chances are you will need to prove that you know how to work with Python. Here are a couple of questions that cover a wide base of skills associated with Python. Focus is placed on the language itself, and not any particular package or framework. Each question will be linked to a suitable tutorial if there is one. Some questions will wrap up multiple topics.

想找一份Python开发工作吗？那你很可能得证明自己知道如何使用Python。下面这些问题涉及了与Python相关的许多技能，问题的关注点主要是语言本身，不是某个特定的包或模块。每一个问题都可以扩充为一个教程，如果可能的话。某些问题甚至会涉及多个领域。

I haven't actually been given an interview test quite as hard as this one, if you can get to the answers comfortably then go get yourself a job.

我之前还没有出过像这些题目一样难的面试测试题，如果你能轻松地回答出来的话，赶紧去找份工作吧！

Question 1
## 问题1


What is Python really? You can (and are encouraged) make comparisons to other technologies in your answer

到底什么是Python？你可以在回答中与其他技术进行对比（（也鼓励这样做））。

Answer
答案

Here are a few key points: - Python is an interpreted language. That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.

下面是一些关键点：

- Python是一种解释型语言。这就是说，与C语言和C的衍生语言不通，Python代码在运行之前不需要编译。其他解释型语言还包括PHP和Ruby。

Python is dynamically typed, this means that you don't need to state the types of variables when you declare them or anything like that. You can do things like x=111 and then x="I'm a string" without error

- Python是动态类型语言，指的是你在声明变量时，不需要说明变量的类型。你可以直接编写类似`x=111`和`x="I'm a string"`这样的代码，程序不会报错。

Python is well suited to object orientated programming in that it allows the definition of classes along with composition and inheritance. Python does not have access specifiers (like C++'s public, private), the justification for this point is given as "we are all adults here"

- Python非常适合面向对象的编程（OOP），因为它支持通过组合（composition）与继承（inheritance）的方式定义类（class）。Python中没有访问说明符（access specifier，类似C++中的`public`和`private`），这么设计的依据是“大家都是成年人了”。

in Python, functions are first-class objects. This means that they can be assigned to variables, returned from other functions and passed into functions. Classes are also first class objects

- 在Python语言中，函数是第一类对象（first-class objects）。这指的是它们可以被指定给变量，其他函数既能返回函数类型，也可以接受函数作为输入。类（class）也是第一类对象。

Writing Python code is quick but running it is often slower than compiled languages. Fortunately， Python allows the inclusion of C based extensions so bottlenecks can be optimised away and often are. The numpy package is a good example of this, it's really quite quick because a lot of the number crunching it does isn't actually done by Python

- Python代码编写快，但是运行速度比编译语言通常要慢。好在Python允许加入基于C语言编写的扩展，因此我们能够优化代码，消除瓶颈，这点通常是可以实现的。`numpy`就是一个很好地例子，它的运行速度真的非常快，因为很多算术运算其实并不是通过Python实现的。

Python finds use in many spheres - web applications, automation, scientific modelling, big data applications and many more. It's also often used as "glue" code to get other languages and components to play nice.

- Python用途非常广泛——网络应用，自动化，科学建模，大数据应用，等等。它也常被用作“胶水语言”，帮助其他语言和组件改善运行状况。

Python makes difficult things easy so programmers can focus on overriding algorithms and structures rather than nitty-gritty low level details.

- Python让困难的事情变得容易，因此程序员可以专注于算法和数据结构的设计，而不用处理底层的细节。

Why this matters:

为什么提这个问题：

If you are applying for a python position, you should know what it is and why it is so gosh-darn cool. And why it isn't o.O

如果你应聘的是一个Python开发岗位，你就应该知道这是门什么样的语言，以及它为什么这么酷。以及它哪里不好。

Question 2

## 问题2

Fill in the missing code:

补充缺失的代码

    :::python
    def print_directory_contents(sPath):
        """
        这个函数接受文件夹的名称作为输入参数，
        返回该文件夹中文件的路径，
        以及其包含文件夹中文件的路径。

        """
        完善代码

Answer

答案

    :::python
    def print_directory_contents(sPath):
        import os                                       
        for sChild in os.listdir(sPath):                
            sChildPath = os.path.join(sPath,sChild)
            if os.path.isdir(sChildPath):
                print_directory_contents(sChildPath)
            else:
                print sChildPath

Pay special attention

特别要注意以下几点：

- 命名规范要统一。如果样本代码中能够看出命名规范，遵循其已有的规范。
- 递归函数需要递归并终止。确保你明白其中的原理，否则你将面临无休无止的调用栈（callstack）。
- 我们使用`os`模块与操作系统进行交互，同时做到交互方式是可以跨平台的。你可以把代码写成`sChildPath = sPath + '/' + sChild`，但是这个在Windows系统上会出错。
- 熟悉基础模块是非常有价值的，但是别想破脑袋都背下来，记住Google是你工作中的良师益友。
- 如果你不明白代码的预期功能，就大胆提问。
- 坚持KISS原则！保持简单，不过脑子就能懂！

be consistent with your naming conventions. If there is a naming convention evident in any sample code, stick to it
recursive functions need to recurse and terminate. Make sure you understand how this happens so that you avoid bottomless callstacks
we use the os module for interacting with the operating system in a way that is cross platform. You could say sChildPath = sPath + '/' + sChild but that wouldn't work on windows
familiarity with base packages is really worthwhile, but don't break your head trying to memorize everything, google is your friend in the workplace
ask questions if you don't understand what the code is supposed to do
KISS! Keep it Simple, Stupid!

Why this matters:
为什么提这个问题：

displays knowledge of basic operating system interaction stuff
recursion is hella useful
- 说明面试者对与操作系统交互的基础知识
- 递归真是太好用啦

Question 3
## 问题3

Looking at the below code, write down the final values of A0, A1, ...An.

阅读下面的代码，写出A0，A1至An的最终值。

    A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
    A1 = range(10)
    A2 = [i for i in A1 if i in A0]
    A3 = [A0[s] for s in A0]
    A4 = [i for i in A1 if i in A3]
    A5 = {i:i*i for i in A1}
    A6 = [[i,i*i] for i in A1]

Answer
答案

    A0 = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
    A1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    A2 = []
    A3 = [1, 3, 2, 5, 4]
    A4 = [1, 2, 3, 4, 5]
    A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

Why this is important

为什么提这个问题：

- 列表解析（list comprehension）十分节约时间，对很多人来说也是一个大的学习障碍。
- 如果你读懂了这些代码，就很可能可以写下正确地值。
- 其中部分代码故意写的怪怪得。因为你共事的人之中也会有怪人。

List comprehension is a wonderful time saver and a big stumbling block for a lot of people
if you can read them you can probably write them down
some of this code was made to be deliberately weird. You may need to work with some weird people


Question 4
## 问题4

Python and multi-threading. Is it a good idea? List some ways to get some Python code to run in a parallel way.

Python和多线程（multi-threading）。这是个好主意码？列表一些让Python代码以并行方式运行的方法。

Answer
答案

Python doesn't allow multi-threading in the truest sense of the word. It has a multi-threading package but if you want to multi-thread to speed your code up, then it's really not a good idea to use it. Python has a construct called the Global Interpreter Lock (GIL). The GIL makes sure that only one of your 'threads' can execute at any one time. A thread acquires the GIL, does a little work, then passes the GIL onto the next thread. This happens very quickly so to the human eye it may seem like your threads are executing in parallel, but they are really just taking turns. All this GIL passing adds overhead to execution. This means that if you want to make your code run faster then using the threading package is really not a good idea.

Python并不支持真正意义上的多线程。Python中提供了[多线程包](https://docs.python.org/2/library/threading.html)，但是如果你想通过多线程提高代码的速度，使用多线程包并不是个好主意。Python中有一个被称为Global Interpreter Lock（GIL）的结构体，它会确保任何时候你的多个线程中，只有一个被执行。线程的执行速度非常之快，程序员会误以为你的线程是并行执行的，但是实际上都是轮流执行。经过GIL这一道关卡处理，会增加执行的开销。这意味着，如果你想提高代码的运行速度，使用`threading`包并不是一个很好的方法。

There are reasons to use Python's threading package. If you want to run some things simultaneously, and efficiency is not a concern, then it's totally fine and convenient. But in most cases, this is not the case. In most cases you'll want to outsource the multi-threading to the operating system (by doing multi-processing), some external application that calls your Python code (eg, Spark or Hadoop), or some code that your Python code calls (eg: you could have your Python code call a C function that does the expensive multi-threaded stuff).

不过还是有很多理由促使我们使用`threading`包得。如果你想同时执行一些任务，而且不考虑效率问题，那么使用这个包是完全没问题的，而且也很方便。但是大部分情况下，并不是这么一回事，你会希望把多线程的部分外包给操作系统完成（通过开启多个进程），或者是某些调用你的Python代码的外部程序（例如Spark或Hadoop），又或者是你的Python代码调用的其他代码（例如，你可以在Python中调用C函数，用于处理开销较大的多线程工作）。

Why this is important

为什么提这个问题

Because the GIL is an A-hole. Lots of people spend a lot of time trying to find bottlenecks in their fancy Python multi-threaded code before they learn what the GIL is.

因为GIL就是个混账东西（A-hole）。很多人花费大量的时间，试图寻找自己多线程代码中的瓶颈，直到他们明白GIL的存在。

Question 5

## 问题5

How do you keep track of different versions of your code?

你如何管理不同版本的代码？

Answer:

答案：

Version control! At this point, you should act excited and tell them how you even use Git (or whatever is your favorite) to keep track of correspondence with Granny. Git is my preferred version control system, but there are others, for example subversion.

版本管理！被问到这个问题的时候，你应该要表现的很兴奋，甚至告诉他们你是如何使用Git（或是其他你最喜欢的工具）追踪自己和奶奶的书信往来。我偏向于使用Git作为版本控制系统（VCS），但还有其他的选择，比如subversion（SVN）。

Why this is important:

为什么提这个问题：

Because code without version control is like coffee without a cup. Sometimes we need to write once-off throw away scripts and that's ok, but if you are dealing with any significant amount of code, a version control system will be a benefit. Version Control helps with keeping track of who made what change to the code base; finding out when bugs were introduced to the code; keeping track of versions and releases of your software; distributing the source code amongst team members; deployment and certain automations. It allows you to roll your code back to before you broke it which is great on its own. Lots of stuff. It's just great.

因为没有版本控制的代码，就像没有杯子的咖啡。有时候我们需要写一些一次性的、可以随手扔掉的脚本，这种情况下不作版本控制没关系。但是如果你面对的是大量的代码，使用版本控制系统是有利的。版本控制能够帮你追踪谁对代码库做了什么操作；发现新引入了什么bug；管理你的软件的不同版本和发行版；在团队成员中分享源代码；部署及其他自动化处理。它能让你退回出现问题之前的版本，单凭这点就特别棒了。还有其他的好功能。怎么一个棒字了得！

Question 6

## 问题6

What does this code output:
下面代码会输出什么：


    :::python    
    def f(x,l=[]):
        for i in range(x):
            l.append(i*i)
        print l 
    
    f(2)
    f(3,[3,2,1])
    f(3)

Answer
答案：

    [0, 1]
    [3, 2, 1, 0, 1, 4]
    [0, 1, 0, 1, 4]

Hu?

呃？

The first function call should be fairly obvious, the loop appends 0 and then 1 to the empty list, l. l is a name for a variable that points to a list stored in memory. The second call starts off by creating a new list in a new block of memory. l then refers to this new list. It then appends 0, 1 and 4 to this new list. So that's great. The third function call is the weird one. It uses the original list stored in the original memory block. That is why it starts off with 0 and 1.

第一个函数调用十分明显，for循环先后将0和1添加至了空列表`l`中。`l`是变量的名字，指向内存中存储的一个列表。第二个函数调用在一块新的内存中创建了新的列表。`l`这时指向了新生成的列表。之后再往新列表中添加0、1、2和4。很棒吧。第三个函数调用的结果就有些奇怪了。它使用了之前内存地址中存储的旧列表。这就是为什么它的前两个元素是0和1了。

Try this out if you don't understand:

不明白的话就试着运行下面的代码吧：

    l_mem = []
    
    l = l_mem           # the first call
    for i in range(2):
        l.append(i*i)
    
    print l             # [0, 1]
    
    l = [3,2,1]         # the second call
    for i in range(3):
        l.append(i*i)
    
    print l             # [3, 2, 1, 0, 1, 4]
    
    l = l_mem           # the third call
    for i in range(3):
        l.append(i*i)
    
    print l             # [0, 1, 0, 1, 4]


Question 7
## 问题7

What is monkey patching and is it ever a good idea?

“猴子补丁”（monkey patching）指的是什么？这种做法好吗？

Answer
答案：

Monkey patching is changing the behaviour of a function or object after it has already been defined. 
“猴子补丁”就是指，在函数或对象已经定义之后，再去改变它们的行为。

For example:

举个例子：

    import datetime
    datetime.datetime.now = lambda: datetime.datetime(2012, 12, 12)


Most of the time it's a pretty terrible idea - it is usually best if things act in a well-defined way. One reason to monkey patch would be in testing. The mock package is very useful to this end.

大部分情况下，这是中很不好的做法 - 因为函数在代码库中的行为最好是都保持一致。打“猴子补丁”的原因可能是为了测试。`mock`包对实现这个目的很有帮助。

Why does this matter?

为什么提这个问题？

It shows that you understand a bit about methodologies in unit testing. Your mention of monkey avoidance will show that you aren't one of those coders who favor fancy code over maintainable code (they are out there, and they suck to work with). Remember the principle of KISS? And it shows that you know a little bit about how Python works on a lower level, how functions are actually stored and called and suchlike.

答对这个问题说明你对单元测试的方法有一定了解。你如果提到要避免“猴子补丁”，可以说明你不是那种喜欢花里胡哨代码的程序员（公司里就有这种人，跟他们共事真是糟糕透了），而是更注重可维护性。还记得KISS原则码？答对这个问题还说明你明白一些Python底层运作的方式，函数实际是如何存储、调用等等。

PS: it's really worth reading a little bit about mock if you haven't yet. It's pretty useful.

Question 8

What does this stuff mean: *args, **kwargs? And why would we use it?

Answer

Use *args when we aren't sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. **kwargs is used when we dont know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use *bob and **billy but that would not be wise.

Here is a little illustration:

def f(*args,**kwargs): print args, kwargs

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}

f()
f(1,2,3)                    # (1, 2, 3) {}
f(1,2,3,"groovy")           # (1, 2, 3, 'groovy') {}
f(a=1,b=2,c=3)              # () {'a': 1, 'c': 3, 'b': 2}
f(a=1,b=2,c=3,zzz="hi")     # () {'a': 1, 'c': 3, 'b': 2, 'zzz': 'hi'}
f(1,2,3,a=1,b=2,c=3)        # (1, 2, 3) {'a': 1, 'c': 3, 'b': 2}

f(*l,**d)                   # (1, 2, 3) {'a': 7, 'c': 9, 'b': 8}
f(*t,**d)                   # (4, 5, 6) {'a': 7, 'c': 9, 'b': 8}
f(1,2,*t)                   # (1, 2, 4, 5, 6) {}
f(q="winning",**d)          # () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
f(1,2,*t,q="winning",**d)   # (1, 2, 4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}

def f2(arg1,arg2,*args,**kwargs): print arg1,arg2, args, kwargs

f2(1,2,3)                       # 1 2 (3,) {}
f2(1,2,3,"groovy")              # 1 2 (3, 'groovy') {}
f2(arg1=1,arg2=2,c=3)           # 1 2 () {'c': 3}
f2(arg1=1,arg2=2,c=3,zzz="hi")  # 1 2 () {'c': 3, 'zzz': 'hi'}
f2(1,2,3,a=1,b=2,c=3)           # 1 2 (3,) {'a': 1, 'c': 3, 'b': 2}

f2(*l,**d)                   # 1 2 (3,) {'a': 7, 'c': 9, 'b': 8}
f2(*t,**d)                   # 4 5 (6,) {'a': 7, 'c': 9, 'b': 8}
f2(1,2,*t)                   # 1 2 (4, 5, 6) {}
f2(1,1,q="winning",**d)      # 1 1 () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
f2(1,2,*t,q="winning",**d)   # 1 2 (4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8} 
Why do we care?

Sometimes we will need to pass an unknown number of arguments or keyword arguments into a function. Sometimes we will want to store arguments or keyword arguments for later use. Sometimes it's just a time saver.

Question 9

What do these mean to you: @classmethod, @staticmethod, @property?

Answer Background knowledge

These are decorators. A decorator is a special kind of function that either takes a function and returns a function, or takes a class and returns a class. The @ symbol is just syntactic sugar that allows you to decorate something in a way that's easy to read.

@my_decorator
def my_func(stuff):
    do_things
Is equivalent to

def my_func(stuff):
    do_things

my_func = my_decorator(my_func)
You can find a tutorial on how decorators in general work here.

Actual Answer

The decorators @classmethod, @staticmethod and @property are used on functions defined within classes. Here is how they behave:

class MyClass(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"
    def normal_method(*args,**kwargs):
        print "calling normal_method({0},{1})".format(args,kwargs)
    @classmethod
    def class_method(*args,**kwargs):
        print "calling class_method({0},{1})".format(args,kwargs)
    @staticmethod
    def static_method(*args,**kwargs):
        print "calling static_method({0},{1})".format(args,kwargs)
    @property
    def some_property(self,*args,**kwargs):
        print "calling some_property getter({0},{1},{2})".format(self,args,kwargs)
        return self._some_property
    @some_property.setter
    def some_property(self,*args,**kwargs):
        print "calling some_property setter({0},{1},{2})".format(self,args,kwargs)
        self._some_property = args[0]
    @property
    def some_other_property(self,*args,**kwargs):
        print "calling some_other_property getter({0},{1},{2})".format(self,args,kwargs)
        return self._some_other_property

o = MyClass()
# undecorated methods work like normal, they get the current instance (self) as the first argument

o.normal_method 
# <bound method MyClass.normal_method of <__main__.MyClass instance at 0x7fdd2537ea28>>

o.normal_method() 
# normal_method((<__main__.MyClass instance at 0x7fdd2537ea28>,),{})

o.normal_method(1,2,x=3,y=4) 
# normal_method((<__main__.MyClass instance at 0x7fdd2537ea28>, 1, 2),{'y': 4, 'x': 3})

# class methods always get the class as the first argument

o.class_method
# <bound method classobj.class_method of <class __main__.MyClass at 0x7fdd2536a390>>

o.class_method()
# class_method((<class __main__.MyClass at 0x7fdd2536a390>,),{})

o.class_method(1,2,x=3,y=4)
# class_method((<class __main__.MyClass at 0x7fdd2536a390>, 1, 2),{'y': 4, 'x': 3})

# static methods have no arguments except the ones you pass in when you call them

o.static_method
# <function static_method at 0x7fdd25375848>

o.static_method()
# static_method((),{})

o.static_method(1,2,x=3,y=4)
# static_method((1, 2),{'y': 4, 'x': 3})

# properties are a way of implementing getters and setters. It's an error to explicitly call them
# "read only" attributes can be specified by creating a getter without a setter (as in some_other_property)

o.some_property
# calling some_property getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# 'properties are nice'

o.some_property()
# calling some_property getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object is not callable

o.some_other_property
# calling some_other_property getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# 'VERY nice'

# o.some_other_property()
# calling some_other_property getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object is not callable

o.some_property = "groovy"
# calling some_property setter(<__main__.MyClass object at 0x7fb2b7077890>,('groovy',),{})

o.some_property
# calling some_property getter(<__main__.MyClass object at 0x7fb2b7077890>,(),{})
# 'groovy'

o.some_other_property = "very groovy"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute

o.some_other_property
# calling some_other_property getter(<__main__.MyClass object at 0x7fb2b7077890>,(),{})
# 'VERY nice'
Question 10

Consider the following code, what will it output?

class A(object):
    def go(self):
        print "go A go!"
    def stop(self):
        print "stop A stop!"
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print "go B go!"

class C(A):
    def go(self):
        super(C, self).go()
        print "go C go!"
    def stop(self):
        super(C, self).stop()
        print "stop C stop!"

class D(B,C):
    def go(self):
        super(D, self).go()
        print "go D go!"
    def stop(self):
        super(D, self).stop()
        print "stop D stop!"
    def pause(self):
        print "wait D wait!"

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards

a.go()
b.go()
c.go()
d.go()
e.go()

a.stop()
b.stop()
c.stop()
d.stop()
e.stop()

a.pause()
b.pause()
c.pause()
d.pause()
e.pause()
Answer

The output is specified in the comments in the segment below:

a.go()
# go A go!

b.go()
# go A go!
# go B go!

c.go()
# go A go!
# go C go!

d.go()
# go A go!
# go C go!
# go B go!
# go D go!

e.go()
# go A go!
# go C go!
# go B go!

a.stop()
# stop A stop!

b.stop()
# stop A stop!

c.stop()
# stop A stop!
# stop C stop!

d.stop()
# stop A stop!
# stop C stop!
# stop D stop!

e.stop()
# stop A stop!

a.pause()
# ... Exception: Not Implemented

b.pause()
# ... Exception: Not Implemented

c.pause()
# ... Exception: Not Implemented

d.pause()
# wait D wait!

e.pause()
# ...Exception: Not Implemented
Why do we care?

Because OO programming is really, really important. Really. Answering this question shows your understanding of inheritance and the use of Python's super function.

Question 11

Consider the following code, what will it output?

class Node(object):
    def __init__(self,sName):
        self._lChildren = []
        self.sName = sName
    def __repr__(self):
        return "<Node '{}'>".format(self.sName)
    def append(self,*args,**kwargs):
        self._lChildren.append(*args,**kwargs)
    def print_all_1(self):
        print self
        for oChild in self._lChildren:
            oChild.print_all_1()
    def print_all_2(self):
        def gen(o):
            lAll = [o,]
            while lAll:
                oNext = lAll.pop(0)
                lAll.extend(oNext._lChildren)
                yield oNext
        for oNode in gen(self):
            print oNode

oRoot = Node("root")
oChild1 = Node("child1")
oChild2 = Node("child2")
oChild3 = Node("child3")
oChild4 = Node("child4")
oChild5 = Node("child5")
oChild6 = Node("child6")
oChild7 = Node("child7")
oChild8 = Node("child8")
oChild9 = Node("child9")
oChild10 = Node("child10")

oRoot.append(oChild1)
oRoot.append(oChild2)
oRoot.append(oChild3)
oChild1.append(oChild4)
oChild1.append(oChild5)
oChild2.append(oChild6)
oChild4.append(oChild7)
oChild3.append(oChild8)
oChild3.append(oChild9)
oChild6.append(oChild10)

# specify output from here onwards

oRoot.print_all_1()
oRoot.print_all_2()
Answer

oRoot.print_all_1() prints:

<Node 'root'>
<Node 'child1'>
<Node 'child4'>
<Node 'child7'>
<Node 'child5'>
<Node 'child2'>
<Node 'child6'>
<Node 'child10'>
<Node 'child3'>
<Node 'child8'>
<Node 'child9'>
oRoot.print_all_2() prints:

<Node 'root'>
<Node 'child1'>
<Node 'child2'>
<Node 'child3'>
<Node 'child4'>
<Node 'child5'>
<Node 'child6'>
<Node 'child8'>
<Node 'child9'>
<Node 'child7'>
<Node 'child10'>
Why do we care?

Because composition and object construction is what objects are all about. Objects are composed of stuff and they need to be initialised somehow. This also ties up some stuff about recursion and use of generators.

Generators are great. You could have achieved similar functionality to print_all_2 by just constructing a big long list and then printing it's contents. One of the nice things about generators is that they don't need to take up much space in memory.

It is also worth pointing out that print_all_1 traverses the tree in a depth-first manner, while print_all_2 is width-first. Sometimes one kind of traversal is more appropriate than the other. But that depends very much on your application.

Question 12

Describe Python's garbage collection mechanism in brief.

Answer

A lot can be said here. There are a few main points that you should mention:

Python maintains a count of the number of references to each object in memory. If a reference count goes to zero then the associated object is no longer live and the memory allocated to that object can be freed up for something else
occasionally things called "reference cycles" happen. The garbage collector periodically looks for these and cleans them up. An example would be if you have two objects o1 and o2 such that o1.x == o2 and o2.x == o1. If o1 and o2 are not referenced by anything else then they shouldn't be live. But each of them has a reference count of 1.
Certain heuristics are used to speed up garbage collection. For example, recently created objects are more likely to be dead. As objects are created, the garbage collector assigns them to generations. Each object gets one generation, and younger generations are dealt with first.
Question 13

Place the following functions below in order of their efficiency. They all take in a list of numbers between 0 and 1. The list can be quite long. An example input list would be [random.random() for i in range(100000)]. How would you prove that your answer is correct?

def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]
Answer

Most to least efficient: f2, f1, f3. To prove that this is the case, you would want to profile your code. Python has a lovely profiling package that should do the trick.

import cProfile
lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')
For completion's sake, here is what the above profile outputs:

>>> cProfile.run('f1(lIn)')
         4 function calls in 0.045 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.009    0.009    0.044    0.044 <stdin>:1(f1)
        1    0.001    0.001    0.045    0.045 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.035    0.035    0.035    0.035 {sorted}


>>> cProfile.run('f2(lIn)')
         4 function calls in 0.024 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.008    0.008    0.023    0.023 <stdin>:1(f2)
        1    0.001    0.001    0.024    0.024 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.016    0.016    0.016    0.016 {sorted}


>>> cProfile.run('f3(lIn)')
         4 function calls in 0.055 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.016    0.016    0.054    0.054 <stdin>:1(f3)
        1    0.001    0.001    0.055    0.055 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.038    0.038    0.038    0.038 {sorted}
Why do we care?

Locating and avoiding bottlenecks is often pretty worthwhile. A lot of coding for efficiency comes down to common sense - in the example above it's obviously quicker to sort a list if it's a smaller list, so if you have the choice of filtering before a sort it's often a good idea. The less obvious stuff can still be located through use of the proper tools. It's good to know about these tools.

Question 14

Something you failed at?

Wrong answer

I never fail!

Why this is important:

Shows that you are capable of admitting errors, taking responsibility for your mistakes, and learning from your mistakes. All of these things are pretty darn important if you are going to be useful. If you are actually perfect then too bad, you might need to get creative here.

Question 15

Do you have any personal projects?

Really?

This shows that you are willing to do more than the bare minimum in terms of keeping your skillset up to date. If you work on personal projects and code outside of the workplace then employers are more likely to see you as an asset that will grow. Even if they don't ask this question I find it's useful to broach the subject.

Conclusion

These questions intentionally touched on many topics. And the answers were intentionally verbose. In a programming interview, you will need to demonstrate your understanding and if you can do it in a concise way then by all means do that. I tried to give enough information in the answers that you could glean some meaning from them even if you had never heard of some of these topics before. I hope you find this useful in your job hunt.

Go get 'em tiger.