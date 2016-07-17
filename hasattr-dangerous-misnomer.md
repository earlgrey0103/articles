# hasattr()：危险的函数，不推荐使用

关键词：python最佳实践, python教程, hasattr用法, python3编程, getattr


本文由编程派根据 [Hacker News 上曾经排名第一的文章](https://hynek.me/articles/hasattr/)编译而来，作者 Hynek Schlawack 是一名德国软件工程师。

他建议，**除非是编写只兼容 Python 3 的代码而且清楚地了解``hasattr()``的用法，否则不要使用``hasattr()``**。

在 Python 2 下，不建议编写这样的代码：

```python
if hasattr(x, "y"):
    print(x.y)
else:
    print("no y!")
```

更好的做法是像如下两例所示：

```python
try:
    print(x.y)
except AttributeError:
    print("no y!")
```

或者

```python
y = getattr(x, "y", None)
if y is not None:
    print(y)
else:
    print("no y!")
```

如果处理的不是用户自行创建的类，更应该采用上述写法。

上面有一处用到了``getattr()``，这里将属性缺失视作属性的值为``None``（常见的情况），如果想与此区分开来，可使用一个标记值（sentinel value）。``getattr``的速度不比``hasattr()``低，因为二者的查找过程完全相同，并且后者不会保存结果（至少在CPython实现下是如此）。

## 为什么不建议使用``hasattr()``

在 Python 2 下使用``hasattr()``，和下面的代码几乎没有分别：

```python
try:
    print(x.y)
except:
    print("no y!")
```

但是这样会隐藏掉特性（property）：

```python
>>> class C(object):
...     @property
...     def y(self):
...         0/0
...
>>> hasattr(C(), "y")
False
```

对于第三方库中类，我们无法确定某个属性（attribute）是否为特性（或者之后某次更新将其变成特性），因此上面那样使用``hasattr()``是非常危险的。

你或许不信，但是 Hacker News 上确实有程序员回复说经历过这个情况，``hasattr()``隐藏了一个非常深的错误，让程序调式工作变得异常艰难。

另外一个原因是，对特性使用``hasttr()``会执行它们的 getter 函数，但这样和``hasattr()``这个函数的名称并不相符。

不过，在 Python 3 中，``hasattr()``不存在这些问题：

```python
>>> class C:
...     @property
...     def y(self):
...         0/0
...
>>> hasattr(C(), "y")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in y
ZeroDivisionError: division by zero
```

因此，在编写兼容 Python 2 和 3 的混合代码时，要特别注意这个函数。另外，你应该想不到``hasattr()``会引发``ZeroDivisionError``吧？

留心的读者可能会问，如果出现``AttributeError``呢？？的确，如果真出现，我们没有办法区分到底是因为真的缺失该属性，还是特性存在问题。**文首提到的写法可以将可能的错误减少为只有一种，避免出现 Python 2 和 3 之间让人困惑的行为差异。**

## 结语

当然，在你自己写的代码中仍然可以使用``hasattr()``，但是**如果后来修改了类，记得也要修改对应的``hasattr()``，确保不会出错**。不过虽然这样可以少写些代码，但是却增加了不必要的心理负担。


