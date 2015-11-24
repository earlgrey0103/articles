Configuring a data science environment can be a pain. Dealing with inconsistent package versions, having to dive through obscure error messages, and having to wait hours for packages to compile can be frustrating. This makes it hard to get started with data science in the first place, and is a completely arbitrary barrier to entry.

配置数据科学开发环境让人头疼。包版本不一致，陌生的错误信息和等待编译的漫长时间等问题很容易让人垂头丧气。这使得迈入数据科学的这第一步十分艰难，而且也是一个完全不常见的准入门槛。

The past few years have seen the rise of technologies that help with this by creating isolated environments. We’ll be exploring one in particular, Docker. Docker makes it fast and easy to create new data science environments, and use tools such as Jupyter notebooks to explore your data.

还好，过去几年中出现了能够通过搭建孤立的环境，解决这个问题的技术。本文中我们就要介绍其中的一种，Docker。Docker能让开发者简单、快速地搭建数据科学开发环境，并支持使用例如Jupyter notebooks等工具进行数据探索。

With Docker, we can download an image file that contains a set of packages and data science tools. We can then boot up a data science environment using this image within seconds, without the need to manually install packages or wait around. This environment is called a Docker container. Containers eliminate configuration problems – when you start a Docker container, it has a known good state, and all the packages work properly.

要使用Docker，我们要先下载一个包括了一系列包和数据科学工具的镜像文件。之后，我们可以通过该镜像在数秒之内就启动一个数据科学开发环境，免去了手动安装包。这个环境，也被成为Docker容器。容器消除了配置的问题——当你启动一个Docker容器后，它就已经处于了良好的状态，所有的包都是可以正常运转的。

The Docker whale is here to help

Docker的出现是为了帮助你

In addition to lowering the barriers to getting started with data science, Docker also makes it possible to quickly create isolated environments with different Python and package versions without having to wait for packages to install in virtual environments.

除了降低进入数据科学的门槛之外，Docker还可以让我们快速搭建拥有不同Python版本和安装了不同包的孤立环境，不用等待在虚拟环境中安装包。

In this post, we’ll cover the basics of Docker, how to install it, and how to leverage Docker containers to quickly get started with data science on your own machine.

在本文中，我们将介绍Docker的基础知识，如何安装Docker以及如何利用Docker容器快速地在自己的机器上搭建数据科学环境。

Virtual machines
虚拟机

Software that creates virtual machines has existed for decades. Virtual machines allow you to emulate other computing environments on your computer. For example, you could run Linux in a virtual machine, even if your computer runs Windows. This would let you use Linux without having to actually install it on your machine – it would be running virtually, so you would be able to access it from within Windows. You’d be able to essentially click a program, and a Linux desktop would pop up in a window. Virtual machines use images to boot up – you have to start a virtual machine with an image that corresponds to the operating system you want to use. If you want to use Linux, you’d use an image that contains all of the necessary files to create a Linux environment.

能够创建虚拟机的软件已经问世数十年。虚拟机可以让你在自己的电脑上模拟其他的计算环境。举个例子，即使你的电脑运行的是Windows操作系统，你仍可以通过虚拟机运行Linux系统。这可以让你在不重装系统的前提下，使用Linux——也就是说，Linux系统可以虚拟化运行，所以你可以从Windows系统访问虚拟机。基本上，你可以在点击一个程序之后，看到弹出一个Linux桌面的窗口。虚拟机需要镜像来启动——你必须先拥有一个期待使用的系统的镜像，才能启动相应的虚拟机。如果你想使用Linux，你就得使用一个包含了创建Linux环境必须的所有文件的镜像。


An example of using Windows in a virtual machine on a mac

示例：在Mac上通过虚拟机使用Windows

Containers
容器

Although virtual machines enable Linux development to take place on Windows, for example, they have some downsides. Virtual machines take a long time to boot up, they require significant system resources, and it’s hard to create a virtual machine from an image, install some packages, and then create another image. Linux containers solve this problem by enabling multiple isolated environments to run on a single machine. Think of containers as a faster, easier way to get started with virtual machines.

尽管虚拟机有诸多好处，例如能够让在Windows平台进行Linux开发成为现实，但是也有着自身的缺陷。虚拟机的启动时间很长，要消耗大量的系统资源，而且利用镜像创建虚拟机，安装所需要的包，再创建另一个镜像是很困难的。Linux容器通过让多个孤立环境在同一台机器上运行，解决了这个问题。你可以把容器看作是使用虚拟机的一种更快、更简单的方法。

Unfortunately, containers are a bit tricky to use, and it’s not easy to manage and distribute container images. We want these features so we can quickly download and start data science environments with specific package and tool configurations. For instance, you might want to be able to quickly start a container that has Jupyter notebook, spark, and pandas already installed.

但是，容器的使用却有点麻烦，而且管理和发布容器镜像也不容易。作为开发人员，我们希望能够快速下载，并且启动一个拥有指定包和工具配置的数据科学环境。例如，你会希望能快速启动一个案子了Jupyter notebook、spark和pandas的容器。

Docker
容器

Docker containers are a layer over Linux containers that makes them easier to manage and distribute. Docker makes it easy to download images that correspond to a specific set of packages, and start them quickly. Docker is cross-platform, and works on Mac, Windows, and Linux.

Docker容器是Linux容器的一层外围容易，可以支持更简单地对容器进行管理和发布。使用Docker，可以很容易地下载具备相应包的镜像，并且快速启动。另外，Docker是跨平台的，支持包括Mac、Windows和Linux等系统。

These same advantages also apply to virtual environments, a way to create isolated Python environments. The primary advantages of Docker over virtual environments are:

这些优势也适用于虚拟环境（virtual environment）——创建孤立Python环境的一种方式。Docker相较于虚拟环境的主要优势有：

Ability to quickly get started. You don’t need to wait for packages to install when you just want to jump in and start doing analysis.
Known good configuration. Many times, Python packages will require system packages and configuration to be setup. This can cause mysterious errors. With Docker, the packages are already setup and ready to go.
Consistently cross platform. Python packages are cross-platform, but some behave differently on Windows vs Linux, and some have dependencies that can’t be installed on Windows. Docker containers always run in a Linux environment, so they’re consistent.
Ability to checkpoint and restore. You can install packages into a Docker image, then create a new image of that checkpoint. This will give you the ability to quickly undo changes or rollback configurations.
Running a Docker image creates a Docker container. For our purposes, we can run Jupyter notebook inside this container, and use a web browser to work with our data.

- 能够快速启动。如果你想马上就开始进行数据分析，那就免去了你等待各种包进行安装的时间。
- 配置测试无误。很多时候，Python包会需要提前安装某些系统包，并进行相应设置才能正常使用。如果设置不当，会引起一些很奇怪的错误。但是使用Docker后，这些包就已经配置好了，可以立即使用。
- 跨平台一致性。Python中的包是可以跨平台使用的，但是在Windows和Linux平台下有些不同，而且还有部分依赖包无法在Windows中安装。但是由于Docker容器运行的都是Linux环境，所以它们是高度一致的。
- 能够设置checkpoint并且进行恢复。你可以往Docker镜像中安装包，然后将那个checkpoint下的环境创建成一个新的镜像。这让你能够快速撤销该表或者回滚配置。

运行一个Docker镜像，就创建了一个Docker容器。在本文中，我们在容器中运行一个Jupyter notebook，然后通过网络浏览器来处理数据。

Installing Docker

安装Docker

The first step is installing Docker. There’s a graphical installer for Windows and Mac that makes this easy. Here are the instructions for each OS:

第一步就是安装Docker。Docker官方为Windows和Mac用户提供了一个简便安装过程的图形界面安装器。下面是每个操作系统的安装指南。

Mac OS
Linux
Windows

As part of this installation process, you’ll need to use a shell prompt. The shell prompt, also called the terminal or the command line, is a way to run commands on your machine from a text interface instead of graphically. For example, you can launch a text editor by double clicking on notepad in Windows, or by typing nano in a Linux shell session. There’s a special version of the shell that comes pre-configured for using Docker commands. Here’s how to open it:

在安装时，你需要使用shell prompt。shell prompt也被称为终端或命令行，是在你的机器上通过文本界面而非图形界面运行命令的一种方式。例如，你可以在Windows系统中双击记事本就可以打开一个文本编辑器，也可以在Linux终端中输入nano实现这个效果。Docker提供了一个预先配置好的终端，可以用来运行Docker命令。请按照下面的方法打开：

Mac OS – launch the Docker Quickstart Terminal application from Launchpad. There’s more detail here.
Mac OS —— 从Launchpad中打开Docker Quickstart Terminal程序。详情见本篇文章。

Linux – Launch any bash shell prompt, and docker will already be available.
Linux —— 打开任意bash终端，就可以使用docker。
Windows – click the Docker Quickstart Terminal icon on your desktop. There’s more detail here.
Windows —— 双击桌面上的Docker QuickstartTerminal程序的图标。详情见本篇文章。

You’ll need to use this same shell prompt whenever the rest of this post mentions having to run a Docker command or type a specific command.

下文在提到需要运行Docker命令或输入某个命令时，你都需要使用这个特别的终端程序。

Downloading the image
下载镜像

The next step is to download the image you want. Here are our currently available data science images:
下一步是下载你需要的镜像。下面是我们网站目前提供的数据科学开发专用镜像：

dataquestio/python3-starter – This contains a python 3 installation, jupyter notebook, and many popular data science libraries such as numpy, pandas, scipy, scikit-learn, and nltk.

dataquestio/python3-starter —— 这个镜像已经安装好了Python 3, Jupyter notebook和许多其他流行的数据科学库，包括numpy，pandas，scipy，scikit-learn和nltk。

dataquestio/python2-starter – This contains a python 2 installation, jupyter notebook, and many popular data science libraries such as numpy, pandas, scrapy, scipy, scikit-learn, and nltk.

dataquestio/python2-starter —— 这个镜像已经安装好了Python 2, Jupyter notebook和许多其他流行的数据科学库，包括numpy，pandas，scipy，scikit-learn和nltk。

You can download the images by typing docker pull IMAGE_NAME. If you wanted to pull dataquestio/python3-starter, you’d type docker pull dataquestio/python3-starter into a shell prompt. This will download the images from Docker Hub, which is like Github, but for Docker images. It will download the image files onto your machine, so you can start a container with the image.

你可以通过输入`docker pull IMAGE_NAME`下载相应的镜像。如果你想下载dataquestio/python3-starter这个镜像，你需要在终端输入`docker pull dataquestio/python3-starter`命令。输入这段命令后，程序会自动从Docker Hub下载镜像，Docker Hub与Github类似，不过确实Docker镜像的一个中枢。它会将相应的镜像文件下载至你的本地机器，这样你才能利用该镜像创建容器。

Make a folder
新建一个文件夹

Make a folder on your local machine that will correspond to where you want the notebooks stored. This folder will contain all of your work, and will persist on your local machine, even if you terminate the docker container. For this example, we’ll make this folder at /home/vik/notebooks.

在本地创建一个文件夹，用于存放notebooks。这个文件夹中将储存你所有的工作文件，并会持续存在于你的机器中，即使是你销毁了docker容器。在这里，我们将床建下面这个文件夹，/home/vik/notebooks。

Running the image
Once you download the image, you can run it using docker run. We need to pass in a few options to ensure that it’s configured properly.

运行镜像
镜像下载完成后，你可以通过`docker run`运行该镜像。我们需要传入一些选项，确保镜像配置正确。

The -p flag sets the ports so that we can access the Jupyter notebook server from our machine.

-p 选项设置虚拟机的端口，让我们可以在本地访问Jupyter notebook服务器。

The -d flag runs the container in detached mode, as a background process.

-d 选项以detached模式运行容器，也就是作为背景进程运行。

The -v flag lets us specify which directory on the local machine to store our notebooks in.

-v 选项让我们指定在本地机器中使用哪个文件夹存储notebook。

The full command looks like docker run -d -p 8888:8888 -v /home/vik/notebooks:/home/ds/notebooks dataquestio/python3-starter.

完整的运行命令是类似这样的：`docker run -d -p 8888:8888 -v /home/vik/notebooks:/home/ds/notebooks dataquestio/python3-starter`。

You should change /home/vik/notebooks to whatever folder you created to store your notebooks in. You should change dataquestio/python3-starter to your preferred docker image.

你应该将`/home/vik/notebooks`更改为你用于存储文件的地址。另外，应该把`dataquestio/python3-starter`更改为自己喜欢的docker镜像。

Executing docker run will create a Docker container. This is isolated from your local machine, and it may be helpful to think of it as a separate computer. Inside this container, Jupyter notebook will be running, and we’ll be able to access many data science packages.

执行`docker run`命令将会创建一个Docker容器。这是与你的本地机器相隔绝的，也可以把它看作是一台单独的电脑。在容器内部，会运行一个Jupyter notebook服务器，我们也可以使用许多数据科学工具包。

The docker run command will print a long string. This is the unique id of your container, and is used when modifying the container with other docker containers. We’ll refer to it as the container id from now on.

另外，`docker run`命令也会在终端打印出一段长字符串。这是你的容器的独有ID，在通过其他docker容器对该容器进行修改时，就必须要使用这个ID。在下文中我们称该ID为容器ID。

Viewing the notebook server
查看notebook服务器

If you’re running Linux, the next step is easy – just go to localhost:8888, and you should see the notebook running. If you’re on Windows or OSX, and you followed the Docker installation instructions earlier, you used docker-machine in your docker installation process. The name of your local machine is default, and running docker-machine ip default will tell you the ip of the docker container. If you used a different name, like dev, just swap it for default in the command. Then, you just visit CONTAINER_IP:8888 to see the notebook (replace CONTAINER_IP with the ip of your container).

如果你的系统是Linux，那么下一步非常简单——只需要在浏览器中打开localhost:8888，之后应该就能看到运行中的notebook。如果你使用的是Windows或OSX，之前也按照Docker官方安装指南进行了操作，那在安装过程中应该就使用了docker-machine。你的本地机器的名称是默认的（default），运行`docker-machine ip default`命令就可以得知docker容器的ip。如果使用了其他的名字，例如dev，那在命令中将default替换为dev即可。接下来，在浏览器中访问`CONTAINER_IP:8888`就可以看到notebook（将CONTAINER_IP替换为你的容器的ID）。


This is what you should see
下面就是你应该看到的样子。


Making a notebook
At this point, you can make a new Jupyter notebook to test how things are working. Try running a scikit-learn example from here:

	from sklearn import datasets
	from sklearn.cross_validation import cross_val_predict
	from sklearn import linear_model
	import matplotlib.pyplot as plt
	%matplotlib inline

	lr = linear_model.LinearRegression()
	boston = datasets.load_boston()
	y = boston.target

	predicted = cross_val_predict(lr, boston.data, y, cv=10)

	fig, ax = plt.subplots()
	ax.scatter(y, predicted)
	ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
	ax.set_xlabel('Measured')
	ax.set_ylabel('Predicted')
	plt.show()

Adding in data files
If you want to add data files into your environment, you have three options. The first is to place them in the folder you created earlier to use for notebooks. Any files you place in there will automatically be accessible from inside your Jupyter notebooks.

The second way is to use the docker cp command. Docker cp can copy files from your machine to the container, and vice versa. Let’s say you want to copy a file at /home/vik/data.csv to a container with id 4greg24134. You would type docker cp /home/vik/data.csv 4greg24134:/home/ds/notebooks. This will copy the data.csv file into the notebooks directory in the container. You can place files anywhere you want, but putting them in the notebooks directory makes them easily accessible from Jupyter notebook.

The third way is to use the upload button at the top right of the Jupyter notebook main page. This will let you select a file and upload it to the notebooks directory in the container.

Regardless of which method you choose, here’s how you would load the file inside a Jupyter notebook:

import pandas
data = pandas.read_csv("data.csv")
Copying data files from the container
You may also want to get files from the container onto your local machine. The easiest way is to place the files in the /home/ds/notebooks folder, where they will be automatically mirrored into your local machine.

Another way is to again use docker cp. Let’s say you want to copy a file at /home/ds/notebooks/data.csv from a container with id 4greg24134 to the folder /home/vik/ on your machine. You would type docker cp 4greg24134:/home/ds/notebooks/data.csv /home/vik/data.csv.

A final way is to use the download options in the Jupyter interface. Clicking on a non-notebook file in the browser view will download it to your local machine. If you’re working on a notebook, clicking “File”, then “download as” will download it to your machine.

Installing more packages
If you want to install your own packages inside the container, you can get into it and run any normal bash shell commands. In order to get into a container, you’ll need to run docker exec. Docker exec takes a specific container id, and a command to run. For instance, typing docker exec -it 4greg24134 /bin/bash will open a shell prompt in the container with id 4greg24134. The -it flags ensure that we keep an input session open with the container, and can enter commands.

After running docker exec, you’ll be put into a shell prompt inside the container. The container is running python in a virtual environment called ds, which should already be activated.

To install packages, just type pip install PACKAGE_NAME. You could install requests with pip install requests.

When you want to exit the container shell prompt, just type exit.

Shutting down your docker container
When you’re done exploring your data, you can shut down the docker container. Use docker rm -f CONTAINER_ID to stop the container. You should have your container id from earlier. If you don’t, you can find it by running docker ps. Your notebooks will still be available on your local machine, in the folder you created, even after you shut down the container.

Building on this
Docker images are created from Dockerfiles. Dockerfiles specify which packages and tools should be installed in an image. By modifying Dockerfiles, you can change which packages and tools come with the image by default.

If you want to build on the images we’ve discussed in this post, you can contribute to our Github repository here, which contains the Dockerfiles. We welcome improvements to our current images, or the addition of new images focusing on tools other than Python.