# 升级到Python 3.6后，你需要注意些什么？

关键词：python 3.6, Python 3.6新特性, Python废弃的方法, 格式化字符串字面量, PYTHONMALLOC, pyvenv脚本使用, 生成器StopIteration

4月8日，[Python官网文档](https://docs.python.org/3.6/whatsnew/3.6.html)中更新了3.6版本的新特性介绍。当然，这其中介绍的特性还不是最终版，随着不断的开发完善，可能会出现更新和变化。

新版本中大致会推出以下特性：

1. [PEP 498](https://www.python.org/dev/peps/pep-0498/#rationale)：格式化字符串字面量
2. 新增[PYTHONMALLOC](https://docs.python.org/3.6/using/cmdline.html#envvar-PYTHONMALLOC)环境变量
3. [PEP 495](https://www.python.org/dev/peps/pep-0495/#rationale)：当地时间消歧（local time disambiguation）

详细内容请点击对应链接了解。 

## Python 3.6时间表

根据[Python 3.6发布时间表](https://www.python.org/dev/peps/pep-0494/)，Python 3.6于去年5月24日开始开发，最终版将于今年12月16日正式发布。目前处于alpha 0阶段。

具体计划如下：

- 3.6.0 alpha 1: 2016-05-15
- 3.6.0 alpha 2: 2016-06-12
- 3.6.0 alpha 3: 2016-07-10
- 3.6.0 alpha 4: 2016-08-07
- 3.6.0 beta 1: 2016-09-07
(此后不再增加新特性。)

- 3.6.0 beta 2: 2016-10-02
- 3.6.0 beta 3: 2016-10-30
- 3.6.0 beta 4: 2016-11-20
- 3.6.0 candidate 1: 2016-12-04
- 3.6.0 candidate 2 (如果需要的话): 2016-12-11
- 3.6.0 final: 2016-12-16

## 升级后，要注意哪些事情？

那么除了新增的特性之外，如果我们升级到3.6的话，还有那些地方需要注意吗？

根据目前的介绍，Python 3.6中还将废弃一些模块、函数、方法和特性，值得以后注意。具体主要包括以下几个方面。

### 新关键字

Python 3.5中引入了`async`和`await`，*不建议将这两个名称用作变量名、类名、函数名和模块名*。它们将在Python 3.7中正式成为关键字。

### 废弃的方法

3.6中正式废弃使用`mportlib.machinery.SourceFileLoader.load_module()`和`importlib.machinery.SourcelessFileLoader.load_module()`方法。

### 废弃的特性

`pyvenv`脚本被废弃，*鼓励使用`python3 -m venv`*。这样可以避免搞错pyvenv所关联的版本。

### 废弃的行为

在生成器内部触发`StopIteration`异常时，会生成一个`DeprecationWarning`，到Python 3.7版本时，则会引发运行时错误。具体见[PEP 479](https://www.python.org/dev/peps/pep-0479/#rationale)。

