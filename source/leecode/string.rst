字符串部分
================

首先从字符串部分开始刷，每刷一题都会记录当时的想法以及用两种脚本语言写出结果。

.. attention::

        因为也是第一次开始干这个事情，很多地方都是需要改进的。慢慢来吧

157. Read N Characters Given Read4 I
-------------------------------

The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
Note:
The read function will only be called once for each test case.


首先让我们先把题目看清楚，题目问的是读取一个文件里面的内容，算出总共有多少个字符。简单点来说就是给你一个字符串，有一个函数叫做read4，读n个char到指定的buf去。那么就需要一个char*4的临时buf来储存一次读出来的结果，然后再把这个结果按要求赋给指定的buf，如果比4小的话，就说明字符串快要读完，数字就代表剩下的几个。特么想不通为什么一开始搞一个(char *buf)，让有的人看了一脸懵逼好么。


这道题木有搞明白

158. Read N Characters Given Read4 II - Call multiple times
------------------------------------------------------

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.


.. important::

        这道题目跟上面一样没有搞明白


28. Implement strStr()
----------------------

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

还没来得及仔细看答案
https://www.youtube.com/watch?v=GTJr8OvyEVQ



557. Reverse Words in a String III
----------------------------------

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
::
        Input: "Let's take LeetCode contest"
        Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.


这道题目的理解还是非常简单

JavaScript答案 ::

        var hello = "Let's take LeetCode contest".split(' ').map(s => s.split().reverse().join()).join(' ')
        console.log(hello)


551. Student Attendance Record I
--------------------------------

You are given a string representing an attendance record for a student. The record only contains the following three characters:
::
        'A' : Absent.
        'L' : Late.
        'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
::
        Input: "PPALLP"
        Output: True
Example 2:
::
        Input: "PPALLL"
        Output: False
