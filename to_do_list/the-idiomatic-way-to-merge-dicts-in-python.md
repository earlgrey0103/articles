# 怎样以符合Python习惯的方式合并字典？

关键词：idiomatic python, 字典合并, 字典合并方法比较, Python教程, Python国外教程

> 这篇教程这两天在Hacker News和Reddit比较热门，探讨了哪种合并字典的方式才是最符合Python语言习惯的（idiomatic）。笔者第一时间翻译出来，与大家一起分享学习。另外，在文末做一个小调查，大家喜欢早上还是晚上阅读Python教程？

你有没有想过在Python中合并两个或以上字典？

有很多种方法可以解决这个问题：有些比较拙劣，有些不准确，而且大部分都要许多行代码。

接下来我们一一介绍解决这个问题的不同方法，一起探讨到底哪一种是最Pythonic的。

## 我们的问题

在讨论解决方案之前，我们需要明确定义问题。

我们的代码中有两个字典：`user`和`defaults`。我们希望将二者合并至一个叫`context`的新字典里。

需要满足以下要求：

1. 如果存在重复的键，`user`字典中的值应覆盖`defaults`字典中的值；
2. `defaults`和`user`中的键可以是任意合法的键；
3. `defaults`和`user`中的值可以是任意值；
4. 在创建`context`字典时，`defaults`和`user`的元素不能出现变化；
5. 更新`context`字典时，不能更改`defaults`或`user`字典。

注意：对于第五个要求，我们关注的是对字典的更新，而不是其中包含的对象。如果担心字典中嵌套对象的可变性，我们可以考虑使用copy.deepcopy。

基本上，我们希望实现下面的操作：

>>> user = {'name': "Trey", 'website': "http://treyhunner.com"}
>>> defaults = {'name': "Anonymous User", 'page_name': "Profile Page"}
>>> context = merge_dicts(defaults, user)  # magical merge function
>>> context
{'website': 'http://treyhunner.com', 'name': 'Trey', 'page_name': 'Profile Page'}

我们还要考虑解决方法是否Pythonic。但是这又是非常主观的。下面是我们使用的一些评判标准：

- 解决方法应该简洁，但不简短；
- 解决方法应该可读，但不过度冗长；
- 可能的话，解决方法应该为一行代码，需要的话可以内联化（written inline）；
- 解决方法的效率不应该太低。

## 可能的解决方法

既然定义完了需要解决的问题，接下来我们探讨下都有哪些解决方法，并分析其中哪个最准确，哪个最符合Python语言习惯。

### 多次更新

下面是一种最简单的合并字典的方式：

	context = {}
	context.update(defaults)
	context.update(user)

这里我们创建了一个新的空字典，并使用其`update`方法从其他字典中添加元素。请注意，我们首先添加的是`defaults`字典中的元素，以保证`user`字典中的重复键会覆盖掉`defaults`中的键。

它满足了全部5个要求，所以这个方法是准确的。它总共有3行代码，不能内联执行，但是代码很清晰。

得分：

- 准确：是。
- 符合语言习惯：比较符合，如果能够内联执行的话就更好了

### 复制，然后更新

Alternatively, we could copy defaults and update the copy with user.

context = defaults.copy()
context.update(user)
This solution is only slightly different from the previous one.

For this particular problem, I prefer this solution of copying the defaults dictionary to make it clear that defaults represents default values.

Score:

Accurate: yes
Idiomatic: yes
Dictionary constructor

We could also pass our dictionary to the dict constructor which will also copy the dictionary for us:

context = dict(defaults)
context.update(user)
This solution is very similar to the previous one, but it’s a little bit less explicit.

Score:

Accurate: yes
Idiomatic: somewhat, though I’d prefer the first two solutions over this
Keyword arguments hack

You may have seen this clever answer before, possibly on StackOverflow:

context = dict(defaults, **user)
This is just one line of code. That’s kind of cool. However, this solution is a little hard to understand.

Beyond readability, there’s an even bigger problem: this solution is wrong.

The keys must be strings. In Python 2 (with the CPython interpreter) we can get away with non-strings as keys, but don’t be fooled: this is a hack that only works by accident in Python 2 using the standard CPython runtime.

Score:

Accurate: no. Requirement 2 is not met (keys may be any valid key)
Idiomatic: no. This is a hack.
Dictionary comprehension

Just because we can, let’s try doing this with a dictionary comprehension:

context = {k: v for d in [defaults, user] for k, v in d.items()}
This works, but this is a little hard to read.

If we have an unknown number of dictionaries this might be a good idea, but we’d probably want to break our comprehension over multiple lines to make it more readable. In our case of two dictionaries, this doubly-nested comprehension is a little much.

Score:

Accurate: yes
Idiomatic: arguably not
Concatenate items

What if we get a list of items from each dictionary, concatenate them, and then create a new dictionary from that?

context = dict(list(defaults.items()) + list(user.items()))
This actually works. We know that the user keys will win out over defaults because those keys come at the end of our concatenated list.

In Python 2 we actually don’t need the list conversions, but we’re working in Python 3 here (you are on Python 3, right?).

Score:

Accurate: yes
Idiomatic: not particularly, there’s a bit of repetition
Union items

In Python 3, items is a dict_items object, which is a quirky object that supports union operations.

context = dict(defaults.items() | user.items())
That’s kind of interesting. But this is not accurate.

Requirement 1 (user should “win” over defaults) fails because the union of two dict_items objects is a set of key-value pairs and sets are unordered so duplicate keys may resolve in an unpredictable way.

Requirement 3 (the values can be anything) fails because sets require their items to be hashable so both the keys and values in our key-value tuples must be hashable.

Side note: I’m not sure why the union operation is even allowed on dict_items objects. What is this good for?

Score:

Accurate: no, requirements 1 and 3 fail
Idiomatic: no
Chain items

So far the most idiomatic way we’ve seen to perform this merge in a single line of code involves creating two lists of items, concatenating them, and forming a dictionary.

We can join our items together more succinctly with itertools.chain:

from itertools import chain
context = dict(chain(defaults.items(), user.items()))
This works well and may be more efficient than creating two unnecessary lists.

Score:

Accurate: yes
Idiomatic: fairly, but those items calls seem slightly redundant
ChainMap

A ChainMap allows us to create a new dictionary without even looping over our initial dictionaries (well sort of, we’ll discuss this):

from collections import ChainMap
context = ChainMap({}, user, defaults)
A ChainMap groups dictionaries together into a proxy object (a “view”); lookups query each provided dictionary until a match is found.

This code raises a few questions.

Why did we put user before defaults?

We ordered our arguments this way to ensure requirement 1 was met. The dictionaries are searched in order, so user returns matches before defaults.

Why is there an empty dictionary before user?

This is for requirement 5. Changes to ChainMap objects affect the first dictionary provided and we don’t want user to change so we provided an empty dictionary first.

Does this actually give us a dictionary?

A ChainMap object is not a dictionary but it is a dictionary-like mapping. We may be okay with this if our code practices duck typing, but we’ll need to inspect the features of ChainMap to be sure. Among other features, ChainMap objects are coupled to their underlying dictionaries and they handle removing items in an interesting way.

Score:

Accurate: possibly, we’ll need to consider our use cases
Idiomatic: yes if we decide this suits our use case
Dictionary from ChainMap

If we really want a dictionary, we could convert our ChainMap to a dictionary:

context = dict(ChainMap(user, defaults))
It’s a little odd that user must come before defaults in this code whereas this order was flipped in most of our other solutions. Outside of that oddity, this code is fairly simple and should be clear enough for our purposes.

Score:

Accurate: yes
Idiomatic: yes
Dictionary concatenation

What if we simply concatenate our dictionaries?

context = defaults + user
This is cool, but it isn’t valid. This was discussed in a python-ideas thread last year.

Some of the concerns brought up in this thread include:

Maybe | makes more sense than + because dictionaries are like sets
For duplicate keys, should the left-hand side or right-hand side win?
Should there be an updated built-in instead (kind of like sorted)?
Score:

Accurate: no. This doesn’t work.
Idiomatic: no. This doesn’t work.
Dictionary unpacking

If you’re using Python 3.5, thanks to PEP 448, there’s a new way to merge dictionaries:

context = {**defaults, **user}
This is simple and Pythonic. There are quite a few symbols, but it’s fairly clear that the output is a dictionary at least.

This is functionally equivalent to our very first solution where we made an empty dictionary and populated it with all items from defaults and user in turn. All of our requirements are met and this is likely the simplest solution we’ll ever get.

Score:

Accurate: yes
Idiomatic: yes
Summary

There are a number of ways to combine multiple dictionaries, but there are few elegant ways to do this with just one line of code.

If you’re using Python 3.5, this is the one obvious way to solve this problem:

context = {**defaults, **user}
If you are not yet using Python 3.5, you’ll need to review the solutions above to determine which is the most appropriate for your needs.