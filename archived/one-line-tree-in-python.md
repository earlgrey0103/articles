# 一行Python代码实现树结构

关键词：树结构, Python树结构实现, Python一行代码, defaultdict, Python数据结构

树结构是一种抽象数据类型，在计算机科学领域有着非常广泛的应用。一颗树可以简单的表示为根， 左子树， 右子树。 而左子树和右子树又可以有自己的子树。这似乎是一种比较复杂的数据结构，那么真的能像我们在标题中所说的那样，用一行Python代码就可以实现吗？

## 一行代码实现？

由于树形结构的外层和内层有着相似的结构，所以多可以用递归的方式定义树。再利用Python中提供的`defaultdict`，我们就可以很轻松地定义树了，而且只有一行代码。

    from collections import defaultdict

    def tree(): return defaultdict(tree)

这个代码分享自[https://gist.github.com/hrldcpr/2012250](https://gist.github.com/hrldcpr/2012250)。根据上面的代码，一棵树就是一个默认值也为树的字典。

## 具体效果演示

这样实现的树有两个奇妙之处，第一点是我们不需要创建节点，就可以直接引用它们。例如：

    users = tree()
    users['codingpy']['username'] = 'earlgrey'
    users['python']['username'] = 'Guido van Rossum'

如果仅从常规字典的特性来看，上面的赋值操作是不成立的，因为我们必须事先声明`users['codingpy'] = {}`。但是我们利用的是`collections`模块中的`defaultdict`类，如果某个键不存在时，它就会利用`tree()`来为该键创建一个初始值，因为tree是提供给`defaultdict`的`default_factory`。[根据文档介绍](https://docs.python.org/2/library/collections.html#collections.defaultdict)，如果提供该参数，参数的值就传给`defaultdict`构造器作为第一个参数。

如果我们以json格式打印上面代码的话（即通过`print(json.dumps(users))`），我们会得到下面的结果：

    {"codingpy": {"username": "earlgrey"}, "python": {"username": "Guido van Rossum"}}

第二点就是我们甚至不用进行上面那样的赋值操作，只需要引用就可以创建一棵树。例如：

    categories = tree()

    categories['Programming Languages']['Python']
    categories['Python']['Standard Library']['sys']
    categories['Python']['Standard Library']['os']

如果我们接着运行`print(json.dumps(categories))`，就会得到下面的结果：

    {"Python": {"Standard Library": {"sys": {}, "os": {}}}, "Programming Languages": {"Python": {}}}

第二个奇妙之处，也被称作[Autovivification](https://en.wikipedia.org/wiki/Autovivification#Python)，该特性最早出现在Perl中，指的是在某个数组被引用时自动创建该数组。Python本身是不支持该特性的，但可以通过本文所述的`defaultdict`模仿。
