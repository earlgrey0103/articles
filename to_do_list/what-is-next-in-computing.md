# 计算的未来是什么？

> 本文首发于微信公众号“编程派”，转载请联系公众号获得授权。

计算行业（computing industry）的发展呈周期性，存在金融与产品两个周期，二者绝大程度上是相互独立的。近来，很多人对金融周期当前所处的阶段感到绝望。金融市场为众人所瞩目，总是发生出乎意料的、有时甚至是剧烈的波动。相比之下，产品周期获得的关注较少，尽管它才是驱动计算行业发展的动力。通过研究历史并推测未来，我们可以更好地理解和预测产品周期。

![每隔10-15年出现新的计算时代](http://ww1.sinaimg.cn/mw690/006faQNTgw1f185v22pmaj30d204pmyr.jpg)

技术产品周期产生于平台与应用之间的相辅相成（mutually reinforcing）的互动。新平台催生新应用，后者反过来提升新平台的价值，形成了正反馈循环。小规模、分枝型技术周期无时不刻不在发生，但是每隔一段时间——从历史上来看大约每10到15年——就会出现颠覆计算行业格局的重大周期。

![金融周期和产品周期绝大程度上是相互独立的](http://ww4.sinaimg.cn/mw690/006faQNTgw1f185vsarkwj30jt0b8my7.jpg)

个人计算机（PC）刺激创业者开发出了文本处理程序、表格处理程序以及许多其他桌面应用。互联网滋生出搜索引擎、电子商务、电子邮件、社交网络、SaaS商业应用以及许多其他网络服务。智能手机使得移动通讯、移动社交网络以及拼车等服务成为可能。如今，我们已经进入移动时代。未来很可能还会出现更多的移动创新。

每个产品时代都可以划分为两个阶段：1）酝酿期，即新平台首次推出，但是价格昂贵，功能不全面，而且/或者使用困难；2）成长期，即出现了一个解决这些问题的新产品，开启了几何式增长时期。

Apple II早在1977年就已推出（MITS Altair 8800更早两年面世），但是却是由1981年发布的IBM PC开启了个人电脑的成长期。

![每年的PC销量（单位：千）](http://ww1.sinaimg.cn/mw690/006faQNTgw1f185vuck7kj30c005umyp.jpg)

互联网的酝酿期是上世纪80年代及90年代早期，当时互联网很大程度上还只是学术界和政府使用的一个基于文本的工具。1993年，Mosaic网络浏览器的出现开启了它的成长期，一直持续至今。

![全球互联网用户的增长情况](http://ww2.sinaimg.cn/mw690/006faQNTgw1f185u6fn1lj30a004haan.jpg)

上世纪90年代就出现了功能机（feature phones），本世纪初出现了Sidekick和Blackberry等早期智能手机，但是智能手机的成长阶段真正开始于2007至2008年之间，这期间iPhone和Android先后发布。此后，智能手机的使用率暴涨：目前约有20亿人拥有智能手机。到2020年时，[全球每十个人中，就会有8个人使用智能手机](http://ben-evans.com/benedictevans/2014/10/28/presentation-mobile-is-eating-the-world)。

![全球每年的智能手机销售数据（单位：百万）](http://ww3.sinaimg.cn/mw690/006faQNTgw1f185ucp8hsj30c005mdgs.jpg)

假如10到15年的间隔是规律性的，下一个计算时代应该会在接下来几年中进入成长期。如果真是这样的话，我们现在应该已经处于其酝酿期了。目前，硬件业和软件业中显示出了一些重要趋势，可以让我们一窥下一个计算时代。在本文中，我将逐一说明这些趋势，并预测未来将会如何发展。

## 硬件：更小，更廉价，无处不在

在主机时代（mainframe era），只有大型机构才用得起计算机。后来，小型机构用上了小型机，普通家庭配备了个人电脑（PC），个人用起了智能手机。

![电脑变得越来越小](http://ww4.sinaimg.cn/mw690/006faQNTgw1f185v2iwquj30c008zdhl.jpg)

当前这个时代，处理器和传感器越变越小，越来越便宜，未来电脑的数量肯定会超过人类总人口。

原因有二。一是过去50年来半导体行业的稳步发展（摩尔定律）。二是克里斯·安德森（Chris Anderson）所说的“智能手机战争的和平红利”：智能手机的巨大成功导致对处理器和传感器的大量投资。如果你拆开一架现代无人机、虚拟头盔或者物联网设备，你会发现其中大部分是智能手机组件。

在现代半导体时代，人们的焦点已经从独立CPU，转变到被称之为系统芯片（systems-on-a-chip）的特殊芯片上。

![电脑的价格在不断降低](http://ww1.sinaimg.cn/mw690/006faQNTgw1f185vtr4nvj30c0086dgy.jpg)

系统芯片一般会将能耗低的ARM CPU，与专门用于图像处理、通信、电源管理及视频处理等功能的芯片捆绑一起。

![Raspberry Pi Zero: 1 GHz Linux computer for $5](http://ww1.sinaimg.cn/mw690/006faQNTgw1f185w0m1pdj307505gwej.jpg)

这种新架构使得基本计算系统的价格，从大概100美元降低到了约10美元。Raspberry Pi Zero是一台功率1 GHz的Linux电脑，花5美元就可以买到。你还可以以类似的价格，买到一个支持wifi、能运行Python的微控制器（microcontroller）。很快，这些芯片的价格会低至不到1美元。那是，我们可以在任何东西里嵌入一台电脑，而且不用担心成本控制问题。

与此同时，高端处理器的性能也得到了极大的提升。尤其重要的是GPU（图形处理器），其中最好的处理器是由Nvidia公司生产的。GPU不仅对传统的图像处理有用，还可以用于机器学习算法和虚拟现实设备（或增强现实设备）。Nvidia的产品路线图昭示了未来几年GPU的性能还将大大提升。

![谷歌的量子计算机](http://ww3.sinaimg.cn/mw690/006faQNTgw1f185v32tslj307y03yjrx.jpg)

另一项普适性技术是量子计算。这项技术目前仍主要存在于实验室中，但是如果成功商业化后，可以极大地提高生物学和人工智能等领域中许多算法的性能。

## 软件：人工智能的黄金时代

软件业如今正在发生许多令人兴奋的事情。分布式系统就是一个很好的例子。随着设备数量几何级增长，这两点变得越来越重要：1）多台机器并行执行任务；2）设备之间进行通信和配合。有意思的分布式系统技术包括：用于并行处理大数据问题的Hadoop和Spark，以及保障数据和资产安全性的Bitcoin/blockchain。

但是或许软件领域最振奋人心的突破来自人工智能（AI）。对AI的热捧及失望由来已久。阿兰·图灵曾预言到2000年时，机器能够成功模仿人类。但是，我们有充分的理由相信，现在AI或许将终于进入一个黄金时代。

> 机器学习是我们反思人类生活一切的一种核心、革命性方式。—— Google CEO，桑达尔·皮查伊（Sundar Pichai）

人工智能领域很多好消息都来自深度学习。这是一种机器学习技术，因2012年一项著名的谷歌项目而流行起来：谷歌使用一个大规模计算机集群学习如何在YouTube视频中识别猫。深度学习源自可以追溯至20世纪40年代的神经网络技术。由于多种因素，包括新的算法、廉价并行计算和大规模数据集的普遍，神经网络技术才得以起死回生。

![ImageNet挑战的错误率（红线为人类水平）](https://cdn-images-1.medium.com/max/600/1*P4BXse9pJYAUbasCEkQanA.png)

It’s tempting to dismiss deep learning as another Silicon Valley buzzword. The excitement, however, is supported by impressive theoretical and real-world results. For example, the error rates for the winners of the ImageNet challenge — a popular machine vision contest — were in the 20–30% range prior to the use of deep learning. Using deep learning, the accuracy of the winning algorithms has steadily improved, and in 2015 surpassed human performance.

Many of the papers, data sets, and software tools related to deep learning have been open sourced. This has had a democratizing effect, allowing individuals and small organizations to build powerful applications. WhatsApp was able to build a global messaging system that served 900M users with just 50 engineers, compared to the thousands of engineers that were needed for prior generations of messaging systems. This “WhatsApp effect” is now happening in AI. Software tools like Theano and TensorFlow, combined with cloud data centers for training, and inexpensive GPUs for deployment, allow small teams of engineers to build state-of-the-art AI systems.

For example, here a solo programmer working on a side project used TensorFlow to colorize black-and-white photos:

Left: black and white. Middle: automatically colorized. Right: true color. (Source)
And here a small startup created a real-time object classifier:

Teradeep real-time object classifier
Which of course is reminiscent of a famous scene from a sci-fi movie:

The Terminator (1984)
One of the first applications of deep learning released by a big tech company is the search function in Google Photos, which is shockingly smart.

User searches photos (w/o metadata) for “big ben”
We’ll soon see significant upgrades to the intelligence of all sorts of products, including: voice assistants, search engines, chat bots, 3D scanners, language translators, automobiles, drones, medical imaging systems, and much more.
“The business plans of the next 10,000 startups are easy to forecast: Take X and add AI. This is a big deal, and now it’s here.” — Kevin Kelly
Startups building AI products will need to stay laser focused on specific applications to compete against the big tech companies who have made AI a top priority. AI systems get better as more data is collected, which means it’s possible to create a virtuous flywheel of data network effects (more users → more data → better products → more users). The mapping startup Waze used data network effects to produce better maps than its vastly better capitalized competitors. Successful AI startups will follow a similar strategy.

## 软件 + 硬件：新型电脑

There are a variety of new computing platforms currently in the gestation phase that will soon get much better — and possibly enter the growth phase — as they incorporate recent advances in hardware and software. Although they are designed and packaged very differently, they share a common theme: they give us new and augmented abilities by embedding a smart virtualization layer on top of the world. Here is a brief overview of some of the new platforms:
Cars. Big tech companies like Google, Apple, Uber, and Tesla are investing significant resources in autonomous cars. Semi-autonomous cars like the Tesla Model S are already publicly available and will improve quickly. Full autonomy will take longer but is probably not more than 5 years away. There already exist fully autonomous cars that are almost as good as human drivers. However, for cultural and regulatory reasons, fully autonomous cars will likely need to be significantly better than human drivers before they are widely permitted.

Autonomous car mapping its environment
Expect to see a lot more investment in autonomous cars. In addition to the big tech companies, the big auto makers are starting to take autonomy very seriously. You’ll even see some interesting products made by startups. Deep learning software tools have gotten so good that a solo programmer was able to make a semi-autonomous car:

Homebrew self-driving car
Drones. Today’s consumer drones contain modern hardware (mostly smartphone components plus mechanical parts), but relatively simple software. In the near future, we’ll see drones that incorporate advanced computer vision and other AI to make them safer, easier to pilot, and more useful. Recreational videography will continue to be popular, but there will also be important commercial use cases. There are tens of millions of dangerous jobs that involve climbing buildings, towers, and other structures that can be performed much more safely and effectively using drones.

Fully autonomous drone flight
Internet of Things. The obvious use cases for IoT devices are energy savings, security, and convenience. Nest and Dropcam are popular examples of the first two categories. One of the most interesting products in the convenience category is Amazon’s Echo.

Three main uses cases for IoT
Most people think Echo is a gimmick until they try it and then they are surprised at how useful it is. It’s a great demo of how effective always-on voice can be as a user interface. It will be a while before we have bots with generalized intelligence that can carry on full conversations. But, as Echo shows, voice can succeed today in constrained contexts. Language understanding should improve quickly as recent breakthroughs in deep learning make their way into production devices.
IoT will also be adopted in business contexts. For example, devices with sensors and network connections are extremely useful for monitoring industrial equipment.
Wearables. Today’s wearable computers are constrained along multiple dimensions, including battery, communications, and processing. The ones that have succeeded have focused on narrow applications like fitness monitoring. As hardware components continue to improve, wearables will support rich applications the way smartphones do, unlocking a wide range of new applications. As with IoT, voice will probably be the main user interface.

Wearable, super intelligent AI earpiece in the movie “Her”

Virtual Reality. 2016 is an exciting year for VR: the launch of the Oculus Rift and HTC/Valve Vive (and, possibly, the Sony Playstation VR), means that comfortable and immersive VR systems will finally be publicly available. VR systems need to be really good to avoid the “uncanny valley” trap. Proper VR requires special screens (high resolution, high refresh rate, low persistence), powerful graphics cards, and the ability to track the precise position of the user (previously released VR systems could only track the rotation of the user’s head). This year, the public will for the first time get to experience what is known as “presence” — when your senses are sufficiently tricked that you feel fully transported into the virtual world.

Oculus Rift Toybox demo

VR headsets will continue to improve and get more affordable. Major areas of research will include: 1) new tools for creating rendered and/or filmed VR content, 2) machine vision for tracking and scanning directly from phones and headsets, and 3) distributed back-end systems for hosting large virtual environments.

3D world creation in room-scale VR

Augmented Reality. AR will likely arrive after VR because AR requires most of what VR requires plus additional new technologies. For example, AR requires advanced, low-latency machine vision in order to convincingly combine real and virtual objects in the same interactive scene.

Real and virtual combined (from The Kingsmen)

That said, AR is probably coming sooner than you think. This demo video was shot directly through Magic Leap’s AR device:

Magic Leap demo: real environment, virtual character

## 接下来是什么？

It is possible that the pattern of 10–15 year computing cycles has ended and mobile is the final era. It is also possible the next era won’t arrive for a while, or that only a subset of the new computing categories discussed above will end up being important.
I tend to think we are on the cusp of not one but multiple new eras. The “peace dividend of the smartphone war” created a Cambrian explosion of new devices, and developments in software, especially AI, will make those devices smart and useful. Many of the futuristic technologies discussed above exist today, and will be broadly accessible in the near future.
Observers have noted that many of these new devices are in their “awkward adolescence.” That is because they are in their gestation phase. Like PCs in the 70s, the internet in the 80s, and smartphones in the early 2000s, we are seeing pieces of a future that isn’t quite here. But the future is coming: markets go up and down, and excitement ebbs and flows, but computing technology marches steadily forward.

原文链接：[Chris Dixon@Medium](https://medium.com/@cdixon/what-s-next-in-computing-e54b870b80cc#.6qc10uowx)