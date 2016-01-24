不经意间在Quora看到这样一个问题：Why did Quora choose Python for its development?2名Quora的创始人给出了答案，我觉得很有参考价值，所以摘录在此。首先，Adam D’Angelo曾就职于Facebook，而这家公司是大量使用PHP的。但Adam D’Angelo几乎对PHP没有好感，说Facebook使用PHP是历史遗留原因（我估计扎克伯格最初只想用PHP快速搭建一个网站吧），它存在太多缺点（原文给出了不少文章，我就不列出了）。
其次是C#，这是一门很有前途的语言，但是选择它就意味着加入了Microsoft的阵营（烧钱啊），而很多开源软件对.NET只有第2级的支持（比如更新太慢，或者性能较差之类的），甚至根本不支持。另外，他们也不能冒使用Mono的风险（性能，更新，甚至可能会被Microsoft扼杀）。

而Java和Python比起来，代码写起来太冗长和痛苦，且很难于非Java的（感觉确切来说应该是非JVM的）东西交互。Scala也有Java和JVM的很多缺点，尽管它没有Java那么糟糕。而且它有点新，可能会存在一些不必要的风险。

他们还考虑过OCaml和Haskell，也有着足够的生态体系和标准库，但是对可能要写一些代码的设计师、分析师来说太难了。

Ruby也是个选择，但他和Charlie Cheever都更懂Python一些。

Python最大的缺点是速度和类型检查。对他们而言Python已经足够快，而对性能有关键影响的部分都用C++写了；对于类型检查，他们写了足够多的单元测试来保证。
既然除去了这2个缺点，他们就很乐意选择Python了：

通过对过去5年的观察，他们确信Python将继续朝着对他们有利的方向发展。
有很多用Python写的库，可以很容易地与邮件服务器和任务队列等通信。他们采用了Python 2.6，这足够支持他们的库了。
Python有太多好框架（Django、Pylons等），且大都在不断进步。他们选择了Tornado（没给原因，但估计是对长连接的支持。）
PyPy可以带来显著的速度提升。
Python的数据结构和JavaScript（JSON）映射得很好，所以浏览器和服务器之间的通信很轻松，而Quora大量采用了这种无需载入页面的交互（还是长连接）。
Python的代码很易读（还应该加上表达能力强）。他们需要和很多人一起工作，这显得非常重要。
顺带一提，知乎可能也是因为这些理由选择Python和Tornado的。Quora Infrastructure这个标签可以知道很多技术内幕，真希望知乎也能增加一个；但国内的技术氛围似乎不方便透露，毕竟得考虑山寨的问题。

## 为什么Quora选择了Python？

关键词：Python企业级应用, Python开发的网站, Python网络开发, Python生态系统, Python开发框架, Python Quora

Quora是国外知名的问答社区，性质与知乎类似。它的创始人Adam D'Angelo曾是Facebook的员工，众所周知，Facebook大量地使用了PHP，而Adam在开发Quora时，使用的确是Python。

We were sure we didn't want to use PHP. Facebook is stuck on that for legacy reasons, not because it's the best choice right now.[1] Our main takeaway from that experience is that programming language choice is very important and is extremely costly to change.

Python was a language that Charlie and I both knew reasonably well (though I know it a lot better now than I did when we started). We also briefly considered C#, Java, and Scala. The biggest issues with Python are speed and the lack of typechecking.

C# seemed pretty promising. As a programming language, it's great, but:
We didn't want to be on the Microsoft stack. We were up for learning something new, and MS SQL Server actually seemed pretty good, but we knew we'd need to integrate with lots of open source code that has only second-class support for .NET, if it supports it at all. Also, most of the best engineers these days are used to open source stuff.
We didn't want to take the risk of being on Mono (an open source implementation of C#/.NET). It's not clear how long funding will be around for that project, and I'd heard of various performance problems. Plus, it seemed like everything else in the C# ecosystem would assume we were on the Microsoft stack.

For a lot of little reasons, Java programs end up being longer and more painful to write than the equivalent Python programs. It's also harder to interoperate with non-Java stuff. Scala had a lot of the downsides of Java and the JVM, although it wasn't quite as bad. The language seemed a little too new and like it would bring some unnecessary risk (for example, who knows how good support will be in 10 years).

Two other languages we very briefly thought about were OCaml and Haskell (neither had big enough ecosystems or good enough standard libraries, and both were potentially too hard for some designers/data analysts/non-engineers who might need to write code).

We decided that Python was fast enough for most of what we need to do (since we push our performance-critical code to backend servers written in C++ whenever possible). As far as typechecking, we ended up writing very thorough unit tests which are worth writing anyway, and achieve most of the same goals. We also had a lot of confidence that Python would continue to evolve in a direction that would be good for the life of our codebase, having watched it evolve over the last 5 years.

So far, we've been pretty happy with the choice. There's a small selection bias, but all of the early employees who'd been working with other languages in the past were happy to transition to Python, especially those coming from PHP. Since starting the following things have happened:

Python 2.6 got to the point where enough of the libraries we used were compatible with it, and we made a very easy transition to it.
Tornado (web framework) was released as open source, and we moved our live updating web service to that.
PyPy got to the point where it looks like it will eventually be usable and will give us a significant speedup.

All together, these give us confidence that the language and ecosystem is moving in a good direction.