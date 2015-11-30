What is a correct term for the following piece of Python syntax: 3 + 4
下面这个Python代码的正确术语是什么：3 + 4
- 表达式（expression）  1
- 闭包（closure）
- lambda
- 代码块（suite）
- 语句（statement）


PEP的全称是什么？
- Particularly Egregious Practices
- Python Echoes Python
- Python Enhancement Proposal
- Python Engagement Pattern


下面这行Python代码在解释器中的输出结果是什么？
lang = list('Python') ; lang[:-4]

- ['t', 'h', 'o', 'n']
- ['P', 'y', 't', 'h']
- ['o', 'n']
- ['P', 'y'] 1

下面哪一项不是网络服务器与Python程序之间的交互接口？
- fcgi
- wsgi
- cgi
- webcat 1


Python可以通过哪种方式与C语言代码进行交互？
- Python C/API
- ctypes
- 全部选项 1
- Cython

What will an octal number and hexadecimal number start with?
Python中八进制和十六进制数字以什么开头？
- 任意数字
- Python中没有八进制数字
- 0  1
- 标识（+或-）

3/2的结果是什么？
- 1
- 要看使用哪个版本的Python
- 1.5


Is it possible to check for more than one error in one except line?
一个except语句中能否检查多个错误？
- 可以，但是异常类型要包含在花括号中
- 可以，但是异常类型要包含在方括号中
- 不可以
- 可以，但是异常类型要包含在括号中 1

In a Python 2 new-style class declared as "Child(Base)", what is the correct way for a method "foo()" to call its base implementation?
在Python 2中，我们按照新的 要求声明了一个“Child(Base)”类，下列哪种是调用父类中“foo()”方法的正确方式？
- super(Child).frob()
- Child.frob(self)
- super(Base, self).foo()
- super(Child, self).foo() 1
- Child.frob(super)

What type of error does "type('1') is int" return?
“type('1') is int”会返回什么类型的错误？
- SyntaxError
- NameError
- None; 返回结果为False 1
- None; 返回结果为True
- TypeError


Is it possible to link a Python program to code written in C?
Yes, but the C code must be provided in a form of a dynamically linked library.
No, it is impossible.
Yes; the C code can be in a form of a dynamically or a statically linked library. 1
Yes, but C code must be provided in a form of statically linked library.


How can one convert [1,2,3] to '1 - 2 - 3' ?
' - '.join([1,2,3])
merge([1,2,3], ' - ')
[1, 2, 3].merge()
' - '.merge([1,2,3])
TypeError 1


What data type is the following: (1, 2, 3) ?
Map.
Tuple.
Set.
Counter.
List.

Given the following assignment: s = ('xxx', 'abcxxxabc', 'xyx', 'abc', 'x.x', 'axa', 'axxxxa', 'axxya'), what is the result of the expression filter ((lambda s: re.search(r'xxx', s)), s)?
('x.x')
('xxx')
('xxx', 'abcxxxabc', 'axxxxa')
This expression will result in a syntax error.


How would you check if the file 'myFile.txt' exists?
os.path.exists("myFile.txt") 1
os.exists("myFile.txt")
file_exists("myFile.txt")
path_exists("myFile.txt")

Which of the following is true about (1,2,3,)
It is an invalid expression
It represents an immutable object 1
It is equivalent to [1,2,3,]
It is equivalent to 1,2,3


Which of these structures cannot contain duplicates?
A Sequence
A List
A Tuple
A Set 1 

If somewhere in a script is the statement f.close(), which of the following may have come before it?
none are correct
f=open("tmp.tmp") 1
f.open("tmp.tmp")
open("tmp.tmp")

Which of the following is a valid class declaration?
class NameClass(self, var1, var2): self.var1 = var1 self.var2 = var2
class NameClass(object): def __init__(self, var1, var2): self.var1 = var1 self.var2 = var2  1
class NameClass(var1, var2): self.var1 = var1 self.var2 = var2
class NameClass(object): def __init__(var1, var2): self.var1 = var1 self.var2 = var2
class NameClass(object): def __init__(var1, var2): this.var1 = var1 this.var2 = var2


What does the spawn family of functions do?
These functions allow a Python program to stop the current process.
These functions allow a Python program to stop another process.
There are no such functions in Python.
These functions allow a Python program to start another process. 1 

Suppose a= [1,2,3]. What will be the value of 'a' after executing this command, a=a*3  ?
[3,6,9]
[1,2,3,1,2,3,1,2,3] 1
None
Lists are Immutable. So, this will result in an error message.

