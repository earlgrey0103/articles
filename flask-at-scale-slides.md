# Flask也能用来开发大规模网站？

关键词：大规模化Flask, Python大规模网站, flask网站开发, pycon 2016课程, miguel grinberg, flask web开发, web开发最佳实践

URL：flask-at-scale-slides

Flask对自己的定位是微框架，很多人据此认为Flask只适合搭建小型站点，无法支撑大规模在线网站。实际上，这是错误的观点。随着网站的成长，Flask也可以处理大规模百万级别的用户。本文将为你分享[《Flask Web开发》一书](http://codingpy.com/article/flask-web-development-book-pdf/)作者[Miguel Grinberg](http://blog.miguelgrinberg.com/post/flask-at-scale-tutorial-at-pycon-2016-in-portland)在PyCon 2016大会上提出的解决方案。

他在PyCon上的课程名叫“Flask at scale”（简译：大规模化Flask），针对的目标学员是中级和高级Flask开发者，时长3个多小时，主要教授的是如何提升Flask应用规模（包括应用大小和负载）的最佳实践。据他本人承认，这是他这么多次在PyCon大会上教授的最为高阶、最为复杂的课程。

主要内容包括：

- 如何组织大型应用
- 使用Blueprints组织应用
- 利用装饰器简化应用代码
- 异步请求
- 使用Celery工作队列
- 使用多进程、多主机和负载均衡服务器
- 使用协程框架
- 使用WebSocket进行服务器推送，降低延迟
- 等等

下面是课程PPT的重点部分：


如需下载完整PPT(或课程视频，无字幕），可以关注“编程派”微信公众号，并回复**“flask01”**获取分享链接（**获取视频分享链接请回复“pyvideo03”**）。

另外在此做一个小尝试，如果你想看中文版的PPT，那么可以选择打赏我。如果最终总打赏超过100或50人（需要的人少我就不用浪费时间了），我会在两天后向所有打赏者发送中文版PPT的分享链接。