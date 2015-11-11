# 自定义Flask中的Response类

Flask框架中的网络响应类名字叫Response，很贴切，但是很少在Flask应用中直接使用。相反，Flask内部实现中，将其作为应用路由程序返回响应数据的容器，容器里还包含了用于创建HTTP响应的其他信息。

但是没多少人知道，Flask框架允许应用将默认的响应类，替换为自定义类。这就给了我们研究小技巧的机会。在本文中，我将展示如何利用这个技巧，简化你的代码。

## Flask中的Response类如何工作？

大部分应用并不直接使用Flask中的Response类，但这并不是说这个类没有被使用。Flask会为每个请求创建响应对象。那么，它是如何实现的呢？

Flask用来处理请求的函数返回时，响应周期就开始了。在网络应用中，路由一般最后会调用`render_template`函数，这个函数会渲染引用的模板文件，将其作为字符串返回：

	@app.route('/index')
	def index():
	    # ...
	    return render_template('index.html')

但是，你可能也知道，Flask的路由函数可以选择多返回两个值，将被设置为HTTP状态码和自定义的HTTP响应头：

	@app.route('/data')
	def index():
	    # ...
	    return render_template('data.json'), 201, {'Content-Type': 'application/json'}

在上面的例子中，状态码被设为201，取代了Flask默认的200，即请求被成功处理的状态码。这个例子还定义了内容类型标头（Content-Type header），表明HTTP响应中包含JSON数据，因为如果你不明确设置内容类型的话，Flask会默认设置为HTML。

上面的例子展示了HTTP响应的三个基本组成部分，即数据或正文，状态码和标头。Flask的应用实例有一个`make_response`函数，可以接受路由函数的返回值（可以是单个值，或是有1-3个变量的元组），将其填入Response类中。

你可以通过在Python控制台会话中，看看这是如何实现的。首先创建一个虚拟环境，并安装Flask，然后开启Python会话，并输入下面的代码：

	>>> from flask import Flask
	>>> app = Flask(__name__)
	>>> app.make_response('Hello, World')
	<Response 12 bytes [200 OK]>
	>>> app.make_response(('Hello, World', 201))
	<Response 12 bytes [201 CREATED]>

这里，我创建了一个简单的Flask应用实例，之后调用了`make_response`方法创建响应类对象。在第一次调用时，我传递了一个字符串作为参数，所以响应对象中使用了默认的状态码和标头。在第二次调用时，我传入了有两个值的元组，强制返回了非默认的状态码。注意第二次调用时使用了两个括号，里面的括号将字符串和状态码包在了元组中。由于`make_response`函数只接受一个参数，所以必须要以元组形式传入。

Flask生成代表路由函数返回值的Response对象之后，会对其进行一些处理。包括将其传至自定义的`after_request`处理程序（handlers），可以让应用有机会插入或修改标头、改变正文或状态码，甚至如果愿意的话用崭新的的响应对象取而代之。最后，Flask获取最重的响应对象，渲染成HTTP响应，并发送给客户端。

## Flask中的Response类
我们来看看Response类中最有趣的特性。下面的类定义在我看来，展示了这个类具备的灵活属性和方法：

    class Response:
        charset = 'utf-8'
        default_status = 200
        default_mimetype = 'text/html'
    
        def __init__(self, response=None, status=None, headers=None,
                     mimetype=None, content_type=None, direct_passthrough=False):
            pass
    
        @classmethod
        def force_type(cls, response, environ=None):
            pass

注意，如果你阅读Flask的源码，是不会发现上面的类定义的。Flask中的`Response`类，实际上是从Werkzeug库中相同名称类衍生而来的一个小壳。而，Werzeug中的`Response`类则继承的是`BaseResponse`类，上面的定义就在其中。

`charset`、`default_status`和`default_mimetype`这三个类属性定义了默认值。如果任何一个默认值不适用你的应用，那你可以创建`Response`类的子类，定义你自己的类，而不必在每一个响应对象中设置自定义值。例如，如果你的程序是一个所有的路由均返回XML格式数据的API接口，你就可以在自定义的类中，将`default_mimetype`改为`application/xml`，这样Flask就会默认返回XML响应。稍后你会看到如何实现。

我不会详细描述`__init__`构造函数（你可以阅读Werkzeug的文档），但请注意，Flask响应对象中的三个重要元素，即响应正文、状态码和标头，是作为参数传入的。在子类中，构造函数可以更改决定如何创建响应的规则。

响应类中的`force_type()`类方法，是唯一意义非比寻常、十分重要的元素。有时候，Werkzeug或是Flask需要自行创建响应对象，比如出现应用错误，并需要返回给客户端时。在这种情况下，响应对象不是应用提供的，而是由框架创建的。在使用自定义响应类的应用中，Flask和Werkzeug没办法直到自定义类的细节，所以它们使用标准响应类来创建响应。响应类中的`force_type()`方法，被设计为可以接受不同响应类的实例，并会将其转换成自身的格式。

我敢肯定，你一定被`force_type()`方法的描述搞糊涂了。说白了，就是如果Flask碰到了一个不是其期望的响应对象，就会使用该方法进行转换。我下面要讲的第三个使用场景，就利用了这个特点，让Flask的路由程序返回例如字典、列表或者是其他任何自定义对象，作为请求的响应对象。

好了，理论就讲这么多了。接下来，我来告诉大家如何应用上面关于Response类的小技巧。准备好了吗？

## 使用自定义的Response类
到现在为止，我确定你会也会认为使用自定义的响应类在部分有趣的场景下是有利的。在给出实际例子之前，我想告诉你在Flask中设置并使用自定义的响应类是多么的简单。请看下面的这个例子：

    from flask import Flask, Response
    
    class MyResponse(Response):
        pass
    
    app = Flask(__name__)
    app.response_class = MyResponse
    
    # ...

在上面的代码中，我定义了一个名叫`MyResponse`的自定义响应类。通常，自定义响应类会增加或修改默认类的行为，所以一般都会通过创建Flask的`Response`类的子类来实现。要想让Flask使用我的自定义类，我所需要做的仅是通过`app.response_class`进行设置。

`Flask`类的`response_class`属性是一个类属性，所以我们可以稍微修改上面的例子，创建一个设置了自定义响应类的Flask子类：
    
    from flask import Flask, Response
    
    class MyResponse(Response):
        pass
    
    class MyFlask(Flask)
        response_class = MyResponse
    
    app = MyFlask(__name__)
    
    # ...

### 例1：更改响应对象的默认值
第一个例子极其简单。假设你的应用中大部分或全部端点（endpoints）都返回的是XML。对于这样的应用，将默认的内容类型设置为`application/xml`是合理的。可以通过下面这个仅有两行代码的响应类轻松实现：

    class MyResponse(Response):
        default_mimetype = 'application/xml'

容易，对吧？如果将该类设为应用的默认响应对象，那么你在编写返回XML的函数时，就不用担心忘记设置内容类型了。举个例子：

    @app.route('/data')
    def get_data():
        return '''<?xml version="1.0" encoding="UTF-8"?>
    <person>
        <name>John Smith</name>
    </person>
    '''

上面这个路由使用的是默认响应类，其内容类型会设置为`text/html`，因为那是默认类型。使用自定义响应类，可以免去你在所有的XML路由的返回语句中，额外加上标头的麻烦。另外，如果有的路由需要其他的内容类型，你仍可以替换掉默认值，就像对待一般的响应类一样。

    @app.route('/')
    def index():
        return '<h1>Hello, World!</h1>', {'Content-Type': 'text/html'}

### 例2：自动决定内容类型
下一个例子更复杂一点。假设我们的应用中HTML路由与XML路由的数量差不多，所以按照第一个例子的做法就不行了，因为不管你选用哪种默认类型，都会有一半的路由需要替换内容类型。

更好的解决办法，则是创建一个能够通过分析响应文本，决定正确的内容类型的响应类。下面的这个类实现了该功能：

    class MyResponse(Response):
        def __init__(self, response, **kwargs):
            if 'mimetype' not in kwargs and 'contenttype' not in kwargs:
                if response.startswith('<?xml'):
                    kwargs['mimetype'] = 'application/xml'
            return super(MyResponse, self).__init__(response, **kwargs)

在这个例子中，我首先确保了响应对象中没有明确设置内容类型。然后，我检查响应的征文是否以`<?xml`开头，是的话就意味着数据是XML文档格式。如果两则条件同时成立，我会在传入父类的构造函数中插入XML内容类型。

有了这个自定义响应类，任何满足XML格式化要求的文档都会自动获得XML内容类型，而其他响应则会继续获得默认的内容类型。而且，在所有的类中，我仍然可以在必要时声明内容类型。

### 例3：自动返回JSON响应
