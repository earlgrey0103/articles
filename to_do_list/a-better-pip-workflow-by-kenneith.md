A Better Pip Workflow

原文：[Kenneth Reitz](http://www.kennethreitz.org/essays/a-better-pip-workflow)

现在大家开发Python应用时，在代码库的根目录中添加一个`requirements.txt`文件已经成了标准实践。

这个文件用处挺多，一般有以下两种形式：

- 某项目的顶层依赖包清单，通常不会说明版本号
- 某项目的全部依赖包清单，每个依赖包都指定版本号

## 方法1：简单的`requirements`文件

> 某项目的顶层依赖包清单，通常不会说明版本号。

	$ cat requirements.txt
	requests[security]
	flask
	gunicorn==19.4.5

方法1非常简单，也是每个使用`requirements`文件的开发者所系统获得的用户体验。但是，如果将这样一个`requirements.txt`文件部署到生产环节，有可能会出现预料之外的问题。因为你没有指定版本号，所以在运行`pip install`后，你今天安装的Python包可能和明天就会不一样。

这是很糟糕的。因为子依赖包可能经常更新版本号，所以重新运行`pip install -r requirements.txt`可能会让你安装不一样的Python包。这有可能会让你的应用因为未知的原因而无法运行。

## 方法2：精确的`requirements`文件

> 某项目的全部依赖包清单，每个依赖包都指定版本号
	$ cat requirements.txt
	cffi==1.5.2
	cryptography==1.2.2
	enum34==1.1.2
	Flask==0.10.1
	gunicorn==19.4.5
	idna==2.0
	ipaddress==1.0.16
	itsdangerous==0.24
	Jinja2==2.8
	MarkupSafe==0.23
	ndg-httpsclient==0.4.0
	pyasn1==0.1.9
	pycparser==2.14
	pyOpenSSL==0.15.1
	requests==2.9.1
	six==1.10.0
	Werkzeug==0.11.4

方法2是部署应用时应采取的最佳实践，可以确保你的运行环境不会出现问题。

所有的依赖包，包括子依赖包都明确列出，而且指定了各自的版本号。

这种类型的`requirements.txt`是在应用的当前工作运行环境下，运行`pip freeze`命令自动生成的。这种做法鼓励平等对待开发/生产环境（dev/prod parity），对待外部依赖包，像对待本身应用的代码一样尊敬（因为它们也是你应用代码的一部分）。

## Frustrations

尽管方法2是使用`requirements.txt`的最佳时间，但实际上还是有点麻烦。举个例子，如果我有一个较大的代码库，希望通过`pip install --upgrade`命令更新部分或全部Python包，我没有办法轻松地做到这点。

之前我的方法是，一个一个把顶层的依赖包挑出来，然后手动输入`pip install requests[security] flask --upgrade`。这个过程可不好受。

我思考了很久，还想过要开发一个工具来解决这个问题。当然，现在已经有了像`pip-tools`这样的工具。可是，我不想在往自己的工具链里再加东西了；这个问题应该利用已有的工具就能解决。

最后，我想出了一个很好的方案，利用我现有的工具解决了这个问题，而且兼具方法1和方法2的优势。我已经在项目中使用这个工作流一段时间，对结果非常满意。

## 工作流

其实很简单：我们不是只放一个`requirements`文件，而是两个：

- requirements-to-freeze.txt
- requirements.txt

### requirements-to-freeze.txt 

	requests[security]
	flask
	gunicorn==19.4.5

### requirements.txt

	cffi==1.5.2
	cryptography==1.2.2
	enum34==1.1.2
	Flask==0.10.1
	gunicorn==19.4.5
	idna==2.0
	ipaddress==1.0.16
	itsdangerous==0.24
	Jinja2==2.8
	MarkupSafe==0.23
	ndg-httpsclient==0.4.0
	pyasn1==0.1.9
	pycparser==2.14
	pyOpenSSL==0.15.1
	requests==2.9.1
	six==1.10.0
	Werkzeug==0.11.4

`requirements-to-freeze.txt`遵循的是方法1，文件中说明了项目的顶层依赖包，以及你需要指定的明确版本号。

`requirements.txt`遵循的是方法2，其中的内容是运行`pip install requirements-to-freeze.txt`命令后，`pip freeze`生成的。

### 基本用法

	$ cd project-repo

	$ pip install -r requirements-to-freeze.txt --upgrade
	Installing collected packages: six, enum34, ipaddress, ...

	$ pip freeze > requirements.txt

鱼与熊掌，二者兼得。

我鼓励你尝试一下这个工作流，很有可能会避免你未来碰到构建失败的问题。
