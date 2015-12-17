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

简而言之，它是物理服务器上搭建的一个网络连接服务器（networking server）

In a nutshell it’s a networking server that sits on a physical server (oops, a server on a server) and waits for a client to send a request. When it receives a request, it generates a response and sends it back to the client. The communication between a client and a server happens using HTTP protocol. A client can be your browser or any other software that speaks HTTP.

What would a very simple implementation of a Web server look like? Here is my take on it. The example is in Python but even if you don’t know Python (it’s a very easy language to pick up, try it!) you still should be able to understand concepts from the code and explanations below:

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
Save the above code as webserver1.py or download it directly from GitHub and run it on the command line like this

$ python webserver1.py
Serving HTTP on port 8888 …
Now type in the following URL in your Web browser’s address bar http://localhost:8888/hello, hit Enter, and see magic in action. You should see “Hello, World!” displayed in your browser like this:

Browser "Hello, World!"

Just do it, seriously. I will wait for you while you’re testing it.

Done? Great. Now let’s discuss how it all actually works.

First let’s start with the Web address you’ve entered. It’s called an URL and here is its basic structure:

URL Structure

This is how you tell your browser the address of the Web server it needs to find and connect to and the page (path) on the server to fetch for you. Before your browser can send a HTTP request though, it first needs to establish a TCP connection with the Web server. Then it sends an HTTP request over the TCP connection to the server and waits for the server to send an HTTP response back. And when your browser receives the response it displays it, in this case it displays “Hello, World!”

Let’s explore in more detail how the client and the server establish a TCP connection before sending HTTP requests and responses. To do that they both use so-called sockets. Instead of using a browser directly you are going to simulate your browser manually by using telnet on the command line.

On the same computer you’re running the Web server fire up a telnet session on the command line specifying a host to connect to localhost and the port to connect to 8888 and then press Enter:

$ telnet localhost 8888
Trying 127.0.0.1 …
Connected to localhost.
At this point you’ve established a TCP connection with the server running on your local host and ready to send and receive HTTP messages. In the picture below you can see a standard procedure a server has to go through to be able to accept new TCP connections. Socket accept

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
