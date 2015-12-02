> - 译文链接：[编程派](http://codingpy.com/article/python-list-comprehensions-now-in-color/)
> - 原文链接：http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/

Sometimes a programming design pattern becomes common enough to warrant its own special syntax. Python’s list comprehensions are a prime example of such a syntactic sugar.

有时候，一个编程设计模式使用得十分普遍，甚至使其逐步形成自己独特的语法。Python编程语言中的列表解析式（list comprehension）就是这类语法糖（syntactic sugar）的绝佳代表。

List comprehensions in Python are great, but mastering them can be tricky because they don’t solve a new problem: they just provide a new syntax to solve an existing problem.

Python中的列表解析式是个伟大的发明，但是要掌握好这个语法则有些难，因为它们并没有解决新问题：只是为解决已有问题提供了新的语法。

Let’s learn what list comprehensions are and how to identify when to use them.

接下来，我们一起来学习什么是列表解析式，以及如何掌握使用这种语法的时机。

## 什么是列表解析式？

List comprehensions are a tool for transforming one list (any iterable actually) into another list. During this transformation, elements can be conditionally included in the new list and each element can be transformed as needed.

列表解析式是将一个列表（实际上适用于任何可迭代对象）转换成另一个列表的工具。在转换过程中，可以指定元素必须符合一定的条件，才能添加至新的列表中，这样每个元素都可以按需要进行转换。

If you’re familiar with functional programming, you can think of list comprehensions as syntactic sugar for a filter followed by a map:

如果你熟悉函数式编程（functional programming），你可以把列表解析式看作为结合了`filter`函数与`map`函数功能的语法糖：

	>>> doubled_odds = map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers))
	>>> doubled_odds = [n * 2 for n in numbers if n % 2 == 1]

If you’re not familiar with functional programming, don’t worry: I’ll explain using for loops.

如果你不熟悉函数式编程，也不用担心：我稍后会通过`for`循环为大家讲解。

## 从循环到解析式

Every list comprehension can be rewritten as a for loop but not every for loop can be rewritten as a list comprehension.

每个列表解析式都可以重写为`for`循环，但不是每个`for`循环都能重写为列表解析式。

The key to understanding when to use list comprehensions is to practice identifying problems that smell like list comprehensions.

掌握列表解析式使用时机的关键，在于不断练习识别那些看上去像列表解析式的问题（practice identifying problems that smell like list comprehensions）。

If you can rewrite your code to look just like this for loop, you can also rewrite it as a list comprehension:

如果你能将自己的代码改写成类似下面这个`for`循环的形式，那么你也就可以将其改写为列表解析式：

	new_things = []
	for ITEM in old_things:
	    if condition_based_on(ITEM):
	        new_things.append("something with " + ITEM)

你可以将上面的`for`循环改写成这样的列表解析式：
You can rewrite the above for loop as a list comprehension like this:

	new_things = ["something with " + ITEM for ITEM in old_things if condition_based_on(ITEM)]

## 列表解析式：可视化解读 
List Comprehensions: The Animated Movie

可视化解读听上去是个不错的注意，但是我们怎么才能做到这点呢？
That’s great, but how did we do that?

嘿嘿，只需要从`for`循环中复制粘贴，稍微调整一下就变成了列表解析式啦。
We copy-pasted our way from a for loop to a list comprehension.


![for loop to list comprehension](http://treyhunner.com/images/list-comprehension-condition.gif)

下面是我们复制粘贴的顺序：
Here’s the order we copy-paste in:

- 将变量赋值操作复制到新建的空列表中（第三行）
- 将`append()`方法中的表达式参数复制到新列表中（第六行）
- 复制`for`循环语句，不包括最后的`:`（第四行）
- 复制`if`条件控制语句，同样不包括最后的`:`（第五行）

Copy the variable assignment for our new empty list (line 3)
Copy the expression that we’ve been append-ing into this new list (line 6)
Copy the for loop line, excluding the final : (line 4)
Copy the if statement line, also without the : (line 5)

这样，我们将从下面这段代码：

We’ve now copied our way from this:

	numbers = [1, 2, 3, 4, 5]

	doubled_odds = []
	for n in numbers:
	    if n % 2 == 1:
	        doubled_odds.append(n * 2)

转换成了这两行代码：
To this:

	numbers = [1, 2, 3, 4, 5]

	doubled_odds = [n * 2 for n in numbers if n % 2 == 1]

## 无条件子句的列表解析式 Unconditional Comprehensions

如果是那些没有条件子句（即`if SOMETHING`部分）的代码呢，又该怎样复制粘贴？这些形式的代码甚至比有条件子句的代码更好实现。

But what about comprehensions that don’t have a conditional clause (that if SOMETHING part at the end)? These loop-and-append for loops are even simpler than the loop-and-conditionally-append ones we’ve already covered.

一个没有`if`语句的`for`循环：

A for loop that doesn’t have an if statement:

	doubled_numbers = []
	for n in numbers:
	    doubled_numbers.append(n * 2)

上面这段代码页可以改写为一个列表解析式：

That same code written as a comprehension:

	doubled_numbers = [n * 2 for n in numbers]

下面是转换过程的详细演示：

Here’s the transformation animated:

![for loop transformation animated](http://treyhunner.com/images/list-comprehension-no-condition.gif)

我们可以从上面那个简单的`for`循环中，安装这样的顺序复制粘贴：

We can copy-paste our way from a simple loop-and-append for loop by:

- 将变量赋值操作复制到新建的空列表中（第三行）
- 将`append()`方法中的表达式参数复制到新列表中（第五行）
- 复制`for`循环语句，不包括最后的`:`（第四行）

Copying the variable assignment for our new empty list (line 3)
Copying the expression that we’ve been append-ing into this new list (line 5)
Copying the for loop line, excluding the final : (line 4)

## 嵌套循环 Nested Loops

那么嵌套循环（nested loop）又该怎样改写为列表解析式呢？

What about list comprehensions with nested looping?… 

下面是一个拉平（flatten）矩阵（以列表为元素的列表）的`for`循环：

Here’s a for loop that flattens a matrix (a list of lists):

	flattened = []
	for row in matrix:
	    for n in row:
	        flattened.append(n)

下面这个列表解析式实现了相同的功能：
Here’s a list comprehension that does the same thing:

	flattened = [n for row in matrix for n in row]

列表解析式中的嵌套循环读起来就有点绕口了。

Nested loops in list comprehensions do not read like English prose.

注意：我本能地会想把这个列表解析式写成这样：
Note: My brain wants to write this list comprehension as:

	flattened = [n for n in row for row in matrix]

但是这是错误的。这里我不小心颠倒了两个`for`循环的顺序。正确的代码是之前那个。

But that’s not right! I’ve mistakenly flipped the for loops here. The correct version is the one above.

如果要在列表解析式中处理嵌套循环，请记住**`for`循环子句的顺序与我们原来`for`循环的顺序是一致的**。

When working with nested loops in list comprehensions remember that the for clauses remain in the same order as in our original for loops.

同样地原则也适用集合解析式（set comprehension）和字典解析式（dictionary comprehension）。
This same principle applies to set comprehensions and dictionary comprehensions.

## 其他解析式

下面的代码提取单词序列中每个单词的首字母，创建了一个集合（set）：
Code that creates a set of all the first letters in a sequence of words:

	first_letters = set()
	for w in words:
	    first_letters.add(w[0])

同样的代码可以改写为集合解析式：
That same code written as a set comprehension:

	first_letters = {w[0] for w in words}

下面的代码将原有字典的键和值互换，从而创建了一个新的字典：
Code that makes a new dictionary by swapping the keys and values of the original one:

	flipped = {}
	for key, value in original.items():
	    flipped[value] = key

同样的代码可以改写为字典解析式：
That same code written as a dictionary comprehension:

	flipped = {value: key for key, value in original.items()}

## 还要注意可读性

你有没有发现上面的列表解析式读起来很困难？我经常发现，如果较长的列表解析式写成一行代码，那么阅读起来就非常困难。

Did you find the above list comprehensions hard to read? I often find longer list comprehensions very difficult to read when they’re written on one line.

不过，还好Python支持在括号和花括号之间断行。
Remember that Python allows line breaks between brackets and braces.

### 列表解析式 List comprehension

断行前：

	doubled_odds = [n * 2 for n in numbers if n % 2 == 1]

断行后：

	doubled_odds = [
	    n * 2
	    for n in numbers
	    if n % 2 == 1
	]

### 带嵌套循环的列表解析式
Nested loops in list comprehension

断行前：

	flattened = [n for n in row for row in matrix]

断行后：

	flattened = [
	    n
	    for row in matrix
	    for n in row
	]

### 字典解析式
Dictionary comprehension

断行前：

	flipped = {value: key for key, value in original.items()}

断行后：

	flipped = {
	    value: key
	    for key, value in original.items()
	}

请注意，我们并不是随意进行断行：我们是在每一行复制过来的代码之后断行的。
Note that we are not adding line breaks arbitrarily: we’re breaking between each of the lines of code we copy-pasted to make these comprehension. Our line breaks occur where color changes occur in the colorized versions.

## 总结

Summary

When struggling to write a comprehension, don’t panic. Start with a for loop first and copy-paste your way into a comprehension.

纠结于写不出列表解析式吗？不要担心。先写一个`for`循环，能后按照本文说的顺序复制粘贴，就可以写出解析式了。

任何类似下面代码形式的`for`循环：

Any for loop that looks like this:

	new_things = []
	for ITEM in old_things:
	    if condition_based_on(ITEM):
	        new_things.append("something with " + ITEM)

都可以被改写为下面这种列表解析式：
Can be rewritten into a list comprehension like this:

	new_things = ["something with " + ITEM for ITEM in old_things if condition_based_on(ITEM)]
	
（有删减）