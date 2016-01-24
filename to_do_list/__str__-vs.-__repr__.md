# __str__与__repr__之间的区别

According to the official Python documentation, __repr__ is a built-in function used to compute the "official" string reputation of an object, while __str__ is a built-in function that computes the "informal" string representations of an object. So both __repr__ and __str__ are used to represent objects, but in different ways. The best way to understand the difference between these two functions is to see them in action:

	>>>x=4
	>>>repr(x)
	'4'
	>>>str(x)
	'4'
	>>>y='stringy'
	>>>repr(y)
	"'stringy'"
	>>>str(y)
	'stringy'

The returns of repr() and str() are identical for int x, but there's a difference between the return values for str  y -- one is formal and the other is informal. One of the most important differences between the formal and informal representations is that the default implementation of __repr__ for a str value can be called as an argument to eval, and the return value would be a valid string object, like this:

	>>>repr(y)
	"'a string'"
	>>>y2=eval(repr(y))
	>>>y==y2
	True

If you try to call the return value of __str__ as an argument to eval, the result won't be valid.