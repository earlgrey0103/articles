# 什么是非局部语句？

有同学曾在微信中问小编什么是非局部语句（nonlocal statement），因为被全局（global）、局部（local）和非局部这三个术语给搞晕了。

非局部语句是Python 3.x中新引入的特性，可以让你给外层但非全局作用域中的变量赋值。看完下面这个示例，你就明白刚才说的是什么意思了。

	>>> def outside():
	        msg = "Outside!"
	        def inside():
	            msg = "Inside!"
	            print(msg)
	        inside()
	        print(msg)

	>>> outside()
	Inside!
	Outside!

`outside`函数中声明了`msg`变量，并赋值为“Outside!”。然后，在`inside`函数中，又给一个名叫`msg`的变量赋值为"Inside!"。运行`outside`时，`inside`函数中`msg`的值为"Inside!"，但是在`outside`函数中仍保留了原先的值。

之所以出现这个原因，在于Python实际上并没有为之前已经创建的`msg`变量赋值，而是在`inside`函数的局部作用域（local scope）中创建了一个名叫`msg`的新变量，但是这样就和外层作用域（outer scope）中的变量重名了。

非局部语句的引入，就是为了避免这个情况的发生。

>>> def outside():
        msg = "Outside!"
        def inside():
            nonlocal msg
            msg = "Inside!"
            print(msg)
        inside()
        print(msg)
 
>>> outside()
Inside!
Inside!

现在，我们在`inside`函数的顶部添加了`nonlocal msg`语句。这样Python解释器碰到为`msg`赋值的语句时，就知道应该向外层作用域的变量赋值，而不是声明一个重名的新变量。

`nonlocal`的用法和`global`非常类似，除了前者针对的是外层函数作用域的变量，后者针对的则是全局作用域的变量。

有时候，你可能会疑惑什么时候才应该使用`nonlocal`。以下面的函数为例：

	>>> def outside():
	        d = {"outside": 1}
	        def inside():
	            d["inside"] = 2
	            print(d)
	        inside()
	        print(d)

	>>> outside()
	{'inside': 2, 'outside': 1}
	{'inside': 2, 'outside': 1}

你可能会想，因为没有使用`nonlocal`，`inside`函数中往`d`中插入的"inside": 2键值对（key-value pair）不会体现在`outside`函数中。你这么想挺合理，但却是错的。因为字典插入并不是赋值操作，而是方法调用（method call）。事实上，往字典中插入一个键值对相当于调用字典对象中的`__setitem__`方法。

	>>> d = {}
	>>> d.__setitem__("inside", 2)
	>>> d
	{'inside': 2}

> 非局部语句可以让所列的标识符（identifier）指向最近的嵌套作用域（enclosing scope）中已经绑定过的变量，全局变量除外。

## 参考资料

1. [Simple Statements](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)

2. [PEP-3104](http://legacy.python.org/dev/peps/pep-3104/)

3. [Global-Nonlocal](http://www.dotnetperls.com/global-nonlocal)

4. [PyTips](https://github.com/rainyear/pytips/blob/master/Markdowns/2016-03-10-Scope-and-Closure.md)

5. [A Quick Guide to nonlocal in Python 3](https://www.smallsurething.com/a-quick-guide-to-nonlocal-in-python-3/)