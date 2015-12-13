> 原文链接：[http://ruslanspivak.com/lsbaws-part1/](http://ruslanspivak.com/lsbaws-part1/)

How Python Properties Help With Refactoring
# 如何使用Python中的@property装饰器重构代码？

Originally published in the Advanced Python Newsletter

从前，Python程序员Alice要打算创建一个代表金钱的类。她的第一个实现形式大概是下面这样：

Once upon a time, Alice the Python developer had to create a class representing money. Her first implemented version looked like this:

	:::python
	# 以美元为基础货币的Money类的首个版本
	class Money:
	    def __init__(self, dollars, cents):
	        self.dollars = dollars
	        self.cents = cents
	    # 还有其他一些方法，我们暂时不必理会

这个类后来被打包到一个Python库里，并且慢慢地被许多不同的应用使用。举个例子，另一个团队中的Python程序员Bob是这样使用Money类的：

	:::python
	money = Money(27, 12)
	message = "I have {:d} dollars and {:d} cents."
	print(message.format(money.dollars, money.cents))
	# "I have 27 dollars and 12 cents."

	money.dollars += 2
	money.cents += 20
	print(message.format(money.dollars, money.cents))
	# "I have 29 dollars and 32 cents."

这样使用并没有错，但是却出现了代码可维护性的问题。你发现了吗？

时间再往前几个月或几年。Alice想要重构Money类的内部实现，不再记录美元和美分，而是仅仅记录美分，因为这样做可以让某些操作简单横多。下面是她很可能会作的修改：


	# Money类的第二个版本
	class Money:
	    def __init__(self, dollars, cents):
	        self.total_cents = dollars * 100 + cents

这一修改带来一个后果：引用Money类的每一行代码都必须要调整。有时候很幸运，你就是所有这些代码的维护者，只需要自己直接重构即可。但是Alice的情况就没有这么好了；许多其他团队都复用了她的代码。因此，她需要协调他们的代码库与自己的修改保持一致，也许甚至要经历一段特别痛苦、漫长的正式弃用过程（deprecation process）。

幸运的是，Alice知道一种更好的解决办法，可以避免这个令人头疼的局面出现：使用Python内建的property装饰器。@property一般应用在Python方法上，可以有效地将属性访问（attribute access）变成方法调用（method call）。举个例子，暂时将Money类抛至一边，假设有一个代表人类的类（class）：

	class Person:
	    def __init__(self, first, last):
	        self.first = first
	        self.last = last
	
	    @property
	    def full_name(self):
	        return '{} {}'.format(self.first, self.last)

请注意`full_name`方法。除了在`def`语句上方装饰了@property之外，该方法的声明没有什么不同的地方。但是，这却改变了`Person`对象的运作方式：
	
	>>> buddy = Person('Jonathan', 'Doe')
	>>> buddy.full_name
	'Jonathan Doe'

我们发现，尽管`full_name`被定义为一个方法，但却可以通过变量属性的方式访问。在最后一行代码中没有`()`操作符；我并没有调用`full_name`方法。我们所做的，可以说是创建了某种动态属性。

回到本文中的Money类，Alice对它作了如下修改：

	# Money类的最终版本
	class Money:
	    def __init__(self, dollars, cents):
	        self.total_cents = dollars * 100 + cents
	
	    # Getter and setter for dollars...
	    @property
	    def dollars(self):
	        return self.total_cents // 100;
	    @dollars.setter
	    def dollars(self, new_dollars):
	        self.total_cents = 100 * new_dollars + self.cents
	
	    # And the getter and setter for cents.
	    @property
	    def cents(self):
	        return self.total_cents % 100;
	    @cents.setter
	    def cents(self, new_cents):
	        self.total_cents = 100 * self.dollars + new_cents

除了使用@property装饰器定义了`dollars`属性的`getter`外，Alice还利用@dollars.setter`创建了一个`setter`。Alice还对`cents`属性作了类似处理。

那么现在，Bob的代码会变成什么样呢？完全和以前一样！

	# 他的代码完全没有变动，但是却可以正常调用Money类。
	money = Money(27, 12)
	message = "I have {:d} dollars and {:d} cents."
	print(message.format(money.dollars, money.cents))
	# "I have 27 dollars and 12 cents."

	money.dollars += 2
	money.cents += 20
	print(message.format(money.dollars, money.cents))
	# "I have 29 dollars and 32 cents."

	# 代码逻辑也没有问题。
	money.cents += 112
	print(message.format(money.dollars, money.cents))
	# "I have 30 dollars and 44 cents."

事实上，所有使用了Money类的代码都不需要进行修改。Bob不知道或根本不在乎Alice去除了类中的dollars和cents属性：他的代码还是和以前一样正常执行。唯一修改过的代码就是Money类本身。

正是由于Python中处理装饰器的方式，你可以在类中自由使用简单的属性。如果你所写的类改变了管理状态的方法，你可以自信地通过@property装饰器对这个类（且只有这个类）进行修改。每个人都不会有损失！相反，在类似Java等语言中，程序员必须主动去定义访问属性的方法（例如，`getDollars`或`setCents`）。

最后要提示大家：这个问题对于那些被其他程序员和团队复用的代码最为重要。假设仅仅是在你自己一个维护的应用中创建一个类似Money的类，那么如果你改变了Money的接口，你只需要重构自己的代码就可以。这种情况下，你没有必要像上面说的那样使用@property装饰器。
