# 学习Python：做数据科学还是网站开发？

> 本文的英文原文地址是：[Python for Data Science vs Python for Web Development](http://www.dezyre.com/article/python-for-data-science-vs-python-for-web-development/177)，发布时间是10月29日。译者一开始在Python日报上看到推荐，初步看看了，觉得对于决定学习Python的方向有一定参考价值。不过，在翻译过程中，越来越觉得这其实就是一篇搞Python数据科学培训的公司写的软文，里面写的内容还是比较浅的，只适合像我这样的初学者了解大致情况。当然，文章提到了Python作为网络开发技能的市场需求并不是很高，这点感觉并不是没有根据。作为一篇软文，它成功地激起了我学习数据科学的兴趣，而原因嘛，自然就是**做数据科学工作的工资比一般开发工作，高很多**（按文章中信息图的数据，比一般岗位的年薪高5万美刀！！！）！
> 译者注：-- <cite>EarlGrey@codingpy</cite>

Python编程语言拥有诸多用于网络应用开发、图形用户界面、数据分析、数据可视化等工作的框架和特性。Python可能不是网络应用开发的理想选择，但是正被很多机构广泛用于评估大型数据集（dataset）、数据可视化、进行数据分析或制作原型。在数据科学领域，Python编程语言正不断获得用户的亲睐，而作为网络开发语言，Python显得有点过时了。本篇博文，就是要对这两种截然不同的Python使用方式，进行详细的对比，并且帮助大家明白一点：如果要利用Python做数据科学工作，并没有必要了解它用于网络开发的部分。

![python:web development vs data science](http://files.dezyre.com/images/blog/Python+for+Data+Science+vs.+Python+for+Web+Development/Python+for+Data+Science+vs+Web+Devlopment.png)

## 面向数据科学的Python

从顶级金融机构到最小的大数据创业公司，各行各业、各种规模的机构都在使用Python编程语言支撑业务运作。Python作为数据科学编程语言，不仅受顶级大数据公司欢迎，还有众多技术创业企业拥泵。它还位列2015推荐学习的前10种编程语言。

> 世上只有两种编程语言：一种是总是被人骂的，一种是从来没人用的。
> -- <cite>Bjarne Stroustrup</cite>

Python属于前一种，而且日益被用于数学计算、机器学习和多种数据科学应用。除了性能依赖性强和底层的业务外，它能够做其他任何事情。利用Python编程语言的最好选择，就是做数据分析和统计计算。学习面向网络开发的Python，需要程序员掌握像Django这样的多种网络框架协助建设网站；但是学习面向数据科学的Python，则要求数据科学家学习如何使用正则表达式和科学计算库，并掌握数据可视化的概念。由于目的、方向不同，那些不了解Python网络开发的程序员，能很轻松地走上利用Python编程语言做数据科学工作的道路。

Python是一个有着23年历史的强大动态编程语言，语言表现力很强。程序员编码完成后，不需要编译器即可运行程序。面向网络开发的Python支持多种编程范式，包括结构化编程（structured programming）、函数式编程（functional programming）和面向对象编程（object-oriented programming, OOP）。Python代码可以很容易地嵌入到许多拥有编程接口的网络应用中。但是，Python更是开发学术研究和科学计算程序的绝佳选择，这些程序要求运行快速、数学计算精确。

而面向网络编程的Python，则要求程序员学习多种网络开发框架，这个学习难度比较大，因为现有Python网络开发框架的文档不太容易理解。当然，不容否认的是，要想利用Python开发一个动态网站或网络应用，学习网络框架是必需的。

## Python网络开发框架

目前，Python社区已经有多种免费的网络应用开发框架，比如：

### Django

Django是帮助完美主义者按时完成工作的Python网络开发框架（译者注：原文是Django is the python web development framework for perfectionists with deadlines。这也是Django官网上对该框架的描述）。使用Django进行网络开发，最适合的场景是开发那些依靠数据库驱动，同时也具备类似自动化后台管理界面和模板系统等炫酷功能的应用。对于不需要太多功能的网络开发项目来说，Django可能是大材小用，主要是它的文件系统容易让人搞混，而且文件目录结构要求严格。使用Django进行Python网络开发的公司有纽约时报、Instagram和Pinterest（译者注：Pinterest联合创始人Paul Sciarra在Quora上的回答提到了使用Django，[Quora地址](https://www.quora.com/What-is-the-technology-stack-behind-Pinterest-1)）。

### Flask

Flask是针对初学者的框架，它简单，轻量，初学者很快就可以上手开发单页网络应用。这个框架并不支持验证，没有数据抽象层和其他许多框架所包括的组件。它不是一个全栈开发框架，也只用于小型网站的开发。（译者注：其实Pinterest也使用了Flask，只是没用在整站开发上，而是用来开发API，具体见[链接](https://www.quora.com/What-challenges-has-Pinterest-encountered-with-Flask)。）

### CherryPy

CherryPy框架强调要符合Python语言规范，做到程序员像进行面向对象编程一样开发网络应用。它还是诸如TurboGears和Web2py等流行全栈框架的基础模板引擎。

还有很多其他框架，包括Pyramid、Bottle和Pylons等，但是无论Python开发者使用哪一种框架，他/她都要花精力仔细地研究教程和文档。

### 为什么使用Python进行网络开发不现实？

Python作为网络开发语言，很可能是一个不太现实的选择：

- 面向网络开发的Python需要非标准化、昂贵的主机服务，尤其是程序员使用流行的Python网络框架开发网站时。由于利用PHP进行网络编程如此的便捷，大部分的用户没有兴趣在Python上投入太多的精力。
- 面向网络开发的Python与诸如PHP、Java或Ruby on Rails等语言不同，不是一个经常需要的技能。但是面向数据科学的Python却越来越受欢迎，而且由于它更多地被用于机器学习和其他数据科学程序，Python更是招聘数据科学家的公司所最看重的技能。
- 面向网络开发的Python已经经历了较长的发展，但是它的学习曲线并没有像PHP这样的网络编程语言那么高。


## 为什么将Python用于数据科学是最好的选择？

Python编程是驱动大数据、金融、统计和数字运算的核心科技，而**它的语法却像英语一样易懂**。近来，由于拥有多个针对机器学习、自然语言处理、数据视觉化、数据探索、数据分析和数据挖掘的插件，丰富的Python数据科学生态体系得到了较大的发展，甚至有将数据科学社区Python化的趋势。今天，面向数据科学的Python已经具备了清洗、转换和处理大数据的所有工具。对于数据分析师岗位来说，掌握Python也是最受欢迎的技能。一名具备Python编程能力的数据科学家，可以在纽约挣到平均年薪14万美元的工资。

## 为什么数据科学家喜欢使用Python语言？

![为什么数据科学家喜欢使用Python语言](http://files.dezyre.com/images/blog/Python+for+Data+Science+vs.+Python+for+Web+Development/Python+for+Data+Science.png)

数据科学家喜欢那些能够快速输出原型，帮助他们轻松地记录下自己的想法和模型的编程环境。他们喜欢通过分析巨量的数据集，得出结论，完成工作。而Python编程语言则是开发数据科学应用的多面手，因为它能帮助数据科学家，以最短最优的时间进行编码、调试、运行并获取结果，从而高效地完成工作。

一名技术娴熟的企业数据科学家的真正价值，在于利用多种数据视觉化手段，向公司的不同利益相关者有效地传递数据模式和预测。否则，数据科学工作就是一场零和游戏。Python以其优良特性，符合高强度科学计算的几乎所有方面要求，这使得它成为在不同的数据科学应用之间进行编程的绝佳选择，原因很简单：开发人员仅用一种语言就可以完成开发和分析工作。面向数据科学的Python将企业业务的不同部分连接在一起，提供了一个数据分享和处理的直接媒介。

- Python遵循统一的设计哲学，注重可用性、可读性，对于数据科学的学习曲线也较低。
- Python有很高的可扩展性，且与Matlab、Stata等语言相比，运行更加快速。
- 另外，Python生态系统中还在涌现出更多的数据视觉化库，以及炫酷的应用编程结构，目的是使用图形更好地展现数据分析的结果。Python社区有着诸如Sci-Kit learn、NumPy、Pandas、Statsmodel和SciPy等许多优秀的数据分析库。这些库的数量还在不断增长。

![面向数据科学的Python库](http://files.dezyre.com/images/blog/Python+for+Data+Science+vs.+Python+for+Web+Development/Python+Libraries+for+Data+Science.png)

### 面向数据科学中数字处理与科学计算的Python编程

数据分析与Python编程语言十分契合。如果你决定要通过Python语言学习数据科学，那么你应该考虑的下一个问题，就是Python库中有哪些是可以完成大部分的数据分析工作？接下来，我们给大家介绍全球的企业数据科学家都在使用的Python数据分析库。

**NumPy**

Numpy是使用Python开发的高级（high level）工具的基础。这个库不能用于高级数据分析，但是深入理解Numpy中面向数组的计算，可以帮助数据科学家有效使用Pandas库。

**SciPy**

SciPy主要用于科学计算，拥有许多不同的模块，可用于特殊函数、图像处理、插值法（interpolation）、线性代数、常微分方程（ODE）求解器以及其他多种用途。这个库还可以与NumPy数组一起使用，实现许多高效的数学运算。

**Pandas**

Pandas是用于数据再加工最好的库，因为它使得处理遗失的数据、自动数据对齐（data alignment）变得更加简单，它还支持处理从不同的数据源收集而来的索引数据。

**SciKit**
这个流行的机器学习库拥有多种回归、分类和聚类算法，还支持gradient boosting、向量机、朴素贝叶斯模型和逻辑回归。这个库还被设计成能够与NumPy和SciPy进行交互。

**Matplotlib**

这是一个二维绘图库，有着交互性很强的特性，生成的图标可以放大、推移，并且能够用于发行刊物印刷出版。而且，还支持多平台的交互环境。

Matplotlib、NumPy和SciPy是科学计算的基础。还有许多其他的Python库，诸如用于网络挖掘的Pattern，用于自然语言处理的NLTK，用于深度学习的Theano，用于爬取网络的Scrappy，IPython，Statsmodels，Mlpy等。对于初学Python数据科学的人，他们需要很好地掌握上面提到的优秀数据分析库。
