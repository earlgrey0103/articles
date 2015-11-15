# Python科学计算环境Anaconda 2.4版发布
<img src="https://www.continuum.io/sites/default/files/Anaconda_Logo_0702_0.png" alt="Anaconda new log" style="width:300px">

11月3日，Continuum对外发布了Anaconda 2.4版，其中包括Python 3.5安装器和Numpy 1.10。Continuum公司前不久为Anaconda产品设计了新的logo（见上图），这次新版本中也是将新的logo设计融入到了安装界面中。

## Anaconda 2.4的一些亮点
- 支持Python 3.5
- Numpy 1.10
- Linux版本支持OpenBLAS
- 包管理器conda获得明显速度提升
- 从IPython转换至Jupyter
- 改进了Windows版本的开始菜单
- 将全平台的Qt升级至4.8.7
- 更新了60多个包

## 如何更新Anaconda
已经安装了Anaconda的朋友，运行如下代码即可更新。

    :::python     
    conda update conda
    conda install anaconda=2.4 

- 全新安装Anaconda，请前往[下载页面](https://www.continuum.io/downloads)

## 为什么有Anaconda这样的环境
Python是一种强大的编程语言，其提供了很多用于科学计算的模块，常见的包括numpy、scipy和matplotlib。要利用Python进行科学计算，就需要一一安装所需的模块，而这些模块可能又依赖于其它的软件包或库，因而安装和使用起来相对麻烦。幸好有人专门在做这一类事情，将科学计算所需要的模块都编译好，然后打包以发行版的形式供用户使用，Anaconda就是其中一个常用的科学计算发行版。

## Anaconda的特点
- 包含了众多流行的科学、数学、工程、数据分析的Python包 http://docs.continuum.io/anaconda/pkgs.html
- 完全开源和免费
- 额外的加速、优化是收费的，但对于学术用途可以申请免费的License
- 全平台支持：Linux、Windows、Mac
- 支持Python 2.6、2.7、3.3、3.4、3.5，可自由切换

