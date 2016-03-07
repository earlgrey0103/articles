# Python文本分析：2016年政府工作报告的十大关键词是什么？

昨天看到中国网一篇名为[《全球媒体梳理十大关键词 解读中国政府工作报告》](http://news.163.com/16/0306/13/BHFS3VF200014JB6.html)的新闻，文中有这么一段话：

> 英国《金融时报》3月4日报道指出，比较工作报告中高频词的变化，可以发现“大力”、“加快”等高频报告用语，在历年工作报告里出现的次数逐渐降低，而“创新”、“增长”等词出现频率则有微幅增加。

## 国内媒体梳理的高频词

下面是[法制日报公布的十大高频词](http://news.sohu.com/20160305/n439473591.shtml)。

| 高频词       | 词频           | 1978年以来政府工作报告中的提及总数  |
| ------------- |:-------------:| -----:|
| 发展|	151	|	4828 |
| 经济 |	90	|	4449 |
|改革|	74	|	2758|
|建设	|71	|	3274|
|社会|	66	|	3402|
|推进	|61	|	1096|
|创新	|61	|	414|
|政策	|52	|	1231|
|企业|	48	|	2304|
|加强|	41	|	2238|

下面是[新华网数据新闻部统计的高频词汇](http://www.mnw.cn/news/china/1118242.html)。

![新网话数据新闻部的统计](http://upload.mnw.cn/2016/0306/1457227986426.jpg)

我们来看一看，利用Boson NLP得出的结果与上面媒体的统计有没有出入。我们会利用到Boson的关键词提取接口，这个接口计算的是每个关键词的权重，不是词频。但是关键词的排序还有比较价值的。

----

## 准备工作

### 注册波森NLP，获取API Key

http://bosonnlp.com/account/register

### 安装相关Python包

	pip requests beautifulsoup bosonnlp

### 导入所需的库

	import requests
	from bs4 import BeautifulSoup
	from bosonnlp import BosonNLP

## 文本提取

	def extract_text(url):
	    """Extract html content."""
	    page_source = requests.get(url).content
	    bs_source = BeautifulSoup(page_source)
	    report_text = bs_source.find_all('p')

	    text = ''

	    for p in report_text:
	        text += p.get_text()
	        text += '\n'

	    text = text.encode('utf-8').decode('utf-8')

	    return text

## 关键词提取

关键词作为一个对文本常用的概括，可以被应用于关键词云计算等应用上。BosonNLP 的关键词提取引擎可以将文本自动进行关键词分析，给出每个词语相应的权重。

玻森的关键词提取技术综合考虑词语在文本中的频率，和词语在千万级背景数据中的频率，选择出最具有代表性的关键词并给出相应权重。

	def extract_keywords(text, top_num=10):
	    """Extract Keywords."""
	    # 注意：在测试时请更换为您的 API token
	    nlp = BosonNLP('')
	    result = nlp.extract_keywords(text, top_k=top_num)

	    result_dict = {k: v for (v, k) in result}

	    return result_dict

## 计算权重变化

	def cal_change(keywords1, keywords2):
	    """Calculate keywords weight change percentage between 2015 and 2016."""
	    template1 = """2016年工作报告关键词 '%s' 的权重为%f，比去年同比上升了百分之%f。"""
	    template2 = """2016年工作报告关键词 '%s' 的权重为%f，比去年同比下降了百分之%f。"""

	    print("本次脚本执行过程共分析了出现次数前%d的关键词" % len(keywords1))

	    for k in keywords1:
	        if k in keywords2:
	            v1 = keywords1[k]
	            v2 = keywords2[k]
	            change = (v1 - v2) / v2 * 100
	            # 同比增长速度=（本期发展水平-去年同期水平）/去年同期水平×100%。
	            if change > 0:
	                print(template1 % (k, v1, change))
	            else:
	                print(template2 % (k, v1, -change))
	        else:
	            print("关键词 '%s' 不是2015年工作报告的十大关键词，它在2016年工作报告中的权重是%f" % (k, keywords1[k]))

## 执行脚本

	def main():
	    """Main function."""
	    # 2016年和2015年工作报告，这两个网页中报告的p元素都是报告内容
	    url_2016 = 'http://www.gov.cn/guowuyuan/2016-03/05/content_5049372.htm'
	    url_2015 = 'http://www.guancha.cn/politics/2015_03_17_312511_s.shtml'

	    text_2016 = extract_text(url_2016)
	    text_2015 = extract_text(url_2015)

	    keywords1 = extract_keywords(text_2016)
	    keywords2 = extract_keywords(text_2015)

	    cal_change(keywords1, keywords2)
