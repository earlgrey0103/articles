# 怎样合并字典最符合Python语言习惯？

关键词：idiomatic python, 字典合并, 字典合并方法比较, Python教程, Python国外教程

> 这篇教程探讨了哪种合并字典的方式才是最符合Python语言习惯的（idiomatic）。笔者第一时间翻译出来，与大家一起分享学习。

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

### 多次更新（multiple_update）

下面是一种最简单的合并字典的方式：

	context = {}
	context.update(defaults)
	context.update(user)

这里我们创建了一个新的空字典，并使用其`update`方法从其他字典中添加元素。请注意，我们首先添加的是`defaults`字典中的元素，以保证`user`字典中的重复键会覆盖掉`defaults`中的键。

它满足了全部5个要求，所以这个方法是准确的。它总共有3行代码，不能内联执行，但是代码很清晰。

得分：

- 准确：是。
- 符合语言习惯：比较符合，如果能够内联执行的话就更好了

### 复制，然后更新（copy and update）

另外，我们可以复制`defaults`字典，然后使用`user`来更新复制的字典。

	context = defaults.copy()
	context.update(user)

这种方法与前一种区别不大。

对于本文所探讨的问题，我更喜欢这种复制`defaults`字典的方法，可以很明显地看出`defaults`字典代表了默认值。

得分：

- 准确：是。
- 符合语言习惯：是。

### 字典构造器

我们还可以将需要处理的字典传入字典构造器（`dict()`），这样也能复制字典。

	context = dict(defaults)
	context.update(user)

此法与前一种非常相似， 但是没有前一种直接明了（less explicit）。

得分：

- 准确：是。
- 符合语言习惯：一定程度上符合，不过我更喜欢前两种方案。

### 关键词参数hack（keywords hack）

你以前可能见过下面这个巧妙的解决方法：

	context = dict(defaults, **user)

只有一行代码，看上去很酷嘛。不过，这种解决方法有点难理解。

除了可读性之外，还有一个更严重的问题：这种方案是错的。

字典的键必须是字符串。在Python 2（解释器是CPython）中，我们可以使用非字符串作为键，但别被蒙骗了：这种hack只是凑巧在使用标准CPython运行环境的Python 2中才有效。

得分：

- 准确：否。没有满足第二点要求（键必须有效）
- 符合语言习惯：否。这是一个hack。

### 字典解析（Dictionary comprehension）

我们尝试下使用字典解析式来解决这个问题：

	context = {k: v for d in [defaults, user] for k, v in d.items()}

成功了，但是可读性有点差。

如果我们要处理未知数量的字典，这可能是种好方法，但是我们应该会想把字典解析式拆成多行，提高可读性。在只处理两个字典的情况下，这个双嵌套（double nested）的解析式有点大材小用了。

得分：

- 准确：是。
- 符合语言习惯：可以认为不符合。

### 元素拼接（concatenate items）

假如我们从每个字典中获取一个元素列表，将列表拼接起来，然后再利用拼接的列表在构建新字典？

	context = dict(list(defaults.items()) + list(user.items()))

结果真的成功了。我们可以确定`user`字典中的键值会覆盖掉`defaults`字典中的值，因为`user`字典的元素位于拼接列表的尾部。

在Python 2下，我们不需要先将字典转换成列表，但是本文中我们使用的是Python 3（你也用的是Python 3，对吧？）。

得分：

- 准确：是。
- 符合语言习惯：不特别符合，代码有些重复。

### 元素并集（union items）

在Python 3中，字典的items方法会返回一个dict_items对象，这是一个奇怪对象，居然支持并集操作。

	context = dict(defaults.items() | user.items())

这种方案挺有意思。可惜并不准确。

首先，没有满足第一点要求（`user`字典应该覆盖`defaults`）。因为两个dict_items对象的并集是一个键值对（key-value pairs）的集合，而集合是无序的，所以重复键的处理方法无法预测。

另外，没有满足第三点要求（可以是任意的值），因为集合要求其中元素必须可哈希的，所以键-值元组中的键和值都必须是可哈希的才行。

得分：

- 准确：否。没有满足第一点和第三点要求。
- 符合语言习惯：否。

### Chain items

目前为止，我们讨论的解决方案中，最符合Python语言习惯而且又只有一行代码的实现，是创建两个items的列表，然后拼接并组成新字典。

我们可以使用`itertools.chain`来简化items拼接的过程：

	from itertools import chain
	context = dict(chain(defaults.items(), user.items()))

这种方案效果不错，可能比另外创建两个不必要的列表更加高效。

得分：

准确：是。
符合语言习惯：比较符合，但是有点重复调用items方法。

### ChainMap

ChainMap可以让我们不用遍历初始字典，就创建一个新字典：

	from collections import ChainMap
	context = ChainMap({}, user, defaults)

ChainMap将多个字典打包成一个proxy对象（一个“视图”）；ChainMap查找命令（译者注：如context['name']）会检索其中的字典，直到找到匹配的对象。

这里有几个问题需要回答。

1. 我们为什么把`user`放在`defaults`前面？

将参数按这样的顺序排列的目的，是为了确保满足第一个点要求。ChainMap是按照顺序检索字典的，所以`user`会在`defaults`之前返回匹配的值。

2. 为什么`user`之前有一个空字典？

这是为了满足第五点要求。如果我们修改ChainMap对象，会影响到里面提供的第一个字典。我们不希望`user`发生变化，所以在前面放了一个空字典。

3. 这样真的会返回一个字典吗？

ChainMap对象不是字典，而是类似字典的映射。如果我们的代码中使用鸭子类型（duck typing），使用ChainMap是没问题的，但是需要具体查看ChainMap的特性才能确定。此外，ChainMap对象与其底层的字典是相互勾连的，而且其删除元素的方式也很有趣。

得分：

- 准确：可能准确，需要考虑具体的用例。
- 符合语言习惯：如果我们认为这种实现符合用例，那就是符合习惯的。

## ChainMap转换成字典（dict from ChainMap）

如果我们特别想要字典，可以将ChainMap转换成字典：

context = dict(ChainMap(user, defaults))

需要注意的是，在其他解决方案中，`user`一般出现在`defaults`之后；但是在这里却相反。除了这点外，上面的代码还是比较简单，也明显符合我们的要求。

得分：

- 准确：是。
- 符合语言习惯：是。

## 字典拼接（Dictionary concatenation）

我们能不能把两个字典拼接起来呢？

context = defaults + user

这个想法很好，但可惜却是不合法的。

得分：

- 准确：否。无法执行。
- 符合语言习惯：否。

### 字典拆分（Dictionary unpacking）

如果你在用Python 3.5，你可以使用一种全新的合并字典的方式（对亏了PEP 448）：

	context = {**defaults, **user}

这行代码很简洁，很Pythonic。里面有一些特殊符号，但是很明显最后的结果至少是一个字典。

这段代码在功能上与本文介绍的第一个方案是等价的：在第一个方案中，我们新建了一个空字典，然后依次往里面填充了来自`defaults`和`user`的元素。它满足我们所有的要求，而且很可能是最简单的一个解决方案。

得分：

- 准确：是。
- 符合语言习惯：是。

## 小结

在Python中有许多种合并字典的方法，但是能用一行代码优雅地实现的方法并不多。

如果你使用Python 3.5，那么你应该这样解决合并字典的问题：

	context = {**defaults, **user}

如果你还没有使用Python 3.5，建议你一一查看上面介绍的那些方法，确定哪一种最符合你的需求。


作者：[Trey Hunner](https://treyhunner.com/2016/02/how-to-merge-dictionaries-in-python/)
译者：[EarlGrey](https://codingpy.com)

各种方案的性能比较如下：

multiple_update: 57 ms
copy_and_update: 46 ms
dict_constructor: 56 ms
kwargs_hack: 45 ms
dict_comprehension: 45 ms
concatenate_items: 166 ms
union_items: 163 ms
chain_items: 122 ms
chainmap: 86 ms
dict_from_chainmap: 445 ms
dict_unpacking: 27 ms