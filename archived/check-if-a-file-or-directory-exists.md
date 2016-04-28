# Python：检查某个文件或文件夹是否存在

在编程的世界中，一个问题通常有许多种解决办法，对于 Python 来说这点尤为明显。很多时候，你会发现很多标准模块的用途基本相同，只是功能略有区别。利用 Python 检查某个文件或文件夹是否存在就是一个证明这点的例子。

下面列出了检查文件或文件夹是否存在的几种方法及其区别之处。在下面的示例中，我们假设当前工作目录下有这些文件和文件夹：

	drwxr-xr-x  3 scott  staff  102 Jan 12 10:01 dir  
	-rw-r--r--  1 scott  staff    5 Jan 12 09:56 file.txt
	lrwxr-xr-x  1 scott  staff    8 Jan 12 09:56 link.txt -> file.txt  
	lrwxr-xr-x  1 scott  staff    3 Jan 12 10:00 sym -> dir  

我们有一个文件夹（`dir`）、一个文件（`file.txt`）、一个文件符号链接（`link.txt`）和一个目录符号链接（`sym`）。


## 检查某个文件是否存在

下面的代码可以说是检查文件是否存在以及其是否为文件的最简单方法。

	import os  
	os.path.isfile('./file.txt')    # True  
	os.path.isfile('./link.txt')    # True  
	os.path.isfile('./fake.txt')    # False  
	os.path.isfile('./dir')    # False  
	os.path.isfile('./sym')    # False  
	os.path.isfile('./foo')    # False 

注意`os.path.isfile`能够追踪符号链接（symlinks），所以在检查`link.txt`时得到的结果是`True`。

`isfile`实际上只是一个辅助方法（helper method），其内部使用了`os.stat`和`stat.S_ISREG(mode)`，稍后再详细介绍。

## 检查某个文件夹是否存在

与`isfile`方法类似，`os.path.isdir`是检查某个文件夹是否存在或者某个给定路径是否是文件夹的最简单方法。

	import os  
	os.path.isdir('./file.txt')    # False  
	os.path.isdir('./link.txt')    # False  
	os.path.isdir('./fake.txt')    # False  
	os.path.isdir('./dir')    # True  
	os.path.isdir('./sym')    # True  
	os.path.isdir('./foo')    # False  

同样，`os.path.isdir`也能够追踪符合链接。它也只是一个简单的辅助函数，其底层调用了`os.stat`和`stat.S_ISDIR(mode)`。

## 检查是否存在文件或文件夹

检查某个路径（前提是你不关心其指向的是文件还是文件夹）是否存在的另一种方法，是使用`os.path.exists`。

	import os  
	os.path.exists('./file.txt')    # True  
	os.path.exists('./link.txt')    # True  
	os.path.exists('./fake.txt')    # False  
	os.path.exists('./dir')    # True  
	os.path.exists('./sym')    # True  
	os.path.exists('./foo')    # False  

这个函数不关心路径指向的是文件、文件夹还是符号链接，因此这就好像你在使用的是`isfile(path)`或`isdir(path)`。但实际上，它调用的是`os.stat(path)`，如果出错的话它会返回`False`。

## 高级方法

上面我一直在说那些方法利用了`os.stat`模块，因此我觉得详细了解下这个模块是有好处的。这是一个底层方法，可以提高关于文件、文件夹、套接字、缓存等的详细信息。

和前面提到的两种方法一样，`os.stat`也会追踪符号链接，因此如何你想获得某个链接的状态信息，应该使用的是`os.lstat()`方法。

由于操作系统之间存在差异，`os.stat`提供的数据可能有所区别。下面是每个操作系统都会提供的一些数据：

	st_mode: protection bits
	st_uid: owner's user id
	st_gid: owner's group id
	st_size: size of file in bytes
	st_atime: time of last access
	st_mtime: time of last modification
	st_ctime: time of last metadata change on Unix, or time of creation on Windows

你可以使用`stat`模块提供的这些数据，获取自己感兴趣的信息，比如说某个路径是否指向一个套接字（`stat.S_ISSOCK(mode）`），或则是某个文件是不是其实只是一个有命名的管道（`stat.S_ISFIFO(mode)`）。

如果你需要更高级的功能，那么应该使用`os.stat`这个模块。但是大部分情况下，你只需要使用`os`或`os.path`中的模块就足够了。

当然，其中一个合理的使用场景是需要对同一个文件进行多次测试，同时向避免stat系统调用带来的消耗。因此，如果你有不少的测试要做，那么这个模块会提高你的效率哦。

英文原文：[http://stackabuse.com/python-check-if-a-file-or-directory-exists/](http://stackabuse.com/python-check-if-a-file-or-directory-exists/)