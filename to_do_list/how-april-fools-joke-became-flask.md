# 这可能是开发者社区最成功的愚人节笑话

关键词：Flask是怎么来的, Python微框架, Python愚人节笑话, 开发者愚人节笑话, Flask开发框架

愚人节笑话很少有成真的，毕竟那只是一时娱乐而已。但同样的话，对于开发者社区来说或许有例外。

据[Python官方维基](https://wiki.python.org/moin/AprilFools)介绍，Python社区中有着优良的愚人节传统，其中一个特别明显的例子就是[PEP 0401 -- BDFL Retirement](https://www.python.org/dev/peps/pep-0401/)，说的就是Python发明者Guido van Rossum决定让出终生仁慈独裁者(BDFL)的位置。

当然，上面这个愚人节笑话并不是我们要说的例外。本文的主角是Python Web开发微框架Flask。没错！Flask就是诞生于于作者Armin Ronacher六年前的一个愚人节笑话。

目前，Flask在Github网站上已经获得近2万个Star，已经跻身主流Python Web开发框架之列，我认为或许可以说是开发者社区最成功的愚人节笑话。

**对于自己有开源项目的开发者来说，本文或许也能为你提供一些项目推广方面的启示。**

## Denied：Flask的“前身”

据[Armin在博客中的介绍](http://lucumr.pocoo.org/2010/4/3/april-1st-post-mortem/)，当时他注意到微框架开始流行，出现了很多类似web.py（Python）和camping（Ruby）的微框架。这些框架都没有外部的依赖包，而且只有一个文件，似乎特别受大家欢迎。所以他决定自己也开发一个这样的框架，娱乐一下。

因为目的只是作为愚人节笑话，所以他只是利用现有的技术，将Werkzeug、simplejson和Jinja2打包进了一个文件，并添加了一些胶水代码。最终的产物就是一个名叫Denied的微框架。

![Flask的前身Denied，愚人节笑话](http://ww2.sinaimg.cn/mw690/006faQNTgw1f2gy7ofvrmj30rh0i278f.jpg)

为了让这个笑话更加可信、看上去更真实，他请人录制了一个视频，上线了一个网站，还找了几位知名Python开发者为这个框架背书。愚人节当天，Armin通过Twitter发布了Denied。

![Armin Ronacher关于Denied的推文](http://ww4.sinaimg.cn/mw690/006faQNTgw1f2gy7oulw8j30gd06sabr.jpg)

开发者社区对此的反应出乎意料。Armin在4月3日总结此事时提到，视频三天内被下载了1万次，网站点击量超过5万。而且转推数量远远超过之前自己的纪录。

![Denied在发布时的网站界面](http://ww2.sinaimg.cn/mw690/006faQNTgw1f2gypgqnwej30ml0keadj.jpg)

可惜，我没有找到当时录制的那个视频。

## Denied的成功有什么启示？

据Armin Ronacher在2011年的PyCon的分享，他从那次愚人节笑话中学到了以下几点：

- 没人有时间去充分测试这个框架并阅读代码
- 营销胜过质量
- 功能并不重要
- 不一定要是新东西

当然，这并不是要推荐你不去测试代码；市场营销和高质量代码也并不冲突。

另外，在项目网站上提供一些小块代码段特别有作用。作者此前的Werkzeug提供的示例非常复杂，Jinja2甚至没有相关代码示例，必须要看文档才能了解大致的情况。

宣传项目时要大胆。很少有人会马上去检验你的说法。

## Flask诞生

开发者们对这个项目的极大兴趣，促使Armin最终决定重新造轮子（reinventing the wheel），2010年4月6日在Github上发布了Flask。

![Flask项目的第一次提交](http://ww3.sinaimg.cn/mw690/006faQNTgw1f2gy7nznm3j30rf07g40d.jpg)

他后来解释了自己开发Flask的两大原因：

- 灵活性更高，应用可能要求一些现有框架没有的东西
- 可以自己掌握全局，快速解决遇到的问题

最终的框架使用起来非常简单。用Flask开发的“Hello World”应用可能是下面这样的：

	from flask import Flask

	app = Flask(__name__)

	@app.route('/')
	def index():
		return 'Hello World!'

	if __name__ == '__main__':
		app.run()


使用如此简单，那么Flask今天的成功就不难解释了。

## 参考资料

- [http://lucumr.pocoo.org/2010/4/3/april-1st-post-mortem/](http://lucumr.pocoo.org/2010/4/3/april-1st-post-mortem/)
- [http://lucumr.pocoo.org/2010/6/14/opening-the-flask/](http://lucumr.pocoo.org/2010/6/14/opening-the-flask/)
- [http://mitsuhiko.pocoo.org/flask-pycon-2011.pdf](http://mitsuhiko.pocoo.org/flask-pycon-2011.pdf)
- [https://us.pycon.org/2011/blog/2011/02/10/pycon-2011-interview-armin-ronacher-opening-flask/](https://us.pycon.org/2011/blog/2011/02/10/pycon-2011-interview-armin-ronacher-opening-flask/)