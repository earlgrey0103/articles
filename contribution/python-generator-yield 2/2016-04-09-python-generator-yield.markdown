---
layout:     post
title:      "Python之生成器详解"
subtitle:   "从Iterable,Iterator知Generator,Yield"
date:       2016-04-09
author:     "kissg"
header-img: "img/python-generator-yield/sisyphus.jpg"
tags:
    - 菜鸟成长日记
    - python
    - generator
    - yield
---

> 一叶落知天下秋,知秋更可知叶落.

## 引文

编程派前几天推送了一篇文章,叫["Python学习进阶路线(简版)"](http://codingpy.com/article/python-progression-path-simple-version/),`生成器(generator)`赫然在列.可是我不太会.不会怎么办?学咯.于是上网看了不少教程,又看了官方文档,学到了不少知识.在此,权且做个学习笔记,也与大家分享一下.

## 正文

要理解`generator`,我们先从`迭代(iteration)`与`迭代器(iterator)`讲起.当然,本文的重点是`generator`,`iteration`与`iterator`的知识将点到即止.[直接看`generator`](#generator)

> 迭代是重复反馈过程的活动，其目的通常是为了接近并到达所需的目标或结果。每一次对过程的重复被称为一次“迭代”，而每一次迭代得到的结果会被用来作为下一次迭代的初始值。

以上是[维基百科](http://zh.wikipedia.org/wiki/%E8%BF%AD%E4%BB%A3)对迭代的定义.在python中,迭代通常是通过`for ... in ...`来完成的,而且只要是`可迭代对象(iterable)`,都能进行迭代.这里简单讲下`iterable`与`iterator`:

> `iterable`是实现了`__iter__()`方法的对象.更确切的说,是`container.__iter__()`方法,该方法返回的是的一个`iterator`对象,因此`iterable`是你可以从其获得`iterator`的对象.~~使用`iterable`时,将一次性返回所有结果,都存放在内存中,并且这些值都能重复使用.~~以上说法严重错误!对于`iterable`,我们该关注的是,它是一个能一次返回一个成员的对象(iterable is an object capable of returning its members one at a time),一些`iterable`将所有值都存储在内存中,比如`list`,而另一些并不是这样,比如我们下面将讲到的`iterator`.

> `iterator`是实现了`iterator.__iter__()`和`iterator.__next__()`方法的对象.`iterator.__iter__()`方法返回的是`iterator`对象本身.根据官方的说法,正是这个方法,实现了`for ... in ...`语句.而`iterator.__next__()`是`iterator`区别于`iterable`的关键了,它允许我们***显式***地获取一个元素.当调用`next()`方法时,实际上产生了2个操作:

  1. 更新`iterator`状态,令其指向后一项,以便下一次调用
  2. 返回当前结果

如果你学过`C++`,它其实跟指针的概念很像(如果你还学过链表的话,或许能更好地理解).

正是`__next__()`,使得`iterator`能在每次被调用时,返回一个单一的值(有些教程里,称为一边循环,一边计算,我觉得这个说法不是太准确.但如果这样的说法有助于你的理解,我建议你就这样记),从而极大的节省了内存资源.另一点需要格外注意的是,`iterator`是消耗型的,即每一个值被使用过后,就消失了.因此,你可以将以上的操作2理解成`pop`.对`iterator`进行遍历之后,其就变成了一个空的容器了,但不等于`None`哦.因此,若要重复使用`iterator`,利用`list()`方法将其结果保存起来是一个不错的选择.

我们通过代码来感受一下.

```python
>>> from collections import Iterable, Iterator
>>> a = [1,2,3]   # 众所周知,list是一个iterable
>>> b = iter(a)   # 通过iter()方法,得到iterator,iter()实际上调用了__iter__(),此后不再多说
>>> isinstance(a, Iterable)
True
>>> isinstance(a, Iterator)
False
>>> isinstance(b, Iterable)
True
>>> isinstance(b, Iterator)
True
# 可见,iterable是iterator,但iterator不一定是iterable

# iterator是消耗型的,用一次少一次.对iterator进行变量,iterator就空了!
>>> c = list(b)
>>> c
[1, 2, 3]
>>> d = list(b)
>>> d
[]


# 空的iterator并不等于None.
>>> if b:
...   print(1)
...
1
>>> if b == None:
...   print(1)
...

# 再来感受一下next()
>>> e = iter(a)
>>> next(e)     #next()实际调用了__next__()方法,此后不再多说
1
>>> next(e)
2
```

既然提到了`for ... in ...`语句,我们再来简单讲下其工作原理吧,或许能帮助理解以上所讲的内容.

```python
>>> x = [1, 2, 3]
>>> for i in x:
...     ...
```

我们对一个`iterable`用`for ... in ...`进行迭代时,实际是先通过调用`iter()`方法得到一个`iterator`,假设叫做X.然后循环地调用X的`next()`方法取得每一次的值,直到iterator为空,返回的`StopIteration`作为循环结束的标志.`for ... in ... `会自动处理`StopIteration`异常,从而避免了抛出异常而使程序中断.如图所示

![what-really-happens-in-for-in-statement](/img/python-generator-yield/for-in.png)

<p id = "generator"></p>

磨刀不误砍柴工,有了前面的知识,我们再来理解`generator`与`yield`将会事半功倍.

首先先理清几个概念:

> `generator`: A function which returns a generator iterator. It looks like a normal function except that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.

> `generator iterator`: An object created by a generator funcion.

> `generator expression`: An expression that returns an iterator.

以上的定义均来自[python官方文档](https://docs.python.org/3/glossary.html#term-generator).可见,我们常说的`生成器`,就是带有`yield`的函数,而`generator iterator`则是`generator function`的返回值,即一个`generator`对象,而形如`(elem for elem in [1, 2, 3])`的表达式,称为`generator expression`,实际使用与`generator`无异.

```python
>>> a = (elem for elem in [1, 2, 3])
>>> a
<generator object <genexpr> at 0x7f0d23888048>
>>> def fib():
...     a, b = 0, 1
...     while True:
...         yield b
...         a, b = b, a + b
...
>>> fib
<function fib at 0x7f0d238796a8>
>>> b = fib()
<generator object fib at 0x7f0d20bbfea0>
```

其实说白了,`generator`就是`iterator`的一种,以更优雅的方式实现的`iterator`.官方的说法是:

> Python’s generators provide a convenient way to implement the iterator protocol.

你完全可以像使用`iterator`一样使用`generator`,当然除了定义.定义一个`iterator`,你需要分别实现`__iter__()`方法和`__next__()`方法,但`generator`只需要一个小小的`yield`(好吧,`generator expression`的使用比较简单,就不展开讲了.)

前文讲到`iterator`通过`__next__()`方法实现了每次调用,返回一个单一值的功能.而`yield`就是实现`generator`的`__next__()`方法的关键!先来看一个最简单的例子:

```python
>>> def g():
...     print("1 is")
...     yield 1
...     print("2 is")
...     yield 2
...     print("3 is")
...     yield 3
...
>>> z = g()
>>> z
<generator object g at 0x7f0d2387c8b8>
>>> next(z)
1 is
1
>>> next(z)
2 is
2
>>> next(z)
3 is
3
>>> next(z)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

第一次调用`next()`方法时,函数似乎执行到`yield 1`,就暂停了.然后再次调用`next()`时,函数从`yield 1`之后开始执行的,并再次暂停.第三次调用`next()`,从第二次暂停的地方开始执行.第四次,抛出`StopIteration`异常.

事实上,`generator`确实在遇到`yield`之后暂停了,确切点说,是先返回了`yield`表达式的值,再暂停的.当再次调用`next()`时,从先前暂停的地方开始执行,直到遇到下一个`yield`.这与上文介绍的对`iterator`调用`next()`方法,执行原理一般无二.

有些教程里说`generator`保存的是算法,而我觉得用`中断服务子程序`来描述`generator`或许能更好理解,这样你就能将`yield`理解成一个中断服务子程序的`断点`,没错,是中断服务子程序的断点.我们每次对一个`generator`对象调用`next()`时,函数内部代码执行到"断点"`yield`,然后返回这一部分的结果,并保存上下文环境,"中断"返回.

怎么样,是不是瞬间就明白了`yield`的用法?

我们再来看另一段代码.

```python
>>> def gen():
...     while True:
...         s = yield
...         print(s)
...
>>> g = gen()
>>> g.send("kissg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't send non-None value to a just-started generator
>>> next(g)
>>> g.send("kissg")
kissg
```

我正是看到这个形式的`generator`,懵了,才想要深入学习`generator`与`yield`的.结合以上的知识,我再告诉你,`generator`其实有第2种调用方法(恢复执行),即通过`send(value)`方法将`value`作为`yield`表达式的当前值,你可以用该值再对其他变量进行赋值,这一段代码就很好理解了.当我们调用`send(value)`方法时,`generator`正由于`yield`的缘故被暂停了.此时,`send(value)`方法传入的值作为`yield`表达式的值,函数中又将该值赋给了变量`s`,然后print函数打印`s`,循环再遇到`yield`,暂停返回.

调用`send(value)`时要注意,要确保,`generator`是在`yield`处被暂停了,如此才能向`yield`表达式传值,否则将会报错(如上所示),可通过`next()`方法或`send(None)`使`generator`执行到`yield`.

再来看一段`yield`更复杂的用法,或许能加深你对`generator`的`next()`与`send(value)`的理解.

```python
>>> def echo(value=None):
...   while 1:
...     value = (yield value)
...     print("The value is", value)
...     if value:
...       value += 1
...
>>> g = echo(1)
>>> next(g)
1
>>> g.send(2)
The value is 2
3
>>> g.send(5)
The value is 5
6
>>> next(g)
The value is None
```

上述代码既有`yield value`的形式,又有`value = yield`形式,看起来有点复杂.但以`yield`分离代码进行解读,就不太难了.第一次调用`next()`方法,执行到`yield value`表达式,保存上下文环境暂停返回`1`.第二次调用`send(value)`方法,从`value = yield`开始,打印,再次遇到`yield value`暂停返回.后续的调用`send(value)`或`next()`都不外如是.

但是,这里就引出了另一个问题,`yield`作为一个暂停恢复的点,代码从`yield`处恢复,又在下一个`yield`处暂停.可见,在一次`next()`(非首次)或`send(value)`调用过程中,实际上存在**2**个`yield`,一个作为恢复点的`yield`与一个作为暂停点的`yield`.因此,也就有2个`yield`表达式.`send(value)`方法是将值传给*恢复点*`yield`;调用`next()`表达式的值时,其**恢复点**`yield`的值总是为`None`,而将**暂停点**的`yield`表达式的值返回.为方便记忆,你可以将此处的**恢复点**记作当前的(current),而将**暂停点**记作下一次的(next),这样就与`next()`方法匹配起来啦.

`generator`还实现了另外两个方法`throw(type[, value[, traceback]])`与`close()`.前者用于抛出异常,后者用于关闭`generator`.不过这2个方法似乎很少被直接用到,本文就不再多说了,有兴趣的同学请看[这里](https://docs.python.org/3/reference/expressions.html#generator.throw)

## 小结

![iterable-iterator-generator](/img/python-generator-yield/iterators-generators-iterables.png)

1. 可迭代对象(Iterable)是实现了`__iter__()`方法的对象,通过调用`iter()`方法可以获得一个迭代器(Iterator)

2. 迭代器(Iterator)是实现了`__iter__()`和`__next__()`的对象

3. `for ... in ...`的迭代,实际是将可迭代对象转换成迭代器,再重复调用`next()`方法实现的

4. 生成器(generator)是一个特殊的迭代器,它的实现更简单优雅.

5. `yield`是生成器实现`__next__()`方法的关键.它作为生成器执行的暂停恢复点,可以对`yield`表达式进行赋值,也可以将`yield`表达式的值返回.

> (本人刚开始写博客,本文写得狠辛苦,转载希望著明出处,不胜感谢.)
