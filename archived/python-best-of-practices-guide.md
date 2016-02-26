# Python开发指南：最佳实践精选

> 原文地址：https://gist.github.com/sloria/7001839

## 总体原则
### 价值
- “为别人开发你也想要使用的工具。” ——Kenneth Reitz
- "简洁总是胜过可用。" ——Pieter Hintjens
- "满足90%的使用场景。忽略那些说不的人。" ——Kenneth Reitz
- "优美胜过丑陋。" ——PEP 20
- 为开源（甚至是闭源项目）而开发。

### 一般开发准则
- “明确胜过含蓄。” —— PEP 20
- “易读亦有价。” —— PEP 20
- “人人都能打补丁。” —— 可汗学院开发文档
- 一旦发现破窗（设计错误，决策失误或编码质量低），马上修补。
- “现在做也要胜过不去做。” —— PEP 20
- "测试要彻底。为新功能撰写文档。"
- 更重要的是从测试驱动型开发，转到人力驱动型开发
- 这些准则可能——应该是很可能——会改变。

## 特殊准则
### 风格
合乎情理时，遵循PEP 8。

#### 命名
- 变量、函数、方法、包、模块
  - 小写，并在单词之间使用下划线（lower_case_with_underscores）
- 类、异常
  - 大写单词
- 受保护的方法和内部函数
  - 单下划线开头（_single_leading_underscore(self, ...)） 
- 私有的方法
  - 双下划线开头（__double_leading_underscore(self, ...)）
- 常量
  - 全部大写，单词间用下划线分隔（ALL_CAPS_WITH_UNDERSCORES） 

##### 一般性命名准则
尽量不要使用只有一个字母的变量名（例如，l，I，O等）。

例外：在很简短的代码块中，如果变量名的意思可以从上下文明显地看出来，即可。

**很好**

	for e in elements:
	    e.mutate()

避免重复使用变量名。

**正确的做法**

	import audio
	
	core = audio.Core()
	controller = audio.Controller()

**错误的做法**

	import audio
	
	core = audio.AudioCore()
	controller = audio.AudioController()

“反向标记”更好。

**正确的做法**

	elements = ...
	elements_active = ...
	elements_defunct = ...

**错误的做法**

	elements = ...
	active_elements = ...
	defunct_elements ...


避免使用getter和setter方法。

**正确的做法**

	person.age = 42

**错误的做法**

	person.set_age(42)

#### 缩进

用4个空格符——永远别用Tab制表符。就说这么多。

#### 模块引用

引用整个模块，而不是模块中的独立组成部分。举个例子，假设一个cantee模块下面，有一个sessions.py文件，

**正确的做法**

	import canteen
	import canteen.sessions
	from canteen import sessions

**错误的做法**

	from canteen import get_user  # Symbol from canteen/__init__.py
	from canteen.sessions import get_session  # Symbol from canteen/sessions.py

例外：如果第三方代码的文档中明确说明要引用独立部分，即可。

理由：避免循环引用。看这里。

把代码引用部分放在文件的顶部，按下面的顺序分成三个部分，以一个空行相区分。
1. 系统引用
2. 第三方引用
3. 本地引用

理由：明确显示每个模块的引用来源。

#### 文档
遵循PEP 257提出的文档字符串准则。reStructuredText (reST) 和Sphinx有助于确保文档符合标准。

对于功能明显的函数，使用一行文档字符串。

"""返回``foo``的路径."""

多行文档字符串应包括：

- 一行摘要
- 合适的话描述使用场景
- 参数
- 返回数据类型和语义信息，除非返回None

	:::python
	"""训练一个用来区分Foo和Bar的模型。
	
	用法::
	
	    >>> import klassify
	    >>> data = [("green", "foo"), ("orange", "bar")]
	    >>> classifier = klassify.train(data)
	
	:param train_data:  ``(color, label)``形式的一个元祖列表。
	
	:rtype: A :class:`Classifier <Classifier>`
	
	"""

注意

使用动作性的单词（“返回”），而不是描述性的单词（“返回值”）。
在类的文档字符串中记录`__init__`方法。

	class Person(object):
	    """A simple representation of a human being.
	
	    :param name: A string, the person's name.
	    :param age: An int, the person's age.
	    """
	    def __init__(self, name, age):
	        self.name = name
	        self.age = age

##### 关于注释

尽量少用。与其写很多注释，不如提高代码可读性。通常情况下，短小的方法比注释更有效。

**错误的做法**

	# If the sign is a stop sign
	if sign.color == 'red' and sign.sides == 8:
	    stop()

**正确的做法**
	
	def is_stop_sign(sign):
	    return sign.color == 'red' and sign.sides == 8
	
	if is_stop_sign(sign):
	    stop()

但的确要写注释时，记住：“遵循斯托克与怀特所写的《风格的要素》。” —— PEP 8

#### 每行的长度

不要过分在意。80到100个字符都是没问题的。

使用括号延续当前行。

	wiki = (
	    "The Colt Python is a .357 Magnum caliber revolver formerly manufactured "
	    "by Colt's Manufacturing Company of Hartford, Connecticut. It is sometimes "
	    'referred to as a "Combat Magnum". It was first introduced in 1955, the '
	    "same year as Smith & Wesson's M29 .44 Magnum."
	)

### 测试

尽量争取测试100%的代码，但也不必执着于覆盖率。

#### 一般测试准则

使用较长的、描述性的名称。这经常避免在测试方法走写文档。
测试之间应该是孤立的。不要与真实地数据库或网络进行交互。使用单独的测试数据库，测试完即可销毁，或者是使用模拟对象。
使用工厂模式，而不是fixture。
别让不完整的测试通过，否则你就有可能忘记。你应该加上一些占位数据，比如`assert False, "TODO: finish me"`。

#### 单元测试
每次聚焦在一个很小的功能点。
运行速度要快，但是速度慢总比不测试好。
通常，每一个类或模型都要有一个测试用例。

	import unittest
	import factories
	
	class PersonTest(unittest.TestCase):
	    def setUp(self):
	        self.person = factories.PersonFactory()
	
	    def test_has_age_in_dog_years(self):
	        self.assertEqual(self.person.dog_years, self.person.age / 7)

#### 功能测试

功能测试是更高层次的测试，更接近最终用户如何与应用交互这一层面。通常用在网络和图形应用测试。
按照场景撰写测试。测试用例的测试方法命名应该看上去像场景描述。
在编写代码之前，通过注释说明具体场景信息。

	import unittest
	
	class TestAUser(unittest.TestCase):
	
	    def test_can_write_a_blog_post(self):
	        # Goes to the her dashboard
	        ...
	        # Clicks "New Post"
	        ...
	        # Fills out the post form
	        ...
	        # Clicks "Submit"
	        ...
	        # Can see the new post
	        ...

请注意，测试用例的类名称和测试方法的名称放在一起，就是“测试一名用户能否发布博文”。



## 本文受到下列资料的启发...

- PEP 20 (The Zen of Python)
- PEP 8 (Style Guide for Python)
- The Hitchiker's Guide to Python
- Khan Academy Development Docs
- Python Best Practice Patterns
- Pythonic Sensibilities
- The Pragmatic Programmer
- and many other bits and bytes