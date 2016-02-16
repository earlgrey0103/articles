# LIGO的科学家们是如何使用Python语言的？

关键词：引力波 Python, LIGO引力波, 引力波数据分析, GWPY, LIGO-CBC, Python数据分析, 引力波发现, AMA问答互动, Python 科学家, 科学家如何使用Python

几天前，编程派介绍了一个[可以分析引力波数据的Python包——GWPY](http://codingpy.com/article/gwpy-ligo-analyze-gravitational-waves-data/)，这个包整理自发现引力波的科研机构LIGO。但是有的读者觉得我很能扯，居然能把引力波发现与Python联系在一起。但事实是，我说的一点也没错：**Python在这次引力波大发现的过程中起到了非常重要的作用**。

在公布了引力波大发现之后，LIGO在国外知名网站Reddit发起了一个[AMA（Ask Me Anything）问答互动活动](https://www.reddit.com/r/IAmA/comments/45g8qu/we_are_the_ligo_scientific_collaboration_and_we/czxnlux)。来自LIGO各地分支机构的科学家们在线回答网友的问题，其中就有网友问到了Python在科学界的作用和地位。LIGO科学家的回答充分支持了我上面的观点。

## LIGO Reddit Ask Me Anything

LIGO在Reddit上发起的这个问答活动是周六（2月13日）开始的，按介绍活动会持续两天。由于LIGO其实是一个类似合作联盟的机构，它的团队成员来自全球各地，因此Reddit上共有5个来自LIGO的账号回答问题，分别是：

- LIGO_WA：华盛顿州Hanford观测站的科学家
- LIGO_LA：路易斯安那州Livingston观测站的科学家
- EGO_VIRGO：在意大利研究VIRGO观测器的科学家
- LIGO_Instrumentation：负责建造、管理引力波监测设备的科学家
- LIGO_Astrophysics：负责对监测数据进行天体物理学解释和分析的科学家

有关Python问题的回答就来自最后两个账号，即负责管理监测设备和分析监测数据的科学家们。

## LIGO Instrumentation

![Python自动化管理引力波监测设备](http://ww2.sinaimg.cn/mw690/006faQNTgw1f0yziyiz3xj31bo0b4jwh.jpg)

据负责管理引力波监测设备的科学家介绍，他们使用Python语言对大部分监测设备进行**自动化管理**。为了确保这些设备处于最佳的敏感度，科学家要执行很多个控制循环（control loops），可是又不能同时启动。这些控制步骤必须要按照正确的步骤，一步一步进行，程序非常复杂，还要考虑反馈增益（feedback gains）等因素。因此，他们使用Python编写了一个软件来进行自动化处理。这仅仅是众多自动化操作中的一个。

![监听引力波的主要数据分析管道](http://ww1.sinaimg.cn/mw690/006faQNTgw1f0yziyuyh0j31ao07842d.jpg)

还有一个回答提到，负责监听引力波的主要数据分析管道（pipelines）之一，就是运行在Python环境上。

## LIGO Astrophysics

![Python用于分析引力波数据](http://ww4.sinaimg.cn/mw690/006faQNTgw1f0yzizrehij31au07yq5z.jpg)

LIGO负责数据分析的科学家认为，Python在科学界发挥着极其重要的作用。LIGO使用的许多分析工具都是用Python开发的，而且**这次引力波大发现**最终的统计显著性（final significance）就是用这些工具计算得出。

![Python用于分析引力波数据](http://ww4.sinaimg.cn/mw690/006faQNTgw1f0yzizrehij31au07yq5z.jpg)

LIGO介绍这次发现的论文中，几乎所有的图表都是用Python绘制的。其中，大家在媒体报道中看到的下面这幅图，也是使用Python绘制而成（具体来说是matplotlib库）。

![引力波大发现数据图](http://ww4.sinaimg.cn/mw690/006faQNTgw1f0yziy8am8j30b407djst.jpg)

可以说，Python已经成为LIGO科学家日常使用的主要编程语言。

## LIGO 都开发了哪些Python库？

除了之前介绍的[GWPY](http://codingpy.com/article/gwpy-ligo-analyze-gravitational-waves-data/)，LIGO还开发了下面的Python库。

- [LIGO-CBC](https://github.com/ligo-cbc)
- [LSCSOFT](https://github.com/lscsoft)
- 等等

另外，[LIGO已经在网站上公开了这次发现的相关数据](https://losc.ligo.org/events/GW150914/)，供其他科学家研究分析，并且提供了[详细的数据分析教程](https://losc.ligo.org/s/events/GW150914/GW150914_tutorial.html)。

**欢迎大家扫描下方二维码关注我的公众号“编程派”，谢谢支持！祝大家新春快乐，猴年大吉！**

<p style="text-align:center">
    <img src="http://codingpy.com/static/images/wechat-of-codingpy.jpg" alt="编程派的微信公众号二维码" style="width:215px;height:215px">
</p>