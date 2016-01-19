# Python之父：为什么Python的索引从零开始？

关键词：Python之父, Python的索引值, 从零开始索引, Guido van Rossum, Python的历史

刚开始学习Python语言的时候，并不是很理解为什么Python列表的索引值是从0开始的，不过却很喜欢列表切片的语法，非常简单、优雅。而最近在翻阅Python之父Guido老爹的Google+发文时，看到了他自己对这个问题的解释。

下面是Guido老爹的回答。

> 最近有人在Twitter上问我，为什么Python中的索引从0开始(0-based indexing)，还提供了一篇关于这个话题的[文章链接](http://exple.tive.org/blarg/2013/10/22/citation-needed/)(文章写的很有趣）。我记得自己就这个问题思考过很久；Python的祖先之一ABC语言，使用的索引是从1开始的（1-based indexing），而对Python语言有巨大影响的另一门语言，C语言的索引则是从0开始的。我最早学习的几种编程语言(Algol, Fortran, Pascal)中的索引方式，有的是1-based的，有的是从定义的某个变量开始（variable-based indexing）。而我决定在Python中使用0-based索引方式的一个原因，就是切片语法(slice notation)。

> 让我们来先看看切片的用法。可能最常见的用法，就是“取前n位元素”或“从第i位索引起，取后n位元素”(前一种用法，实际上是i==起始位的特殊用法)。如果这两种用法实现时可以不在表达式中出现难看的`+1`或`-1`，那将会非常的优雅。

> 使用0-based的索引方式、半开区间切片和缺省匹配区间的话（Python最终采用这样的方式），上面两种情形的切片语法就变得非常漂亮：`a[:n]`和`a[i:i+n]`，前者是a[0:n]的缩略写法。

> 如果使用1-based的索引方式，那么，想让`a[:n]`表达“取前n个元素”的意思，你要么使用闭合区间切片语法，要么在切片语法中使用切片起始位和切片长度作为切片参数。半开区间切片语法如果和1-based的索引方式结合起来，则会变得不优雅。而使用闭合区间切片语法的话，为了从第i位索引开始取后n个元素，你就得把表达式写成`a[i:i+n-1]`。这样看来，1-based的索引方式，与切片起始位+长度的语法形式配合使用会不会更合适？这样你可以写成`a[i:n]`。事实上，ABC语言就是这样做的——它发明了一个独特的语法，你可以把表达式写成`a@i|n`。(参看http://homepages.cwi.nl/~steven/abc/qr.html#EXPRESSIONS。）

> 但是，`index:length`这种方式在其它情况下适用吗？说实话，这点我有些记不清了，但我想我是被半开区间语法的优雅迷住了。特别是当两个切片操作位置邻接时，第一个切片操作的终点索引值是第二个切片的起点索引值时，太漂亮了，无法舍弃。例如，你想将一个字符串以i，j两个位置切成三部分，这三部分的表达式将会是`a[:i]`，`a[i:j]`和`a[j:]`。

> 这就是为什么Python索引方式是从零开始的。

原文链接：https://plus.google.com/115212051037621986145/posts/YTUxbXYZyfi

相关链接：http://c2.com/cgi/wiki?ZeroAndOneBasedIndexes

End

**欢迎大家扫描下方二维码关注我的公众号“编程派”，谢谢支持！**

<p style="text-align:center">
    <img src="http://codingpy.com/static/images/wechat-of-codingpy.jpg" alt="编程派的微信公众号二维码" style="width:215px;height:215px">
</p>




