> 原文链接：[http://ruslanspivak.com/lsbaws-part1/](http://ruslanspivak.com/lsbaws-part1/)
> 译文链接：[http://codingpy.com/article/build-a-simple-web-server-part-one/](http://codingpy.com/article/build-a-simple-web-server-part-one/)

# 从头开发一个网络服务器(一)

Let’s Build A Web Server. Part 1.

有一天，一位女士散步时经过一个工地，看见有三个工人在干活。她问第一个人，“你在做什么？”第一个人有点不高兴，吼道“难道你看不出来我在砌砖吗？”女士对这个答案并不满意，接着问第二个人他在做什么。第二个人回答道，“我正在建造一堵砖墙。”然后，他转向第一个人，说道：“嘿，你砌的砖已经超过墙高了。你得把最后一块砖拿下来。”女士对这个答案还是不满意，她接着问第三个人他在做什么。第三个人抬头看着天空，对她说：“我在建造这个世界上有史以来最大的教堂”。就在他望着天空出神的时候，另外两个人已经开始争吵多出的那块砖。他慢慢转向前两个人，说道：“兄弟们，别管那块砖了。这是一堵内墙,之后还会被刷上石灰的，没人会注意到这块砖。接着砌下层吧。”

这个故事的寓意在于，当你掌握了整个系统的设计，明白不同的组件是以何种方式组合在一起的（砖块，墙，教堂）时候，你就能够更快地找到并解决问题（多出的砖块）。

但是，这个故事与从头开发一个网络服务器有什么关系呢？

在我看来，要成为一名更优秀的程序员，你**必须**更好地立即自己日常使用的软件系统，而这就包括了编程语言、编译器、解释器、数据库与操作系统、网络服务器和网络开发框架。而要想更好、更深刻地理解这些系统，你**必须**从头重新开发这些系统，一步一个脚印地重来一遍。

孔子曰：不闻不若闻之，闻之不若见之，见之不若知之，知之不若行之。

> 不闻不若闻之

[听别人说怎么做某事](http://ruslanspivak.com/lsbasi-part4/LSBAWS_confucius_hear.png)

> 闻之不若见之

[看别人怎么做某事](http://ruslanspivak.com/lsbasi-part4/LSBAWS_confucius_see.png)

> 见之不若知之，知之不若行之。

[自己亲自做某事](http://ruslanspivak.com/lsbasi-part4/LSBAWS_confucius_do.png)

> 译者注：上面孔子那段话在国外的翻译是：I hear and I forget, I see and I remember, I do and I understand。但在查找这句英文的出处时，查到[有篇博文](http://blog.sina.com.cn/s/blog_60ebcd1d0100f4tv.html)称这句话的中文实际出自荀子的《儒效篇》，经查确实如此。

我希望，你读到这里的时候，已经相信通过重新开发不同软件系统的方式学习其原理的方式是正确的。

《从头开发网络服务器》将会分为三个部分，将介绍如何自己开发一个基础的网络服务器。我们这就开始吧。

首先，到底什么是网络服务器？

[HTTP请求/响应](http://ruslanspivak.com/lsbaws-part1/LSBAWS_HTTP_request_response.png)

简而言之，它是物理服务器上搭建的一个网络连接服务器（networking server），永久地等待客户端发送请求。当服务器收到请求之后，它会生成响应并返回至客户端。客户端与服务器之间的沟通，是以HTTP协议进行的。客户端可以是浏览器，也可以任何支持HTTP协议的软件。

那么，网络服务器的简单实现形式会是怎样的呢？下面是我对此的理解。示例代码使用Python语言实现，不过即使你不懂Python语言，你也应该可以从代码和下面的解释中理解相关的概念：

    :::python
    import socket

    HOST, PORT = '', 8888

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
    print 'Serving HTTP on port %s ...' % PORT
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        print request
        
        http_response = """\
        HTTP/1.1 200 OK
        
        Hello, World!
        """
        
        client_connection.sendall(http_response)
        client_connection.close()

将上面的代码保存为`webserver1.py`，或者直接从我的[Github仓库](https://github.com/rspivak/lsbaws/blob/master/part1/webserver1.py)下载，然后通过命令行运行该文件：

    $ python webserver1.py
    Serving HTTP on port 8888 …

接下来，在浏览器的地址栏输入这个链接：http://localhost:8888/hello,然后按下回车键，你就会看见神奇的一幕。在浏览器中，应该会出现“Hello, World!”这两个英文单词：

[浏览器返回“Hello World""](http://ruslanspivak.com/lsbaws-part1/browser_hello_world.png)

是不是很神奇？接下来，我们来分析背后的实现原理。

首先，我们来看你所输入的网络地址。它的名字叫URL（Uniform Resource Locator，统一资源定位符），其基本结构如下：

[URL的基本结构](http://ruslanspivak.com/lsbaws-part1/LSBAWS_URL_Web_address.png)

通过URL，你告诉了浏览器它所需要发现并连接的网络服务器地址，以及获取服务器上的页面路径。不过在浏览器发送HTTP请求之前，它首先要与目标网络服务器建立TCP连接。然后，浏览器再通过TCP连接发送HTTP请求至服务器，并等待服务器返回HTTP响应。当浏览器收到响应的时候，就会在页面上显示响应的内容，而在上面的例子中浏览器显示的就是“Hello, World!”这句话。

那么，在客户端发送请求、服务器返回响应之前，二者究竟是如何建立起TCP连接的呢？要建立起TCP连接，服务器和客户端都使用了所谓的套接字（socket）。接下来，我们不直接使用浏览器，而是在命令行使用`telnet`手动模拟浏览器。

在运行网络服务器的同一台电脑商，通过命令行开启一次`telnet`会话，将需要连接的主机设置为`localhost`，主机的连接断开设置为`8888`，然后按回车键：

    $ telnet localhost 8888
    Trying 127.0.0.1 …
    Connected to localhost.

完成这些操作之后，你其实已经与本地运行的网络服务器建立了TCP连接，随时可以发送和接收HTTP信息。在下面这张图片里，展示的是服务器接受新的TCP连接所需要完成的标准流程。

[服务器接受TCP连接的标准流程](http://ruslanspivak.com/lsbaws-part1/LSBAWS_socket.png)

In the same telnet session type GET /hello HTTP/1.1 and hit Enter:

$ telnet localhost 8888
Trying 127.0.0.1 …
Connected to localhost.
GET /hello HTTP/1.1

HTTP/1.1 200 OK
Hello, World!
You’ve just manually simulated your browser! You sent an HTTP request and got an HTTP response back. This is the basic structure of an HTTP request:

HTTP Request Aanatomy

The HTTP request consists of the line indicating the HTTP method (GET, because we are asking our server to return us something), the path /hello that indicates a “page” on the server we want and the protocol version.

For simplicity’s sake our Web server at this point completely ignores the above request line. You could just as well type in any garbage instead of “GET /hello HTTP/1.1” and you would still get back a “Hello, World!” response.

Once you’ve typed the request line and hit Enter the client sends the request to the server, the server reads the request line, prints it and returns the proper HTTP response.

Here is the HTTP response that the server sends back to your client (telnet in this case): HTTP Response Anatomy

Let’s dissect it. The response consists of a status line HTTP/1.1 200 OK, followed by a required empty line, and then the HTTP response body.

The response status line HTTP/1.1 200 OK consists of the HTTP Version, the HTTP status code and the HTTP status code reason phrase OK. When the browser gets the response, it displays the body of the response and that’s why you see “Hello, World!” in your browser.

And that’s the basic model of how a Web server works. To sum it up: The Web server creates a listening socket and starts accepting new connections in a loop. The client initiates a TCP connection and, after successfully establishing it, the client sends an HTTP request to the server and the server responds with an HTTP response that gets displayed to the user. To establish a TCP connection both clients and servers use sockets.

Now you have a very basic working Web server that you can test with your browser or some other HTTP client. As you’ve seen and hopefully tried, you can also be a human HTTP client too, by using telnet and typing HTTP requests manually.

Here’s a question for you: “How do you run a Django application, Flask application, and Pyramid application under your freshly minted Web server without making a single change to the server to accommodate all those different Web frameworks?”
