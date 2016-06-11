# Python数据持久化：JSON

关键词：Python数据持久化, Json数据格式, pickle序列化, json序列化, dbm数据模块, 网络数据传输
URL：using-json-for-data-persistence

上周更新的《Think Python 2e》第14章讲述了几种数据持久化的方式，包括dbm、pickle等，但是考虑到篇幅和读者等因素，并没有将各种方式都列全。

本文将介绍一个与pickle类似的轻量级数据持久化方式，即json。而且json也是在网络数据传输的一种常见格式，非常有了解和学习的必要。
​
## JSON与Pickle的区别

Python官方文档中是这么比较JSON与Pickle的：

1. JSON是文本形式的存储，Pickle则是二进制形式（至少常用二进制）
2. JSON是人可读的，Pickle不可读
3. JSON广泛应用于除Python外的其他领域，Pickle是Python独有的
4. JSON只能dump一些python的内置对象，Pickle可以存储几乎所有对象

## JSON一般使用方式

Python中处理json的自带库就是json模块，需要用到的方法大致就是以下4个，其实它们的参数有很多这里暂且省略。

    import json
    obj = {'a' : 'b', 'c' : 'd'}
    fp = open('obj.json', 'w')
    json.dump(obj, fp)
    fp.close()s = json.dumps(obj)
    x = json.load(open('obj.json', 'r'))
    y = json.loads(s)

可以看到，**结尾带s就是在字符串层面上操作，如果不带s就是在文件层级操作**。obj指的是需要转化的对象，可以是一个字典或者列表，fp是文件句柄，用open打开。s则是一个字符串。

dumps返回的是一个字符串，load和loads则会返回python的对象。

以上是最简单的一些使用方式，这里还有一些实用的参数可以选择。

    import json
    obj = {u'姓名' : u'无名氏', u'国籍' : u'中国'}
    s = json.dumps(obj, ensure_ascii=False, indent=4)
    obj2 = json.loads(s, encoding='utf8')

ensure_ascii参数，是在有中文的情况下，设置为False可以防止将其解码而得到乱码，在loads的时候可以指定encoding来保持编码。

中文编码问题请参考之前发的文章：《如何正确解决Python中的中文编码问题》。

indent参数如果不指定的话，输出的字符串就是紧凑的形式，indent指定为4就可以输出缩进为4的美化形式，在需要给人看的时候用这个不错。

## JSON序列化datetime问题

Python自己的json.dumps不能序列化datetime对象，如果需要dump这类对象时可以自己定义JSONEncoder。

    import json
    from datetime import date, datetime
    class AdvEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(obj, date):
                return obj.strftime('%Y-%m-%d')
            else:
                return super().default(self, obj)

    obj = {}
    json.dumps(obj, cls=MyEncoder)

这样在dump时指定cls参数就可以完成序列化datetime的任务了，如果觉得麻烦的话，可以使用偏函数的方法自己封装一下。

    import functools
    adumps = functools.partial(json.dumps, cls=AdvEncoder)
    d = datetime.now()
    adumps(d)

## simplejson

Python中自带的json库是在2.6版本中才加入的。因此，如果你需要使用一个更早的Python版本并且处理json数据，那么你可以安装一个第三方库：simplejson。

simplejson模拟了自带的json库，目前支持Python 2.5+和Python 3.3+。根据官方文档的介绍，该库在没有安装C扩展的情况下，速度仍优于自带的json库。这应该也是为什么simplejson在PyPI的下载数超高的原因之一。

要使用simplejson，你只需要像下面这样导入即可：

    import simplejson as json

其他的代码不需要修改。

## 参考资料

[Python Data Persistence](http://brieflyx.me/2015/python-module/python-data-persistence/。)
