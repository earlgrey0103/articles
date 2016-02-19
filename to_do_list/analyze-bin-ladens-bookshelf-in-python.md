# 本·拉登的书架：Python文本分析拉登最常念叨什么？

关键词：Python文本分析, AlchemyAPI, 本·拉登的书架, 本·拉登的书信, Python PDF处理, Python教程, Python自动下载文件, 拉登最常念叨什么

> **本文首发于编程派的微信公众号，搜索“codingpy”关注编程吧。**

2015年，美国官方解密了一系列有关本·拉登的文件，其中最引人瞩目的，是美国国家情报总监办公室（The Office of the Director of National Intelligence）在其官网上列出的“本·拉登的书架”。

曝光的这份阅读清单涉及书籍和其他材料400余种。其中包含了已解密的书信等文档103份、公开发表的美国政府文件75份、英文书籍39册、恐怖组织发表的材料35份、与法国有关的材料19份、媒体文章33篇、其他宗教文档11份、智库或其他研究40种、软件或技术手册30份，及一些零散资料。

在本文中，我们将学习如何分析PDF文档，并且利用AlchemyAPI来进行实体抽取分析，看看本·拉登在这些信件中最常提到的10个实体是什么。

![本拉登的书架](http://ww1.sinaimg.cn/mw690/006faQNTgw1f13uqwr6tcj30mx0bvdhy.jpg)

## 什么是AlchemyAPI？

![AlchemyAPI logo](http://ww4.sinaimg.cn/mw690/006faQNTgw1f13tvh1wflj30m609dwfl.jpg)

AlchemyAPI是IBM旗下的一家公司，具有深度学习的自然语言处理和图片识别技术，可利用人工智能分析理解网页、文档、电子邮件、微博等形式的内容。它还将同Google 一样的神经网络分析技术应用其中。

AlchemyAPI目前共提供了12个文本分析功能：实体抽取（entitiy extraction），情感分析，关键字抓取，概念标识，关系提取，分类识别，作者提取，语言识别，文本提取，微格式分析，订阅内容识别，数据连接等。

接下来，我们开始进行准备工作。

> 本文中的代码大部分来自[automatingosint](http://automatingosint.com/blog/2015/05/osint-python-analyze-bin-ladins-bookshelf/)，我对源代码进行更新。目前的脚本支持Python 3。

## 安装依赖包

由于美国ODNI公开的本·拉登信件都是PDF格式的，因此我们首先必须要安装能够处理PDF文档的Python包。这里，我使用的是PyPDF2。我们通过`pip`包管理器进行安装：

	pip install pypdf2

另外，你肯定不想一封一封地手动103封书信吧？！省时省力的办法就是写个脚本把这些文档都爬取下来。由于要访问网页和解析网页，我们选择使用两个常用的第三方库：requests和BeautifulSoup 4：

	pip install requests beautifulsoup4

## 获取免费AlchemyAPI Key

AlchemyAPI是IBM旗下的一家公司，具有深度学习的自然语言处理和图片识别技术，可利用人工智能分析理解网页、文档、电子邮件、微博等形式的内容。它还将同Google 一样的神经网络分析技术应用其中。AlchemyAPI目前共提供了12个文本分析功能：实体抽取（entitiy extraction），情感分析，关键字抓取，概念标识，关系提取，分类识别，作者提取，语言识别，文本提取，微格式分析，订阅内容识别，数据连接等。

AlchemyAPI有一个免费的基础服务包，每天的事务处理上限为1000次。在本文中，我们将使用他们的实体抽取服务来执行文本分析。

获取免费AlchemyAPI Key非常简单，只需要[填写一个表单](http://www.alchemyapi.com/api/register.html)即可，输入自己的邮箱地址。

申请处理完成之后，你就可以在邮箱中看到发送给你的API Key了。

![AlchemyAPI Key申请邮件回复](http://ww1.sinaimg.cn/mw690/006faQNTgw1f13tgh8r7zj310m03eaay.jpg)

## 安装Alchemy Python SDK

获得API Key之后，我们可以通过AlchemyAPI提供的Python SDK和HTTP REST接口调用其提供的文本分析服务。在本文中，我们选择安装SDK的方式。

PyPI上之前有AlchemyAPI包，但是后来移除了下载包，因此我们不能使用pip来安装，只能通过Git克隆Python SDK的代码库或是直接下载代码库:

	git clone https://github.com/AlchemyAPI/alchemyapi_python.git

接下来，我们要把申请到的API Key与SDK关联起来。打开终端，进入SDK文件夹，然后按下面的示例执行alchemyapi.py文件：

	cd alchemyapi_python
	python alchemyapi.py YOUR_API_KEY # 将YOUR_API_KEY替换成你收到的Key

为确保SDK正常安装，可以按照提示运行example.py查看演示程序：

	python example.py

如果最后出现了下图的文字，就证明SDK安装正确，API Key也可以使用。

![AlchemyAPI安装正常](http://ww4.sinaimg.cn/mw690/006faQNTgw1f13telx4vvj30w00oyah8.jpg)

## 下载文档

然后就到了怎么自动将103份PDF文档下载到本地了。

我们可以写一个简单的Python脚本来完成这项工作，但是我选择把它封装在download_bld_documents这个函数里，因为我想把所有的代码都放在一个脚本里，这样大家就可以直接运行这个脚本，等待一段时间，就可以看到最后的结果了。

这个函数写的比较简单，但是已经能够满足我们的需求了。

	def download_bld_documents():
	    """Download Bin Laden's Declassified documents from ODNI."""
	    import os
	    import time
	    import requests    
	    from bs4 import BeautifulSoup	
	    
	    # 创建一个名为“pdfs”的文件夹，用于保存所有下载的PDF文档。
	    try:
	        os.mkdir("pdfs")
	    except:
	        pass

	    # 获取ODNI网站上有关本·拉登书架的网页，
	    # 将其交给Beautiful Soup，以进行HTML解析。
	    response = requests.get(
	        "http://www.dni.gov/index.php/resources/bin-laden-bookshelf?start=1")

	    if response.status_code == 200:

	        html = BeautifulSoup(response.content)

	    link_list = []
	    # 从网页中第54个超链接开始，我们遍历所有的文档链接，
	    # 仅保留那些我们所需要的链接：即含有“pdf”但不包含“Arabic”
	    # 字样的链接。我们将满足要求的链接保存到列表`link_list`中。

	    for i in html.findAll("a")[54:]:
	        if "pdf" in i['href'] and "Arabic" not in i.text:
	            link_list.append("http://www.odni.gov%s" % i['href'])
	    # 接下来，我们遍历列表中所有的元素，
	    # 从原链接中获取PDF的文件名，
	    #然后从ODNI网站下载相应的文档。

	    for i in link_list:
	        response = requests.get(i)
	        file_name = i.split("/")[::-1][0]
	        fd = open("pdfs/%s" % file_name, "wb")
	        fd.write(response.content)
	        fd.close()

	        time.sleep(1)

由于文件数量比较多，因此在最终执行脚本时，耗费在文件下载的时间可能会比较长。如果你从ODNI网站下载的速度非常慢，那么可以前往我的百度网盘下载，但是在最终执行时要对脚本做修改。只需要执行下文中的函数即可。

> **在微信号中，回复“laden”即可获得分享链接及提取码。**

## 处理文档

下面，我们就可以正式对下载的PDF文档进行分析了。我们将要利用Alchemy API提供的强大工具，对这些PDF文档进行实体抽取（entitiy extraction）分析。通过实体分析，我们可以了解本·拉登在这些信件和文件中，谈到最多的人、地方或东西是什么。

所以，我们要一一打开这些PDF文件，从文档中提取所有的文本，然后将其提交至Alchemy进行分析处理。在处理每一个文档时，我们可以得到其中的实体数据，最后将所有文档的分析数据结合在一起，就可以得到出现频率最高的实体了。

我们将这部分代码封装在process_documents函数中：

	def process_documents():
	    """Process downloaded documents using AlchemyAPI."""

	    # 导入所需要的模块，包括我们安装的PyPDF2和AlchemyAPI。
	    import PyPDF2
	    import glob
	    import time    
	    from collections import Counter    
	    from alchemyapi import AlchemyAPI

	    alchemyapi = AlchemyAPI() # 初始化AlchemyAPI。
	    file_list = glob.glob("pdfs/*.pdf") 
	    # 通过`glob`模块获取我们下载的所有PDF文件的文件名。
	    entities = {} 
	    # 我们要使用`entities`字典来保存每个PDF文档的分析结果。    # 下面的for循环将遍历所有的PDF文件
	    for pdf_file in file_list:

	        # read in the PDF
	        print("[*] Parsing %s" % pdf_file)

		# 初始化一个PyPDF2对象，用于保存从PDF文档中提取的文本数据
	        pdf_obj = PyPDF2.PdfFileReader(open(pdf_file, "rb"))

		# 创建一个空字符串，用于后续构建这个PDF的全部文本数据
	        full_text = ""

	        # 从每页中提取文本数据
	        for page in pdf_obj.pages:
	            full_text += page.extractText()
		# 接下来我们使用Alchemy API进行实体抽取
	        print("[*] Sending %d bytes to the Alchemy API" % len(full_text))
	        # 调用AlchemyAPI，并明确我们提交的是文本数据（第一个参数）
	        # 然后传入需要分析的文本，第三个参数代表禁用情感分析功能，
	        # 因为本文中我们只关注频率最��的实体。

	        response = alchemyapi.entities('text', full_text, {'sentiment': 0})

	        if response['status'] == 'OK':
	            # 遍历返回的全部实体数据。
	            # Alchemy返回的每个实体中，都包含有`count`数据，
	            # 我们要确保在`entities`字典中，将所有相同实体的count相加
	            for entity in response['entities']:
	                # add each entity to our master list
	                if entity['text'] in entities:
	                    entities[entity['text']] += int(entity['count'])
	                else:
	                    entities[entity['text']] = int(entity['count'])

	            print("[*] Retrieved %d entities from %s" %
	                  (len(entities), pdf_file))

	        else:
	            print("[!] Error receiving Alchemy response: %s" %
	                  response['statusInfo'])

	        time.sleep(1)

	    # 上面的循环执行结束，我们可以统计最常见的实体，
	    # 并把相关的结果打印出来了！
	    entity_counter = Counter(entities)

	    top_entities = entity_counter.most_common()

	    # 接下来就开始打印本·拉登提到次数最多的实体吧！
	    for top_entity in top_entities[0:10]:

	        # most_common returns a tuple (entity,count)
	        print("%s => %d" % (top_entity[0], top_entity[1]))


上面函数的最后，我们使用了Counter类来加载entities字典，并且很容易地就得出了最常见的实体。

## 快速执行脚本

最后执行脚本时，一定要注意：要把脚本放在alchemyapi_python这个文件夹里。这是因为AlchemyAPI SDK并没有在Python的PATH上。

为了让大家少复制粘贴，我已经把相关的操作写在一个bash脚本里。大家下载脚本后**修改API KEY**即可。

	curl https://raw.githubusercontent.com/bingjin/funscripts/master/laden/bld.sh --output bld.sh
	sh bld.sh

![拉登信件分析脚本运行中](http://ww3.sinaimg.cn/mw690/006faQNTgw1f13ts8u4f3j30w80oqh1v.jpg)

上图就是正在执行的脚本。想不想看看最终的分析结果？

我直接告诉你们就太没趣了，大家可以运行脚本自己看，等待的同时可以品尝一杯咖啡。当然，剧透也是有的：**伊斯兰教先知穆罕默德居然才排第七！**

你分析的结果是怎样的，留言告诉大家本·拉登提到次数最多的三个实体吧！

## 结语

本文中仅使用了AlchemyAPI的实体提取功能，其他诸如关键词分析、情感分析、图像分析等功能都没有涉及。大家可以在本文的基础上，进一步发挥自己的想象力，看看还能从本·拉登的书架中得到什么信息。

**欢迎大家扫描下方二维码关注我的公众号“编程派”，谢谢支持！**

<p style="text-align:center">
    <img src="http://codingpy.com/static/images/wechat-of-codingpy.jpg" alt="编程派的微信公众号二维码" style="width:215px;height:215px">
</p>
