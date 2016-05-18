# Reaper：Python脚本加速音乐制作过程

> 这是编程派发布的第二篇投稿，作者是amt。文章讲述的是Python在音乐制作软件Reaper中的应用。内容虽然不长，对于大多数人来说用处也不大，但是算是开拓一些眼界。下次在知乎碰到Python能干什么有趣的事这样的问题，就可以加上这个例子了。

众所周知，音乐创作是一个创意密集型的工作，但是许多音乐工作者每天很大一部分的工作都是重复性的。幸运的是，软件开发商制作了各种省时省力的软件，如[Reaper](http://www.reaper.fm/)。但是这远远不够。
音乐软件开发商在不断努力，音乐工作者的需求也在不断刷新，于是有一些持开放态度的开发商开放了接口，让使用者也可以DIY软件的功能。以下是我在Reaper这一款音乐制作软件重，使用Python自己写脚本实现功能的例子。

这次要实现的功能是根据关键字查询轨道并选中目标轨道，听起来就像是在txt文件里找关键字那么简单，但在大部分的音乐制作软件里，竟没有这个功能。

我们使用的模块：reaper_python。

## 设置Reaper使用Python

在菜单栏Preference -> Plugins中选择使用Python作为脚本语言，具体设置方式如下：

![]()

## 导入模块，定义撤销范围

导入模块，若导入模块失败，抛出异常。RPR_ShowConsoleMsg的函数可在Reaper里弹出带提示信息的窗口。

```python
try:
	from reaper_python import *
except:
	RPR_ShowConsoleMsg('Could not load reaper python')
```

接下来定义撤销范围，这样可以在Reaper里撤销操作过的命令，就像在软件里原生的功能一样。

```python
RPR_Undo_BeginBlock2(0)
# 功能代码片段
RPR_Undo_EndBlock2(0, 'RecArmChange', -1)
```

## 获取关键字输入信息

这一步使用的是RPR_GetUserInputs。这一步执行时会弹出窗口让用户输入字符。最后对大小写实行标准化，并获取输入值。

```python
names = 'Key word:'
dvalues = ''
maxreturnlen = 10

nitems = len(dvalues.split(','))

res = RPR_GetUserInputs('Search Tracks', nitems, 
		names, dvalues, maxreturnlen)

searchName = res[4].split(',')
if res[0]:
	reslen = len(searchName)
	i = 0;
	if i < reslen:
		searchName = str(searchName[i]).lower()
		i += 1
```

## 遍历所有轨道名，并选中对应轨道

我们要用到一下函数：

- RPR_CountTracks计算轨道数量；
- RPR_GetTrack获取轨道id；
- RPR_GetSetMediaTrackInfo_String来获取轨道名字。

对用户输入的字符与轨道名的字符进行对比，若存在，便选中轨道。

```python
trackCount = int(RPR_CountTracks(0))
for x in range(trackCount):
	trackId = RPR_GetTrack(0, x)
	trackName = str(RPR_GetSetMediaTrackInfo_String(trackId,
		 'P_Name', '', False)[3])
	RPR_SetTrackSelected(trackId, 0)

	if str(searchName) in str(trackName.lower()):
		RPR_SetTrackSelected(trackId, 1)

```

至此，我们实现了上面所描述的功能需求：根据关键字查询轨道并选中目标轨道。

我们只需要在菜单Actions -> Load，选择编写好的Python脚本加载。

具体演示效果如下：

![]()

## 结语

这是初学Python的我做出的第一个成功的尝试。我后面在这个尝试的基础上做出了根据midi旋律长度，自动选择轨道使用硬件音源录制的功能。大家也可以来玩一玩，有国外用户还做出了根据歌词文本自动滚动歌词的功能（卡拉ok），非常有趣。
