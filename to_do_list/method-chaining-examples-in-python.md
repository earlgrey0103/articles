# 如何在Python中使用方法链？

关键词：方法链, 面向对象编程, method chaining example, Python实现方法链, Python基础教程, Python国外教程

方法链（method chaining）是面向对象的编程语言中的一种常见语法，可以让开发者在只引用对象一次的情况下，对同一个对象进行多次方法调用。举个例子：

假设我们有一个Foo类，其中包含有两个方法——`bar`和`baz`。

我们创建一个Foo类的实例：

    foo = Foo()

如果不使用方法链，要想连续调用对象`foo`的`bar`和`baz`方法的话，我们得这样做：

    foo.bar() # Call method bar() on object foo.
    foo.baz() # Call method baz() on object foo.

如果使用方法链的话，我们就能这样实现：
    foo.bar().baz()

方法链的一个好处，是可以减少你使用对象名的次数。调用的方法越多，能够减少的次数就越多。因此，这个方法也能一定程度上减少需要阅读、测试、调试、维护的代码数量。这个好处不大，但也是有用的。

请注意，方法链的一个限制是，只能用在不需要返回其他值的方法上，因为你需要返回`self`对象。即使Python支持用一个`return`语句返回多个值，也可能无法解决这个问题。

下面是在Python中实现方法链的一个示例：

    class Person:
        def name(self, value):
            self.name = value
            return self
     
        def age(self, value):
            self.age = value
            return self
     
        def introduce(self):
            print "Hello, my name is", self.name, "and I am", self.age, "years old."
     
    person = Person()
    person.name("EarlGrey").age(21).introduce()
    # => Hello, my name is EarlGrey and I am 21 years old.

上面那种实现可能太简单了。下面我们来看一种更加现实的方法链使用方法：编写一个字符串处理程序`string_processor.py`，支持方法链。

    import copy

    class StringProcessor(object):
        '''
        A class to process strings in various ways.
        '''
        def __init__(self, st):
            '''Pass a string for st'''
            self._st = st

        def lowercase(self):
            '''Make lowercase'''
            self._st = self._st.lower()
            return self

        def uppercase(self):
            '''Make uppercase'''
            self._st = self._st.upper()
            return self

        def capitalize(self):
            '''Make first char capital (if letter); make other letters lower'''
            self._st = self._st.capitalize()
            return self

        def delspace(self):
            '''Delete spaces'''
            self._st = self._st.replace(' ', '')
            return self

        def rep(self):
            '''Like Python's repr'''
            return self._st

        def dup(self):
            '''Duplicate the object'''
            return copy.deepcopy(self)

    def process_string(s):
        print
        sp = StringProcessor(s)
        print 'Original:', sp.rep()
        print 'After uppercase:', sp.dup().uppercase().rep()
        print 'After lowercase:', sp.dup().lowercase().rep()
        print 'After uppercase then capitalize:', sp.dup().uppercase().\
        capitalize().rep()
        print 'After delspace:', sp.dup().delspace().rep()

    def main():
        print "Demo of method chaining in Python:"
        # Use extra spaces between words to show effect of delspace.
        process_string('hOWz  It     GoInG?')
        process_string('The      QUIck   brOWn         fOx')

    main()

下面是这个程序的运行结果：

    $ python string_processor.py

    Original: hOWz  It     GoInG?
    After uppercase: HOWZ  IT     GOING?
    After lowercase: howz  it     going?
    After uppercase then capitalize: Howz  it     going?
    After delspace: hOWzItGoInG?

    Original: The      QUIck   brOWn         fOx
    After uppercase: THE      QUICK   BROWN         FOX
    After lowercase: the      quick   brown         fox
    After uppercase then capitalize: The      quick   brown         fox
    After delspace: TheQUIckbrOWnfOx

综上，我们可以发现，方法链有其用处，不过过度使用可能不太好。

本文摘译、修改自[Vasudev Ram](http://jugad2.blogspot.com/2016/02/examples-of-method-chaining-in-python.html)。

**欢迎大家扫描下方二维码关注我的公众号“编程派”，谢谢支持！**

<p style="text-align:center">
    <img src="http://codingpy.com/static/images/wechat-of-codingpy.jpg" alt="编程派的微信公众号二维码" style="width:215px;height:215px">
</p>