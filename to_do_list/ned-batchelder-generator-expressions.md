# 有没有生成器推导式？

关键词：生成器表达式, 列表推导式, python工程师, 字典推导式, 集合推导式

URL：what-is-generator-comprehension

> 本文作者为Ned Batchelder，是一名资深Python工程师，目前就职于在线教育网站Edx。

Python中有一种紧凑的语法，可以通过一个循环和条件构建一个列表，这种语法叫做列表推导式（list comprehension）：

```python
my_list = [ f(x) for x in sequence if cond(x) ]
```

类似地，我们可以通过字典推导式（dictionary comprehension）创建字典，通过集合推导式（set comprehension）创建集合：

```python
my_dict = { k(x): v(x) for x in sequence if cond(x) }
my_set = { f(x) for x in sequence if cond(x) }
```
（这一语法支持更加复杂的操作，但这里仅作示例）

最后，你还可以使用类似的语法创建一个生成器：

```python
my_generator = ( f(x) for x in sequence if cond(x) )
```

不过，这并不叫做生成器推导式，而是叫做生成器表达式（generator expression）。为什么不叫前者呢？如果前三个语法都被称为“推导式”，为什么生成器这个不叫呢？

[PEP 289 —— 生成器表达式](https://www.python.org/dev/peps/pep-0289/) 的最后给出了详细的备注，其中指出Raymond Hettinger起初提议使用“生成器推导式（generator comprehension）”一词，后来Peter Norvig提出了“累计显示（accumulation displays）”，后来Tim Peters推荐了“生成器表达式”这个名词。但是它并没有名词出现了这样的变化。

> EarlGrey：上面提到的这几位都是大牛啊！具体大家可以谷歌一下。

所以我[在Twitter上提出了这个问题](https://twitter.com/nedbat/status/727926142909468672)：

> #python 有个我不懂的问题：为什么它们被称为“生成器表达式”，而不是“生成器推导式”？

Guido的回答指出了核心原因：

> 推导式一开始属于“字面量显示（literal display）”这一概念。而生成器表达式不是一种显示（display）。


Matt Boehm后来找到了[Tim Peters提出“生成器表达式”一词的邮件](https://mail.python.org/pipermail/python-dev/2003-October/039186.html)，其中讲述了一些细节：

读完邮件后，我对这个问题的理解更深了。首先，为什么会使用“推导式”（comprehension）一词？Tim在邮件中指出，这个词来源于集合论中的[推导公理（Axiom of Comprehension）](https://en.wikipedia.org/wiki/Axiom_schema_of_specification)，它指的是通过对另一个集合的元素应用某个谓词（predicate，即条件）而组成新的集合。这和向另一个序列中的元素应用某个条件从而生成列表的做法非常类似。

> EarlGrey：我之前看到很多翻译为“解析”，看到这里才觉得“推导式”才是更准确的说法。

正如Guido所指出的，Python的设计者当时更注重的是显示，而不是条件。“显示”一词在这里意味着代码的语法看上和它将创建的数据结构很像。列表显示（列表推导式）看上去像一个列表。对于集合和字典显示来说，也是一样的道理。但是由于没有生成器字面量语法，因此根本就没有一个生成器显示可以进行对比，也就不存在生成器显示了。

在设计该功能的那封邮件中，“推导式”一次是“显示”的同义词，由于生成器没有显示，所以也不可能有推导式。

不过Time在他的邮件中也说到，推导式的奇妙之处在于条件。推导公理的核心则是谓语。也许是因为Python推导式中的条件是可选的，关注的焦点被转移到了显示方面。

但是我认为，我们应该叫它们“生成器推导式”。我们在描述这类语法时，并没有使用“显示”一词。我们没有理由将“推导式”与“显示”和字面量语法联系在一起。

列表推导式、字典推导式、集合推导式和生成器表达式，这四个表达式各自之间有着许多相似之处。如果将四者之间的类似点总结为“推导式”，将极大地简化相关概念。它们之间的相似点远大于不同之处，我建议大家对这四个表达式使用同样的概念。

**建议：统称为“推导式”。**
