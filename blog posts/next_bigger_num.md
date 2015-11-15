# Codewars编码套路练习：给定一个正整数，找到由相同数字组成的下一个更大的整数

## 问题描述 

在Codewars对套路练习的分类中，这是一个难度为4的题目。难度数字越低，代表越困难。完成之后得到的积分，就越高。

你得编写一个函数，接受一个正整数作为输入，然后输出由相同数字组成的下一个更大的数：

    next_bigger(12)==21
    next_bigger(513)==531
    next_bigger(2017)==2071

如果找不到由相同数字组成的更大整数，则返回-1：

    next_bigger(9)==-1
    next_bigger(111)==-1
    next_bigger(531)==-1

### 测试用例
    
    Test.assert_equals(next_bigger(12),21)
    Test.assert_equals(next_bigger(513),531)
    Test.assert_equals(next_bigger(2017),2071)
    Test.assert_equals(next_bigger(414),441)
    Test.assert_equals(next_bigger(144),414)
    
### 问题标签
算法 数字 字符串 整型数

### 问题链接

http://www.codewars.com/kata/55983863da40caa2c900004e/train/python

## 问题解答

### 解题思路

一开始，我曾经想的很简单，计划把全部数字的排列组合都算出来并按顺序排列在列表中，然后找到给定数字在列表中的索引值。如果索引值为列表的最后一位，则返回-1；如果不是，则返回更大一个索引位置的值。

看上去思路很简单，但是实现起来的效率很差。首先，随着数字变大，进行初步排列的时间会很长，因为会有很多种排列方法；其次，在排列过程中，可能需要较大的内存空间来保存过程中生成的列表。最后的两步操作的效率倒是还好。

综合上面的考虑，没有继续按照这种思路实现。

最后，经过尝试和思考，我找到了如下的思路：

首先，找到给定数字中，从右至左没有按从大到小顺序排列的一段数字。假如给定数字式987685432，那么没有按顺序排列的一段数字就是，685432。

然后，对找到的这段数字重新排列。先把给定数字变成两个列表，[9,8,7]与[6,8,5,4,3,2]，然后对后面列表中的这些数字，取比6大一位的数字，即8。最后，把除8以外的数字，按从小到大得顺序重新排列。

最后，再把重排后的列表，与没有变动的列表相加，组成最后的数字。


### 编程派的解法

具体实现如下：

    def next_bigger(n):
        to_list = list(int(i) for i in str(n))
        length = len(to_list)
        if length == 1:
            return -1
    
        i = -1
        while to_list[i] <= to_list[i - 1]:
            i -= 1
            if i == -length:
                return -1
    
        process_list = to_list[i - 1:]
        replace = 0
    
        for num in sorted(process_list):
            if num > process_list[0]:
                replace = num
                break
    
        process_list.remove(replace)
    
        result = to_list[:i - 1] + [replace] + sorted(process_list)
    
        return int(''.join(str(i) for i in result))

### 网友解法摘录
目前在Codewars.com，完成这道题目的网友只有389人。

**网友pavel.koshev**：得到三个最佳实践投票

    def next_bigger(n):
      n = str(n)[::-1]
      try:
        i = min(i+1 for i in range(len(n[:-1])) if n[i] > n[i+1])
        j = n[:i].index(min([a for a in n[:i] if a > n[i]]))
        return int(n[i+1::][::-1]+n[j]+''.join(sorted(n[j+1:i+1]+n[:j]))) 
      except:
        return -1

**网友adam-tokarski**
    
    def next_bigger(n):
        i, ss = n, sorted(str(n))
    
        if str(n) == ''.join(sorted(str(n))[::-1]):
            return -1;
    
        while True:
            i += 1;
            if sorted(str(i)) == ss and i != n:
                return i;