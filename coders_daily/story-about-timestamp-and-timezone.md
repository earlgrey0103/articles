# 程序员的日常：时间戳和时区的故事

- 关键词：程序员的日常, 程序员漫画, 程序员的冷笑话, 时间戳和时区的故事, 时间戳, 时区, 时间戳和时区的区别

什么是时间戳（timestamp）？它和时区（timezone）又有什么关系？初学者可能一开始很难搞懂时间戳这个概念，就像这期《程序员的日常》漫画中的主人公一样。

![程序员的日常：时间戳和时区的故事](http://ww1.sinaimg.cn/mw690/006faQNTgw1f02m3qnlr7j30i20hgaf6.jpg)

## 漫画注释

从漫画中举的例子来看，这里的时间戳，指的就是Unix时间戳(Unix timestamp)。它也被称为Unix时间(Unix time)、POSIX时间(POSIX time)，是一种时间表示方式，定义为从格林威治时间1970年01月01日00时00分00秒起至现在的总秒数。因此，严格来说，不管你处在地球上的哪个地方，任意时间点的时间戳都是相同的。这点有利于线上和客户端分布式应用统一追踪时间信息。

Unix时间戳不仅被使用在Unix系统、类Unix系统中，也在许多其他操作系统中被广泛采用。但是，这并不意味着目前的时间戳规范会一直持续使用下去。**因为到2038年1月19日时，Unix时间戳就会因为32位内存溢出（32-bit overflow）而无法继续使用。因此，在这一天之前，上千万的网络应用要么采用新的时间戳规范，要么迁移到64位系统，后者可以给时间戳争取“一点”时间。**

## Python中获取时间戳并进行转换

Python中日期信息的处理也是一大难点。这里列举几个相关的用法。

### 获取当前的时间戳

	:::python
	from time import time
	time()
	# 1453021629.990758

### 将时间戳转换成datetime对象

	:::python
	from datetime import datetime

	print datetime.fromtimestamp(1346236702)

	#2012-08-29 11:38:22	

### 将datetime对象转换成可读字符串

	:::python
	from datetime import date time

	my_date_object = datetime.utcnow()

	my_date_string = my_date_object.strftime('%Y-%m-%d')

END

**欢迎大家扫描下方二维码关注我的公众号“编程派”，谢谢支持！**

<p style="text-align:center">
    <img src="http://codingpy.com/static/images/wechat-of-codingpy.jpg" alt="编程派的微信公众号二维码" style="width:215px;height:215px">
</p>