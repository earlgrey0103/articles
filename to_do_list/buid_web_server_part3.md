<<<<<<< HEAD
> 原文链接：[http://ruslanspivak.com/lsbaws-part3/](http://ruslanspivak.com/lsbaws-part3/)
> 译文链接：[http://codingpy.com/article/build-a-simple-web-server-part-three/](http://codingpy.com/article/build-a-simple-web-server-part-three/)


“We learn most when we have to invent” —Piaget

在第二部分中，你开发了一个能够处理HTTPGET请求的简易WSGI服务器。在上一篇的最后，我问了你一个问题：“怎样让服务器一次处理多个请求？”读完本文，你就能够完美地回答这个问题。接下来，请你做好准备，因为本文的内容非常多，节奏也很快。文中的所有代码都可以在[Github仓库](https://github.com/rspivak/lsbaws/blob/master/part3/)下载。

首先，我们简单回忆一下简易网络服务器是如何实现的，服务器要处理客户端的请求需要哪些条件。你在前面两部分文章中开发的服务器，是一个迭代式服务器（iterative server），还只能一次处理一个客户端请求。只有在处理完当前客户端请求之后，它才能接收新的客户端连接。这样，有些客户端就必须要等待自己的请求被处理了，而对于流量大的服务器来说，等待的时间就会特别长。

![客户端逐个等待服务器响应](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it1.png)

下面是迭代式服务器`webserver3a.py`的代码：

    :::python
    #####################################################################
    # Iterative server - webserver3a.py                                 #
    #                                                                   #
    # Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X  #
    #####################################################################
    import socket

    SERVER_ADDRESS = (HOST, PORT) = '', 8888
    REQUEST_QUEUE_SIZE = 5


    def handle_request(client_connection):
        request = client_connection.recv(1024)
        print(request.decode())
        http_response = b"""\
    HTTP/1.1 200 OK

    Hello, World!
    """
        client_connection.sendall(http_response)


    def serve_forever():
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(SERVER_ADDRESS)
        listen_socket.listen(REQUEST_QUEUE_SIZE)
        print('Serving HTTP on port {port} ...'.format(port=PORT))

        while True:
            client_connection, client_address = listen_socket.accept()
            handle_request(client_connection)
            client_connection.close()

    if __name__ == '__main__':
        serve_forever()

如果想确认这个服务器每次只能处理一个客户端的请求，我们对上述代码作简单修改，在向客户端返回响应之后，增加60秒的延迟处理时间。这个修改只有一行代码，即告诉服务器在返回响应之后睡眠60秒。

![让服务器睡眠60秒](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it2.png)

下面就是修改之后的服务器代码：

    :::python
    #########################################################################
    # Iterative server - webserver3b.py                                     #
    #                                                                       #
    # Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X      #
    #                                                                       #
    # - Server sleeps for 60 seconds after sending a response to a client   #
    #########################################################################
    import socket
    import time

    SERVER_ADDRESS = (HOST, PORT) = '', 8888
    REQUEST_QUEUE_SIZE = 5


    def handle_request(client_connection):
        request = client_connection.recv(1024)
        print(request.decode())
        http_response = b"""\
    HTTP/1.1 200 OK

    Hello, World!
    """
        client_connection.sendall(http_response)
        time.sleep(60)  # sleep and block the process for 60 seconds


    def serve_forever():
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(SERVER_ADDRESS)
        listen_socket.listen(REQUEST_QUEUE_SIZE)
        print('Serving HTTP on port {port} ...'.format(port=PORT))

        while True:
            client_connection, client_address = listen_socket.accept()
            handle_request(client_connection)
            client_connection.close()

    if __name__ == '__main__':
        serve_forever()

接下来，我们启动服务器：

    $ python webserver3b.py

现在，我们打开一个新的终端窗口，并运行`curl`命令。你会立刻看到屏幕上打印出了“Hello, World!”这句话：

    $ curl http://localhost:8888/hello
    Hello, World!

接着我们立刻再打开一个终端窗口，并运行`curl`命令：


    $ curl http://localhost:8888/hello

如果你在60秒了完成了上面的操作，那么第二个`curl`命令应该不会立刻产生任何输出结果，而是处于挂死（hang）状态。服务器也不会在标准输出中打印这个新请求的正文。下面这张图就是我在自己的Mac上操作时的结果（右下角那个边缘高亮为黄色的窗口，显示的就是第二个`curl`命令挂死）：

![Mac上操作时的结果](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it3.png)

当然，你等了足够长时间之后（超过60秒），你会看到第一个`curl`命令结束，然后第二个`curl`命令会在屏幕上打印出“Hello, World!”，之后再挂死60秒，最后才结束：

![curl命令演示](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it4.png)

这背后的实现方式是，服务器处理完第一个`curl`客户端请求后睡眠60秒，才开始处理第二个请求。这些步骤是线性执行的，或者说迭代式一步一步执行的。在我们这个实例中，则是一次一个请求这样处理。

接下来，我们简单谈谈客户端与服务器之间的通信。为了让两个程序通过网络进行通信，二者均必须使用套接字。你在前两章中也看到过套接字，但到底什么是套接字？

![什么是套接字](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_socket.png)

套接字是通信端点（communication endpoint）的抽象形式，可以让一个程序通过文件描述符（file descriptor）与另一个程序进行通信。在本文中，我只讨论Linux/Mac OS X平台上的TCP/IP套接字。其中，尤为重要的一个概念就是TCP套接字对（socket pair）。

> TCP连接所使用的套接字对是一个4元组（4-tuple），包括本地IP地址、本地端口、外部IP地址和外部端口。一个网络中的每一个TCP连接，都拥有独特的套接字对。IP地址和端口号通常被称为一个套接字，二者一起标识了一个网络端点。

![套接字对合套接字](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_socketpair.png)

因此，`{10.10.10.2:49152, 12.12.12.3:8888}`元组组成了一个套接字对，代表客户端侧TCP连接的两个唯一端点，`{12.12.12.3:8888, 10.10.10.2:49152}`元组组成另一个套接字对，代表服务器侧TCP连接的两个同样端点。构成TCP连接中服务器端点的两个值分别是IP地址`12.12.12.3`和端口号`8888`，它们在这里被称为一个套接字（同理，客户端端点的两个值也是一个套接字）。

服务器创建套接字并开始接受客户端连接的标准流程如下：

![服务器创建套接字并开始接受客户端连接的标准流程](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_server_socket_sequence.png)

1. 服务器创建一个TCP/IP套接字。通过下面的Python语句实现：

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

2. 服务器可以设置部分套接字选项（这是可选项，但你会发现上面那行服务器代码就可以确保你重启服务器之后，服务器会继续使用相同的地址）。

    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

3. 然后，服务器绑定地址。绑定函数为套接字指定一个本地协议地址。调用绑定函数时，你可以单独指定端口号或IP地址，也可以同时指定两个参数，甚至不提供任何参数也没问题。

    listen_socket.bind(SERVER_ADDRESS)

4. 接着，服务器将该套接字变成一个侦听套接字：

    listen_socket.listen(REQUEST_QUEUE_SIZE)

`listen`方法只能由服务器调用，执行后会告知服务器应该接收针对该套接字的连接请求。

完成上面四步之后，服务器会开启一个循环，开始接收客户端连接，不过一次只接收一个连接。当有连接请求时，`accept`方法会返回已连接的客户端套接字。然后，服务器从客户端套接字读取请求数据，在标准输出中打印数据，并向客户端返回消息。最后，服务器会关闭当前的客户端连接，这时服务器又可以接收新的客户端连接了。

要通过TCP/IP协议与服务器进行通信，客户端需要作如下操作：

![客户端与服务器进行通信所需要的操作](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_client_socket_sequence.png)

下面这段示例代码，实现了客户端连接至服务器，发送请求，并打印响应内容的过程：

    :::python
    import socket

    # create a socket and connect to a server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8888))

    # send and receive some data
    sock.sendall(b'test')
    data = sock.recv(1024)
    print(data.decode())

在创建套接字之后，客户端需要与服务器进行连接，这可以通过调用`connect`方法实现：

    sock.connect(('localhost', 8888))

客户端只需要提供远程IP地址或主机名，以及服务器的远程连接端口号即可。

你可能已经注意到，客户端不会调用`bind`和`accept`方法。不需要调用`bind`方法，是因为客户端不关心本地IP地址和本地端口号。客户端调用`connect`方法时，系统内核中的TCP/IP栈会自动指定本地IP地址和本地端口。本地端口也被称为临时端口（ephemeral port）。

![本地端口——临时端口号](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_ephemeral_port.png)

服务器端有部分端口用于连接熟知的服务，这种端口被叫做“熟知端口”（well-known port），例如，80用于HTTP传输服务，22用于SSH协议传输。接下来，我们打开Python shell，向在本地运行的服务器发起一个客户端连接，然后查看系统内核为你创建的客户端套接字指定了哪个临时端口（在进行下面的操作之前，请先运行`webserver3a.py`或`webserver3b.py`文件，启动服务器）：

    :::python
    >>> import socket
    >>> sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    >>> sock.connect(('localhost', 8888))
    >>> host, port = sock.getsockname()[:2]
    >>> host, port
    ('127.0.0.1', 60589)

在上面的示例中，我们看到内核为套接字指定的临时端口是60589。

在开始回答第二部分最后提的问题之前，我需要快速介绍一些其他的重要概念。稍后你就会明白我为什么要这样做。我要介绍的重要概念就是进程（process）和文件描述符（file descriptor）。

什么是进程？进程就是正在执行的程序的一个实例。举个例子，当服务器代码执行的时候，这些代码就被加载至内存中，而这个正在被执行的服务器的实例就叫做进程。系统内核会记录下有关进程的信息——包括进程ID，以便进行管理。所以，当你运行迭代式服务器`webserver3a.py`或`webserver3b.py`时，你也就开启了一个进程。

![服务器进程](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_server_process.png)

我们在终端启动`webserver3a.py`服务器：

    $ python webserver3b.py

然后，我们在另一个终端窗口中，使用`ps`命令来获取上面那个服务器进程的信息：

    $ ps | grep webserver3b | grep -v grep 
    7182 ttys003    0:00.04 python webserver3b.py

The ps command shows you that you have indeed run just one Python process webserver3b. When a process gets created the kernel assigns a process ID to it, PID. In UNIX, every user process also has a parent that, in turn, has its own process ID called parent process ID, or PPID for short. I assume that you run a BASH shell by default and when you start the server, a new process gets created with a PID and its parent PID is set to the PID of the BASH shell.



Try it out and see for yourself how it all works. Fire up your Python shell again, which will create a new process, and then get the PID of the Python shell process and the parent PID (the PID of your BASH shell) using os.getpid() and os.getppid() system calls. Then, in another terminal window run ps command and grep for the PPID (parent process ID, which in my case is 3148). In the screenshot below you can see an example of a parent-child relationship between my child Python shell process and the parent BASH shell process on my Mac OS X:



Another important concept to know is that of a file descriptor. So what is a file descriptor? A file descriptor is a non-negative integer that the kernel returns to a process when it opens an existing file, creates a new file or when it creates a new socket. You’ve probably heard that in UNIX everything is a file. The kernel refers to the open files of a process by a file descriptor. When you need to read or write a file you identify it with the file descriptor. Python gives you high-level objects to deal with files (and sockets) and you don’t have to use file descriptors directly to identify a file but, under the hood, that’s how files and sockets are identified in UNIX: by their integer file descriptors.



By default, UNIX shells assign file descriptor 0 to the standard input of a process, file descriptor 1 to the standard output of the process and file descriptor 2 to the standard error.



As I mentioned before, even though Python gives you a high-level file or file-like object to work with, you can always use the fileno() method on the object to get the file descriptor associated with the file. Back to your Python shell to see how you can do that:

>>> import sys
>>> sys.stdin
<open file '<stdin>', mode 'r' at 0x102beb0c0>
>>> sys.stdin.fileno()
0
>>> sys.stdout.fileno()
1
>>> sys.stderr.fileno()
2
And while working with files and sockets in Python, you’ll usually be using a high-level file/socket object, but there may be times where you need to use a file descriptor directly. Here is an example of how you can write a string to the standard output using a write system call that takes a file descriptor integer as a parameter:

>>> import sys
>>> import os
>>> res = os.write(sys.stdout.fileno(), 'hello\n')
hello
And here is an interesting part - which should not be surprising to you anymore because you already know that everything is a file in Unix - your socket also has a file descriptor associated with it. Again, when you create a socket in Python you get back an object and not a non-negative integer, but you can always get direct access to the integer file descriptor of the socket with the fileno() method that I mentioned earlier.

>>> import socket
>>> sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> sock.fileno()
3
One more thing I wanted to mention: have you noticed that in the second example of the iterative server webserver3b.py, when the server process was sleeping for 60 seconds you could still connect to the server with the second curl command? Sure, the curl didn’t output anything right away and it was just hanging out there but how come the server was not accept ing a connection at the time and the client was not rejected right away, but instead was able to connect to the server? The answer to that is the listen method of a socket object and its BACKLOG argument, which I called REQUEST_QUEUE_SIZE in the code. The BACKLOG argument determines the size of a queue within the kernel for incoming connection requests. When the server webserver3b.py was sleeping, the second curl command that you ran was able to connect to the server because the kernel had enough space available in the incoming connection request queue for the server socket.

While increasing the BACKLOG argument does not magically turn your server into a server that can handle multiple client requests at a time, it is important to have a fairly large backlog parameter for busy servers so that the accept call would not have to wait for a new connection to be established but could grab the new connection off the queue right away and start processing a client request without delay.

Whoo-hoo! You’ve covered a lot of ground. Let’s quickly recap what you’ve learned (or refreshed if it’s all basics to you) so far.



Iterative server
Server socket creation sequence (socket, bind, listen, accept)
Client connection creation sequence (socket, connect)
Socket pair
Socket
Ephemeral port and well-known port
Process
Process ID (PID), parent process ID (PPID), and the parent-child relationship.
File descriptors
The meaning of the BACKLOG argument of the listen socket method

Now I am ready to answer the question from Part 2: “How can you make your server handle more than one request at a time?” Or put another way, “How do you write a concurrent server?”



The simplest way to write a concurrent server under Unix is to use a fork() system call.



Here is the code of your new shiny concurrent server webserver3c.py that can handle multiple client requests at the same time (as in our iterative server example webserver3b.py, every child process sleeps for 60 secs):



###########################################################################
# Concurrent server - webserver3c.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
#                                                                         #
# - Child process sleeps for 60 seconds after handling a client's request #
# - Parent and child processes close duplicate descriptors                #
#                                                                         #
###########################################################################
import os
import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(
        'Child PID: {pid}. Parent PID {ppid}'.format(
            pid=os.getpid(),
            ppid=os.getppid(),
        )
    )
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    time.sleep(60)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))
    print('Parent PID (PPID): {pid}\n'.format(pid=os.getpid()))

    while True:
        client_connection, client_address = listen_socket.accept()
        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)  # child exits here
        else:  # parent
            client_connection.close()  # close parent copy and loop over

if __name__ == '__main__':
    serve_forever()
Before diving in and discussing how fork works, try it, and see for yourself that the server can indeed handle multiple client requests at the same time, unlike its iterative counterparts webserver3a.py and webserver3b.py. Start the server on the command line with:

$ python webserver3c.py
And try the same two curl commands you’ve tried before with the iterative server and see for yourself that, now, even though the server child process sleeps for 60 seconds after serving a client request, it doesn’t affect other clients because they are served by different and completely independent processes. You should see your curl commands output “Hello, World!” instantly and then hang for 60 secs. You can keep on running as many curl commands as you want (well, almost as many as you want :) and all of them will output the server’s response “Hello, World” immediately and without any noticeable delay. Try it.

The most important point to understand about fork() is that you call fork once but it returns twice: once in the parent process and once in the child process. When you fork a new process the process ID returned to the child process is 0. When the fork returns in the parent process it returns the child’s PID.



I still remember how fascinated I was by fork when I first read about it and tried it. It looked like magic to me. Here I was reading a sequential code and then “boom!”: the code cloned itself and now there were two instances of the same code running concurrently. I thought it was nothing short of magic, seriously.

When a parent forks a new child, the child process gets a copy of the parent’s file descriptors:



You’ve probably noticed that the parent process in the code above closed the client connection:

else:  # parent
    client_connection.close()  # close parent copy and loop over
So how come a child process is still able to read the data from a client socket if its parent closed the very same socket? The answer is in the picture above. The kernel uses descriptor reference counts to decide whether to close a socket or not. It closes the socket only when its descriptor reference count becomes 0. When your server creates a child process, the child gets the copy of the parent’s file descriptors and the kernel increments the reference counts for those descriptors. In the case of one parent and one child, the descriptor reference count would be 2 for the client socket and when the parent process in the code above closes the client connection socket, it merely decrements its reference count which becomes 1, not small enough to cause the kernel to close the socket. The child process also closes the duplicate copy of the parent’s listen_socket because the child doesn’t care about accepting new client connections, it cares only about processing requests from the established client connection:

listen_socket.close()  # close child copy
I’ll talk about what happens if you do not close duplicate descriptors later in the article.

As you can see from the source code of your concurrent server, the sole role of the server parent process now is to accept a new client connection, fork a new child process to handle that client request, and loop over to accept another client connection, and nothing more. The server parent process does not process client requests - its children do.

A little aside. What does it mean when we say that two events are concurrent?



When we say that two events are concurrent we usually mean that they happen at the same time. As a shorthand that definition is fine, but you should remember the strict definition:

Two events are concurrent if you cannot tell by looking at the program which will happen first.2
Again, it’s time to recap the main ideas and concepts you’ve covered so far.



The simplest way to write a concurrent server in Unix is to use the fork() system call
When a process forks a new process it becomes a parent process to that newly forked child process.
Parent and child share the same file descriptors after the call to fork.
The kernel uses descriptor reference counts to decide whether to close the file/socket or not
The role of a server parent process: all it does now is accept a new connection from a client, fork a child to handle the client request, and loop over to accept a new client connection.

Let’s see what is going to happen if you don’t close duplicate socket descriptors in the parent and child processes. Here is a modified version of the concurrent server where the server does not close duplicate descriptors, webserver3d.py:

###########################################################################
# Concurrent server - webserver3d.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
###########################################################################
import os
import socket

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5


def handle_request(client_connection):
    request = client_connection.recv(1024)
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    clients = []
    while True:
        client_connection, client_address = listen_socket.accept()
        # store the reference otherwise it's garbage collected
        # on the next loop run
        clients.append(client_connection)
        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)  # child exits here
        else:  # parent
            # client_connection.close()
            print(len(clients))

if __name__ == '__main__':
    serve_forever()
Start the server with:

$ python webserver3d.py
Use curl to connect to the server:

$ curl http://localhost:8888/hello
Hello, World!
Okay, the curl printed the response from the concurrent server but it did not terminate and kept hanging. What is happening here? The server no longer sleeps for 60 seconds: its child process actively handles a client request, closes the client connection and exits, but the client curl still does not terminate.



So why does the curl not terminate? The reason is the duplicate file descriptors. When the child process closed the client connection, the kernel decremented the reference count of that client socket and the count became 1. The server child process exited, but the client socket was not closed by the kernel because the reference count for that socket descriptor was not 0, and, as a result, the termination packet (called FIN in TCP/IP parlance) was not sent to the client and the client stayed on the line, so to speak. There is also another problem. If your long-running server doesn’t close duplicate file descriptors, it will eventually run out of available file descriptors:



Stop your server webserver3d.py with Control-C and check out the default resources available to your server process set up by your shell with the shell built-in command ulimit:

$ ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 3842
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 3842
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
As you can see above, the maximum number of open file descriptors (open files) available to the server process on my Ubuntu box is 1024.

Now let’s see how your server can run out of available file descriptors if it doesn’t close duplicate descriptors. In an existing or new terminal window, set the maximum number of open file descriptors for your server to be 256:

$ ulimit -n 256
Start the server webserver3d.py in the same terminal where you’ve just run the $ ulimit -n 256 command:

$ python webserver3d.py
and use the following client client3.py to test the server.

#####################################################################
# Test client - client3.py                                          #
#                                                                   #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X  #
#####################################################################
import argparse
import errno
import os
import socket


SERVER_ADDRESS = 'localhost', 8888
REQUEST = b"""\
GET /hello HTTP/1.1
Host: localhost:8888

"""


def main(max_clients, max_conns):
    socks = []
    for client_num in range(max_clients):
        pid = os.fork()
        if pid == 0:
            for connection_num in range(max_conns):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(SERVER_ADDRESS)
                sock.sendall(REQUEST)
                socks.append(sock)
                print(connection_num)
                os._exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Test client for LSBAWS.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '--max-conns',
        type=int,
        default=1024,
        help='Maximum number of connections per client.'
    )
    parser.add_argument(
        '--max-clients',
        type=int,
        default=1,
        help='Maximum number of clients.'
    )
    args = parser.parse_args()
    main(args.max_clients, args.max_conns)
In a new terminal window, start the client3.py and tell it to create 300 simultaneous connections to the server:

$ python client3.py --max-clients=300
Soon enough your server will explode. Here is a screenshot of the exception on my box:



The lesson is clear - your server should close duplicate descriptors. But even if you close duplicate descriptors, you are not out of the woods yet because there is another problem with your server, and that problem is zombies!



Yes, your server code actually creates zombies. Let’s see how. Start up your server again:

$ python webserver3d.py
Run the following curl command in another terminal window:

$ curl http://localhost:8888/hello
And now run the ps command to show running Python processes. This the example of ps output on my Ubuntu box:

$ ps auxw | grep -i python | grep -v grep
vagrant   9099  0.0  1.2  31804  6256 pts/0    S+   16:33   0:00 python webserver3d.py
vagrant   9102  0.0  0.0      0     0 pts/0    Z+   16:33   0:00 [python] <defunct>
Do you see the second line above where it says the status of the process with PID 9102 is Z+ and the name of the process is <defunct>? That’s our zombie there. The problem with zombies is that you can’t kill them.



Even if you try to kill zombies with $ kill -9 , they will survive. Try it and see for yourself.

What is a zombie anyway and why does our server create them? A zombie is a process that has terminated, but its parent has not waited for it and has not received its termination status yet. When a child process exits before its parent, the kernel turns the child process into a zombie and stores some information about the process for its parent process to retrieve later. The information stored is usually the process ID, the process termination status, and the resource usage by the process. Okay, so zombies serve a purpose, but if your server doesn’t take care of these zombies your system will get clogged up. Let’s see how that happens. First stop your running server and, in a new terminal window, use the ulimit command to set the max user processess to 400(make sure to set open files to a high number, let’s say 500 too):

$ ulimit -u 400
$ ulimit -n 500
Start the server webserver3d.py in the same terminal where you’ve just run the $ ulimit -u 400 command:

$ python webserver3d.py
In a new terminal window, start the client3.py and tell it to create 500 simultaneous connections to the server:

$ python client3.py --max-clients=500
And, again, soon enough your server will blow up with an OSError: Resource temporarily unavailable exception when it tries to create a new child process, but it can’t because it has reached the limit for the maximum number of child processes it’s allowed to create. Here is a screenshot of the exception on my box:



As you can see, zombies create problems for your long-running server if it doesn’t take care of them. I will discuss shortly how the server should deal with that zombie problem.

Let’s recap the main points you’ve covered so far:



If you don’t close duplicate descriptors, the clients won’t terminate because the client connections won’t get closed.
If you don’t close duplicate descriptors, your long-running server will eventually run out of available file descriptors (max open files).
When you fork a child process and it exits and the parent process doesn’t wait for it and doesn’t collect its termination status, it becomes a zombie.
Zombies need to eat something and, in our case, it’s memory. Your server will eventually run out of available processes (max user processes) if it doesn’t take care of zombies.
You can’t kill a zombie, you need to wait for it.

So what do you need to do to take care of zombies? You need to modify your server code to wait for zombies to get their termination status. You can do that by modifying your server to call a wait system call. Unfortunately, that’s far from ideal because if you call wait and there is no terminated child process the call to wait will block your server, effectively preventing your server from handling new client connection requests. Are there any other options? Yes, there are, and one of them is the combination of a signal handler with the wait system call.



Here is how it works. When a child process exits, the kernel sends a SIGCHLD signal. The parent process can set up a signal handler to be asynchronously notified of that SIGCHLD event and then it can wait for the child to collect its termination status, thus preventing the zombie process from being left around.



By the way, an asynchronous event means that the parent process doesn’t know ahead of time that the event is going to happen.

Modify your server code to set up a SIGCHLD event handler and wait for a terminated child in the event handler. The code is available in webserver3e.py file:

###########################################################################
# Concurrent server - webserver3e.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
###########################################################################
import os
import signal
import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5


def grim_reaper(signum, frame):
    pid, status = os.wait()
    print(
        'Child {pid} terminated with status {status}'
        '\n'.format(pid=pid, status=status)
    )


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    # sleep to allow the parent to loop over to 'accept' and block there
    time.sleep(3)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        client_connection, client_address = listen_socket.accept()
        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:  # parent
            client_connection.close()

if __name__ == '__main__':
    serve_forever()
Start the server:

$ python webserver3e.py
Use your old friend curl to send a request to the modified concurrent server:

$ curl http://localhost:8888/hello
Look at the server:



What just happened? The call to accept failed with the error EINTR.



The parent process was blocked in accept call when the child process exited which caused SIGCHLD event, which in turn activated the signal handler and when the signal handler finished the accept system call got interrupted:



Don’t worry, it’s a pretty simple problem to solve, though. All you need to do is to re-start the accept system call. Here is the modified version of the server webserver3f.py that handles that problem:

###########################################################################
# Concurrent server - webserver3f.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
###########################################################################
import errno
import os
import signal
import socket

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 1024


def grim_reaper(signum, frame):
    pid, status = os.wait()


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args
            # restart 'accept' if it was interrupted
            if code == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:  # parent
            client_connection.close()  # close parent copy and loop over


if __name__ == '__main__':
    serve_forever()
Start the updated server webserver3f.py:

$ python webserver3f.py
Use curl to send a request to the modified concurrent server:

$ curl http://localhost:8888/hello
See? No EINTR exceptions any more. Now, verify that there are no more zombies either and that your SIGCHLD event handler with wait call took care of terminated children. To do that, just run the ps command and see for yourself that there are no more Python processes with Z+ status (no more <defunct> processes). Great! It feels safe without zombies running around.



If you fork a child and don’t wait for it, it becomes a zombie.
Use the SIGCHLD event handler to asynchronously wait for a terminated child to get its termination status
When using an event handler you need to keep in mind that system calls might get interrupted and you need to be prepared for that scenario

Okay, so far so good. No problems, right? Well, almost. Try your webserver3f.py again, but instead of making one request with curl use client3.py to create 128 simultaneous connections:

$ python client3.py --max-clients 128
Now run the ps command again

$ ps auxw | grep -i python | grep -v grep
and see that, oh boy, zombies are back again!



What went wrong this time? When you ran 128 simultaneous clients and established 128 connections, the child processes on the server handled the requests and exited almost at the same time causing a flood of SIGCHLD signals being sent to the parent process. The problem is that the signals are not queued and your server process missed several signals, which left several zombies running around unattended:



The solution to the problem is to set up a SIGCHLD event handler but instead of wait use a waitpid system call with a WNOHANG option in a loop to make sure that all terminated child processes are taken care of. Here is the modified server code, webserver3g.py:

###########################################################################
# Concurrent server - webserver3g.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
###########################################################################
import errno
import os
import signal
import socket

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 1024


def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,          # Wait for any child process
                 os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0:  # no more zombies
            return


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args
            # restart 'accept' if it was interrupted
            if code == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:  # parent
            client_connection.close()  # close parent copy and loop over

if __name__ == '__main__':
    serve_forever()
Start the server:

$ python webserver3g.py
Use the test client client3.py:

$ python client3.py --max-clients 128
And now verify that there are no more zombies. Yay! Life is good without zombies :)



Congratulations! It’s been a pretty long journey but I hope you liked it. Now you have your own simple concurrent server and the code can serve as a foundation for your further work towards a production grade Web server.

I’ll leave it as an exercise for you to update the WSGI server from Part 2 and make it concurrent. You can find the modified version here. But look at my code only after you’ve implemented your own version. You have all the necessary information to do that. So go and just do it :)

What’s next? As Josh Billings said,

“Be like a postage stamp — stick to one thing until you get there.”
Start mastering the basics. Question what you already know. And always dig deeper.



=======
> 原文链接：[http://ruslanspivak.com/lsbaws-part3/](http://ruslanspivak.com/lsbaws-part3/)
> 译文链接：[http://codingpy.com/article/build-a-simple-web-server-part-three/](http://codingpy.com/article/build-a-simple-web-server-part-three/)


“We learn most when we have to invent” —Piaget

在第二部分中，你开发了一个能够处理HTTPGET请求的简易WSGI服务器。在上一篇的最后，我问了你一个问题：“怎样让服务器一次处理多个请求？”读完本文，你就能够完美地回答这个问题。接下来，请你做好准备，因为本文的内容非常多，节奏也很快。文中的所有代码都可以在[Github仓库](https://github.com/rspivak/lsbaws/blob/master/part3/)下载。

首先，我们简单回忆一下简易网络服务器是如何实现的，服务器要处理客户端的请求需要哪些条件。你在前面两部分文章中开发的服务器，是一个迭代式服务器（iterative server），还只能一次处理一个客户端请求。只有在处理完当前客户端请求之后，它才能接收新的客户端连接。这样，有些客户端就必须要等待自己的请求被处理了，而对于流量大的服务器来说，等待的时间就会特别长。

![客户端逐个等待服务器响应](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it1.png)

下面是迭代式服务器`webserver3a.py`的代码：

    :::python
    #####################################################################
    # Iterative server - webserver3a.py                                 #
    #                                                                   #
    # Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X  #
    #####################################################################
    import socket

    SERVER_ADDRESS = (HOST, PORT) = '', 8888
    REQUEST_QUEUE_SIZE = 5


    def handle_request(client_connection):
        request = client_connection.recv(1024)
        print(request.decode())
        http_response = b"""\
    HTTP/1.1 200 OK

    Hello, World!
    """
        client_connection.sendall(http_response)


    def serve_forever():
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(SERVER_ADDRESS)
        listen_socket.listen(REQUEST_QUEUE_SIZE)
        print('Serving HTTP on port {port} ...'.format(port=PORT))

        while True:
            client_connection, client_address = listen_socket.accept()
            handle_request(client_connection)
            client_connection.close()

    if __name__ == '__main__':
        serve_forever()

如果想确认这个服务器每次只能处理一个客户端的请求，我们对上述代码作简单修改，在向客户端返回响应之后，增加60秒的延迟处理时间。这个修改只有一行代码，即告诉服务器在返回响应之后睡眠60秒。

![让服务器睡眠60秒](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it2.png)

下面就是修改之后的服务器代码：

    :::python
    #########################################################################
    # Iterative server - webserver3b.py                                     #
    #                                                                       #
    # Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X      #
    #                                                                       #
    # - Server sleeps for 60 seconds after sending a response to a client   #
    #########################################################################
    import socket
    import time

    SERVER_ADDRESS = (HOST, PORT) = '', 8888
    REQUEST_QUEUE_SIZE = 5


    def handle_request(client_connection):
        request = client_connection.recv(1024)
        print(request.decode())
        http_response = b"""\
    HTTP/1.1 200 OK

    Hello, World!
    """
        client_connection.sendall(http_response)
        time.sleep(60)  # sleep and block the process for 60 seconds


    def serve_forever():
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(SERVER_ADDRESS)
        listen_socket.listen(REQUEST_QUEUE_SIZE)
        print('Serving HTTP on port {port} ...'.format(port=PORT))

        while True:
            client_connection, client_address = listen_socket.accept()
            handle_request(client_connection)
            client_connection.close()

    if __name__ == '__main__':
        serve_forever()

接下来，我们启动服务器：

    $ python webserver3b.py

现在，我们打开一个新的终端窗口，并运行`curl`命令。你会立刻看到屏幕上打印出了“Hello, World!”这句话：

    $ curl http://localhost:8888/hello
    Hello, World!

接着我们立刻再打开一个终端窗口，并运行`curl`命令：


    $ curl http://localhost:8888/hello

如果你在60秒了完成了上面的操作，那么第二个`curl`命令应该不会立刻产生任何输出结果，而是处于挂死（hang）状态。服务器也不会在标准输出中打印这个新请求的正文。下面这张图就是我在自己的Mac上操作时的结果（右下角那个边缘高亮为黄色的窗口，显示的就是第二个`curl`命令挂死）：

![Mac上操作时的结果](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it3.png)

当然，你等了足够长时间之后（超过60秒），你会看到第一个`curl`命令结束，然后第二个`curl`命令会在屏幕上打印出“Hello, World!”，之后再挂死60秒，最后才结束：

![curl命令演示](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it4.png)

这背后的实现方式是，服务器处理完第一个`curl`客户端请求后睡眠60秒，才开始处理第二个请求。这些步骤是线性执行的，或者说迭代式一步一步执行的。在我们这个实例中，则是一次一个请求这样处理。

接下来，我们简单谈谈客户端与服务器之间的通信。为了让两个程序通过网络进行通信，二者均必须使用套接字。你在前两章中也看到过套接字，但到底什么是套接字？

![什么是套接字](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_socket.png)

套接字是通信端点（communication endpoint）的抽象形式，可以让一个程序通过文件描述符（file descriptor）与另一个程序进行通信。在本文中，我只讨论Linux/Mac OS X平台上的TCP/IP套接字。其中，尤为重要的一个概念就是TCP套接字对（socket pair）。

> TCP连接所使用的套接字对是一个4元组（4-tuple），包括本地IP地址、本地端口、外部IP地址和外部端口。一个网络中的每一个TCP连接，都拥有独特的套接字对。IP地址和端口号通常被称为一个套接字，二者一起标识了一个网络端点。

![套接字对合套接字](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_socketpair.png)

因此，`{10.10.10.2:49152, 12.12.12.3:8888}`元组组成了一个套接字对，代表客户端侧TCP连接的两个唯一端点，`{12.12.12.3:8888, 10.10.10.2:49152}`元组组成另一个套接字对，代表服务器侧TCP连接的两个同样端点。构成TCP连接中服务器端点的两个值分别是IP地址`12.12.12.3`和端口号`8888`，它们在这里被称为一个套接字（同理，客户端端点的两个值也是一个套接字）。

服务器创建套接字并开始接受客户端连接的标准流程如下：

![服务器创建套接字并开始接受客户端连接的标准流程](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_server_socket_sequence.png)

1. 服务器创建一个TCP/IP套接字。通过下面的Python语句实现：

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

2. 服务器可以设置部分套接字选项（这是可选项，但你会发现上面那行服务器代码就可以确保你重启服务器之后，服务器会继续使用相同的地址）。

    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

3. 然后，服务器绑定地址。绑定函数为套接字指定一个本地协议地址。调用绑定函数时，你可以单独指定端口号或IP地址，也可以同时指定两个参数，甚至不提供任何参数也没问题。

    listen_socket.bind(SERVER_ADDRESS)

4. 接着，服务器将该套接字变成一个侦听套接字：

    listen_socket.listen(REQUEST_QUEUE_SIZE)

`listen`方法只能由服务器调用，执行后会告知服务器应该接收针对该套接字的连接请求。

完成上面四步之后，服务器会开启一个循环，开始接收客户端连接，不过一次只接收一个连接。当有连接请求时，`accept`方法会返回已连接的客户端套接字。然后，服务器从客户端套接字读取请求数据，在标准输出中打印数据，并向客户端返回消息。最后，服务器会关闭当前的客户端连接，这时服务器又可以接收新的客户端连接了。

要通过TCP/IP协议与服务器进行通信，客户端需要作如下操作：

![客户端与服务器进行通信所需要的操作](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_client_socket_sequence.png)

下面这段示例代码，实现了客户端连接至服务器，发送请求，并打印响应内容的过程：

    :::python
    import socket

    # create a socket and connect to a server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8888))

    # send and receive some data
    sock.sendall(b'test')
    data = sock.recv(1024)
    print(data.decode())

在创建套接字之后，客户端需要与服务器进行连接，这可以通过调用`connect`方法实现：

    sock.connect(('localhost', 8888))

客户端只需要提供远程IP地址或主机名，以及服务器的远程连接端口号即可。

你可能已经注意到，客户端不会调用`bind`和`accept`方法。不需要调用`bind`方法，是因为客户端不关心本地IP地址和本地端口号。客户端调用`connect`方法时，系统内核中的TCP/IP栈会自动指定本地IP地址和本地端口。本地端口也被称为临时端口（ephemeral port）。

![本地端口——临时端口号](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_ephemeral_port.png)

服务器端有部分端口用于连接熟知的服务，这种端口被叫做“熟知端口”（well-known port），例如，80用于HTTP传输服务，22用于SSH协议传输。接下来，我们打开Python shell，向在本地运行的服务器发起一个客户端连接，然后查看系统内核为你创建的客户端套接字指定了哪个临时端口（在进行下面的操作之前，请先运行`webserver3a.py`或`webserver3b.py`文件，启动服务器）：

    :::python
    >>> import socket
    >>> sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    >>> sock.connect(('localhost', 8888))
    >>> host, port = sock.getsockname()[:2]
    >>> host, port
    ('127.0.0.1', 60589)

在上面的示例中，我们看到内核为套接字指定的临时端口是60589。

在开始回答第二部分最后提的问题之前，我需要快速介绍一些其他的重要概念。稍后你就会明白我为什么要这样做。我要介绍的重要概念就是进程（process）和文件描述符（file descriptor）。

什么是进程？进程就是正在执行的程序的一个实例。举个例子，当服务器代码执行的时候，这些代码就被加载至内存中，而这个正在被执行的服务器的实例就叫做进程。系统内核会记录下有关进程的信息——包括进程ID，以便进行管理。所以，当你运行迭代式服务器`webserver3a.py`或`webserver3b.py`时，你也就开启了一个进程。

![服务器进程](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_server_process.png)

我们在终端启动`webserver3a.py`服务器：

    $ python webserver3b.py

然后，我们在另一个终端窗口中，使用`ps`命令来获取上面那个服务器进程的信息：

    $ ps | grep webserver3b | grep -v grep 
    7182 ttys003    0:00.04 python webserver3b.py

从`ps`命令的结果，我们可以看出你的确只运行了一个Python进程`webserver3b`。进程创建的时候，内核会给它指定一个进程ID——PID。在UNIX系统下，每个用户进程都会有一个父进程（parent process），而这个父进程也有自己的进程ID，叫做父进程ID，简称PPID。在本文中，我默认大家使用的是BASH，因此当你启动服务器的时候，系统会创建服务器进程，指定一个PID，而服务器进程的父进程PID则是BASH shell进程的PID。

![进程ID与父进程ID](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_ppid_pid.png)

接下来请自己尝试操作一下。再次打开你的Python shell程序，这会创建一个新进程，然后我们通过`os.gepid()`和`os.getppid()`这两个方法，分别获得Python shell进程的PID及它的父进程PID（即BASH shell程序的PID）。接着，我们打开另一个终端窗口，运行`ps`命令，`grep`检索刚才所得到的PPID（父进程ID，本操作时的结果是3148）。在下面的截图中，你可以看到我在Mac OS X上的操作结果：

![Mac OS X系统下进程ID与父进程ID演示](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_pid_ppid_screenshot.png)

另一个需要掌握的重要概念就是文件描述符（file descriptor）。那么，到底什么是文件描述符？文件描述符指的就是当系统打开一个现有文件、创建一个新文件或是创建一个新的套接字之后，返回给进程的那个正整型数。系统内核通过文件描述符来追踪一个进程所打开的文件。当你需要读写文件时，你也通过文件描述符说明。Python语言中提供了用于处理文件（和套接字）的高层级对象，所以你不必直接使用文件描述符来指定文件，但是从底层实现来看，UNIX系统中就是通过它们的文件描述符来确定文件和套接字的。

![文件描述符](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_process_descriptors.png)

一般来说，UNIX shell会将文件描述符0指定给进程的标准输出，文件描述富1指定给进程的标准输出，文件描述符2指定给标准错误。

![标准输入的文件描述符](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_it_default_descriptors.png)

正如我前面提到的那样，即使Python语言提供了高层及的文件或类文件对象，你仍然可以对文件对象使用`fileno()`方法，来获取该文件相应的文件描述符。我们回到Python shell中来试验一下。

    :::python
    >>> import sys
    >>> sys.stdin
    <open file '<stdin>', mode 'r' at 0x102beb0c0>
    >>> sys.stdin.fileno()
    0
    >>> sys.stdout.fileno()
    1
    >>> sys.stderr.fileno()
    2

在Python语言中处理文件和套接字时，你通常只需要使用高层及的文件/套接字对象即可，但是有些时候你也可能需要直接使用文件描述符。下面这个示例演示了你如何通过`write()`方法向标准输出中写入一个字符串，而这个`write`方法就接受文件描述符作为自己的参数：

    :::python
    >>> import sys
    >>> import os
    >>> res = os.write(sys.stdout.fileno(), 'hello\n')
    hello

还有一点挺有意思——如果你知道Unix系统下一切都是文件，那么你就不会觉得奇怪了。当你在Python中创建一个套接字后，你获得的是一个套接字对象，而不是一个正整型数，但是你还是可以和上面演示的一样，通过`fileno()`方法直接访问这个套接字的文件描述符。

    >>> import socket
    >>> sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    >>> sock.fileno()
    3

我还想再说一点：不知道大家有没有注意到，在迭代式服务器`webserver3b.py`的第二个示例中，我们的服务器在处理完请求后睡眠60秒，但是在睡眠期间，我们仍然可以通过`curl`命令与服务器建立连接？当然，`curl`命令并没有立刻输出结果，只是出于挂死状态，但是为什么服务器既然没有接受新的连接，客户端也没有立刻被拒绝，而是仍然继续连接至服务器呢？这个问题的答案在于套接字对象的`listen`方法，以及它使用的`BACKLOG`参数。在示例代码中，这个参数的值被我设置为`REQUEST_QUEQUE_SIZE`。`BACKLOG`参数决定了内核中外部连接请求的队列大小。当`webserver3b.py`服务器睡眠时，你运行的第二个`curl`命令之所以能够连接服务器，是因为连接请求队列仍有足够的位置。

虽然提高`BACKLOG`参数的值并不会让你的服务器一次处理多个客户端请求，但是业务繁忙的服务器也应该设置一个较大的`BACKLOG`参数值，这样`accept`函数就可以直接从队列中获取新连接，立刻开始处理客户端请求，而不是还要花时间等待连接建立。

呜呼！到目前为止，已经给大家介绍了很多知识。我们现在快速回顾一下之前的内容。

> - 迭代式服务器
> - 服务器套接字创建流程（socket, bind, listen, accept）
> - 客户端套接字创建流程（socket, connect）
> - 套接字对（Socket pair）
> - 套接字
> - 临时端口（Ephemeral port）与熟知端口（well-known port）
> - 进程
> - 进程ID（PID），父进程ID（PPID）以及父子关系
> - 文件描述符（File descriptors）
> - 套接字对象的`listen`方法中`BACKLOG`参数的意义

现在，我可以开始回答第二部分留下的问题了：如何让服务器一次处理多个请求？换句话说，如何开发一个并发服务器？

![并发服务器手绘演示](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_conc2_service_clients.png)

在Unix系统中开发一个并发服务器的最简单方法，就是调用系统函数`fork()`。

![fork()系统函数调用](http://ruslanspivak.com/lsbaws-part3/lsbaws_part3_fork.png)

下面就是崭新的`webserver3c.py`并发服务器，支持同时处理多个客户端请求：

    :::python
    ###########################################################################
    # Concurrent server - webserver3c.py                                      #
    #                                                                         #
    # Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
    #                                                                         #
    # - Child process sleeps for 60 seconds after handling a client's request #
    # - Parent and child processes close duplicate descriptors                #
    #                                                                         #
    ###########################################################################
    import os
    import socket
    import time

    SERVER_ADDRESS = (HOST, PORT) = '', 8888
    REQUEST_QUEUE_SIZE = 5


    def handle_request(client_connection):
        request = client_connection.recv(1024)
        print(
            'Child PID: {pid}. Parent PID {ppid}'.format(
                pid=os.getpid(),
                ppid=os.getppid(),
            )
        )
        print(request.decode())
        http_response = b"""\
    HTTP/1.1 200 OK

    Hello, World!
    """
        client_connection.sendall(http_response)
        time.sleep(60)


    def serve_forever():
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(SERVER_ADDRESS)
        listen_socket.listen(REQUEST_QUEUE_SIZE)
        print('Serving HTTP on port {port} ...'.format(port=PORT))
        print('Parent PID (PPID): {pid}\n'.format(pid=os.getpid()))

        while True:
            client_connection, client_address = listen_socket.accept()
            pid = os.fork()
            if pid == 0:  # child
                listen_socket.close()  # close child copy
                handle_request(client_connection)
                client_connection.close()
                os._exit(0)  # child exits here
            else:  # parent
                client_connection.close()  # close parent copy and loop over

    if __name__ == '__main__':
        serve_forever()

Before diving in and discussing how fork works, try it, and see for yourself that the server can indeed handle multiple client requests at the same time, unlike its iterative counterparts webserver3a.py and webserver3b.py. Start the server on the command line with:

$ python webserver3c.py
And try the same two curl commands you’ve tried before with the iterative server and see for yourself that, now, even though the server child process sleeps for 60 seconds after serving a client request, it doesn’t affect other clients because they are served by different and completely independent processes. You should see your curl commands output “Hello, World!” instantly and then hang for 60 secs. You can keep on running as many curl commands as you want (well, almost as many as you want :) and all of them will output the server’s response “Hello, World” immediately and without any noticeable delay. Try it.

The most important point to understand about fork() is that you call fork once but it returns twice: once in the parent process and once in the child process. When you fork a new process the process ID returned to the child process is 0. When the fork returns in the parent process it returns the child’s PID.



I still remember how fascinated I was by fork when I first read about it and tried it. It looked like magic to me. Here I was reading a sequential code and then “boom!”: the code cloned itself and now there were two instances of the same code running concurrently. I thought it was nothing short of magic, seriously.

When a parent forks a new child, the child process gets a copy of the parent’s file descriptors:



You’ve probably noticed that the parent process in the code above closed the client connection:

else:  # parent
    client_connection.close()  # close parent copy and loop over
So how come a child process is still able to read the data from a client socket if its parent closed the very same socket? The answer is in the picture above. The kernel uses descriptor reference counts to decide whether to close a socket or not. It closes the socket only when its descriptor reference count becomes 0. When your server creates a child process, the child gets the copy of the parent’s file descriptors and the kernel increments the reference counts for those descriptors. In the case of one parent and one child, the descriptor reference count would be 2 for the client socket and when the parent process in the code above closes the client connection socket, it merely decrements its reference count which becomes 1, not small enough to cause the kernel to close the socket. The child process also closes the duplicate copy of the parent’s listen_socket because the child doesn’t care about accepting new client connections, it cares only about processing requests from the established client connection:

listen_socket.close()  # close child copy
I’ll talk about what happens if you do not close duplicate descriptors later in the article.

As you can see from the source code of your concurrent server, the sole role of the server parent process now is to accept a new client connection, fork a new child process to handle that client request, and loop over to accept another client connection, and nothing more. The server parent process does not process client requests - its children do.

A little aside. What does it mean when we say that two events are concurrent?



When we say that two events are concurrent we usually mean that they happen at the same time. As a shorthand that definition is fine, but you should remember the strict definition:

Two events are concurrent if you cannot tell by looking at the program which will happen first.2
Again, it’s time to recap the main ideas and concepts you’ve covered so far.



The simplest way to write a concurrent server in Unix is to use the fork() system call
When a process forks a new process it becomes a parent process to that newly forked child process.
Parent and child share the same file descriptors after the call to fork.
The kernel uses descriptor reference counts to decide whether to close the file/socket or not
The role of a server parent process: all it does now is accept a new connection from a client, fork a child to handle the client request, and loop over to accept a new client connection.

Let’s see what is going to happen if you don’t close duplicate socket descriptors in the parent and child processes. Here is a modified version of the concurrent server where the server does not close duplicate descriptors, webserver3d.py:

###########################################################################
# Concurrent server - webserver3d.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
###########################################################################
import os
import socket

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5


def handle_request(client_connection):
    request = client_connection.recv(1024)
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    clients = []
    while True:
        client_connection, client_address = listen_socket.accept()
        # store the reference otherwise it's garbage collected
        # on the next loop run
        clients.append(client_connection)
        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)  # child exits here
        else:  # parent
            # client_connection.close()
            print(len(clients))

if __name__ == '__main__':
    serve_forever()
Start the server with:

$ python webserver3d.py
Use curl to connect to the server:

$ curl http://localhost:8888/hello
Hello, World!
Okay, the curl printed the response from the concurrent server but it did not terminate and kept hanging. What is happening here? The server no longer sleeps for 60 seconds: its child process actively handles a client request, closes the client connection and exits, but the client curl still does not terminate.



So why does the curl not terminate? The reason is the duplicate file descriptors. When the child process closed the client connection, the kernel decremented the reference count of that client socket and the count became 1. The server child process exited, but the client socket was not closed by the kernel because the reference count for that socket descriptor was not 0, and, as a result, the termination packet (called FIN in TCP/IP parlance) was not sent to the client and the client stayed on the line, so to speak. There is also another problem. If your long-running server doesn’t close duplicate file descriptors, it will eventually run out of available file descriptors:



Stop your server webserver3d.py with Control-C and check out the default resources available to your server process set up by your shell with the shell built-in command ulimit:

$ ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 3842
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 3842
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
As you can see above, the maximum number of open file descriptors (open files) available to the server process on my Ubuntu box is 1024.

Now let’s see how your server can run out of available file descriptors if it doesn’t close duplicate descriptors. In an existing or new terminal window, set the maximum number of open file descriptors for your server to be 256:

$ ulimit -n 256
Start the server webserver3d.py in the same terminal where you’ve just run the $ ulimit -n 256 command:

$ python webserver3d.py
and use the following client client3.py to test the server.

#####################################################################
# Test client - client3.py                                          #
#                                                                   #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X  #
#####################################################################
import argparse
import errno
import os
import socket


SERVER_ADDRESS = 'localhost', 8888
REQUEST = b"""\
GET /hello HTTP/1.1
Host: localhost:8888

"""


def main(max_clients, max_conns):
    socks = []
    for client_num in range(max_clients):
        pid = os.fork()
        if pid == 0:
            for connection_num in range(max_conns):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(SERVER_ADDRESS)
                sock.sendall(REQUEST)
                socks.append(sock)
                print(connection_num)
                os._exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Test client for LSBAWS.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '--max-conns',
        type=int,
        default=1024,
        help='Maximum number of connections per client.'
    )
    parser.add_argument(
        '--max-clients',
        type=int,
        default=1,
        help='Maximum number of clients.'
    )
    args = parser.parse_args()
    main(args.max_clients, args.max_conns)
In a new terminal window, start the client3.py and tell it to create 300 simultaneous connections to the server:

$ python client3.py --max-clients=300
Soon enough your server will explode. Here is a screenshot of the exception on my box:



The lesson is clear - your server should close duplicate descriptors. But even if you close duplicate descriptors, you are not out of the woods yet because there is another problem with your server, and that problem is zombies!



Yes, your server code actually creates zombies. Let’s see how. Start up your server again:

$ python webserver3d.py
Run the following curl command in another terminal window:

$ curl http://localhost:8888/hello
And now run the ps command to show running Python processes. This the example of ps output on my Ubuntu box:

$ ps auxw | grep -i python | grep -v grep
vagrant   9099  0.0  1.2  31804  6256 pts/0    S+   16:33   0:00 python webserver3d.py
vagrant   9102  0.0  0.0      0     0 pts/0    Z+   16:33   0:00 [python] <defunct>
Do you see the second line above where it says the status of the process with PID 9102 is Z+ and the name of the process is <defunct>? That’s our zombie there. The problem with zombies is that you can’t kill them.



Even if you try to kill zombies with $ kill -9 , they will survive. Try it and see for yourself.

What is a zombie anyway and why does our server create them? A zombie is a process that has terminated, but its parent has not waited for it and has not received its termination status yet. When a child process exits before its parent, the kernel turns the child process into a zombie and stores some information about the process for its parent process to retrieve later. The information stored is usually the process ID, the process termination status, and the resource usage by the process. Okay, so zombies serve a purpose, but if your server doesn’t take care of these zombies your system will get clogged up. Let’s see how that happens. First stop your running server and, in a new terminal window, use the ulimit command to set the max user processess to 400(make sure to set open files to a high number, let’s say 500 too):

$ ulimit -u 400
$ ulimit -n 500
Start the server webserver3d.py in the same terminal where you’ve just run the $ ulimit -u 400 command:

$ python webserver3d.py
In a new terminal window, start the client3.py and tell it to create 500 simultaneous connections to the server:

$ python client3.py --max-clients=500
And, again, soon enough your server will blow up with an OSError: Resource temporarily unavailable exception when it tries to create a new child process, but it can’t because it has reached the limit for the maximum number of child processes it’s allowed to create. Here is a screenshot of the exception on my box:



As you can see, zombies create problems for your long-running server if it doesn’t take care of them. I will discuss shortly how the server should deal with that zombie problem.

Let’s recap the main points you’ve covered so far:



If you don’t close duplicate descriptors, the clients won’t terminate because the client connections won’t get closed.
If you don’t close duplicate descriptors, your long-running server will eventually run out of available file descriptors (max open files).
When you fork a child process and it exits and the parent process doesn’t wait for it and doesn’t collect its termination status, it becomes a zombie.
Zombies need to eat something and, in our case, it’s memory. Your server will eventually run out of available processes (max user processes) if it doesn’t take care of zombies.
You can’t kill a zombie, you need to wait for it.

So what do you need to do to take care of zombies? You need to modify your server code to wait for zombies to get their termination status. You can do that by modifying your server to call a wait system call. Unfortunately, that’s far from ideal because if you call wait and there is no terminated child process the call to wait will block your server, effectively preventing your server from handling new client connection requests. Are there any other options? Yes, there are, and one of them is the combination of a signal handler with the wait system call.



Here is how it works. When a child process exits, the kernel sends a SIGCHLD signal. The parent process can set up a signal handler to be asynchronously notified of that SIGCHLD event and then it can wait for the child to collect its termination status, thus preventing the zombie process from being left around.



By the way, an asynchronous event means that the parent process doesn’t know ahead of time that the event is going to happen.

Modify your server code to set up a SIGCHLD event handler and wait for a terminated child in the event handler. The code is available in webserver3e.py file:

###########################################################################
# Concurrent server - webserver3e.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
###########################################################################
import os
import signal
import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5


def grim_reaper(signum, frame):
    pid, status = os.wait()
    print(
        'Child {pid} terminated with status {status}'
        '\n'.format(pid=pid, status=status)
    )


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    # sleep to allow the parent to loop over to 'accept' and block there
    time.sleep(3)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        client_connection, client_address = listen_socket.accept()
        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:  # parent
            client_connection.close()

if __name__ == '__main__':
    serve_forever()
Start the server:

$ python webserver3e.py
Use your old friend curl to send a request to the modified concurrent server:

$ curl http://localhost:8888/hello
Look at the server:



What just happened? The call to accept failed with the error EINTR.



The parent process was blocked in accept call when the child process exited which caused SIGCHLD event, which in turn activated the signal handler and when the signal handler finished the accept system call got interrupted:



Don’t worry, it’s a pretty simple problem to solve, though. All you need to do is to re-start the accept system call. Here is the modified version of the server webserver3f.py that handles that problem:

###########################################################################
# Concurrent server - webserver3f.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
###########################################################################
import errno
import os
import signal
import socket

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 1024


def grim_reaper(signum, frame):
    pid, status = os.wait()


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args
            # restart 'accept' if it was interrupted
            if code == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:  # parent
            client_connection.close()  # close parent copy and loop over


if __name__ == '__main__':
    serve_forever()
Start the updated server webserver3f.py:

$ python webserver3f.py
Use curl to send a request to the modified concurrent server:

$ curl http://localhost:8888/hello
See? No EINTR exceptions any more. Now, verify that there are no more zombies either and that your SIGCHLD event handler with wait call took care of terminated children. To do that, just run the ps command and see for yourself that there are no more Python processes with Z+ status (no more <defunct> processes). Great! It feels safe without zombies running around.



If you fork a child and don’t wait for it, it becomes a zombie.
Use the SIGCHLD event handler to asynchronously wait for a terminated child to get its termination status
When using an event handler you need to keep in mind that system calls might get interrupted and you need to be prepared for that scenario

Okay, so far so good. No problems, right? Well, almost. Try your webserver3f.py again, but instead of making one request with curl use client3.py to create 128 simultaneous connections:

$ python client3.py --max-clients 128
Now run the ps command again

$ ps auxw | grep -i python | grep -v grep
and see that, oh boy, zombies are back again!



What went wrong this time? When you ran 128 simultaneous clients and established 128 connections, the child processes on the server handled the requests and exited almost at the same time causing a flood of SIGCHLD signals being sent to the parent process. The problem is that the signals are not queued and your server process missed several signals, which left several zombies running around unattended:



The solution to the problem is to set up a SIGCHLD event handler but instead of wait use a waitpid system call with a WNOHANG option in a loop to make sure that all terminated child processes are taken care of. Here is the modified server code, webserver3g.py:

###########################################################################
# Concurrent server - webserver3g.py                                      #
#                                                                         #
# Tested with Python 2.7.9 & Python 3.4 on Ubuntu 14.04 & Mac OS X        #
###########################################################################
import errno
import os
import signal
import socket

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 1024


def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,          # Wait for any child process
                 os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0:  # no more zombies
            return


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port=PORT))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args
            # restart 'accept' if it was interrupted
            if code == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()
        if pid == 0:  # child
            listen_socket.close()  # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:  # parent
            client_connection.close()  # close parent copy and loop over

if __name__ == '__main__':
    serve_forever()
Start the server:

$ python webserver3g.py
Use the test client client3.py:

$ python client3.py --max-clients 128
And now verify that there are no more zombies. Yay! Life is good without zombies :)



Congratulations! It’s been a pretty long journey but I hope you liked it. Now you have your own simple concurrent server and the code can serve as a foundation for your further work towards a production grade Web server.

I’ll leave it as an exercise for you to update the WSGI server from Part 2 and make it concurrent. You can find the modified version here. But look at my code only after you’ve implemented your own version. You have all the necessary information to do that. So go and just do it :)

What’s next? As Josh Billings said,

“Be like a postage stamp — stick to one thing until you get there.”
Start mastering the basics. Question what you already know. And always dig deeper.



>>>>>>> 03a62a1658c21b57e1f1e3fbeab2a07187c98ecf
“If you learn only methods, you’ll be tied to your methods. But if you learn principles, you can devise your own methods.” —Ralph Waldo Emerson