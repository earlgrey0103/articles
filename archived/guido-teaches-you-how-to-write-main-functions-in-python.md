# Python之父教你写main()函数

关键词：Ptyhon之父, Python Guido van Rossum, Python main函数, Guido van Rossum, 怎么写main()函数

URL：guido-shows-how-to-write-main-function

每个程序员在学习编程的过程中，肯定没少写过`main()`函数，Python程序员也不例外。本文为大家分享Python之父Guido van Rossum推荐的函数写法，可以大大提高这个函数的灵活性。

一般来说，Python程序员可能是这样写main()函数的：


    """Module docstring.

    This serves as a long usage message.
    """
    import sys
    import getopt

    def main():
        # parse command line options
        try:
            opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        except getopt.error, msg:
            print msg
            print "for help use --help"
            sys.exit(2)
        # process options
        for o, a in opts:
            if o in ("-h", "--help"):
                print __doc__
                sys.exit(0)
        # process arguments
        for arg in args:
            process(arg) # process() is defined elsewhere

    if __name__ == "__main__":
        main()

Guido也承认之前自己写的main()函数也是类似的结构，但是这样写的灵活性还不够高，尤其是需要解析复杂的命令行选项时。为此，他向大家提出了几点建议。

## 添加可选的 argv 参数

首先，修改main()函数，使其接受一个可选参数 argv，支持在交互式shell中调用该函数：

    def main(argv=None):
        if argv is None:
            argv = sys.argv
        # etc., replacing sys.argv with argv in the getopt() call.

这样做，我们就可以动态地提供 argv 的值，这比下面这样写更加的灵活：

    def main(argv=sys.argv):
        # etc.

这是因为在调用函数时，sys.argv 的值可能会发生变化；**可选参数的默认值都是在定义main()函数时，就已经计算好的**。

但是现在`sys.exit()`函数调用会产生问题：当`main()`函数调用`sys.exit()`时，交互式解释器就会推出！解决办法是让`main()`函数的返回值指示退出状态（exit status）。因此，最后面的那行代码就变成了这样：

    if __name__ == "__main__":
        sys.exit(main())

并且，main()函数中的`sys.exit(n)`调用全部变成`return n`。


## 定义一个Usage()异常

另一个改进之处，就是定义一个Usage()异常，可以在`main()`函数最后的`except`子句捕捉该异常：

    import sys
    import getopt

    class Usage(Exception):
        def __init__(self, msg):
            self.msg = msg

    def main(argv=None):
        if argv is None:
            argv = sys.argv
        try:
            try:
                opts, args = getopt.getopt(argv[1:], "h", ["help"])
            except getopt.error, msg:
                 raise Usage(msg)
            # more code, unchanged
        except Usage, err:
            print >>sys.stderr, err.msg
            print >>sys.stderr, "for help use --help"
            return 2

    if __name__ == "__main__":
        sys.exit(main())

这样`main()`函数就只有一个退出点（exit）了，这比之前两个退出点的做法要好。而且，参数解析重构起来也更容易：在辅助函数中引发`Usage`的问题不大，但是使用`return 2`却要求仔细处理返回值传递的问题。


阅读原文：[http://www.artima.com/weblogs/viewpost.jsp?thread=4829](http://www.artima.com/weblogs/viewpost.jsp?thread=4829)
