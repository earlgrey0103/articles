> 原文链接：[https://www.airpair.com/python/posts/python-tips-and-traps][1]
> 译文链接：
## 1. 引言

Python语言博大精深，用途广泛，已被大量应用于系统自动化、网络应用、大数据、统计分析和安全软件等领域。本文旨在介绍一些不太为人所知的技巧，帮助你实现更快地开发，更简单地调试，并且保持工作的乐趣。

与其他语言一样，一旦掌握Python语言之后，你所得到的真正资源并不是仅限于这种语言的超能力。而是灵活使用Python相关惯用法、第三方库以及Python社区集体智慧的能力。

## 标准数据类型
### 谦卑的`enumerate`
Python中遍历对象中的内容很简单，只需要使用for循环即可，例如`for foo in bar:`。

	drinks = ["coffee", "tea", "milk", "water"]()
	for drink in drinks:
		print("thirsty for", drink)
	# thirsty for coffee
	# thirsty for tea
	# thirsty for milk
	# thirsty for water

但是除了获取每个元素之外，我们还经常需要知道这些元素的索引值。Python程序员经常使用`len()`和`range()`两个函数，根据索引值来遍历列表，但是还有一种更简便的方法。

	drinks = ["coffee", "tea", "milk", "water"]()
	for index, drink in enumerate(drinks):
		print("Item {} is {}".format(index, drink))
	# Item 0 is coffee
	# Item 1 is tea
	# Item 2 is milk
	# Item 3 is water

内建的`enumerate`函数可以返回元素及其索引值。

## `set`的成员
集合（`set`）数据类型支持许多中操作。想确保列表中没有重复的元素？需知道两个列表中有哪些相同的元素？Python中的`set`可以让你快速实现这些操作。

	# 列表元素*快速*去重
	print(set(["ham", "eggs", "bacon", "ham"]()))
	# {'bacon', 'eggs', 'ham'}


	# 比较列表，得出相同或不同的元素
	# {} without "key":"value" pairs makes a set
	menu = {"pancakes", "ham", "eggs", "bacon"}
	new_menu = {"coffee", "ham", "eggs", "bacon", "bagels"}

	new_items = new_menu.difference(menu)
	print("Try our new", ", ".join(new_items))
	# Try our new bagels, coffee

	discontinued_items = menu.difference(new_menu)
	print("Sorry, we no longer have", ", ".join(discontinued_items))
	# Sorry, we no longer have pancakes


	old_items = new_menu.intersection(menu)
	print("Or get the same old", ", ".join(old_items))
	# Or get the same old eggs, bacon, ham

	full_menu = new_menu.union(menu)
	print("At one time or another, we've served:", ", ".join(full_menu))
	# At one time or another, we've served: coffee, ham, pancakes, bagels, bacon, eggs

## `intersection`函数会对比所有的元素，返回两个集合中的相同元素。在上面的例子中，返回的是bacon，eggs和ham。

## `collections.namedtuple`
如果你不需要往类中添加方法，但是想保留`offoo.prop`带来的便利，那么使用`namedtuple`就再好不过了。你可以提前定义属性，然后实例化一个轻量级的类，它占用的内存比完整的对象要少。

	LightObject = namedtuple('LightObject', ['shortname', 'otherprop']())
	m = LightObject()
	m.shortname = 'athing'
	> Traceback (most recent call last):
	> AttributeError: can't set attribute

元组的成员无法更改，同样你也不能改变`namedtuple`中的属性。你必须在创建`namedtuple`实例时，就设置好相应的属性。

	LightObject = namedtuple('LightObject', ['shortname', 'otherprop']())
	n = LightObject(shortname='something', otherprop='something else')
	n.shortname # something


## `collections.defaultdict`

Python应用中经常需要应对这样的逻辑情况，即字典中一开始不存在某个哈希键。

	login_times = {}
	for t in logins:
		if login_times.get(t.username, None):
			login_times[t.username]().append(t.datetime)
		else:
			login_times[t.username]() = [t.datetime]()

通过`defaultdict`，你可以指定访问未定义的哈希键时，返回一个空列表（或任何其他类型），这样就避免了上面所说的情况。

	login_times = collections.defaultdict(list)
	for t in logins:
		login_times[t.username]().append(t.datetime)

你甚至可以使用自定义的类，前提是已有用于构建该类的调用函数。

	from datetime import datetime
	class Event(object):
		def __init__(self, t=None):
			if t is None:
				self.time = datetime.now()
			else:
				self.time = t

	events = collections.defaultdict(Event)

	for e in user_events:
	print(events[e.name]().time)

如果不满足`defaultdict`所提供的能力，想将嵌套哈希键设置为属性的话，可以考虑使用[`addict`包](https://github.com/mewwts/addict)

	normal_dict = {
	    'a': {
	        'b': {
	            'c': {
	                'd': {
	                    'e': 'really really nested dict'
	                }
	            }
	        }
	    }
	}

	from addict import Dict
	addicted = Dict()
	addicted.a.b.c.d.e = 'really really nested'
	print(addicted)
	# {'a': {'b': {'c': {'d': {'e': 'really really nested'}}}}}

这个代码段比起标准的字典类型更容易编写，但是如果使用`defaultdict`呢？看上去那样似乎也比较简单。

	from collections import defaultdict
	default = defaultdict(dict)
	default['a']['b']['c']['d']['e'] = 'really really nested dict' # fails

上面的代码看上去没问题，但是实际上却会抛出KeyError异常，因为`default['a']`是字典，而不是`defaultdict`。

That looks ok, but it will actually throw a KeyError exception because default['a']()is a dict, not a defaultdict. Let's make a defaultdict that defaults to defaulted dictionaries (say that a couple times fast).
If you just need a defaulted counter, you can use the collections.Counter class which provides some convenience functions like most_common.
Control Flow
When learning control structures in Python, it's common to go over for, while, if-elif-else, and try-except. Properly used, those few control structures can handle most every case. There's a reason equivalents exist in almost every language you run across. Python also offers some additions to the basic structures that aren't often used, but can make your code more readable and easier to maintain.
Great Exceptations
Exceptions as flow control is a common pattern when dealing with databases, sockets, files, or any resource that is likely to fail. With the standard try and exceptsomething simple like working with a database might look like this.
try:
# get API data
data = db.find(id='foo') # may raise exception
# manipulate the data
db.add(data)
# save it again
db.commit() # may raise exception
except Exception:
# log the failure
db.rollback()

db.close()












Can you spot the problem here? There are two possible exceptions that will trigger the same except block. Meaning that failure to find the data (or to connect to find the data) would cause a rollback attempt. This almost definitely isn't what we want, because a failure at that point wouldn't have even begun a transaction yet. A rollback also probably isn't the right response to a connection failure, so let's break these cases apart.
First, we'll handle finding the data.
try:
# get API data
data = db.find(id='foo') # may raise exception
except Exception:
# log the failure and bail out
log.warn("Could not retrieve FOO")
return

# manipulate the data
db.add(data)










Now that the data retrieval has its own try-except we can take whatever action makes sense if we don't have any data to work with. It's not likely our code will do anything useful without data, so we'll just exit the function. Instead of exiting you could also make a default object, retry the query, or kill the entire program.
Now let's wrap the commit so it fails gracefully as well.
try:
db.commit() # may raise exception
except Exception:
log.warn("Failure committing transaction, rolling back")
db.rollback()
else:
log.info("Saved the new FOO")
finally:
db.close()









We've actually added two clauses here. First, let's look at the else, which runs if no exception occurs. In our example, all it does is log that the transaction succeeded, but you could put more interesting actions in as needed. One potential use would be to fire off a background job or notification.
The finally clause is there to make it clear that the db.close() will always run. Looking back, we can see that all the code related to persisting our data ended up in a nice logical grouping at the same indentation level. Editing this code later, it will be easy for us to see that all these lines are tied to the commit.
Context and Control
We've seen control flow using exceptions before. In general, the steps are something like:
1.	Attempt to acquire a resource (file, network connection, whatever)
2.	If it fails, clean up anything left behind
3.	Otherwise, perform actions on the resource
4.	Log what happened
5.	Program complete
With that in mind, let's take a second look at the database example from the last section. We used try-except-finally to make sure that any transaction we began was either committed or rolled back.
try:
# attempt to acquire a resource
db.commit()
except Exception:
# If it fails, clean up anything left behind
log.warn("Failure committing transaction, rolling back")
db.rollback()
else:
# If it works, perform actions
# In this case, we just log success
log.info("Saved the new FOO")
finally:
# Clean up
db.close()
# Program complete















Our previous example mapped to the steps above almost exactly. But how much of this logic ever changes? Not very much.
Just about every time we save data, we'll do these exact same steps. We could pull this logic into a method, or we could use a context manager.
db = db_library.connect("fakesql://")
# as a function
commit_or_rollback(db)

# context manager
with transaction("fakesql://") as db:
# retrieve data here
# modify data here








A context manager makes it easy to protect some block by setting up resources (context) that the block needs at runtime. In our example, we need a database transaction that will be:
1.	Connected to a database
2.	Started at the beginning of the block
3.	Committed or rolled back at the end of the block
4.	Cleaned up at the end of the block
Let's build a context manager that will hide all this database setup for us. Thecontextmanager interface is simple. The object is required to have a __enter__()method to set up whatever context is needed and a __exit__(exc_type, exc_val, exc_tb) method that will be called at the end of the block. If there was no exception, then all three of the exc_* arguments will be None.
The __enter__ method will be pretty simple, so let's start with that.
class DatabaseTransaction(object):
def __init__(self, connection_info):
self.conn = db_library.connect(connection_info)

def __enter__(self):
return self.conn






The __enter__ method actually does nothing except return the database connection, which we can use inside the block to retrieve or save data. The __init__method is where the connection is actually made, and if it fails the block won't run at all.
Now let's define how the transaction will be finished in the __exit__ method. This has a lot more to it, since it has to handle any exceptions thrown in the block and close out the transaction.
def __exit__(self, exc_type, exc_val, exc_tb):
if exc_type is not None:
self.conn.rollback()

try:
self.conn.commit()
except Exception:
self.conn.rollback()
finally:
self.conn.close()










Now we can use our DatabaseTransaction as the context manager for our block of actions. Under the hood, the __enter__ and __exit__ methods will run and handle setting up the database connection and tear it down when we're through.
# context manager
with DatabaseTransaction("fakesql://") as db:
# retrieve data here
# modify data here




To improve our (primitive) transaction manager, we could add handling for different exception types. Even in its current state, this hides a ton of complexity that you don't need to be worrying about every time you pull in something from the database.
Generators
Introduced in Python 2, generators are a simple way to implement an iterator that doesn't hold all its values at once. Typically a function in Python starts its execution, does some operations, and returns the result (or nothing).
Generators are different.
def my_generator(v):
yield 'first ' + v
yield 'second ' + v
yield 'third ' + v

print(my_generator('thing'))
# \<generator object my_generator at 0x....\>







Instead of return we use the yield keyword, which is what makes a generator special. When calling my_generator('thing') instead of getting the result of the function we get a generator object, which can be used anywhere you could use a list or other iterable.
Most often, you'll use generators as part of a loop as below. The loop will continue until the generator stops yielding values.
for value in my_generator('thing'):
print value

# first thing
# second thing
# third thing

gen = my_generator('thing')
next(gen)
# 'first thing'
next(gen)
# 'second thing'
next(gen)
# 'third thing'
next(gen)
# raises StopIteration exception
















After being instantiated, a generator doesn't do anything until it is asked for a value. It will execute until the first yield and pass that value to the caller, then wait (saving its state) until another value is requested.
Now let's make a generator that's a bit more useful than just giving back 3 hard-coded items. The classic generator example is an endless fibonacci generator, so let's give that a try. It will start at 1 and give the sum of the prior two numbers for as long as you ask it to.
def fib_generator():
a = 0
b = 1
while True:
yield a
a, b = b, a + b






A while True loop in a function would normally be something to avoid because the function would never return, but for a generator it's fine as long as there's a yield in the loop. We do need to be careful to have an end condition when we use this generator, because it will happily add numbers forever.
Now let's use our generator to calculate the first fibonacci number that's greater than 10,000.
min = 10000
for number in fib_generator():
if number \> min:
print(number, "is the first fibonacci number over", min)
break





That was pretty easy, and we can make that number as large as we want and it will still (eventually) come up with the first number larger than X in the fibonacci sequence.
Let's try out a more practical example. Paginating APIs is common practice to limit usage and avoid sending 50 megabytes of JSON (!!!) to a mobile device. First, we'll define the API we're using and then we'll write a generator around it to hide the paging from our code.
The API we're using is called Scream, a place where users can argue about restaurants they've eaten at or want to eat at. Their API for searching is pretty simple, and looks like this.
GET http://scream-about-food.com/search?q=coffee
{
"results": [
](){"name": "Coffee Spot",
 "screams": 99
},
{"name": "Corner Coffee",
 "screams": 403
},
{"name": "Coffee Moose",
 "screams": 31
},
{...}
]
"more": true,
"_next": "http://scream-about-food.com/search?q=coffee?p=2"
}

















Neat! They embedded the link to the next page in the API response so it'll be extremely easy to get the next page when it's time. We can also leave off the page number to just get the first page. To get the data, we'll use the always-handy requestslibrary and wrap it in a generator to display our search results.
The generator will handle pagination and have limited retry logic, and will work something like:
1.	Receive search term
2.	Query the scream-about-food API
3.	Try again if the API fails
4.	Yield the results from the page it gets one at a time
5.	Get the next page if there is one
6.	Exit when there are no more results
Easy enough. To start with, we'll implement the generator without retries to keep the code simple.
import requests

api_url = "http://scream-about-food.com/search?q={term}"

def infinite_search(term):
url = api_url.format(term)
while True:
data = requests.get(url).json()

for place in data['results']():
yield place

# end if we've gone through all the results
if not data['more'](): break

url = data['_next']()
















When you create a generator, you only need to pass in search terms and the generator will build the query and get results as long as they exist. There are (of course) some rough edges here. Exceptions aren't handled at all, and if the API fails or returns unexpected JSON the generator will raise an exception.
Despite these rough spots, we can still use it to find out what number our restaurant is in the search results for the term "coffee".
# pass a number to start at as the second argument if you don't want
# zero-indexing
for number, result in enumerate(infinite_search("coffee"), 1):
if result['name']() == "The Coffee Stain":
print("Our restaurant, The Coffee Stain is number ", number)
return
print("Our restaurant, The Coffee Stain didnt't show up at all! :(")







The generator handles iterating over each page of search results, so all we have to do is use the enumerate builtin from earlier in the article to keep track of the number of results and print them when we find our shop.
As an exercise, go ahead and add a counter to the infinite_search generator so we can write code like this instead.
for result in infinite_search("coffee"):
if result['name']() == "The Coffee Stain":
print("Our restaurant, The Coffee Stain is number ", result['number']())
return
print("Our restaurant, The Coffee Stain didn't show up at all! :(")





If you write Python 3, you already use generators when you use the standard library. Calls like dict.items() now return generators instead of lists. To get this behavior in Python 2 dict.iteritems() was added, but isn't as frequently used.
Python 2 and 3 compatibility
Moving from Python 2 to Python 3 can be an undertaking for any codebase (or any developer) but it's possible to write code that runs in both. Support for Python 2.7 will continue until 2020, but it's unlikely that many new features will be backported. For now, it's recommended to support Python 2.7 and 3+ unless it's feasible for you to drop Python 2 support entirely.
For a comprehensive guide on supporting both versions, see the Porting Python 2 Code guide from python.org.
Let's look over the most common things you'll run into when trying to write compatible code, and how to use __future__ to work around them.
print or print()
Just about every developer who has switched from Python 2 to 3 has typed the wrongprint statement. Fortunately, you can standardize on using print as a function (Python 3 style) instead of a keyword by just importing print_function.
print "hello"  # Python 2
print("hello") # Python 3

from __future__ import print_function
print("hello") # Python 2
print("hello") # Python 3






Divided Over Division
The default behavior for division in Python also changed between 2 and 3. In Python 2, dividing integers would perform integer-only division, chopping off any trailing decimals. This wasn't what most users expected, so it was changed in Python 3 to use floating point division even when dividing integers.
print(1 / 3) # Python 2
# 0
print(1 / 3) # Python 3
# 0.3333333333333333
print(1 // 3) # Python 3
# 0






This sort of behavior change brings in a bunch of subtle bugs when writing code to run in both major versions. Again, we're saved by the __future__ module. Importingdivision makes these behaviors identical in both versions.
from __future__ import division
print(1 / 3)# Python 2
# 0.3333333333333333
print(1 // 3)# Python 2
# 0
print(1 / 3) # Python 3
# 0.3333333333333333
print(1 // 3)# Python 3
# 0


Fin - Thanks for Reading
Thanks for reading, I hope you learned at least one thing. If you have something to add (or correct, no writer is perfect) I'll be checking the comments section frequently. If you enjoyed this article, you might want to check out this one on list and dictcomprehensions or a more in-depth treatment of Python 2 and 3
Thanks to commenters dalke (on HackerNews), György Kiss, mikemikemikemikemike, Karl-Aksel Puulmann, Bartłomiej "furas" Burek, and Peter Venable for finding errors and omissions in this article.

[1]:	https://www.airpair.com/python/posts/python-tips-and-traps
[12]:	https://github.com/mewwts/addict "addict包"
