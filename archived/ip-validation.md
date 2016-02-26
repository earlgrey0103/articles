#Codewars编程套路练习：验证IPv4地址

## 问题描述
设计一个算法，判断点分十进制格式的IPv4地址是否符合协议要求。函数的输入限制为一个字符串。

合理的输入：1.2.3.4 123.45.67.89

不合理的输入：1.2.3 1.2.3.4.5 123.456.78.90 123.045.067.089

### 问题标签
算法、正则表达式、高级语言特性、基础知识、字符串、声明式编程（Declarative Programming）

### 函数命名
	:::python
	def is_valid_IP(strng):
	    return None

### 测试用例
	:::python
	Test.assert_equals(is_valid_IP('12.255.56.1'),     True)
	Test.assert_equals(is_valid_IP(''),                False)
	Test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
	Test.assert_equals(is_valid_IP('123.456.789.0'),   False)
	Test.assert_equals(is_valid_IP('12.34.56'),        False)
	Test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
	Test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
	Test.assert_equals(is_valid_IP('123.045.067.089'), False)

### 原文链接
http://www.codewars.com/kata/ip-validation/python

## 编程派解法
	:::python
	def is_valid_IP(s):
	    a = s.split('.')
	    if len(a) != 4:
	        return False
	    for x in a:
	        if not x.isdigit() or x.startswith('0'):
	            return False
	        i = int(x)
	        if i < 0 or i > 255:
	            return False
	    return True

## 网友解法摘录
**网友cwhy**：获得最佳实践推荐12次

	:::python
	def is_valid_IP(strng):
	    lst = strng.split('.')
	    passed = 0
	    for sect in lst:
	        if sect.isdigit():
	            if sect[0] != '0':
	                if 0 < int(sect) <= 255:
	                    passed += 1
	    return passed == 4

**网友saurus**：使用正则表达式

	:::python
	import re
	def is_valid_IP(strng):
	    return re.match('\.'.join(['(\d|1?\d\d|2[0-4]\d|25[0-5])']*4) + '$', strng) is not None

**网友pacofvf**：超长一行流

	:::python
	import re
	def is_valid_IP(address):
	    return bool(re.match("^([1][0-9][0-9]\.|^[2][5][0-5].|^[2][0-4][0-9]\.|^[1][0-9][0-9]\.|^[0-9][0-9]\.|^[0-9]\.)([1][0-9][0-9]\.|[2][5][0-5]\.|[2][0-4][0-9]\.|[1][0-9][0-9]\.|[0-9][0-9]\.|[0-9]\.)([1][0-9][0-9]\.|[2][5][0-5]\.|[2][0-4][0-9]\.|[1][0-9][0-9]\.|[0-9][0-9]\.|[0-9]\.)([1][0-9][0-9]|[2][5][0-5]|[2][0-4][0-9]|[1][0-9][0-9]|[0-9][0-9]|[0-9])$",address))

**网友natict**：更简单的一行流

	:::python
	def is_valid_IP(s):
	    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))

## 下一个
http://www.codewars.com/kata/5262119038c0985a5b00029f