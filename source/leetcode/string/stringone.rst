题目序号 
============================================================


157. Read N Characters Given Read4 I
------------------------------------

#. The API: int read4(char *buf) reads 4 characters at a time from a file.
#. The return value is the actual number of characters read. 
#. For example, it returns 3 if there is only 3 characters left in the file.
#. By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.


Note:
The read function will only be called once for each test case.

.. note::

    首先让我们先把题目看清楚，题目问的是读取一个文件里面的内容，算出总共有多少个字符。

    #. 简单点来说就是给你一个字符串，有一个函数叫做read4，读n个char到指定的buf去。
    #. 那么就需要一个char*4的临时buf来储存一次读出来的结果，
    #. 然后再把这个结果按要求赋给指定的buf，
    #. 如果比4小的话，就说明字符串快要读完，数字就代表剩下的几个。
    #. 特么想不通为什么一开始搞一个(char *buf)，让有的人看了一脸懵逼好么。



这道题木有搞明白



158. Read N Characters Given Read4 II - Call multiple times
-----------------------------------------------------------

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



151. Reverse Words in a String
------------------------------



Given an input string, reverse the string word by word.

For example
::
    Given s = "the sky is blue",
    return "blue is sky the".



For C programmers: Try to solve it in-place in O(1) space.

Clarification:

    #. What constitutes a word?
       
    A sequence of non-space characters constitutes a word.
    #. Could the input string contain leading or trailing spaces?
    
    Yes. However, your reversed string should not contain leading or trailing spaces.


    #. How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.




186. Reverse Words in a String II
---------------------------------


Given an input string, reverse the string word by word.
A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces
and the words are always separated by a single space.

For example,
::
    Given s = "the sky is blue",
    return "blue is sky the".

Could you do it in-place without allocating extra space?


Hints:
Two-pass:
#. 1. reverse all strings:
"the sky is blue" -> "eulb si yks eht"

#. 2. reverse one word:
"eulb si yks eht" -> "blue is sky the"


.. code-block:: python

    def reverseWords(s):
        return ' '.join(reversed(s.split()))

    def reverseWords2(s):
        print " ".join(s.split()[::-1])

.. code-block:: javascript

        var hello = 'the sky is blue'.split(' ').reverse().join(' ');
        console.log(hello)


557. Reverse Words in a String III
----------------------------------

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
::
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.



JavaScript答案

.. code-block:: javascript

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


.. code-block:: Javascript

    function baby (s) {
            let twoStr = s.split('').sort().join('').toLowerCase().indexOf('aa');
            let oneStr = s.toLowerCase().indexOf('lll');
        
        if( twoStr < 0 && oneStr < 0 ) {
            return true;
        }else{
            return false;
        }
    }
    console.log(baby('ACFHPLLL'))



541. Reverse String II
----------------------


#. Given a string and an integer k, 
#. you need to reverse the first k characters for every 2k characters counting from the start of the string. 
#. If there are less than k characters left, reverse all of them. 
#. If there are less than 2k but greater than or equal to k characters, 
#. then reverse the first k characters and left the other as original.
   
Example:
::
    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"

Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]


.. code-block:: Javascript 

    var reverseStr = function(s, k) {
        var arr = s.split('');
        var i = 0;
        var n = arr.length;
        while(i < n) {
            var j = Math.min(i + k - 1, n - 1);
            reverse(arr,i,j);
            i += 2 * k;
        }
        return arr.join('');
    };
    function reverse(arr,i,j){
        while(i < j) {
            var tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
    }



521. Longest Uncommon Subsequence I
-----------------------------------

Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
::
    Input: "aba", "cdc"
    Output: 3

Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
because "aba" is a subsequence of "aba", 
but not a subsequence of any other strings in the group of two strings. 


Note:
.. admontion::
    Both strings' lengths will not exceed 100.
    Only letters from a ~ z will appear in input strings.



比较两个字符串的长度，若不相等，则返回长度的较大值，若相等则再判断两个字符串是否相同，若相同则返回-1，否则返回长度。


522. Longest Uncommon Subsequence II
------------------------------------

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
::
    Input: "aba", "cdc", "eae"
    Output: 3

Note:

.. hint ::
    All the given strings' lengths will not exceed 10.
    The length of the given list will be in the range of [2, 50].


题目大意：
给定一组字符串，寻找其最长不公共子序列。最长不公共子序列是指：这组字符串中某一个的子序列，该子序列不是其余任意字符串的子序列，并且长度最长。

子序列是指从一个序列中删除一些字符，剩余字符顺序保持不变得到的新序列。任何字符串都是其本身的子序列，空串不属于任意字符串的子序列。

返回最长不公共子序列，若不存在，返回-1。

Answerone
这道题让找最长的独有子序列，解题思路可以分三步：
#. 1、按照字符串长度降序排列strs
#. 2、遍历strs，如果str不是所有strs的独有子字符串，返回str的长度
#. 3、如果没有找到独有字符串，返回-1


Answertwo
#. 首先将输入字符串列表strs按照长度递减排序，记得到的新列表为slist。

#. 利用计数器cnt统计每个字符串出现的次数。

#. 遍历slist，记当前字符串为c，其下标为i：
#. 若c在strs中出现不止一次，跳过该字符串
#. 否则，利用贪心算法对c和slist[0 .. i - 1]的字符串进行匹配，若均匹配失败，则返回len(c)

#. 遍历结束，返回-1



.. code-block:: Python

    class Solution(object):
        def uncommon(self, parent, child):
            lp, lc = len(parent), len(child)
            pp = pc = 0
            while pp < lp and pc < lc:
                if parent[pp] == child[pc]:
                    pc += 1
                pp += 1
            return pc != lc
        def findLUSlength(self, strs):
            """
            :type strs: List[str]
            :rtype: int
            """
            cnt = collections.Counter(strs)
            slist = sorted(set(strs), key=len, reverse=True)
            for i, c in enumerate(slist):
                if cnt[c] > 1: continue
                if all(self.uncommon(p, c) for p in slist[:i]):
                    return len(c)
            return -1



