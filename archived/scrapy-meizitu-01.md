# 程序猿都会爬的妹子图

关键词：scrapy, 美女图片爬虫, 下载妹子图, 数据抓取框架, 妹子图爬虫

URL：scrapy-01-meizitu

Scrapy 是一个非常流行的 Python 数据抓取框架，用于抓取web站点并从页面中提取结构化的数据。它的用途广泛，可以用于数据挖掘、监测和自动化测试。

今天我们使用 Scrapy 来干一件程序猿喜闻乐见的事。

## 准备工作

我们使用 Python 2.7 进行开发，需要安装的库如下：

``pip install -U scrapy pillow``

使用 Scrapy 下载图片时默认需要使用 PIL 库，但是并没有自动安装。我们这里使用更新的 pillow 库替代。

## 快速开发

### 1. 初始化项目

```
scrapy startproject mzt
cd mzt
scrapy genspider meizitu meizitu.com
```

### 2. 修改 meizitu.py


定义 PItem 类，添加需要使用的 image_urls 、images 和 name 等属性，为下载图片做准备。

```python
import os
import scrapy

class PItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    name = scrapy.Field()
```

修改 start_urls 为网站的初始页面, 添加 parse 用于处理列表页， 添加 parse_item 处理项目页面。

```python

class MeizituSpider(scrapy.Spider):
    name = "meizitu"
    allowed_domains = ["meizitu.com"]
    start_urls = (
        'http://meizitu.com/a/list_1_1.html',
    )

    def parse(self, response):
        exp = u'//div[@id="wp_page_numbers"]//a[text()="下一页"]/@href'
        _next = response.xpath(exp).extract_first()
        next_page = os.path.join(os.path.dirname(response.url), _next)
        yield scrapy.FormRequest(next_page, callback=self.parse)
        for p in response.xpath('//li[@class="wp-item"]//a/@href').extract():
            yield scrapy.FormRequest(p, callback=self.parse_item)

    def parse_item(self, response):
        item = PItem()
        urls = response.xpath("//div[@id='picture']//img/@src").extract()
        name = response.xpath("//div[@id='picture']//img/@alt").extract()[0]
        item['image_urls'] = urls
        item['name'] = name.split(u'，')[0]
        return item
```

### 3. 修改 settings.py

```python
DOWNLOAD_DELAY = 1
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = '.'
```

### 4. 运行项目：

```
scrapy crawl meizitu
```

实际运行效果如下：

![Scrapy项目运行效果1](http://ww1.sinaimg.cn/mw690/006faQNTgw1f5i7j5kqp1j31kw0n9gyk.jpg)

这里的效果不是很理想，图片文件名被默认为图片 URL 的 SHA1 值。我们浏览时无法知道图片的大致内容。

我们希望能够保存为比较有意义的名称，最好是分为不同的文件夹存储。


## 重命名图片

如果想重命名保存文件的名称，我们需要重新定义自己的ImagePipeline。

```python
# pipelines.py
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem

class MztImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item})
            # 这里把item传过去，因为后面需要用item里面的书名和章节作为文件名

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def file_path(self, request, response=None, info=None):
    	item = request.meta['item']
        image_guid = request.url.split('/')[-1]
        filename = u'full/{0[name]}/{1}'.format(item, image_guid)
        return filename
```
然后修改 settings.py：

```python
ITEM_PIPELINES = {'mzt.pipelines.MztImagesPipeline': 1}
```

之后重新运行项目，效果图如下：

![Scrapy项目运行效果2](http://ww4.sinaimg.cn/mw690/006faQNTgw1f5i7j5xrmyj31kw0n9qew.jpg)

这个网站图片太多了，由于没有开启多个线程，导致整整爬了3个多小时，最终一共下载了12000多张图片：

![Scrapy项目最终运行结果](http://ww3.sinaimg.cn/mw690/006faQNTgw1f5i7j4vyvhj31kw0wo7ec.jpg)


如果你不想自己重新运行一遍爬虫，**可以考虑在微信公众号的后台回复“mzt”**，会有惊喜。

## 参考资料

http://toutiao.com/a6300929522393841921/
http://mazih.com/post/cibuwb7bu0000rfa2m169vzv9/

