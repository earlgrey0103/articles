# Scrapy下载妹子图

关键词：scrapy, 美女图片爬虫, 下载妹子图

URL：scrapy-01-meizitu


## Scrapy简介

scrapy 是一个 python 下面功能丰富、使用快捷方便的爬虫框架。用 scrapy 可以快速的开发一个简单的爬虫。


## 准备工作

我们使用 Python 2.7 进行开发，需要安装的库如下：

``pip install -U scrapy pillow``

安装 pillow 是因为我们下载图片时需要使用，而在安装 scrapy 时默认是不安装 pillow 的。

## 快速设置

1. 初始化项目

```
scrapy startproject mzt
cd mzt
scrapy genspider meizitu meizitu.com
```
     
2. 修改 meizitu.py


定义 scrapy.Item ，添加 image_urls 和 images ，为下载图片做准备。


```python
import os
import scrapy

class PItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    name = scrapy.Field()
```
修改 start_urls 为初始页面, 添加 parse 用于处理列表页， 添加 parse_item 处理项目页面。

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

3. 修改 settings.py

```python
DOWNLOAD_DELAY = 1 # 添加下载延迟配置
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1} # 添加图片下载 pipeline
IMAGES_STORE = '.' # 设置图片保存目录
```

4. 运行项目：

```
scrapy crawl meizitu
```

看，项目运行效果图。

这里的效果不是很理想，图片文件名被默认为图片 URL 的 SHA1 值，我们希望能够保存为比较有意义的名称，最好是按每期分文件夹存储。

## 重命名图片

如果想重命名保存文件的名称，我们需要重新定义自己的ImagePipeline。

```python
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

最终效果：

60 page / min



## 参考资料

http://toutiao.com/a6300929522393841921/
http://mazih.com/post/cibuwb7bu0000rfa2m169vzv9/

