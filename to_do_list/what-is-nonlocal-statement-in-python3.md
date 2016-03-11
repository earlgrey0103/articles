# Python基础知识：什么是非局部语句？

关键词：Python基础知识, 非局部语句, Python 作用域, Python 全局变量, Python 非局部变量, Python nonlocal

> 本文首发于[微信公众号号“编程派”](http://mp.weixin.qq.com/s?__biz=MzAwNDc0MTUxMw==&mid=401863291&idx=2&sn=cd633d850050c8f96a72d69e3a23bdbd#rd)。微信搜索“编程派”，获取更多Python编程一手教程及优质资源吧。

有同学曾在微信中问小编什么是非局部语句（nonlocal statement），本文就是对此的回答，希望没有发的太晚。

非局部语句是Python 3.x中新引入的特性，可以让你给外层但非全局作用域中的变量赋值。官方文档中的说法是，非局部语句可以让所列的标识符（identifier）指向*最近*的嵌套作用域（enclosing scope）中已经绑定过的变量，全局变量除外。

## 如果没有非局部语句

一般来说，嵌套函数对于其外层作用域中的变量是有访问权限的。

	>>> def outside():
		    msg = "Outside!"

		    def inside():
		        print(msg)

		    inside()
		    print(msg)

	>>> outside()
	Outside!
	Outside!

我们在`outside`函数中声明了`msg`变量，并赋值为“Outside!”。然后，在`inside`函数中打印`msg`的值。结果证明，`inside`成功获得了外层作用域中`msg`的值。

但是如果我们想给外层作用域中的变量赋值时，是不是按照平常的赋值操作就可以修改它的值呢？

	>>> def outside():
	        msg = "Outside!"
	        def inside():
	            msg = "Inside!"
	            print(msg)
	        inside()
	        print(msg)

	>>> outside()
	Inside! # inside函数打印的msg
	Outside! # outside函数打印的msg

在`inside`函数中，我们想给`msg`变量赋值为"Inside!"。运行`outside`时，`inside`函数中`msg`的值为"Inside!"，但是在`outside`函数中却保留了原先的值！

之所以出现这个情况，是因为在`inside`函数中，Python实际上并没有为之前已经创建的`msg`变量赋值，而是在`inside`函数的局部作用域（local scope）中创建了一个名叫`msg`的新变量，但是这样就和外层作用域（outer scope）中的变量重名了。

这说明，嵌套函数对外层作用域中的变量其实只有只读访问权限。如果我们在这个示例中的`inside`函数的顶部再加一个`print(msg)`语句，那么就会出现`UnboundLocalError: local variable 'msg' referenced before assignment`这个错误。

非局部语句的引入，就是要尽量减少这种变量名冲突情况的出现，同时也让嵌套函数更加方便的操作外层函数中的变量。更加详细的原因，请看参考资料部分的PEP-3104。

## 使用非局部语句之后

接下来，我们引入nonlocal语句。

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

现在，我们在`inside`函数的顶部添加了`nonlocal msg`语句。这个语句的作用，就是告诉Python解释器在碰到为`msg`赋值的语句时，应该向外层作用域的变量赋值，而不是声明一个重名的新变量。这样，两个函数的打印结果就一致了。

`nonlocal`的用法和`global`非常类似，只是前者针对的是外层函数作用域的变量，后者针对的则是全局作用域的变量。

## 什么时候该使用非局部语句

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

你可能会想，因为没有使用`nonlocal`，`inside`函数中往字典`d`中插入的`"inside": 2`键值对（key-value pair）不会体现在`outside`函数中。你这么想挺合理，但却是错的。因为字典插入并不是赋值操作，而是方法调用（method call）。事实上，往字典中插入一个键值对相当于调用字典对象中的`__setitem__`方法。

	>>> d = {}
	>>> d.__setitem__("inside", 2)
	>>> d
	{'inside': 2}

所以，这个示例中我们*可以不使用nonlocal*，就能直接操作外层作用域中的变量。

## 小结

其实在许多Python程序中，很少用到非局部语句。但是，有了这种语句之后，我们就可以减少不同作用域之间变量名的冲突。非局部语句，也让我们更加容易地访问、操作外层作用域中的变量。不过，这在一定程度上也让语法变得更加复杂。

有关变量、语句等术语的基础知识，还可以参考[《Think Python 2e》的第二章：量、表达式和语句](http://codingpy.com/books/thinkpython2/02-variables-expressions-and-statements.html)。

## 参考资料

1. [Simple Statements](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)

2. [PEP-3104](http://legacy.python.org/dev/peps/pep-3104/)

3. [Global-Nonlocal](http://www.dotnetperls.com/global-nonlocal)

4. [PyTips](https://github.com/rainyear/pytips/blob/master/Markdowns/2016-03-10-Scope-and-Closure.md)