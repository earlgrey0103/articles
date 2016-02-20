# Python中的字符串模运算符与format函数

关键词：Python 字符串运算, Python 字符串插值, 字符串替换, format函数, 模运算符%, 字符串操作性能比较

如果你在网上搜索Python中如何进行字符串插值（string interpolation），那么你很可能会发现一些留言和旧文档中说字符串模运算符（%）以后会被废弃，并移除出标准库。但是这完全是杞人忧天。至于为什么字符串模运算符不会被废弃，大家看下面的代码运行结果就会知道了。

	:::python
	from timeit import timeit
	
	# 使用字符串模运算符进行字符串插值操作 
	def test_modulo():
	    'Don\'t %s, I\'m the %s.' % ('worry', 'Doctor')

	# 使用字符串的format函数**显示地**进行字符串插值操作  
	def test_format_explicit():
	    'Don\'t {0}, I\'m the {1}.'.format('worry', 'Doctor')

	# 使用字符串的format函数**非显示地**进行字符串插值操作 
	def test_format_implicit():
	    'Don\'t {}, I\'m the {}.'.format('worry', 'Doctor')
 
	timeit(stmt=test_modulo, number=1000000)
	timeit(stmt=test_format_explicit, number=1000000)
	timeit(stmt=test_format_implicit, number=1000000)

通过Python 2.7.5版本执行上面的代码，我们可以得到下面的结果：

	:::python
	Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win
	32
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from string_interpolation import *
	>>> timeit(stmt=test_modulo, number=1000000)
	0.22551053128719545
	>>> timeit(stmt=test_format_explicit, number=1000000)
	0.44482803557693984
	>>> timeit(stmt=test_format_implicit, number=1000000)
	0.4307239080015748
	>>>

请注意，`test_format_explicit`是检索时最常见的Python字符串插值的操作方式。但是，从上面的运行时间来看，使用字符串莫运算符的性能是最高的，是使用format函数的两倍。

这样来看的话，在format函数的运行速度达到模运算符的水平之前，莫运算符并不会被废弃。当然，我也支持format函数的存在，在某些场合下它的确是更加优秀的选择。

正如[PEP 461](http://legacy.python.org/dev/peps/pep-0461/)中所提到的的，字符串的莫运算符并不会就这样悄无声息地从Python中消失。

**欢迎大家扫描下方二维码关注我的公众号“编程派”，谢谢支持！**

<p style="text-align:center">
    <img src="http://codingpy.com/static/images/wechat-of-codingpy.jpg" alt="编程派的微信公众号二维码" style="width:215px;height:215px">
</p>
