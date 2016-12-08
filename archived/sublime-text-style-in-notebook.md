# 好用！在 Notebook 中使用 Sublime Text 快捷键

关键词：sublime text 快捷键, jupyter notebook, codemirror, 代码效率, custom.js

URL：sublime-text-style-keymap-in-jupyter-notebook

前几天，我在公众号上发布了两篇译文，对 Jupyter Notebook 做了一些基础性的介绍。虽然说比较基础，而且第二篇阅读量并不高，但是我认为对于其他对于 Notebook 不太了解的朋友来说，还是有作用的。

> - [Jupyter Notebook 快速入门（上）](http://codingpy.com/article/getting-started-with-jupyter-notebook-part-1/)
> - [Jupyter Notebook 快速入门（下）](http://codingpy.com/article/getting-started-with-jupyter-notebook-part-2/)

今天，我想分享一个配置 Notebook 的技巧，可以支持在 Notebook 中使用 Sublime Text 的快捷键。因为平常用 ST3 比较多，所以已经习惯了一些它的快捷键，如果能在 Notebook 中也用上的话，那么编写 Notebook 的效率将有很大提升。

经过一番搜索，我得出了以下步骤和代码，可以实现我们想要的功能。

## 第一步：找到 custom.js 文件的地址

在 MacOS 和 Linux 系统下，该文件的默认地址是``~/.jupyter/custom/custom.js``。如果你是第一次配置这个文件，那么很可能这个地址下并不存在该文件。当然，你也可以选择在 Notebook 中运行下面的代码，来确定 custom.js 的路径和内容：

```python
# 打印 Jupyter  配置目录的路径
from jupyter_core.paths import jupyter_config_dir
jupyter_dir = jupyter_config_dir()
print(jupyter_dir)

# 打印 custom.js 的路径
import os.path
custom_js_path = os.path.join(jupyter_dir, 'custom', 'custom.js')
print(custom_js_path)

# 如果 custom.js 文件存在，打印其内容
if os.path.isfile(custom_js_path):
    with open(custom_js_path) as f:
        print(f.read())
else:
    print("You don't have a custom.js file")
```

如果目标路径下没有 custom.js ，那么先创建该文件。为了确保 custom.js 文件确实能其作用，可以在文件的开头加上这样一句代码：

```javascript
alert("hello world from custom.js")
```

然后重启 Jupyter Notebook 。如果一切顺利，重启之后你会看到浏览器弹出一个对话框。

## 添加配置快捷键的代码

接下来，你可以先把上面写的那句 js 代码注释掉。然后在 custom.js 文件中加入以下代码：

```javascript
require(["codemirror/keymap/sublime", "notebook/js/cell", "base/js/namespace"],
    function(sublime_keymap, cell, IPython) {
        // setTimeout(function(){ // uncomment line to fake race-condition
        cell.Cell.options_default.cm_config.keyMap = 'sublime';
        var cells = IPython.notebook.get_cells();
        for(var cl=0; cl< cells.length ; cl++){
            cells[cl].code_mirror.setOption('keyMap', 'sublime');
        }

        // }, 1000)// uncomment  line to fake race condition
    }
);
```

然后再次重启 Jupyter Notebook。

输入一些文本和代码，然后试着按下 Ctrl + D 或者 Ctrl + L 的快捷键。如果顺利的话，你会发现可以在 Notebook 中使用 Sublime Text 的快捷键了！

## 说明

之所以能够实现这个功能，得益于较新版本的 Jupyter Notebook 中使用了 CodeMirror 这个基于 JavaScript 的文本编辑器组件。除了 ST 之外，CodeMirror 还支持 Vim 和 Emacs 按键绑定。

大家有兴趣可以尝试着开启 Vim 或 Emacs 绑定。
