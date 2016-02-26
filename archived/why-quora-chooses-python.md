## 为什么Quora选择了Python？

关键词：Python企业级应用, Python开发的网站, Python网络开发, Python生态系统, Python开发框架, Python Quora

Quora是国外知名的问答社区，性质与知乎类似。它的创始人Adam D'Angelo曾是Facebook的员工，众所周知，Facebook大量地使用了PHP，而Adam在开发Quora时，使用的却是Python。这到底是为什么呢？有人在Quora上提出了这个问题，而那个最佳答案自然就是来自Adam本人的了，对于那些犹豫要不要使用Python建站的开发者应该有一定的参考意义。

Adam在回答中很明确地表明了不希望使用PHP，提到Facebook由于历史遗留原因而不得不使用PHP，并不是因为PHP是目前最好的选择。他从自己在Facebook供职的那段经历中，明白了一个道理：选择哪个编程语言是非常重要的，变更的成本极其高昂。

![Quora创始人Adam D'Angelo](http://ww1.sinaimg.cn/large/006faQNTjw1f0cxd5pjv7j30ri0icdi0.jpg)

Adam和另外一名创始人当时对Python语言都比较熟悉。但还是考察了C#、Java和Scala等其他语言。

## C#

在Adam看来，C#当时是非常值得考虑的对象。作为编程语言来说，C#非常优秀，但是选择了C#，就意味着要被捆绑在微软的技术栈上。而他们心里更倾向于尝试新的技术方案。另外，虽然微软的SQL服务器也很好，但是考虑到他们要集成许多开源代码，而这些代码对于.NET平台的支持较差。而且，当时大部分最有优秀的工程师都已经习惯于使用开源的产品。除此之外，他们还不愿意冒险使用Mono（C#/.NET的开源实现），因为不知道这个项目能持续多长时间，还存在一些性能问题。

## Java和Scala

由于许多原因，Java程序比相同功能的Python代码写起来更加冗长、更加痛苦，而且很难与非Java的代码进行交互。另外，虽然Scala并没有Java那么差，但是也有许多Java和JVM的缺点。Scala语言当时也有点太新潮了，可能会带来一些不必要的风险，因为谁也不知道10年后对这个语言的支持会如何。

## Ocaml和Haskell

他们还考虑过OCaml和Haskell，但是二者都没有足够大的生态体系或是足够优秀的标准库，而且对可能要写一些代码的设计师、分析师来说太难了。

## Python

Python最大的缺点是速度和类型检查。经过比较和分析，两位创始人认为Python对他们而言已经足够快，而对性能有关键影响的部分都用C++写了；对于类型检查，他们最后编写了非常完善的单元测试，确保不会出现类型错误。既然除去了这2个缺点，他们就很乐意选择Python了。另外，通过过去5年的观察，他们确信Python将继续朝着对他们有利的方向发展。

Adam在回答中指出，Quora的员工目前对选择的这门编程语言还是十分满意的。虽然当初在选择时有一些倾向性，但是公司的所有早期员工对于转型到Python并没有怨言，尤其是之前的PHP程序员。最后他还提到了当时Python语言的几个好的发展趋势。

- Python 2.6发布后，Quora使用的大部分库都对该版本兼容，因此很快就迁移到了新版本Python
- Tornado Web开发框架正式开源，Quora则将实时更新网络服务迁移到了Tornado上
- PyPy发展迅速，最终应该可以正式用于生产，相信以后会大幅提高性能

回答的最后，Adam表示自己对Python语言和Python生态系统的未来充满了信心。

[查看Quora创始人的回答原文](https://www.quora.com/Why-did-Quora-choose-Python-for-its-development)

END

**欢迎大家扫描下方二维码关注我的公众号“编程派”，谢谢支持！**

<p style="text-align:center">
    <img src="http://codingpy.com/static/images/wechat-of-codingpy.jpg" alt="编程派的微信公众号二维码" style="width:215px;height:215px">
</p>