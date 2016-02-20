# GWPY：发现引力波的机构使用的Python包

关键词：引力波数据分析, 引力波 LIGO, LIGO Python, GWPY引力波分析, Python教程, 数据可视化, 引力波探测, 什么是引力波

美国科学家11日宣布，他们去年9月首次探测到引力波。这一发现印证了物理学大师爱因斯坦100年前的预言。宣布这一发现的，是激光干涉引力波天文台（LIGO）的负责人。

这个机构诞生于上世纪90年代，进行引力波观测已经有近30年。那么观测到的引力波数据的量应该很大，科学家如何对这些数据进行分析？有没有用到Python编程语言？

**答案是肯定的**。笔者在Github上发现了一个专门用于分析引力波数据的Python包：[GWPY](https://github.com/gwpy/gwpy)。据维护者介绍，GWPY的代码来自LIGO和另一个名叫Virgo的机构，维护者将这两个机构科学家的Python代码整理，最终的产品就是GWPY这个用户友好的Python包。

在具体介绍GWPY之前，先给和笔者一样的小白简单科普一下引力波和LIGO的相关知识。

## 什么是引力波？

![This 3-D visualization shows the gravitational waves produced by two orbiting black holes. (Credit: NASA)](http://www.geekwire.com/wp-content/uploads/2016/02/160208-grav-1240x1240.jpg)

上图是两个黑洞所产生的引力波的3-D模拟图（NASA）。

首先，什么是引力波？在物理学上，引力波是爱因斯坦广义相对论所预言的一种以光速传播的时空波动，如同石头丢进水里产生的波纹一样，引力波被视为宇宙中的“时空涟漪”。通常引力波的产生非常困难，地球围绕太阳以每秒30千米的速度前进，发出的引力波功率仅为200瓦，还不如家用电饭煲功率大。宇宙中大质量天体的加速、碰撞和合并等事件才可以形成强大的引力波，但能产生这种较强引力波的波源距离地球都十分遥远，传播到地球时变得非常微弱。

下面分享两个优秀的视频，很好地解释了引力波及背后的原理。第一个来自LIGO，第二个则是比较通俗的漫画式讲解。

### LIGO科学家的解释：

[http://v.qq.com/boke/page/g/0/0/g0184mxwie0.html](http://v.qq.com/boke/page/g/0/0/g0184mxwie0.html)

### 漫画式通俗解释：

[http://v.qq.com/page/j/x/u/j0184qlilxu.html](http://v.qq.com/page/j/x/u/j0184qlilxu.html)

## LIGO是什么？

激光干涉引力波观测站（ Laser Interferometer Gravitational-Wave Observatory）LIGO是加州理工学院（Caltech）和麻省理工学院（MIT）的合作实验室，现在也有其他的大学参与。实验资金来源于美国国家科学基金会。LIGO是用来寻找宇宙中的引力波，从而可以验证黑洞的存在和检验广义相对论。

![90年代：LIGO计划](http://7te8bu.com1.z0.glb.clouddn.com/uploads/new/article/740_740/201602/56bd272380c1f.png)

LIGO主要有两个观测点，位于路易斯安那Livingston Parish的LIGO Livingston观测点，和华盛顿 Hanford的LIGO Hanford观测点。除此之外，在加州Passadena 的Caltech校园中还有LIGO 40m Prototype 。

### LIGO是如何探测引力波的？

[视频：LIGO是如何探测引力波的？](http://v.qq.com/boke/page/z/0/x/z0184li9kbx.html)

## GWPY：LIGO用它分析引力波数据？

![gwpy](https://camo.githubusercontent.com/6605948b31ce8bb027cf028b7ba917b636e8b568/68747470733a2f2f677770792e6769746875622e696f2f696d616765732f677770795f313230302e706e67)

接下来是本文的重头戏。我们一起来学习如何GWPY分析引力波数据。下面的介绍及示例均来自GWPY的[官方文档](https://gwpy.github.io/docs/v0.1/)。

### 安装

很简单，`pip install gwpy`就可以完成安装。

不过安装的过程可能会比较长，因为gwpy使用的依赖包比较多，包括numpy、 scipy、 cycler、matplotlib、astropy等。

### 面向对象编程

GWPY是一个面向对象编程的Python包，也就是说，数据对象是这个包的核心关注点。每一个数据对象都体现为一个类实例，包含了其属性和包含的数据。

如果想创建一个新的类实例，建议使用标准的构建器（constructor）。举个例子，我们可以使用一个数据数组，生成一个TimeSeries对象：

	>>> from gwpy.timeseries import TimeSeries
	>>> mydata = TimeSeries([1,2,3,4,5,6,7,8,9,10], sample_rate=1, epoch=0)

或者从在线数据服务器上下载：

	>>>
	>>> from gwpy.timeseries import TimeSeries
	>>> mydata = TimeSeries.fetch('H1:LDAS-STRAIN', 964656015, 964656615)

### 核心数据对象

据介绍，GWPY提供了4种核心数据对象，分别代表引力波探测器所产生的四种标准数据：

- TimeSeries（时间序列数据）
- Spectrum（光谱数据）
- Spectrogram（光谱图）
- DataQualityFlag

### 引力波数据可视化

我们知道，将引力波探测器收集的数据可视化，对于理解引力波的特性、研究引力波信号来说非常有帮助。`gwpy.plotter`模块中提供了一些plot类，可以直观地展示相应的数据类型。

GWPY的核心数据对象里，大部分都内置有一个`plot()`方法，可以让研究人员快速对某个数据集进行可视化展示。举个例子：

	>>> from gwpy.timeseries import TimeSeries
	>>> data = TimeSeries.fetch('H1:LDAS-STRAIN', 968654552, 968654562)
	>>> plot = data.plot()
	>>> plot.show()

![gwpy data plot](https://gwpy.github.io/docs/v0.1/_images/index-1.png)

## GWPY：利用公开的LIGO数据进行绘图

我们接下来利用LIGO公开的一些引力波时间序列数据进行绘图。我们可以直接在线加载这些数据。首先导入我们需要的模块：

	>>>
	>>> from urllib2 import urlopen
	>>> from numpy import asarray
	>>> from gwpy.timeseries import TimeSeries

然后，下载数据，保存为文本字符串：

	>>>
	>>> data = urlopen('http://www.ligo.org/science/GW100916/L-strain_hp30-968654552-10.txt').read()

现在，我们可以对文本进行解析，补充必要的元数据之后，就可以生成一个TimeSeries：

	>>>
	>>> ts = TimeSeries(asarray(data.splitlines(), dtype=float),
	>>>                 epoch=968654552, sample_rate=16384, unit='strain')

最后，我们就可以绘图了：

	>>>
	>>> plot = ts.plot()
	>>> plot.set_title('LIGO Livingston Observatory data for GW100916')
	>>> plot.set_ylabel('Gravitational-wave strain amplitude')
	>>> plot.show()

![LIGO Livingston Observatory data for GW100916](https://gwpy.github.io/docs/v0.1/_images/public.png)

**欢迎大家扫描下方二维码关注我的公众号“编程派”，谢谢支持！祝大家新春快乐，猴年大吉！**

<p style="text-align:center">
    <img src="http://codingpy.com/static/images/wechat-of-codingpy.jpg" alt="编程派的微信公众号二维码" style="width:215px;height:215px">
</p>