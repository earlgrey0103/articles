# 为什么print在Python 3中变成了函数？

- 原作者：Bret Cannon
- 原文链接：http://www.snarky.ca/why-print-became-a-function-in-python-3
- 译者：EarlGrey@编程派

在Python 2中，print是一个语句（statement）；而在Python 3中变成了函数（function）。很多Python用户都会问，为什么Python 3将print变成了函数呢？本文就是Python核心开发者Bret Cannon对此的解释。

## print语句与print函数的区别

### print语句

在Python 2中，print语句最简单的使用形式就是`print A`，这相当于执行了`sys.stdout.write(str(A) + '\n')`。如果你以逗号为分隔符，传递额外的参数（argument），这些参数会被传递至`str()`函数，最终打印时每个参数之间会空一格。例如，`print A, B, C`相当于`sys.stdout.write(' '.join(map(str, [A, B, C])) + '\n')`。如果print语句的最后再加上一个逗号，那么就不会再添加断行符（`\n`），也就是说：`print A`相当于`sys.stdout.write(str(A))`。

从 2.0版本开始，Python引入了`print >>`的语法，作用是重定向`print`语句最终输出字符串的文件。例如，`print >> output, A`相当于`output.write(str(A) + '\n')`。

### print函数

如果用Python来实现print函数，它的函数定义应该是这样的：

    import sys

    def print(*objects, sep=None, end=None, file=None, flush=False):
        """A Python translation of the C code for builtins.print().


    """
        if sep is None:
            sep = ' '
        if end is None:
            end = '\n'
        if file is None:
            file = sys.stdout
        file.write(sep.join(map(str, objects)) + end)
        if flush:
            file.flush()

从上面的代码中，我们可以发现：Python 3中的print函数实现了print语句的所有特性。

    print A == print(A)
    print A, B, C == print(A, B, C)
    print A, == print(A, end='')
    print >> output, A == print(A, file=output)

从上面的示例代码中我们就可以看出，使用print函数有明显的好处：与使用print语句相比，我们现在能够指定其他的分隔符（separator）和结束符（end string）。

## 关键在于灵活性

将print变成函数的真正巧妙之处在与灵活性，但这点并不容易被人发觉。print成为函数之后，给Python用户和Python开发团队带来了很大的灵活性。对于用户来说，这可以让你把`print`当作表达式（expression）使用；相比之下，print语句就只能作为语句使用。举个例子，假设你想在每一行后面打印一个省略号（ellipsis），表示这行尚未结束。使用print语句的话，你有两种选择：

    # 手动实现 ...
    print A, '...'

    # 可复用的实现（这种方式也适用于print函数） ...
    def ellipsis_print(*args):
        for arg in args:
            print arg, '',
        print '...'

但是在Python 3中，你可以选择更好的解决方式：

    # 手动实现 ...
    print(A, end='...\n')

    # 多个可复用的解决方案，利用print语句无法实现...
    ellipsis_print = lambda *args, **kwargs: print(*args, **kwargs, end='...\n')
    # 或者 ...
    import functools
    ellipsis_print = functools.partial(print, end='...\n')

换句话说，变成函数之后，`print`就可以组件化了，作为语句的`print`是无法支持的。还有，你还可以编写自己喜欢的`print`函数，将其赋值给`builtins.print`，就可以覆盖掉自带的函数实现了。这一点在Python 2中是不可能实现的。

对于Python开发团队来说，他们不必再从语法层面来实现`print`的相关功能了。例如，如果你想让`print`语句也一样可以灵活地支持指定分隔符，你要怎样去实现呢？这会是一个相当难解决的设计难题。但是如果print变成了函数，只需要新增一个参数就解决了。在Python中，函数可以接受任意数量的参数，这比从底层实现语法带来的灵活性要大的多。

我们还要注意，语法实现应该仅限于那些非这样做不可的功能，或者是以语法形式实现后，大幅提高了可读性的功能。在`print`这个案例中，`print A`与`print(A)`之间的区别可以忽略不计，因此并没有影响可读性。而且，由于我们能够完全将`print`语句替换为函数，对于Python语言的功能性也没有损失。这就是为什么将`print`变成函数的原因。