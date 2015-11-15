> 原文链接：http://mirnazim.org/writings/python-ecosystem-introduction/
> 
> 译者按：

When developers shift from PHP, Ruby or any other platform to Python, the very first road block they face (most often) is a lack of an overall understanding of the Python ecosystem. Developers often yearn for a tutorial or resource that explains how to accomplish most tasks in a more or less standard way.

What follows is an extract from the internal wiki at my workplace, which documents the basics of the Python ecosystem for web application development for our interns, trainees and experienced developers who shift to Python from other platforms.

This is not a complete resource. My target is to make it a work in perpetual progress. Hopefully, over time, this will develop into an exhaustive tutorial.

## Intended Audience

This is not about teaching Python - the programming language. This tutorial will not magically transform you into a Python ninja. I am assuming that you already know the basics of Python. If you don't, then stop right now. Go read Zed Shaw's brilliant free book Learn Python The Hard Way first and then come back.

I am assuming you are working on Linux (preferably Ubuntu/Debian) or a Linux-like operating system. Why? Because that is what I know best. I have not done any serious programming related work on MS Windows or Mac OS X, other than testing for cross-browser compatibility. Check out the following tutorials on how to install Python on other platforms:

Search the web for the best possible ways of installing Python on your operating system. I highly recommend asking on Stack Overflow.

## The version confusion

TL;DR: Python 2.x is the status quo; Python 3 is the shiny new thing. If you don't care, just skip to Installing Python section below.

When starting with Python, installing version 3.x will seem like a natural first step, but it might not be exactly what you want.

Currently there are two actively developed versions of Python - 2.7.x and 3.x (also called Python 3, Py3K and Python 3000). Python 3 is a different language from Python 2. There are some subtle and some stark semantic and syntactic differences. As of today, Python 2.6/2.7 is the most installed and most used version. Many mainstream and important packages/frameworks/tools/utilities/modules are not yet 100% compatible with Python 3.

Therefore, the safest choice would be to use 2.x (2.7.x to be more specific). Choose Python 3 only if you need it and/or fully understand the implications.

Python 3 Wall of Shame documents the Python 3 compatibility for various packages. Check it thoroughly before deciding to start with Python 3.

## Which VM to use

The Python interpreter or the Python Virtual Machine has a number of different implementations, CPython being the main and most popularly installed implementation. CPython also acts as the reference implementation for other virtual machines.

PyPy is Python implemented in Python, Jython is implemented in Java and runs on the Java VM and IronPython is the Python implementation for Microsoft .NET CLR.

Unless it is really, really important to choose otherwise, CPython should be used to avoid any surprises.

If all this jibber jabber about versions and virtual machines is giving you headaches, then all you need is CPython version 2.7.x. Trust me on this.



