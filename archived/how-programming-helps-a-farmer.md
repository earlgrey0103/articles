# 农民自制黑科技：无人驾驶拖拉机

关键词：自制黑科技, 黑科技, 无人驾驶拖拉机, MIT网络课程, MIT News, 远程控制, Python现实应用

上周，谷歌旗下的波士顿动力发布的新一代人形机器人Atlas。看到Atlas倒地后又站起来的样子，相信很多人已经被惊到了。谷歌到底还有多少黑科技？！

![Atlas摔倒后站起来](http://ww4.sinaimg.cn/mw690/006faQNTgw1f1e348bm70g30dc07bx6p.gif)

说到黑科技，不只是谷歌这样的科技巨头才有，普通人也是可以完全实现的。没错，而且还是一个农民！

这个农民名叫Matt Reimer，在加拿大有一个自家的农场。平常他都是日出而作，日落也接着作。O(∩_∩)O~不过，和大多数美国商人一样，这位农场主也一直在致力于提高自家农场的工作效率、产量和利润率。最近这几年，他一直在研究如何使用远程控制技术，来加快收割速度。

![发明无人驾驶拖拉机的农民](http://ww4.sinaimg.cn/mw690/006faQNTgw1f1e34izyeoj30hr0buq66.jpg)

他的想法是，是不是能够控制拖拉机的车轮，让它能在没有人操作的情况下，就到达指定的地点。

起初，因为没有相关的背景知识，他根本不知道该怎么着手实现。只能是依靠着谷歌搜索大法，尝试过[一个开源的硬件平台](http://diydrones.com/profiles/blogs/reimer-robotics-autonomous-tractor)，捣鼓过某个无人机自动导航程序，但是很明显都是无疾而终。问题就在于，他根本就不具备实现这套系统的知识。

> 编者注：这个开源硬件平台叫[DIY Drones](http://diydrones.com/)。有类似爱好的朋友可以关注。

还好，Matt有一个从MIT毕业的兄弟，给他指了一条明路。那就是参加MIT的网络公开课，学习编程知识，更好地理解远程控制软件背后的原因，以及如何将拖拉机上的硬件与联合收割机集成在一起。

Matt报名参加的网络公开课小编之前也介绍过，就是MIT机电学院经典的计算机入门课程6.001x（计算机科学及编程导论）。目前这门课的授课语言就是Python！

学完这门课程后，这个原来零编程基础的农民，居然技能直线飙升，成功开发出了一个远程控制拖拉机的app。使用者只需要按一个按钮，拖拉机就会靠近联合收割机，开到螺旋钻之下，实时装载从收割机上卸载下来的谷物。

什么？无图无真相？！好吧，给你上图，不给你上视频。请注意一分半处。

<div id="mod_tenvideo_flash_player_1456569011851" class="tenvideo_player"><embed wmode="window" flashvars="vid=s0186ytc2v4&amp;tpid=3&amp;showend=1&amp;showcfg=1&amp;searchbar=1&amp;shownext=1&amp;list=2&amp;autoplay=1&amp;ptag=%7Cuc.manage.li.title&amp;outhost=http%3A%2F%2Fv.qq.com%2Fpage%2Fs%2Fv%2F4%2Fs0186ytc2v4.html&amp;refer=http%3A%2F%2Fv.qq.com%2Fu%2Fvideos%2F&amp;openbc=0&amp;fakefull=1&amp;title=%20%E5%86%9C%E6%B0%91%E8%87%AA%E5%88%B6%E9%BB%91%E7%A7%91%E6%8A%80%EF%BC%9A%E6%97%A0%E4%BA%BA%E9%A9%BE%E9%A9%B6%E6%8B%96%E6%8B%89%E6%9C%BA" src="http://imgcache.qq.com/tencentvideo_v1/player/TencentPlayer.swf?max_age=86400&amp;v=20140714" quality="high" name="tenvideo_flash_player_1456569011851" id="tenvideo_flash_player_1456569011851" bgcolor="#000000" width="650px" height="472px" align="middle" allowscriptaccess="always" allowfullscreen="true" type="application/x-shockwave-flash" pluginspage="http://get.adobe.com/cn/flashplayer/"></div>

在收割的时候，无人驾驶拖拉机没有出一点问题，从收割机上成功装载谷物500多次，为Matt节省了预计5000美元。你可能会想，如果有了无人驾驶拖拉机后，原来的驾驶员是不是就得失业啦？当然不会啦。原来的驾驶员终于摆脱了无聊的工作，因为他之前的工作就是连续几个小时直线开拖拉机，你说是多无聊！现在，他反而能去负责其他更有趣、更高生产力的工作。

![无人驾驶拖拉机在工作](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1e34jd1paj30h809pmza.jpg)

这么好的成绩让其他农民着实眼红，很多人都表示对他开发的技术非常感兴趣。很快，Matt就要帮周围其他农场上马这套系统啦，而且还有国际化的计划哦！虽然软件是免费提供的，但是Matt会收取一定的硬件集成费用，因为这毕竟是一个十分复杂的工作，需要处理很多问题。

> 链接：Matt开源了自己的软件，[戳这个地址](https://github.com/mattdreimer/AutonomousGrainCart)。从说明来看，他使用了Pygame库和DroneKit库。此外，无人驾驶拖拉机还具备GPS跟踪功能，因为使用一个名为GPSd软件工具。

据小编了解，目前Matt已经开了一家名为Reimer Robotics的公司，主攻拖拉机自动化业务。下面是今年2月份他公司的第一个宣传视频。看着这全自动的拖拉机，小编只想竖起两个大拇指！

<div id="mod_tenvideo_flash_player_1456570914707" class="tenvideo_player"><embed wmode="window" flashvars="vid=u0186ddfnoz&amp;tpid=3&amp;showend=1&amp;showcfg=1&amp;searchbar=1&amp;shownext=1&amp;list=2&amp;autoplay=1&amp;ptag=%7Cuc.manage.li.title&amp;outhost=http%3A%2F%2Fv.qq.com%2Fpage%2Fu%2Fo%2Fz%2Fu0186ddfnoz.html&amp;refer=http%3A%2F%2Fv.qq.com%2Fu%2Fvideos%2F&amp;openbc=0&amp;fakefull=1&amp;title=%20%E5%86%9C%E6%B0%91%E8%87%AA%E5%88%B6%E9%BB%91%E7%A7%91%E6%8A%80%EF%BC%9A%E6%97%A0%E4%BA%BA%E9%A9%BE%E9%A9%B6%E6%8B%96%E6%8B%89%E6%9C%BA%E5%B7%A5%E4%BD%9C%E5%AE%A3%E4%BC%A0%E8%A7%86%E9%A2%91" src="http://imgcache.qq.com/tencentvideo_v1/player/TencentPlayer.swf?max_age=86400&amp;v=20140714" quality="high" name="tenvideo_flash_player_1456570914707" id="tenvideo_flash_player_1456570914707" bgcolor="#000000" width="650px" height="472px" align="middle" allowscriptaccess="always" allowfullscreen="true" type="application/x-shockwave-flash" pluginspage="http://get.adobe.com/cn/flashplayer/"></div>

虽然Matt成功提高了农场的生产力，而且还有了自己的公司，他始终觉得自己还有很多需要学习，所以会继续坚持学习MIT的网络课程。他很感谢MIT和它的公开课，没有它们，他肯定没法开发出这套系统。

他说，他想为这套无人驾驶拖拉机系统开发更多的功能。为了做好准备，他打算参加MIT的下一个课程，即6.002x。没错，MIT的6.00系列课程总共两部分！

对于6.001x这个导论课程，小编之前就在公众号分享过相关离线视频，希望学习的朋友除了在Edx平台注册学习外，还可以考虑下载离线视频，自己掌握节奏一步一步学习。视频提取暗号可以点击公众号菜单“优质资源” —> “视频教程”查看。（一般人我不告诉他O(∩_∩)O~）

而这6.002x课程的视频，小编也不藏着掖着，明天也会分享给大家。

更多有关编程和Python语言的学习资源和视频，请关注我们，不时会有惊喜放送。

----

资料来源：MIT News、Github、Youtube
