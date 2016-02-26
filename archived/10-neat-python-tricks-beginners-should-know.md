# 初学者应该了解的10个Python技巧

## 技巧1

字符串倒置

	>>> a =  "codementor"
	>>> print "Reverse is",a[::-1]

倒置之后的结果是“rotnemedoc”。

## 技巧2

转置矩阵（transposing a matrix）(译者注：把矩阵A的行换成相应的列，得到的新矩阵称为A的转置矩阵)

	>>> mat = [[1, 2, 3], [4, 5, 6]]
	>>> zip(*mat)
	[(1, 4), (2, 5), (3, 6)]

## 技巧3

`a = [1,2,3]`

将上述列表中的三个值分别存储在3个新变量中。

	>>> a = [1, 2, 3]
	>>> x, y, z = a 
	>>> x
	1
	>>> y
	2
	>>> z
	3

## 技巧4

`a = ["Code", "mentor", "Python", "Developer"] `

利用上述列表中的所有元素，创建一个字符串。

	>>> print " ".join(a)
	Code mentor Python Developer

## 技巧5

```
list1 = ['a', 'b', 'c', 'd']

list2 = ['p', 'q', 'r', 's']
```

编写可以打印出下面结果的代码

```
ap

bq

cr

ds
```

	>>> for x, y in zip(list1,list2):
	...    print x, y
	...
	a p
	b q
	c r
	d s

## 技巧6

一行代码交换两个变量的值

	>>> a=7
	>>> b=5
	>>> b, a =a, b
	>>> a
	5
	>>> b
	7

## 技巧7

不使用循环打印出“codecodecodecode mentormentormentormentormentor”

	>>> print "code"*4+' '+"mentor"*5
	codecodecodecode mentormentormentormentormentor

## 技巧8

`a = [[1, 2], [3, 4], [5, 6]]`

不使用任何循环，将上面的嵌套列表转换成单一列表（即组成元素不是列表）

输出结果应为: [1, 2, 3, 4, 5, 6]

	>>> import itertools 
	>>> list(itertools.chain.from_iterable(a))
	[1, 2, 3, 4, 5, 6]

## 技巧9

判断两个单词是否是回文单词（anagram）？

	def is_anagram(word1, word2):
	    """Checks whether the words are anagrams.
	    word1: string
	    word2: string
	    returns: boolean
	    """

完成上面的函数

	from collections import Counter
	def is_anagram(str1, str2):
	     return Counter(str1) == Counter(str2)
	>>> is_anagram('abcd','dbca')
	True
	>>> is_anagram('abcd','dbaa')
	False

## 技巧10

接受手动输入字符串，并返回一个列表。

例如，输入“1 2 3 4”，需要返回的列表是[1, 2, 3, 4]。

记住，返回列表中的元素是整型数。代码不要超过一行。

	>>> result = map(lambda x:int(x) ,raw_input().split())
	1 2 3 4
	>>> result
	[1, 2, 3, 4]
