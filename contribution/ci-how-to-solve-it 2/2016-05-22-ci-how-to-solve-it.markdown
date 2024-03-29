# 解决问题的智慧：望、闻、问、切

关键词：解决问题, 望闻问切, 头脑风暴, 鱼骨图, 五个为什么分析法, 程序优化

URL：the-process-of-solving-problems

> 本文为编程派的朋友投稿，作者为赵喧典。

本文是对一节“职慧”课堂的记录与思考。那堂课的主题是**解决问题**，提出了解决问题的过程可以概括为四个字: **望**，**闻**，**问**，**切**。本文也将顺着这个思路展开。

### 望

所谓**望**，即**定义问题**。

在定义问题之前，其实有必要先对**"问题"**下一个定义。什么是问题? 在英语里，**question**和**problem**都可以表示问题。但明显，此处所谓的问题是problem，而非question。question更偏向于疑惑，相应地，与之搭配的动词是**answer**，即解答；而problem的定义是——**现状**与**期望**的**差距**——相应地，与之搭配的动词是**solve**，即解决。

知道了**问题**的概念之后，再来定义问题，思路就相对清晰了。既然问题是"差距"，那么**定义问题**就是将这差距给描述出来。一种好的方法是，采用**量化**的思想，即为现状和期望都设一个恰当的数值，中间的差值就是问题所在。

举个简单的例子。一开始我们定义的问题可能是这样的：`这个程序跑得太~慢了，我希望它能跑得更快`。用**量化差距**的方法来修改问题定义，可以是这样：`这个程序执行一次要200ms，我希望它能在100ms以内跑完`。与模糊的**快**和**慢**相比，用时间间隔来刻画现状与期望，一眼就能看出问题所在。

一个更具有普适性的例子是： `我每天都睡太迟了，今天要早点睡 -(量化)-> 我每天都凌晨1点才睡着，今天要11点就睡。`

此外，有必要指出**选项不是问题**，即类似**这个功能是用for循环呢，还是用递归呢**(晚饭是吃面呢，还是吃饭呢)，是一个选项，而非问题。你可以选择用for循环，或者叫递归，全凭心情(当然，考虑到代码实现的难易，可读性和程序效率，你会有所取舍的)。但明显，这个“问题”本身并不涉及现状与期望，也就无从谈差距了。

### 闻

所谓**闻**，即**分析问题，找出原因**。

针对"闻"，老师介绍了2个工具——`鱼骨图`和`五个为什么`——一个用于列出所有原因，一个用于归纳主要原因。

先看看**鱼骨图**，它的大致形状如下所示： 

![鱼骨图](http://ww3.sinaimg.cn/mw690/006faQNTgw1f4k4nenlejj30pc0cfacb.jpg)

鱼头指向当前现状，"脊椎"两侧的"大鱼刺"代表大方面的原因，"大鱼刺"上的各"小鱼刺"则表示更细的原因。

可以看出，鱼骨图可以非常清晰地显示出导致当前现状的各方面原因。这也是使用鱼骨图的关键所在——尽可能列出所有原因。

而**五个为什么**，以一种层层深入地提问的方式，找出根因所在。来看一个具体例子吧(一下子很难想到编程相关的例子，以下摘自[维基百科](https://zh。wikipedia。org/wiki/%E4%BA%94%E4%B8%AA%E4%B8%BA%E4%BB%80%E4%B9%88)，有删改):

- 情景: 汽车无法启动了。
 1. Q: 为什么汽车无法启动?\\
 A: 因为电池电量耗尽了。
 2. Q: 为什么电池电量会耗尽?\\
 A: 因为交流发电机不能正常工作。
 3. Q: 为什么发电机不能正常工作?\\
 A: 因为交流发电机的皮带断裂了。
 4. Q: 为什么皮带会断裂?\\
 A: 因为交流发电机皮带远远超出了其使用寿命，从未更换过。
 5. Q: 为什么超出了使用寿命，却从不更换?\\
 A: 因为我一直没有按照厂家推荐的保养计划对汽车进行过保养和维护。

从上述例子，已经能看出来，五个为什么就是通过不断地**追问**来找出根本原因。一般到第五问时，根因差不多也就出来了。当然具体要追问多少次，还得情况而定。

### 问

所谓**问**，即**产生解决方案**，用到的工具可以是`头难风暴`。这也是我第一次听到这个名词，了解之后，发现确实很有用。

> 头脑风暴法（英语：Brainstorming），又称为脑力激荡法，是一种为激发创造力、强化思考力而设计出来的一种方法。可以由一个人或一组人进行。参与者围在一起，随意将脑中和研讨主题有关的见解提出来，然后再将大家的见解重新分类整理。在整个过程中，无论提出的意见和见解多么可笑、荒谬，其他人都不得打断和批评，从而产生很多的新观点和问题解决方法\\
——[维基百科-头脑风暴](https://zh。wikipedia。org/wiki/%E8%85%A6%E5%8A%9B%E6%BF%80%E7%9B%AA%E6%B3%95)

简单地说，头脑风暴就是一个**群策**的过程，日常的讨论算是广义的头脑风暴吧。进行头脑风暴，有几个要点:

1. 设定一个主题
2. 设定时间限制
3. 列出所有意见
4. 激励大家参与
5. **不做评价**

就“不做评价”做一个简单说明。头脑风暴的目的是尽可能多地产生解决方法，仅此而已，评价筛选的工作在**确定方案**阶段进行。若提早对某一方案做评价(一般会是批判性的)，将影响参与者的积极性，一定程度上也会限制意见的创新。当时我们头脑风暴主题是"如何写学术论文"，连"抄袭"都出来了，不过大家也就默契地一笑置之。

### 切

所谓**切**，就是**确定解决方案**。

一种可行的工具是`评价矩阵`，候选的解决方案就是上一阶段头脑风暴的结果，还需要设置一个或多个评价标准，大概的样子如下所示:

![Fibonacci number in recursion and loop](http://ww1.sinaimg.cn/mw690/006faQNTgw1f4k4nesydjj30oy039gnc.jpg)
（上图总分：循环18，递归17）

由评价矩阵可知，虽然循环和递归方式实现Fibonacci数列，两者各项得分有所不同，但按总分来看，可以优先选择循环的方式(当然更好的构造Fibonacci数列的方式可能是生成器)。

根据使用场景的不同，还可以为各项评价标准设定不同的权重，比如就上述例子而言，若重点考虑空间消耗，可设其权重为2或更多，其他评价标准权重为1或其他值。

另外，得分越高越优还是越低越优，可以根据个人喜好来，但务必保持一致。比如有些同学喜欢用小的数值表示消耗低，而效率则喜欢用大的数值表示高效性，这就造成了混乱，最后究竟是得分高者为优还是低的为优? 这是个问题。

## 小结

至此，解决问题的一套流程算是跑完了。让我们简单梳理一下：

- 定义问题 - 问题，本身就被定义为`现状与期望的差距`，因此一种行之有效的定义问题的方法是: `量化差距`
- 分析原因 - 用`鱼骨图`列出所有原因，或用`五个为什么`找出根本原因
- 产生解决方案 - 可以用`头脑风暴`的方式产生尽可能多的解决方案，注意不要做评价
- 确定解决方案 - 可以用`评价矩阵`来确定最终方案

为了讲解清楚，正文中所举的例子都是针对单个环节的。但在实际使用时，大家`望闻问切`的思路来解决问题，应该会有意料之外的收获。

One more thing，`解决问题的方法是多样的`，本文也仅仅提供了一种解决问题的思路。你完全可以在不同环节采用不同的方法或工具，比如在分析出问题产生的原因之后，针对各原因逐个消除，或解决主要矛盾，再或者完全采用其他的解决之道。用伟大领袖我邓主席的话作结：

> 黑猫白猫，能抓住老鼠的，就是好猫。

