Configuring a data science environment can be a pain. Dealing with inconsistent package versions, having to dive through obscure error messages, and having to wait hours for packages to compile can be frustrating. This makes it hard to get started with data science in the first place, and is a completely arbitrary barrier to entry.

The past few years have seen the rise of technologies that help with this by creating isolated environments. We’ll be exploring one in particular, Docker. Docker makes it fast and easy to create new data science environments, and use tools such as Jupyter notebooks to explore your data.

With Docker, we can download an image file that contains a set of packages and data science tools. We can then boot up a data science environment using this image within seconds, without the need to manually install packages or wait around. This environment is called a Docker container. Containers eliminate configuration problems – when you start a Docker container, it has a known good state, and all the packages work properly.


The Docker whale is here to help

In addition to lowering the barriers to getting started with data science, Docker also makes it possible to quickly create isolated environments with different Python and package versions without having to wait for packages to install in virtual environments.

In this post, we’ll cover the basics of Docker, how to install it, and how to leverage Docker containers to quickly get started with data science on your own machine.

Virtual machines
Software that creates virtual machines has existed for decades. Virtual machines allow you to emulate other computing environments on your computer. For example, you could run Linux in a virtual machine, even if your computer runs Windows. This would let you use Linux without having to actually install it on your machine – it would be running virtually, so you would be able to access it from within Windows. You’d be able to essentially click a program, and a Linux desktop would pop up in a window. Virtual machines use images to boot up – you have to start a virtual machine with an image that corresponds to the operating system you want to use. If you want to use Linux, you’d use an image that contains all of the necessary files to create a Linux environment.


An example of using Windows in a virtual machine on a mac

Containers
Although virtual machines enable Linux development to take place on Windows, for example, they have some downsides. Virtual machines take a long time to boot up, they require significant system resources, and it’s hard to create a virtual machine from an image, install some packages, and then create another image. Linux containers solve this problem by enabling multiple isolated environments to run on a single machine. Think of containers as a faster, easier way to get started with virtual machines.

Unfortunately, containers are a bit tricky to use, and it’s not easy to manage and distribute container images. We want these features so we can quickly download and start data science environments with specific package and tool configurations. For instance, you might want to be able to quickly start a container that has Jupyter notebook, spark, and pandas already installed.

Docker
Docker containers are a layer over Linux containers that makes them easier to manage and distribute. Docker makes it easy to download images that correspond to a specific set of packages, and start them quickly. Docker is cross-platform, and works on Mac, Windows, and Linux.

These same advantages also apply to virtual environments, a way to create isolated Python environments. The primary advantages of Docker over virtual environments are:

Ability to quickly get started. You don’t need to wait for packages to install when you just want to jump in and start doing analysis.
Known good configuration. Many times, Python packages will require system packages and configuration to be setup. This can cause mysterious errors. With Docker, the packages are already setup and ready to go.
Consistently cross platform. Python packages are cross-platform, but some behave differently on Windows vs Linux, and some have dependencies that can’t be installed on Windows. Docker containers always run in a Linux environment, so they’re consistent.
Ability to checkpoint and restore. You can install packages into a Docker image, then create a new image of that checkpoint. This will give you the ability to quickly undo changes or rollback configurations.
Running a Docker image creates a Docker container. For our purposes, we can run Jupyter notebook inside this container, and use a web browser to work with our data.

Installing Docker
The first step is installing Docker. There’s a graphical installer for Windows and Mac that makes this easy. Here are the instructions for each OS:

Mac OS
Linux
Windows
As part of this installation process, you’ll need to use a shell prompt. The shell prompt, also called the terminal or the command line, is a way to run commands on your machine from a text interface instead of graphically. For example, you can launch a text editor by double clicking on notepad in Windows, or by typing nano in a Linux shell session. There’s a special version of the shell that comes pre-configured for using Docker commands. Here’s how to open it:

Mac OS – launch the Docker Quickstart Terminal application from Launchpad. There’s more detail here.
Linux – Launch any bash shell prompt, and docker will already be available.
Windows – click the Docker Quickstart Terminal icon on your desktop. There’s more detail here.
You’ll need to use this same shell prompt whenever the rest of this post mentions having to run a Docker command or type a specific command.

Downloading the image
The next step is to download the image you want. Here are our currently available data science images:

dataquestio/python3-starter – This contains a python 3 installation, jupyter notebook, and many popular data science libraries such as numpy, pandas, scipy, scikit-learn, and nltk.
dataquestio/python2-starter – This contains a python 2 installation, jupyter notebook, and many popular data science libraries such as numpy, pandas, scrapy, scipy, scikit-learn, and nltk.
You can download the images by typing docker pull IMAGE_NAME. If you wanted to pull dataquestio/python3-starter, you’d type docker pull dataquestio/python3-starter into a shell prompt. This will download the images from Docker Hub, which is like Github, but for Docker images. It will download the image files onto your machine, so you can start a container with the image.

Make a folder
Make a folder on your local machine that will correspond to where you want the notebooks stored. This folder will contain all of your work, and will persist on your local machine, even if you terminate the docker container. For this example, we’ll make this folder at /home/vik/notebooks.

Running the image
Once you download the image, you can run it using docker run. We need to pass in a few options to ensure that it’s configured properly.

The -p flag sets the ports so that we can access the Jupyter notebook server from our machine.
The -d flag runs the container in detached mode, as a background process.
The -v flag lets us specify which directory on the local machine to store our notebooks in.
The full command looks like docker run -d -p 8888:8888 -v /home/vik/notebooks:/home/ds/notebooks dataquestio/python3-starter.

You should change /home/vik/notebooks to whatever folder you created to store your notebooks in. You should change dataquestio/python3-starter to your preferred docker image.

Executing docker run will create a Docker container. This is isolated from your local machine, and it may be helpful to think of it as a separate computer. Inside this container, Jupyter notebook will be running, and we’ll be able to access many data science packages.

The docker run command will print a long string. This is the unique id of your container, and is used when modifying the container with other docker containers. We’ll refer to it as the container id from now on.

Viewing the notebook server
If you’re running Linux, the next step is easy – just go to localhost:8888, and you should see the notebook running. If you’re on Windows or OSX, and you followed the Docker installation instructions earlier, you used docker-machine in your docker installation process. The name of your local machine is default, and running docker-machine ip default will tell you the ip of the docker container. If you used a different name, like dev, just swap it for default in the command. Then, you just visit CONTAINER_IP:8888 to see the notebook (replace CONTAINER_IP with the ip of your container).


This is what you should see

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