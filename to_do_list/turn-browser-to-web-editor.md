# 怎样用一行代码将浏览器变身代码编辑器？

浏览器不是用来浏览网页、观看网络视频的吗？难道还可以在浏览器里码代码吗？

没错！真的可以。现在已经有很多类似JSFiddle、JSBin这样在线编辑代码的网站，不过我们今天要分享的方法并不需要注册第三方网站，只需要在浏览器的地址栏输入一行代码即可。我们首先来看一下具体的效果。

![编辑器里的Python代码](http://ww2.sinaimg.cn/mw690/006faQNTgw1f1wqvvbffij30ro08uwft.jpg)

上面这幅图中，我们发现在浏览器中可以输入Python代码，而且支持语法高亮和自动缩进功能。那么，这究竟是怎么实现的呢？

这其实可以追溯到2012年时，一位叫Jose Aguinaga的国外开发者在[Coderwall](https://coderwall.com/p/lhsrcq/one-line-browser-notepad)上分享的一个小贴士。

***

## 将浏览器变成一个简易文本编辑器

一开始的功能非常简单，根本没有语法高亮，也没有自动缩进，仅仅是将浏览器变成一个文本编辑器而已。

Jose分享的代码如下：

	data:text/html, <html contenteditable>

只需要将上面的代码复制粘贴到浏览器的地址栏，就可以让浏览器变成编辑器。是不是非常简单？

背后的原理并不高深，只是用到了Data URI格式而已。这行代码告诉浏览器渲染一个HTML页面，而这个页面具备一个H5属性：contenteditable。

> Data URI是由RFC 2397定义的一种把小文件直接嵌入文档的方案。格式如下：data:[<MIME type>][;charset=<charset>][;base64],<encoded data>。其实整体可以视为三部分，即声明：参数+数据，逗号左边的是各种参数，右边的是数据。

请想尝试的朋友注意，这行代码只适用于Chrome等现代浏览器。如果你还在使用IE8等过时浏览器的话，是没有效果的。

***

## 各种样式衍生而出

由于上面这个小技巧的出现，激发了许多开发者的的激情，不断分享自己的版本。

## 自动切换背景颜色

下面这段代码，可以让编辑器在你一边打字时，一遍切换背景颜色：

	data:text/html, <html><head><link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'><style type="text/css"> html { font-family: "Open Sans" } * { -webkit-transition: all linear 1s; }</style><script>window.onload=function(){var e=false;var t=0;setInterval(function(){if(!e){t=Math.round(Math.max(0,t-Math.max(t/3,1)))}var n=(255-t*2).toString(16);document.body.style.backgroundColor="#ff"+n+""+n},1e3);var n=null;document.onkeydown=function(){t=Math.min(128,t+2);e=true;clearTimeout(n);n=setTimeout(function(){e=false},1500)}}</script></head><body contenteditable style="font-size:2rem;line-height:1.4;max-width:60rem;margin:0 auto;padding:4rem;">

### 笔记本样式

下面这段代码可以将浏览器页面变成一个笔记本的样式，看上去很有感觉：

	data:text/html;charset=utf-8, <title>TextEditor</title> <link rel="shortcut icon" href="http://g.etfv.co/https://docs.google.com"/> <style> html{height: 100%;} body{background: -webkit-linear-gradient(#f0f0f0, #fff); padding: 3%; height: 94%;} .paper { font: normal 12px/1.5 "Lucida Grande", arial, sans-serif; width: 50%; height: 80%; margin: 0 auto; padding: 6px 5px 4px 42px; position: relative; color: #444; line-height: 20px; border: 1px solid #d2d2d2; background: #fff; background: -webkit-gradient(linear, 0 0, 0 100%, from(#d9eaf3), color-stop(4%, #fff)) 0 4px; background: -webkit-linear-gradient(top, #d9eaf3 0%, #fff 8%) 0 4px; background: -moz-linear-gradient(top, #d9eaf3 0%, #fff 8%) 0 4px; background: -ms-linear-gradient(top, #d9eaf3 0%, #fff 8%) 0 4px; background: -o-linear-gradient(top, #d9eaf3 0%, #fff 8%) 0 4px; background: linear-gradient(top, #d9eaf3 0%, #fff 8%) 0 4px; -webkit-background-size: 100% 20px; -moz-background-size: 100% 20px; -ms-background-size: 100% 20px; -o-background-size: 100% 20px; background-size: 100% 20px; -webkit-border-radius: 3px; -moz-border-radius: 3px; border-radius: 3px; -webkit-box-shadow: 0 1px 2px rgba(0,0,0,0.07); -moz-box-shadow: 0 1px 2px rgba(0,0,0,0.07); box-shadow: 0 1px 2px rgba(0,0,0,0.07); } .paper::before { content: ''; position: absolute; width: 4px; top: 0; left: 30px; bottom: 0; border: 1px solid; border-color: transparent #efe4e4; } textarea{display: block; width:94%;margin:0 auto;padding:3.8% 3%; border: none; outline: none; height: 94%; background: transparent; line-height: 20px;} </style> <body spellcheck="false"> <div class="paper"> <textarea autofocus="autofocus"></textarea> </div> </body> </html>


![笔记本样式的浏览器编辑器](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1wropk8bkj314u0g0dif.jpg)

## 如何变身Python编辑器？

接下来，我们来看怎样将浏览器打造成Python编辑器。只需要在地址栏输入下面的代码即可：

	data:text/html, <style type="text/css">.e{position:absolute;top:0;right:0;bottom:0;left:0;}</style><div class="e" id="editor"></div><script src="http://d1n0x3qji82z53.cloudfront.net/src-min-noconflict/ace.js" type="text/javascript" charset="utf-8"></script><script>var e=ace.edit("editor");e.setTheme("ace/theme/textmate");e.getSession().setMode("ace/mode/python");</script>

这段代码是由[jdkanani在Github上分享的](https://gist.github.com/jdkanani/4670615)。

事实上，我们只要简单修改一下上面的代码，就可以马上将浏览器变成其他语言的编辑器，包括Markdown、C/C++、Javscript、Java等几乎所有编程语言。你所要做的，只是将代码中的`ace/mode/python`，修改成`ace/mode/相应的语言（如java）`即可。

除了支持多种语言，它还支持更改页面主题！Eclipse、Github、Textmate等众多经典主题，统统支持！
只需要将`ace/theme/textmate`中的textmate替换成你喜欢的主题即可，如monokai。

## 渲染Markdown文本

如果你习惯于用Markdown语法写作，你或许会希望直接在页面中查看渲染后的效果。只需要输入下面这行代码即可：

	data:text/html,<style type="text/css">.e{position:absolute;top:0;right:50%;bottom:0;left:0;} .c{position:absolute;overflow:auto;top:0;right:0;bottom:0;left:50%;}</style><div class="e" id="editor"></div><div class="c"></div><script src="http://d1n0x3qji82z53.cloudfront.net/src-min-noconflict/ace.js" type="text/javascript" charset="utf-8"></script><script src="http://cdnjs.cloudflare.com/ajax/libs/showdown/0.3.1/showdown.min.js"></script><script> function showResult(e){consoleEl.innerHTML=e}var e=ace.edit("editor");e.setTheme("ace/theme/monokai");e.getSession().setMode("ace/mode/markdown");var consoleEl=document.getElementsByClassName("c")[0];var converter=new Showdown.converter;e.commands.addCommand({name:"markdown",bindKey:{win:"Ctrl-M",mac:"Command-M"},exec:function(t){var n=e.getSession().getMode().$id;if(n=="ace/mode/markdown"){showResult(converter.makeHtml(t.getValue()))}},readOnly:true})</script>

输入Markdown代码之后，然后按Ctrl+M或Command+M，就可以将代码转换成HTML。

![渲染Markdown代码](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1ws9bsrb3j314q0csdje.jpg)

## 背后的原理

看了这几个例子之后，大家可能已经明白了：这些示例都是通过Data URI格式让浏览器渲染一段HTML代码。而编辑器相关的样式已经写在了代码中。这与将相应的HTML代码放在单独文件中打开的效果是相同的。

而在前两个例子中，*代码中实际用到了一个叫ace.js的文件*，不知道大家注意到没有？据小编了解，Ace是一个用JavaScript编写的可嵌入式代码编辑器，据称和Sublime、Vim和TextMate等原生编辑的功能和性能相当。而且，它还可以非常容易滴嵌入到任意网页或JavaScript应用中。

而Ace也是一个叫[Cloud9IDE](https://c9.io/)的在线集成开发环境所使用的主要编辑器。具体效果请看下图：

![Cloud9IDE 编辑器效果](http://ww1.sinaimg.cn/mw690/006faQNTgw1f1wt4dtf4rj30sg0lcn61.jpg)

## SlimText

程序员都是爱折腾的物种。有的开发者还是不满足于上面那种手动输入代码、将浏览器变成编辑器的方法，甚至是直接将真正的编辑器搬到了浏览器中运行。这就是我们最后要介绍的[SlimText](http://slimtext.org/)，下面是具体截图。

![SlimText截图](http://ww3.sinaimg.cn/mw690/006faQNTgw1f1wt4dratfj30hs0b4tc5.jpg)

如截图所示，SlimText是一个真正的浏览器端的代码编辑器，以Chrome插件的形式存在，文件结构、文件搜索、文件保存等功能一应具有。它是一位名叫[tylerlong](https://github.com/tylerlong/slim_text)的国人开发的，支持Windows、Linux和Mac OS X等多个平台。

感兴趣的话，建议你直接通过Chrome Web Store安装。Windows 8 系统下安装如果碰到问题，请以Windows 7兼容模式运行Chrome。
