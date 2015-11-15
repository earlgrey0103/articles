
How Python Properties Help With Refactoring

Originally published in the Advanced Python Newsletter

Once upon a time, Alice the Python developer had to create a class representing money. Her first implemented version looked like this:

# First version of dollar-centric Money class.
	:::python
	class Money:
	    def __init__(self, dollars, cents):
	        self.dollars = dollars
	        self.cents = cents
	    # Plus some other methods, which we
	    # don't need to worry about here.

This class was packaged into a library, and over time, was used in many different pieces of code, in many different applications. For example, one developer on another team - Bob - used it this way in his code:

	money = Money(27, 12)
	message = "I have {:d} dollars and {:d} cents."
	print(message.format(money.dollars, money.cents))
	# "I have 27 dollars and 12 cents."

	money.dollars += 2
	money.cents += 20
	print(message.format(money.dollars, money.cents))
	# "I have 29 dollars and 32 cents."

This is all fine, but it creates a software maintainability problem. Can you spot it?

Fast forward a few months or years. Alice needs to refactor the internals of the Money class. Instead of keeping track of dollars and cents, she wants the class to just keep track of cents, because it will make certain operations much simpler. Here's the first change she might try to make:

# Second version of Money class.
	class Money:
	    def __init__(self, dollars, cents):
	        self.total_cents = dollars * 100 + cents

This change has a consequence: every line of code referencing a Money object's dollars has to be changed. Sometimes when this happens, you're luckily the maintainer of all the code using this class, and you merely have a refactoring job on your hands. But Alice isn't so lucky here; many other teams are re-using her code. She needs to coordinate her changes with their code base... maybe even going through an excruciatingly long, formal deprecation process. About as fun as visiting the dentist, but it takes longer.

Fortunately, Alice knows a better way, which will let her avoid the whole more-fun-than-going-to-the-dentist thing: The built-in property decorator. @property is applied to a method, and effectively transforms an attribute access into a method call. Let me show you an example. Push that Money class onto your mental stack for a moment, and imagine instead a class representing a person:

	class Person:
	    def __init__(self, first, last):
	        self.first = first
	        self.last = last
	
	    @property
	    def full_name(self):
	        return '{} {}'.format(self.first, self.last)

Look at full_name. It's declared as a very normal method, except being decorated by @property on the line above. This changes how Person objects operate:
	
	>>> buddy = Person('Jonathan', 'Doe')
	>>> buddy.full_name
	'Jonathan Doe'

Note that even though full_name is defined as a method, it is accessed like a member variable attribute. There are no parenthesis in that last line of code; I'm not invoking the method. What we've done is create a kind of dynamic attribute.

Popping back to the Money class, Alice makes the following change:

	# Final version of Money class!
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

In addition to defining the getter for dollars using @property, Alice has also created a setter, using @dollars.setter. And likewise for cents.

What does Bob's code look like now? Exactly the same!

	# His code is COMPLETELY UNCHANGED, yet works
	# with the final Money class. High five!
	money = Money(27, 12)
	message = "I have {:d} dollars and {:d} cents."
	print(message.format(money.dollars, money.cents))
	# "I have 27 dollars and 12 cents."

	money.dollars += 2
	money.cents += 20
	print(message.format(money.dollars, money.cents))
	# "I have 29 dollars and 32 cents."

	# This works correctly, too.
	money.cents += 112
	print(message.format(money.dollars, money.cents))
	# "I have 30 dollars and 44 cents."

None of the code using the Money class has to change at all. Bob doesn't know, or care, that Alice got rid of the dollars and cents attributes: his code keeps working exactly the same as it did before. The only code that changed is in the Money class itself.

Because of how Python does properties, you can freely use simple attributes in your classes. If and when your class changes how it manages state, you can confidently modify that class, and only that class, by creating properties. Everybody wins! In languages like Java, in contrast, one must instead proactively define property access methods (e.g, getDollars or setCents).

Here's something interesting: this is most critical with code that is reused by other developers and teams. Imagine creating a class like Money inside your own application, where you are the only maintainer. Then if you change the class's interface, you can just refactor your code. You don't necessarily need to create properties as described above (though you might want to use them for other reasons.)