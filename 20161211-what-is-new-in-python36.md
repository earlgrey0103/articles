# Python 3.6 即将发布，都有哪些新特性？

根据[PEP 494](https://www.python.org/dev/peps/pep-0494/)，Python 3.6 预计于下周五（12 月 16 日）发布最终版。截止目前，PSF 已经发布了 9 个测试版本。

在新版本正式发布之前，我们一起来体验一下都会有哪些重要的新特性。

## 1. 格式化字符串字面量

[PEP 498](https://www.python.org/dev/peps/pep-0498)引入了 f-string，一种新型的字符串字面量。中文翻译为**“格式化字符串字面量”**。

这种字符串以 `f` 为前缀，类似 `str.format()` 方法所接受的字符串。其中的可替换字段用 `{}` 包裹起来，在运行时进行求值。

具体代码示例：

```python
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}"  # nested fields
'result:      12.35'
```

## 2. 变量注释语法

此前，Python 已加入了对函数变量类型进行注释的标准，也就是 type hint。而 Python 3.6 中则根据[PEP 526](https://www.python.org/dev/peps/pep-0526)的提议，加入了对更多变量类型注释的功能，包括类变量和实例变量。

具体代码示例：

```python
captain: str # 未设置初始值

class Starship:
    stats: Didct[str, int] = {}

```

与静态语言中的变量声明不同，Python 中的变量声明是为了更加方便地位第三方工具和库提供结构化的类型元数据。会使用到新语法的工具包括：mypy，pytype，PyCharm，等等。

## 3. 数字字面量使用下划线

对于较大的数字来说，位数太多可能不好判断值到底有多大。现在新版本中将允许你在数字字面量中使用下划线，提高可读性。

具体代码示例：

```python
>>> 1_000_000_000_000_000
1000000000000000
>>> 0x_FF_FF_FF_FF
4294967295
```

## 4. 异步生成器

在上一个版本中，Python 引入了对原生协程的支持，并可使用 `async` 或 `await` 语法，但是有一个限制是没办法在同一个函数体中使用 `await` 和 `yield` 。这个限制在 3.6 版中取消了，因此以后将可以定义**异步生成器**。

具体代码示例：

```python
async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)
```

使用新语法，可以让你的代码更简洁，运行速度更快。

## 5. 异步推导

推导（Comprehension）本身就是 Python中一个很棒的语法糖。在新版本中，它将得到一次重大升级。[PEP 530](https://www.python.org/dev/peps/pep-0530)提出了在列表、元组、字典推导或生成器表达式中使用 `async for` 语法。

这样就将原有各种推导式变成了可支持异步。

同时，推导式中还支持使用 `await` 表达式。

以上就是 3.6 版本中新增的 5 大特性：

- 格式化字符串字面量
- 变量注释语法
- 数字字面量使用下划线
- 异步生成器
- 异步推导

新版本中还新增了一些库，而且听说字典类型重新实现了，里面的元素会是有序的。更多内容，请大家访问[What’s New In Python 3.6](https://docs.python.org/3.6/whatsnew/3.6.html#what-s-new-in-python-3-6)查看。


