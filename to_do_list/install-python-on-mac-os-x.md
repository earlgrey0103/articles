As with just about any open source software package, there are quite a few ways to install Python on Mac OSX. I figured it would be helpful to detail a few of the easiest ways to install Python, including the following:

Homebrew
Packaged binaries
From Source

These are the most commons you'll encounter, and each method has its own purpose, all of which I'll detail in the sections below.

Instructions for installing Python 2 and 3 are different in most cases (but not by much), so make sure you're paying attention to which version you need installed.

Now, keep in mind that Mac OSX (10.8) already comes with Python 2.7 pre-installed, so these instructions will only really be helpful if you need to upgrade versions or need a better way to manage installations (like with Homebrew).

Install Python with Homebrew
First of all, if you don't know what Homebrew is and you use Mac OSX, you should. According to their website, Homebrew is "the missing package manager for OS X". I'd say this is pretty accurate.

Homebrew

Homebrew lets you install, update, and uninstall packages from the command line, just like apt-get does for Ubuntu. It makes it much easier to install all the various tools you might need. For example, here are just a few things I've installed with it: android-sdk, go, mongodb, sqlite, git, imagemagick, lua, python3.

To install Homebrew, just follow the instructions on their website (which I linked to at the beginning of this section).

Now that you know what Homebrew is and have it installed, we can get on to installing Python. You can install a few different versions of Python, including 2.7.x and 3.5.x.

To install Python 2.7.x, just type:

$ brew install python
If you'd rather have Python 3, just replace python with python3. To see all the versions available, search Homebrew with this:

$ brew search python
This will show you a list of Python-related packages that can be installed.

Install Python Binaries
If you want to upgrade to the latest 2.7.x version or upgrade to Python 3, you can get a binary directly from the Python website.

To install, just click the link above, then click on the version you want. The latest version 2 and 3 links are at the top. Once you've clicked on the version you want, you should see a list of downloads for different operating systems and package types (like source code tarballs, installers, etc).

Python downloads

I'd recommend using the installer since it'll handle everything for you. Just make sure you download the installer that matches your CPU architecture type (32 or 64-bit). In my case I'd be downloading Mac OS X 64-bit/32-bit installer.

Once you've opened the installer, follow the instructions and Python will be installed for you.

Install Python from Source
The last, and most uncommon, method is to install Python from its source code. Most people don't do this since the binaries are alreay built for them. This is really only ever preferred when you want to really customize the binary by setting certain options/flags during the build process.

Here are the commands to download, unpack, and install Python from source:

curl -OL http://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz  
tar xzvf Python-2.7.11.tgz  
cd Python-2.7.11  
./configure --prefix=/usr/local --enable-shared
make  
make install  
Just make sure you change the version numbers to whichever version you want to install.

Note that the same exact commands can be used for Python 3 source compiling, as long as you replace the approprate version numbers.