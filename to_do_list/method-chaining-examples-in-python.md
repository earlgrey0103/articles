http://jugad2.blogspot.com/2016/02/examples-of-method-chaining-in-python.html

方法链（method chaining）是面向对象的编程语言中的一种常见语法，可以让开发者在只引用对象一次的情况下，对同一个对象进行多次方法调用。举个例子：

假设我们有一个Foo类，其中包含有两个方法——`bar`和`baz`。

我们创建一个Foo类的实例：

    foo = Foo()

如果不使用方法链，要想连续调用对象`foo`的`bar`和`baz`方法的话，我们得这样做：

    foo.bar() # Call method bar() on object foo.
    foo.baz() # Call method baz() on object foo.

如果使用方法链的话，我们就能这样实现：
    foo.bar().baz()

So you can loosely think of method chaining as the object-oriented version of nested function calls in procedural programming, where, instead of this:
# Fragment 3
temp1 = foo(args)
result = bar(temp)
you would do this:
# Fragment 4
result = bar(foo(args))
We use nested function calls all the time in procedural programming, and even in the procedural sections of code that occur in a Python program that uses OOP. We can do the latter because Python supports both styles (procedural and object-oriented) at the same time, even in the same program; Guido be thanked for that :)

The above was my informal description of method chaining. For more details, refer to this Wikipedia article, which includes examples in various programming languages. The article also makes a distinction between method chaining and method cascading, and according to it, what I call method chaining here (involving returning the self reference) is really method cascading. Are you confused enough? :) Kidding, the difference is not really complex.

One advantage of method chaining is that it reduces the number of times you have to use the name of the object: only once in Fragment 2 above, vs. twice in Fragment 1; and this difference will increase when there are more method calls on the same object. Thereby, it also slightly reduces the amount of code one has to read, understand, test, debug and maintain, overall. Not major benefits, but can be useful.

Note: One limitation of method chaining is that it can only be used on methods which do not need to return any other meaningful value, such as a count of lines modified, words found, records deleted, etc. (which some methods need to do), because you need to return the self object. Even the fact that Python (and some other languages) support returning multiple values from a return statement, may not solve this. (There could be some workaround for this, but it might look awkward, is my guess.)

Simple method chaining can be implemented easily in Python.

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
person.name("Peter").age(21).introduce()
# => Hello, my name is Peter and I am 21 years old.

Here is one way of doing it:
# foo_bar_baz.py
# Demonstrates method chaining.

class Foo(object):
    def bar(self):
        print "Method Foo.bar called"
        return self

    def baz(self):
        print "Method Foo.baz called"
        return self

foo = Foo()
# Saving return value in foo2 not needed;
# doing to use with id function below.
foo2 = foo.bar().baz()
print

# We can also do it like this, if we don't want 
# to save the object foo for later use:
Foo().bar().baz()
print

# Show that the original foo's id and the returned foo2's id 
# are the same, i.e. they are the same object:
print " id(foo):", id(foo)
print "id(foo2):", id(foo2)
Here is the output of running the above program:
$ python foo_bar_baz.py
Method Foo.bar called
Method Foo.baz called

Method Foo.bar called
Method Foo.baz called

 id(foo): 34478576
id(foo2): 34478576
While writing this post, I also searched for more information, and found a couple of interesting links on method chaining:

Stack Overflow question on method chaining in Python, with some other approaches.

ActiveState Code Python recipe on method chaining

I also wrote another small program, string_processor.py, which shows a somewhat more realistic situation in which one might want to use method chaining:
'''
Program: string_processor.py
Demo of method chaining in Python.
By: Vasudev Ram - 
http://jugad2.blogspot.in/p/about-vasudev-ram.html
Copyright 2016 Vasudev Ram
'''

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
Does adding the rep() and dup() make it more methodical? :)

Here is the output of running it:
$ python string_processor.py
Demo of method chaining in Python:

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
So, to sum up, we can see that method chaining has its uses, though overdoing it is probably not a good idea.

Method chaining, also known as named parameter idiom, is a common syntax for invoking multiple method calls in object-oriented programming languages. Each method returns an object, allowing the calls to be chained together in a single statement without requiring variables to store the intermediate results.[1] Local variable declarations are syntactic sugar because of the difficulty humans have with deeply nested method calls.[2][3] A method chain is also known as a train wreck due to the increase in the number of methods that come one after another in the same line that occurs as more methods are chained together[4] even though line breaks are often added between methods.

A similar syntax is method cascading, where after the method call the expression evaluates to the current object, not the return value of the method. Cascading can be implemented using method chaining by having the method return the current object itself. Cascading is a key technique in fluent interfaces, and since chaining is widely implemented in object-oriented languages while cascading isn't, this form of "cascading-by-chaining by returning this" is often referred to simply as "chaining". Both chaining and cascading come from the Smalltalk language.