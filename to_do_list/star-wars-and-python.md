# 星球大战与Python之间的那些事

阔别十年时光，全球瞩目的第七部星球大战电影《原力觉醒》将于2016年1月9日在国内上映。它将重新燃起那段神秘的太空岁月与具有原力的宇宙时光。但是，星球大战和Python编程语言又有什么关系呢？

## 星球大战背后的工业光魔

提起Python语言，很多人会想起系统运维、Web开发等工作。很少有人会知道Python也能够用于电影视觉特效的制作，其中就包括了《星球大战》某些电影特效的制作。

星战之父乔治·卢卡斯于1975年创建了工业光魔（全称：Industrial Light and Magic），从第一部《星球大战》起便参与了电影的特效制作。据[Python官网介绍](https://www.python.org/about/success/ilm/)，工业光魔从1996年起开始使用Python语言，取代了此前的Unix shell脚本。工业光魔做出这个决定的原因，在于Python的学习难度低，开发速度快。当时，Python还只是1.4版本。

电影特效行业竞争十分激烈，制作公司会不断地寻找更加优秀的编程语言，提高工作效率。工业光魔也是一直在评估Python语言的使用，但是近20年以来，还没有找到一个更好的替代品。

工业光魔的资深技术总监Tommy Burnette曾经这样评价道：

> Python在我们的生产流程中扮演了至关重要的作用。如果没有它，像《星球大战》第二部这样的大项目就很难完成。从集体渲染到批量处理再到影片合成，Python将所有步骤都紧密的粘合在了一起。

由此可见Python的强大。

## [Star Wars API](https://swapi.co/)

你知道《星球大战》系列大战中出现了多少个种族，多少种飞船吗？这些答案都可以在Star Wars API中找到。

据开发者介绍，Star Wars API是全球首个量化的、可供编程使用的星战数据集。开发者经过漫长的搜集和整理，汇总了星战系列电影中的人物、种族、星球、飞船等详细数据。目前，这个API中已经收录了《原力觉醒》中的新数据。API的作者还用Python开发了一个[helper库](https://github.com/phalt/swapi-python)。

我们来看看可以用这个库做些什么。

### 将所有星球按大小排列：

	import swapi
	for planet in swapi.get_all("planets").order_by("diameter"):
	    print(planet.name)

### 查看哪些人开过1艘以上的飞船：

	import swapi
	for people in swapi.get_all("people").iter():
	    if len(people.starships) > 1:
	        print(people.name)

### 检索Jar Jar Binks是否在电影中出现：

	import swapi
	pm = swapi.get_film(4)
	jj = swapi.get_person(36)
	for c in pm.get_characters().iter():
	    if c.name == jj.name:
	        print("Why George, why.")

## Python编写的Star Wars小游戏

最后，再与大家分享两个国外开发者用Python开发的星战相关游戏，希望大家喜欢。

### [starwars.py](http://www.codeskulptor.org/#demos-starwars.py)

### [Python-Wars-Solo](https://github.com/pydanny/Python-Wars-Solo)

