Developing in Python is very different from developing in other languages. Python is an interpreted language like Ruby or Perl, so developers are able to use read-evaluate-print loops (REPLs) to execute Python in real-time. This feature of Python means that it can be used for rapid development and prototyping because there is no build process. Python includes many functional programming tools akin to Scala or Javascript to assist with closure based script development. But Python is also a fully scalable object-oriented language, a paradigm used to build large modular software rather than to simply execute scripts, more akin to Java or C++.

Python sits in the middle of these paradigms, providing the best of many worlds. Python is used for writing quick one-off scripts, large scale web frameworks like Django, data processing with Celery, even numerical and scientific computing. Python is lightweight, is standard on many operating systems, and is effective, thereby making it the top choice for data scientists and analysts for data engineering and analytical tasks.

However, the breadth of Python means that there is no one workflow to developing with it, and certainly there is no standard IDE or environment framework to make these decisions on your behalf. Most Python educational materials focus on the scripting aspects of the language, leaving out the important details of how to construct larger projects. This post will focus on the question of how a developer interacts with Python to build larger data applications.

A Development Environment

So what do you need in order to successfully develop data apps with Python? Quite simply all you need is:

A text editor - Sublime, Notepad++, Vim, Emacs, and Text Wrangler all work.
A terminal with the python executable in your path.
That's it! There are many development environments for using Python that add additional tools to your workflow including debuggers, code completion, and syntax highlighting. However, when it comes down to it, these software programs are simply wrapping the basic text editor and terminal together with some added functionality. If you must use an IDE, I would suggest the following:

IDLE - this environment will be familiar to Windows users who probably executed their first Python commands in it. It's very simple, but it is the default and effective.
Komodo Edit - this free IDE for Python is written by ActiveState and provides many tools and functionality.
PyCharm - this IDE is not free, but provides an IntelliJ-like experience.
Aptana Studio - Aptana does have some built in Python support, and focuses on web.
Spyder - A Python studio specifically for scientific computing.
iPython - an interactive development environment that allows you to create notebooks for presenting Python code and data.
However, even when using one of these tools, you'll still probably use the basic workflow described below. Many professional Python developers are content with Sublime Text 3 for its subtly powerful features and syntax highlighting coupled with pdb and the command line. This is what I do, and it will enable you to have truly foo development!

As your projects grow larger you will also want to include the following tools into your worklow:

Git/Github.com - code repository, but with Github, also an issue tracker and wiki.
pip - the python package manager for installing third party tools.
virtualenv and virtualenvwrapper - manage virtual environments for development.
There are many tools to aid in software development, but these three tools are a vital part of modern Python development, and will be discussed further in the rest of this post.

Third Party Libraries

As you develop Python code, you'll inevitably start including third party packages, especially if you're doing data science and require tools like Numpy, Pandas, and others. Building these third party libraries and installing them on your system is typically done with pip - the python package manager. Make sure that you have pip installed on your system, it will save you a lot of time and effort!

To install the requests.py Python library, a simple HTTP library that allows you to very easily fetch things from the web, you would simply run the following command:

$ pip install requests
Uninstalling and package management, including upgrading, are also included with the pip command. By using pip freeze you can also get a list of the third party Python packages you have installed on your system. To search for various libraries to use in your code, see the Python Package Index (PyPI).

Virtual Environments

As you start to develop more code, you'll start to find that specific versions of tools or tools that are hard to build and maintain are required for specific projects and that they conflict with versions of software in other projects. Even Python can be a problem if you develop for both Python 2 and 3 depending on your deployment environment! More worringly, Python is also a crucial aspect of many operating systems, the (small) possibility exists that you may end up breaking the system Python during development!

The solution to these problems is to use virtualenv to package a complete development environment with your code. Virtualenv allows you to create a directory that contains a project-specific version of Python, pip, and all third-party dependencies. The virtualenv can be activated and deactivated on the command line, allowing you to create a self-contained environment. Moreover, it can be used to create environments that match your production environment (typically a Linux server).

Virtualenvwrapper is another library that allows you to manage multiple virtual environments and associate them with specific projects. This tool will also quickly become essential to your workflow. To install virtualenv and virtualenvwrapper, use the following code:

$ pip install virtualenv virtualenvwrapper
Then edit your .profile in your home directory and add the following to the end:

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Projects
source /usr/local/bin/virtualenvwrapper.sh
All your virtual environments will be stored in a hidden directory called virtualenvs, and your project directory is where you would store your code. We'll discuss this more in the following section. I also alias many of the virtualenv scripts to make it easier to work with, you can see my extensions at Ben's VirtualEnv Cheat Sheet.

Note: Windows users may have to follow OS-specific instructions, which I would be happy to update and include in this post.

Code Construction Workflow

Creating and executing Python code follows two different workflow patterns.

Create code in a text file and execute it with Python
Create code in a text file and import it into the Python REPL.
Generally speaking, developers do both. Python programs are intended to be executed on the command line via the python binary, and the thing that is executed is usually an entry point to a much larger library of code that is imported. The difference between importing and execution is subtle, but as you do more Python it becomes more important.

With either of these workflows, you create your code in as modular a fashion as possible and, during the creation process, you execute it in one of the methods described above to check it's working. Most Python developers are back and forth between their terminal and the editor, and can do fine grained testing of every single line of code as they're writing it. This is the rapid prototyping aspect of Python.

So let's start with a simple example.

Open a terminal window (see your specific operating system for instructions on how to do this).

NOTE: Commands are in bash (Linux/Mac) or Windows Powershell

Create a workspace for yourself. A workspace, in this sense, is just an empty directory where you can get ready to start doing development work. You should probably also keep your various projects (here, a synonym for workspace) in their own directory as well, for now we'll just call it "Projects" and assume it is in your home directory. Our first project will be called "myproject", but you'd just name this whatever you'd like.

$ cd ~/Projects
$ mkdir myproject
$ cd myproject
Let's create our first Python script. You can either open your favorite editor and save the file into your workspace (the ~/Projects/myproject directory), or you can touch it and then open that file with your editor.

$ touch foo.py
PRO TIP: If you're using Sublime Text 3 and have the subl command line tool installed (See Sublime Text installation instructions), you can use the following command to open up the current directory in the editor:

$ subl . &
I use this so much that I've aliased the command to e.

So here's where you should be: You should have a text editor open and editing the file at ~/Projects/myproject/foo.py, and you should have a terminal window open whose current working directory is ~/Projects/myproject. You're now ready to develop. Add the following code to foo.py:

#!/usr/bin/env python

import csv

def dataset(path):
    with open(path, 'rU') as data:
        reader = csv.reader(data)
        for row in reader:
            row[2] = int(row[2])
            yield row
This code is very simple. It just implements a function that accepts a path and returns an iterator so that you can access every row of a CSV file, while also converting the third item in every row to an integer.

PRO TIP: The #! (pronounced "shebang") line must appear at the very beginning of an executable Python script with nothing before it. It will tell your computer that this is a Python file and execute the script correctly if run from the command line as a standalone app. This line doesn't need to appear in library modules, that is, Python code that you plan to import rather than execute.

Create some data so that we can use our function. Let's keep all of our data in a fixtures directory in our project.

$ mkdir fixtures
$ touch fixtures/calories.csv
Using your editor, add this data to the calories.csv file:

butter,tbsp,102
cheddar cheese,slice,113
whole milk,cup,148
hamburger,item,254
Ok, now it's time to use our code. First, let's try to execute the code in the interpreter. Open up the REPL as follows:

$ python
>>>
You should now be presented with the Python prompt (>>>). Anything you type in now should be in Python, not bash. Always note the prompts in the instructions. A prompt with $ means type in command line instructions (bash), a prompt that says >>> means type in Python on the REPL, and if there is no prompt, you're probably editing a file. Import your code:

>>> from foo import dataset
>>> for row in dataset('fixtures/calories.csv'):
...     print row[0]
butter
cheddar cheese
whole milk
hamburger
>>>
A lot happened here, so let's inspect it. First, when you imported the dataset function from foo, Python looked in your current working directory and found the foo.py file, and that's where it imported it from. Where you are on the command line and what your Python path is matters!

When you import the dataset function the way we did, the module is loaded and executed all at once and provided to the interpreter's namespace. You can now use it by writing a for loop to go through every row and print the first item. Note the ... prompt. This means that Python is expecting an indented block. To exit the block, hit enter twice. The print results appear right in the screen, and then you're returned to the prompt.

But what if you make a change in the code, for example, capitalizing the first letter of the words in first item of each row? The changes you write in your file won't show up in the REPL. This is because Python has already loaded the code once. To get the changes, you either have to exit the REPL and restart or you have to import in a different way:

>>> import foo
>>> for row in foo.dataset('fixtures/calories.csv'):
...
Now you can reload the foo module and get your code changes:

>>> reload(foo)
This can get pretty unwieldy as code gets larger and more changes happen, so let's shift our development strategy over to executing Python files. Inside foo.py, add the following to the end of the file:

if __name__ == '__main__':
    for row in dataset('fixtures/calories.csv'):
        print row[0]
To execute this code, you simply type the following on the command line:

$ python foo.py
butter
cheddar cheese
whole milk
hamburger
The if __name__ == '__main__': statement means that the code will only get executed if the code is run directly, not imported. In fact, if you open up the REPL and type in import foo, nothing will be printed to your screen. This is incredibly useful. It means that you can put test code inside your script as you're developing it without worrying that it will interfere with your project. Not only that, it documents to other developers how the code in that file should be used and provides a simple test to check to make sure that you're not creating errors.

In larger projects, you'll see that most developers put test and debugging code under so called "ifmain" statements at the bottom of their files. You should do this too!

With this example, hopefully you have learned the workflow for developing Python programs both by executing scripts and using "ifmain" as well as importing and reloading scripts in the REPL. Most developers use both methods interchangeably, using whatever is needed at the time.

Structuring Larger Projects

Ok, so how do you write an actual Python program and move from experimenting with short snippets of code to larger programs? The first thing you have to do is organize your code into a project. Unfortunately there is really nothing to do this for you automatically, but most developers follow a well known pattern that was introduce by Zed Shaw in his book Learn Python the Hard Way.

In order to create a new project, you'll implement the "Python project skeleton," a set of directories and files that belong in every single project you create. The project skeleton is very familiar to Python developers, and you'll quickly start to recognize it as you investigate the code of other Python developers (which you should be doing). The basic skeleton is implemented inside of a project directory, which are stored in your workspace as described above. The directory structure is as follows (for an example project called myproject):

$ myproject
.
├── README.md
├── LICENSE.txt
├── requirements.txt
├── setup.py
├── bin
|   └── myapp.py
├── docs
|   ├── _build
|   ├── conf.py
|   ├── index.rst
|   └── Makefile
├── fixtures
├── foo
|   └── __init__.py
└── tests
    └── __init__.py
This is a lot, but don't be intimidated. This structure implements many tools including packaging for distribution, documentation with Sphinx, testing, and more.

Let's go through the pieces one by one. Project documentation is the first part, implemented as README.md and LICENSE.txt files. The README file is a markdown document that you can add developer-specific documentation to your project. The LICENSE can be any open source license, or a Copyright statement in the case of proprietary code. Both of these files are typically generated for you if you create your project in Github. If you do create your file in Github, you should also use the Python .gitignore that Github provides, which helps keep your repositories clean.

The setup.py script is a Python setuptools or distutils installation script and will allow you to configure your project for deployment. It will use the requirements.txt to specify the third party dependencies required to implement your project. Other developers will also use these files to create their development environments.

The docs directory contains the Sphinx documentation generator, Python documentation is written in restructuredText, a Markup language similar to Markdown and others. This documentation should be more extensive and should be for both users and developers. The bin directory will contain any executable scripts you intend to build. Data scientists also typically also have a fixtures directory in which to store data files.

The foo and tests directories are actually Python modules since they contain the __init__.py file. You'll put your code in foo and your tests in tests. Once you start developing inside your foo directory, note that when you open up the REPL, you have to import everything from the 'foo' namespace. You can put import statements in your __init__.py files to make things easier to import as well. You can still also execute your scripts in the foo directory using the "ifmain" method.

Setting Up Your First Project

You don't have to manually create the structure above, many tools will help you build this environment. For example the Cookiecutter project will help you manage project templates and quickly build them. The spinx-quickstart command will generate your documentation directory. Github will add the README.md and LICENSE.txt stubs. Finally, pip freeze will generate the requirements.txt file.

Starting a Python project is a ritual, however, so I will take you through my process for starting one. Light a candle, roll up your sleeves, and get a coffee. It's time.

Inside of your Projects directory, create a directory for your workspace (project). Let's pretend that we're building a project that will generate a social network from emails, we'll call it "emailgraph."

$ mkdir ~/Projects/emailgraph
$ cd ~/Projects/emailgraph
Initialize your repository with Git.

$ git init
Initialize your virtualenv with virtualenv wrapper.

$ mkvirtualenv -a $(pwd) emailgraph
This will create the virtual environment in ~/.virtualenvs/emailgraph and automatically activate it for you. At any time and at any place on the command line, you can issue the workon emailgraph command and you'll be taken to your project directory (the -a flag specifies that this is the project directory for this virtualenv).

Create the various directories that you'll require:

(emailgraph)$ mkdir bin tests emailgraph docs fixtures
And then create the various files that are needed:

(emailgraph)$ touch tests/__init__.py
(emailgraph)$ touch emailgraph/__init__.py
(emailgraph)$ touch setup.py README.md LICENSE.txt .gitignore
(emailgraph)$ touch bin/emailgraph-admin.py
Generate the documentation using sphinx-quickstart:

(emailgraph)$ sphinx-quickstart
You can safely use the defaults, but make sure that you do accept the Makefile at the end to quickly and easily generate the documentation. This should create an index.rst and conf.py file in your docs directory.

Install nose and coverage to begin your test harness:

(emailgraph)$ pip install nose coverage
Open up the tests/__init__.py file with your favorite editor, and add the following initialization tests:

import unittest

class InitializationTests(unittest.TestCase):

    def test_initialization(self):
        """
        Check the test suite runs by affirming 2+2=4
        """
        self.assertEqual(2+2, 4)

    def test_import(self):
        """
        Ensure the test suite can import our module
        """
        try:
            import emailgraph
        except ImportError:
            self.fail("Was not able to import the emailgraph")
From your project directory, you can now run the test suite, with coverage as follows:

(emailgraph)$ nosetests -v --with-coverage --cover-package=emailgraph \
              --cover-inclusive --cover-erase tests
You should see two tests passing along with a 100% test coverage report.

Open up the setup.py file and add the following lines:

#!/usr/bin/env python
raise NotImplementedError("Setup not implemented yet.")
Setting up your app for deployment is the topic of another post, but this will alert other developers to the fact that you haven't gotten around to it yet.

Create the requirements.txt file using pip freeze:

(emailgraph)$ pip freeze > requirements.txt
Finally, commit all the work you've done to email graph to the repository.

(emailgraph)$ git add --all
(emailgraph)$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

    new file:   LICENSE.txt
    new file:   README.md
    new file:   bin/emailgraph-admin.py
    new file:   docs/Makefile
    new file:   docs/conf.py
    new file:   docs/index.rst
    new file:   emailgraph/__init__.py
    new file:   requirements.txt
    new file:   setup.py
    new file:   tests/__init__.py

(emailgraph)$ git commit -m "Initial repository setup"
With that you should have your project all setup and ready to go. Get some more coffee, it's time to start work!

Conclusion

With this post, hopefully you've discovered some best practices and workflows for Python development. Structuring both your code and projects this way will help keep you organized and will also help others quickly understand what you've built, which is critical when working on projects involving more than one person. More importantly, this project structure is the preparation for deployment and the base for larger applications and professional, production grade software. Whether you're scripting or writing apps, I hope that these workflows will be useful.

If you'd like to explore further how to include professional grade tools into your Python development, check out some of the following tools:

Travis-CI is a continuing integration service that will automatically run your test harness when you commit to Github. It will make sure that all of your tests are passing before you push to production!
Waffle.io will turn your Github issues into a full Agile board allowing you to track milestones and sprints, and better coordinate your team.
Pylint will automatically check for good coding standards, error detection, and even draw UML diagrams for your code!
District Data Labs also regularly holds a Building Data Apps with Python workshop. If you're interested in learning more about data products and how to build them with Python, you should definitely consider attending. For more information about that and to see when it is being offered next, check out the course page.

Additional Reading

Learn Python the Hard Way
Learning Python, 5th Edition
Programming Python
Practical Data Science Cookbook

https://districtdatalabs.silvrback.com/how-to-develop-quality-python-code
