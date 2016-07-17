# 《Think Python 2e》中译版电子书分享

关键词：《Think Python 2e》中译版, 《Think Python 2e》电子书, think python pdf, think python epub, python学习教材

URL：think-python-2e-chinese-ebooks

6月19日，我发布了[《Think Python 2e》中译版的最后一章](http://mp.weixin.qq.com/s?__biz=MzAwNDc0MTUxMw==&mid=2649639096&idx=1&sn=66898d07498b1275d735e3e66eef3c61#rd)，之后断断续续在花时间折腾生成PDF和EPUB等格式电子书的问题。这两天总算是取得了一个还比较满意的效果，因此想把我目前生成的一些电子书分享给大家。

我主要生成了两种格式：PDF和EPUB，然后使用Calibre将EPUB再转换为MOBI和AZW3格式，应该可以满足大部分人的电子书阅读需求。

EPUB版本的效果还不错，我已经删除了不必要的导航和尾部版权信息。大家也可以自行生成epub版本，只要克隆[ThinkPython2-CN](https://github.com/bingjin/ThinkPython2-CN.git)，安装好sphinx库，然后运行``make epub``即可。

PDF版本是使用latex格式中转转换的，最终的效果并不非常理想，但也还算不错了。网友@SeikaScarlet目前正在制作精校版的PDF，完成之后会尽快分享给大家。他花了很多时间和精力来整理tex版本，非常辛苦，在此特别感谢SeikaScarlet的贡献！

如果你想自己试着生成PDF，可以先安装texlive-full（苹果系统装的是MacTex），然后``cd``到项目目录下，依次运行以下命令：

```
make latex
cd build/latex
xelatex *.tex
```

这中间可能会碰到问题，记得多谷歌！

最后，还要感谢以下网友对本书中译版的贡献：

1. @ipyher
2. @theJian
3. @lroolle
4. @xpgeng
5. @obserthinker
6. @SeikaScarlet
7. @cxyfreedom

大家在公众号回复“pybook03”即可获得电子版下载链接，希望能够帮助到大家。