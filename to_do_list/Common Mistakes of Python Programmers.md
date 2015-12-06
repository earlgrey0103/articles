> http://www.onlamp.com/pub/a/python/2004/02/05/learn_python.html
> 作者是Mark Luz，为《Learning Python》一书的合著者之一。

在本文中，我将介绍初级和资深Python程序员都会犯的一些最常见错误，希望大家在以后的工作中能够尽量避免。

In this article, I will chronicle some of the most common mistakes made by both new and veteran Python programmers, to help you avoid them in your own work.

首先，我必须要声明的是，这些错误都是来自一手经验的总结。而我也是一名职业Python培训教师。在过去7年中，我有幸教导过100多个Python学习班，学生超过1000名。在教学过程中，我看到他们中的大部分人都犯过相同的错误。也就是说，有一些错误在Python初学者中甚至出现过数百次。实际上，其中一些错误特别常见，以至于基本上每一名Python初学者在刚开始学习的时候，都是必定会犯的。

First of all, I should explain that these come straight from first-hand experience. I earn my living as a Python trainer. Over the last seven years, I've had the privilege of teaching over 100 Python classes, to over 1,000 students -- and have watched most of them make the same mistakes. That is, these are things that I've seen real Python beginners do, hundreds of times. In fact, some are so common they are virtually guaranteed to crop up when you are first starting out.

“到底是什么样的错误？”你会问。“还会犯许多这样的错误码？”答案是肯定的。Python虽然可能是最简单、最灵活的编程语言之一，但是它到底是一门编程语言。它还是有语法、数据类型等难点，还有一些特别难懂的地方。

"What's that?" you say. "You can make lots of mistakes in Python, too?" Well, yes. Python may be one of the simplest and most flexible programming languages out there, but it is still a programming language. It still has syntax, datatypes, and the occasional dark corner inhabited by sorcerers named Tim.

好消息是，一旦你学会了Python，那么这门语言的简洁设计就自然能够帮你避免许多陷阱。Python各个组件之间所需要的交互式最少的，这大大减少了bug的出现。它的语法也简单，意味着犯错误的机会就少。另外，就算你犯了语法错误，Python运行时的错误检查机制会向你报告问题的所在，帮助你快速修复问题。


The good news is that once you learn Python, many pitfalls are avoided naturally, thanks to the clean design of the language. Python has a minimal set of interactions between its components, which helps reduce bugs. It also has a simple syntax, which means there is less opportunity to make mistakes in the first place. And when you do make a mistake, Python's runtime error detection and reporting helps you recover quickly.

但这不并不说Python编程就能够自动化了，在这里提前警醒你就是让你提前做准备。那么接下来，我们就开发介绍把。下文将分为三个部分，分别对应三类错误，包括语用错误（pragmatic mistake）、编码错误（coding mistake）和编程错误（programming mistake）。

But programming Python still isn't quite an automatic task, and forewarned is forearmed. So without further delay, let's jump into the nitty-gritty. The next three sections group mistakes into pragmatics, coding, and programming at large. If you'd like to read more about common Python mistakes and how to avoid them, all of these and more are described further in the new O'Reilly book, Learning Python, 2nd Edition.

## 语用错误

Pragmatic Mistakes

我们首先从基础知识开始；也就是刚开始学习编程的人经常会搞混的内容，甚至是学习语法之前的内容。如果你已经有一定的编程经验，那么接下来的大部分概念在你看起来会非常简单。如果你曾经向新手教过怎么编程，那情况就不一样了。

Let's start out with the basics; things that people who are just learning how to program tend to get tripped up on, even before they delve into syntax. If you've already done a bit of programming, most of these may seem very simple; if you've ever tried to teach programming to novices, they probably won't.

### 通过交互式命令行输入Python代码

Type Python Code at the Interactive Prompt

你只能在`>>>`交互式提示符之后输入Python代码，不能输入系统命令。我经常碰到很多人在提示符后面输入`emacs`、`ls`或`edit`等系统命令，不过可惜它们并不是Python代码。通过Python代码，我们确实可以运行系统命令（例如，通过`os.system`和`os.popen`），但这和直接在提示符后输入这些命令还是有不同的。如果你想从交互式提示符中打开一个Python文件，请使用`import`，而不是系统命令`python file.py`。

You can type only Python code, and not system commands, at the >>> interactive prompt. It's not that uncommon to see people enter emacs, ls, or edit commands at this prompt, but they are not Python code. There are ways to run system commands from within Python code (for example, os.system and os.popen), but they are not as direct as simply typing the command itself. If you want to launch a Python file from the interactive prompt, use import file, not the system command python file.py.

### 只有在Python文件中才需要print语句打印内容

Print Statements are Required in Files (Only)

由于交互式解释器会自动打印表达式的结果，你并不需要完整地输入print语句。这是一个很好地功能，但是要记住在代码文件中，你一般必须要使用print语句才能看到输出结果。

Because the interactive interpreter automatically prints the results of expressions, you do not need to type complete print statements interactively. This is a nice feature, but remember that within a code file, you generally must use print statements to see output.

### 当心Windows平台自动添加的文件扩展名

Beware of Automatic Extensions on Windows

如果你在Windows平台使用记事本程序来编写程序文件的话，那么在保存文件的时候要注意选择所有文件，然后明确地添加.py的文件名后缀。否则的话，记事本会将你的文件以.txt扩展名保存，这样就很难直接运行了。更糟糕的是，Word和Wordpad中默认的格式符也不是合法的Python字符。因此，在Windows平台上要谨记保存文件时选择所有文件，然后保存为文本文件，或是使用更适合编程的文本编辑器，例如IDLE。使用IDLE保存文件的时候，也要记得手动输入.py文件扩展名。

If you use the Notepad program to code program files on Windows, be careful to pick type All Files when it comes time to save your file, and give your file a .py suffix explicitly. Otherwise, Notepad saves your file with a .txt extension, making it difficult to run in some launching schemes. Worse, Word and WordPad add formatting characters by default that are not legal Python syntax. As a rule of thumb, always pick All Files and save as simple text on Windows, or use more programmer-friendly text editors such as IDLE. In IDLE, remember to type .py file extensions manually when saving.

### Windows平台上双击程序文件图标的陷阱

Program-File Icon Click Pitfalls on Windows

在Windows平台，你可以通过双击文件的方式打开一个Python程序文件，但这样很容易出现错误。首先，程序的输出窗口在程序一结束的时候就会消息；要保持窗口不关闭，可以在程序文件的最后添加`raw_input()`。另外，还要记住：如果程序措辞，窗口也会消失；要想查看错误信息，就用通过其他方式运行程序——包括在系统命令行执行，通过交互式解释器执行等方法。

On Windows, you can launch a Python program file by clicking on it, but this can be error-prone. First of all, the program's output window disappears as soon as the program finishes; to keep it open, try adding a raw_input() call at the bottom of the file. Also, keep in mind that the output window goes away if there is a program error; to see your error messages, run your program in other ways--from a system command line, by interactive imports, with IDLE menu options, and so on.

### 相同的`import`语句只会执行一次

Imports Only Work the First Time

你可以在交互式命令行引用一个文件（import），这可以运行该文件，但每次会话中该命令只有在第一次输入时有效；之后的import语句只会返回已经加载的模块。如果要强制Python重载、重新运行文件的代码，可以调用`reload(module)`函数。

You can run a file by importing it at the interactive prompt, but this only works once per session; subsequent imports simply return the already-loaded module. To force Python to reload and rerun a file's code, call the reload(module) function instead. And while you're at it, be sure to use parentheses for reload, but not import.

### 交互式解释器中的空行也是有作用的

Blank Lines Matter at the Interactive Prompt (Only)
在模块文件中，空行和注释行都会被忽略，但是在交互式解释器中输入代码时，空行则表示结束一个复合语句。换句话说，空行告知交互式解释器你已经输入完了一个符合语句。相反，你也会希望在交互式编码时，使用空行来结束一个符合语句，这样才能开始编写新的语句——交互式解释器一次只能执行一个语句。

Blank lines and comment lines are always ignored everywhere in module files, but a blank line ends a compound statement when typing code at the interactive prompt. In other words, a blank line tells the interactive prompt that you've finished a compound statement; don't hit the Enter key on a line by itself until you're really done. Conversely, you really do want to type a blank line to terminate the compound statement interactively, before starting a new statement--the interactive prompt runs one statement at a time.

## 编码错误
Coding Mistakes

一旦你开始急切地想要编写Python代码，接下来的陷阱将会变得更加危险——这些基本的编码错误遍及所有的语言特性，经常会出现在不太小心的程序员身上。

Once you start writing Python code in earnest, the next batch of pitfalls starts becoming more dangerous -- these are basic coding mistakes that span language features, and often snare the unwitting programmer.

### 别忘记冒号

Don't Forget the Colons

这是初学者在编码时最常犯的一个错误：忘记在复合语句的首行（if、while和for语句的第一行）末尾加上冒号（:）。你一开始很可能会记得加上冒号，但慢慢地你下意识地就会忘记。基本上，75%的学生或早或晚都出现过这个错误。

This is easily the most common beginner's coding mistake: don't forget to type a : at the end of compound statement headers (the first line of an if, while, for, etc.). You probably will at first anyhow, but it will soon become an unconscious habit. Typically, 75 percent of students in classes have been burned by this one by the end of the day.

### 初始化变量
Initialize Your Variables

在Python语言中，你在给一个变量赋值之前无法在表达式中使用该变量。这是故意这么设计的：有助于避免常见的打字错误，以及如何确定一个变量的默认值应该是什么（0, None，""还是[]？）。请记住将计数器的值初始化为0，列表累加器初始化为[]，等等。

In Python, you cannot use a name within an expression until it has been assigned a value. This is on purpose: it helps to prevent common typo mistakes, and avoids the ambiguous question of what an automatic default should be (0, None, "", [], ?). Remember to initialize counters to 0, list accumulators to [], and so on.

### Start in Column 1

Be sure to start top-level, unnested code all the way to the left, in column 1. That includes unnested code typed into module files, as well as unnested code typed at the interactive prompt. Python uses indentation to delimit blocks of nested code, so white space to the left of your code means a nested block. White space is generally ignored everywhere, except for indentation.

Indent Consistently
Avoid mixing tabs and spaces in the indentation of a given single block, unless you know what every system that touches your code may do with tabs. Otherwise, what you see in your editor may not be what Python sees when it counts tabs as a number of spaces. It's safer to use all tabs or all spaces for each block; how many is up to you.

Always Use Parentheses to Call a Function
You must add parentheses after a function name to call it, whether it takes arguments or not. That is, use function(), not function. Python functions are simply objects that have a special operation, a call, that you trigger with the parentheses. Like all objects, they can also be assigned to variables, and used indirectly: x = function; x().

In Python training, this seems to occur most often with files. It's common to see beginners type file.close to close a file, rather than file.close(); because it's legal to reference a function without calling it, the first version without parenthesis succeeds silently, but does not close the file!

Don't Use Extensions or Paths in Imports
Use directory paths and file extensions in system command lines (e.g., python dir/mod.py), but not in import statements. That is, say import mod, not import mod.py or import dir/mod.py. In practice, this is probably the second most common beginner mistake. Because modules may have other suffixes besides .py (.pyc, for instance), hardcoding a particular suffix is not only illegal syntax, it doesn't make sense.

Platform-specific directory-path syntax comes from your module search path settings, not the import statement. You can use dots in filenames to refer to package subdirectories (e.g., import dir1.dir2.mod), but the leftmost directory still must be found via the module search path, and no other path syntax can appear in imports. The incorrect statement import mod.py is assumed by Python to be a package import--it imports the module mod, and then tries to find a module named py within a directory named mod, and winds up generating a potentially confusing error message.

Don't Code C in Python
A few reminders for C/C++ programmers new to Python:

You don't need to type parentheses around tests in if and while headers (e.g., if (X==1):). You can, if you like, since any expression can be enclosed in parentheses, but they are fully superfluous in this context.

Don't terminate all of your statements with a semicolon. It's technically legal to do this in Python, but is totally useless unless you're placing more than one statement on a single line (e.g., x=1; y=2; z=3).

Don't embed assignment statements in while loop tests (e.g., while ((x=next() != NULL)). In Python, statements cannot appear where expressions are expected, and an assignment is not an expression.

Programming Mistakes

Finally, here are some of the problems you may come across when you start working with the larger features of the Python language -- datatypes, functions, modules, classes, and the like. Because of space constraints, this section is abbreviated, especially with respect to advanced programming concepts; for the rest of the story, see the tips and "gotchas" sections of Learning Python, 2nd Edition.



File-Open Calls Do Not Use the Module Search Path
When you use the open() call in Python to access an external file, Python does not use the module search path to locate the target file. It uses an absolute path you give, or assumes the filename is relative to the current working directory. The module search path is consulted only for module imports.

Methods Are Specific to Types
You can't use list methods on strings, and vice versa. In general, methods calls are type- specific, but built-in functions may work on many types. For instance, the list reverse method only works on lists, but the len function works on any object with a length.

Immutable Types Can't Be Changed in Place
Remember that you can't change an immutable object (e.g., tuple, string) in place:

T = (1, 2, 3)
T[2] = 4          # Error
Construct a new object with slicing, concatenation, and so on, and assign it back to the original variable if needed. Because Python automatically reclaims unused memory, this is not as wasteful as it may seem:

T = T[:2] + (4,)  # Okay: T becomes (1, 2, 4)
Use Simple for Loops Instead of while or range
When you need to step over all items in a sequence object from left to right, a simple for loop (e.g., for x in seq:) is simpler to code, and usually quicker to run, than a while- or range-based counter loop. Avoid the temptation to use range in a for unless you really have to; let Python handle the indexing for you. All three of the following loops work, but the first is usually better; in Python, simple is good.

S = "lumberjack"

for c in S: print c                   # simplest

for i in range(len(S)): print S[i]    # too much

i = 0                                 # too much
while i < len(S): print S[i]; i += 1
Don't Expect Results From Functions That Change Objects
In-place change operations such as the list.append( ) and list.sort( ) methods modify an object, but do not return the object that was modified (they return None); call them without assigning the result. It's not uncommon for beginners to say something like:

mylist = mylist.append(X)
to try to get the result of an append; instead, this assigns mylist to None, rather than the modified list. A more devious example of this pops up when trying to step through dictionary items in sorted-key fashion:

D = {...}
for k in D.keys().sort(): print D[k]
This almost works -- the keys method builds a keys list, and the sort method orders it -- but since the sort method returns None, the loop fails because it is ultimately a loop over None (a nonsequence). To code this correctly, split the method calls out into statements:

Ks = D.keys()
Ks.sort()
for k in Ks: print D[k]
Conversions Only Happen Among Number Types
In Python, an expression like 123 + 3.145 works -- it automatically converts the integer to a floating point, and uses floating point math. On the other hand, the following fails:

S = "42"
I = 1
X = S + I        # A type error
This is also on purpose, because it is ambiguous: should the string be converted to a number (for addition), or the number to a string (for concatenation)?. In Python, we say that explicit is better than implicit (that is, EIBTI), so you must convert manually:

X = int(S) + I   # Do addition: 43
X = S + str(I)   # Do concatenation: "421" 
Cyclic Datastructures Can Cause Loops
Although fairly rare in practice, if a collection object contains a reference to itself, it's called a cyclic object. Python prints a [...] whenever it detects a cycle in the object, rather than getting stuck in an infinite loop:

>>> L = ['grail']  # Append reference back to L
>>> L.append(L)    # Generates cycle in object
>>> L
['grail', [...]]
Besides understanding that the three dots represent a cycle in the object, this case is worth knowing about because cyclic structures may cause code of your own to fall into unexpected loops if you don't anticipate them. If needed, keep a list or dictionary of items already visited, and check it to know if you have reached a cycle.

Assignment Creates References, Not Copies
This is a core Python concept, which can cause problems when its behavior isn't expected. In the following example, the list object assigned to the name L is referenced both from L and from inside of the list assigned to name M. Changing L in place changes what M references, too, because there are two references to the same object:

>>> L = [1, 2, 3]        # A shared list object
>>> M = ['X', L, 'Y']    # Embed a reference to L
>>> M
['X', [1, 2, 3], 'Y']

>>> L[1] = 0             # Changes M too
>>> M
['X', [1, 0, 3], 'Y']
This effect usually becomes important only in larger programs, and shared references are normally exactly what you want. If they're not, you can avoid sharing objects by copying them explicitly; for lists, you can make a top-level copy by using an empty-limits slice:

>>> L = [1, 2, 3]
>>> M = ['X', L[:], 'Y']   # Embed a copy of L

>>> L[1] = 0               # Change only L, not M
>>> L
[1, 0, 3]
>>> M
['X', [1, 2, 3], 'Y']
Slice limits default to 0 and the length of the sequence being sliced. If both are omitted, the slice extracts every item in the sequence, and so makes a top-level copy (a new, unshared object). For dictionaries, use the dict.copy() method.

Local Names Are Detected Statically
Python classifies names assigned in a function as locals by default; they live in the function's scope and exist only while the function is running. Technically, Python detects locals statically, when it compiles the defs code, rather than by noticing assignments as they happen at runtime. This can also lead to confusion if it's not understood. For example, watch what happens if you add an assignment to a variable after a reference:

>>> X = 99
>>> def func():
...     print X      # Does not yet exist
...     X = 88       # Makes X local in entire def
... 
>>> func( )          # Error!
You get an undefined name error, but the reason is subtle. While compiling this code, Python sees the assignment to X and decides that X will be a local name everywhere in the function. But later, when the function is actually run, the assignment hasn't yet happened when the print executes, so Python raises an undefined name error.

Really, the previous example is ambiguous: did you mean to print the global X and then create a local X, or is this a genuine programming error? If you really mean to print global X, you need to declare it in a global statement, or reference it through the enclosing module name.

Defaults and Mutable Objects
Default argument values are evaluated and saved once, when the def statement is run, not each time the function is called. That's usually what you want, but since defaults retain the same object between calls, you have to be mindful about changing mutable defaults. For instance, the following function uses an empty list as a default value and then changes it in place each time the function is called:

>>> def saver(x=[]):   # Saves away a list object
...     x.append(1)    # and changes it each time
...     print x
...
>>> saver([2])         # Default not used
[2, 1]
>>> saver()            # Default used
[1]
>>> saver()            # Grows on each call!
[1, 1]
>>> saver()
[1, 1, 1]
Some see this behavior as a feature -- because mutable default arguments retain their state between function calls, they can serve some of the same roles as static local function variables in the C language. However, this can seem odd the first time you run into it, and there are simpler ways to retain state between calls in Python (e.g., classes).

To avoid this behavior, make copies of the default at the start of the function body with slices or methods, or move the default value expression into the function body; as long as the value resides in code that runs each time the function is called, you'll get a new object each time:

>>> def saver(x=None):
...     if x is None: x = []   # No arg passed?
...     x.append(1)            # Changes new list
...     print x
...
>>> saver([2])                 # Default not used
[2, 1]
>>> saver()                    # Doesn't grow now
[1]
>>> saver()
[1]
Other Common Programming Traps
Here's a quick survey of other pitfalls we don't have space to cover in detail:

Statement order matters at the top level of a file: because running or importing a file runs its statements from top to bottom, make sure you put unnested calls to functions or classes below the definition of the function or class.

reload doesn't impact names copied with from: reload works much better with the import statement. If you use from statements, remember to rerun the from after the reload, or you'll still have old names.

The order of mixing matters in multiple inheritance: because superclasses are searched left to right, according to the order in the class header line, the leftmost class wins if the same name appears in multiple superclasses.

Empty except clauses in try statements may catch more than you expect. An except clause in a try that names no exception catches every exception -- even things like genuine programming errors, and the sys.exit() call.

Bunnies can be more dangerous than they seem.

Mark Lutz is the world leader in Python training, the author of Python's earliest and best-selling texts, and a pioneering figure in the Python community since 1992.