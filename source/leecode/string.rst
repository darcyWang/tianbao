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


JavaScript答案 ::

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


Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
::
        Input: s = "abcdefg", k = 2
        Output: "bacdfeg"
Restrictions:
::
        The string consists of lower English letters only.
        Length of the given string and k will in the range [1, 10000]


JavaScript答案 ::

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
1、按照字符串长度降序排列strs
2、遍历strs，如果str不是所有strs的独有子字符串，返回str的长度
3、如果没有找到独有字符串，返回-1

Answertwo
首先将输入字符串列表strs按照长度递减排序，记得到的新列表为slist。

利用计数器cnt统计每个字符串出现的次数。

遍历slist，记当前字符串为c，其下标为i：

    若c在strs中出现不止一次，跳过该字符串

    否则，利用贪心算法对c和slist[0 .. i - 1]的字符串进行匹配，若均匹配失败，则返回len(c)

遍历结束，返回-1


python 
::
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



13. Roman to Integer
--------------------


Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.


+-----------------+------+------+------+------+------+------+------+
|  Roman Number   |   I  |  V   |   X  |   L  |   C  |   D  |   M  |  
+-----------------+------+------+------+------+------+------+------+
|  Arab Number    |   1  |  5   |  10  |  50  | 100  |  500 | 1000 |
+-----------------+------+------+------+------+------+------+------+



罗马数字是最早的数字表示方式，比阿拉伯数字早2000多年，起源于罗马。
如今我们最常见的罗马数字就是钟表的表盘符号：Ⅰ，Ⅱ，Ⅲ，Ⅳ（IIII），Ⅴ，Ⅵ，Ⅶ，Ⅷ，Ⅸ，Ⅹ，Ⅺ，Ⅻ……
对应阿拉伯数字（就是现在国际通用的数字），就是1，2，3，4，5，6，7，8，9，10，11，12。（注：阿拉伯数字其实是古代印度人发明的，后来由阿拉伯人传入欧洲，被欧洲人误称为阿拉伯数字。）


1、相同的数字连写，所表示的数等于这些数字相加得到的数，如：Ⅲ = 3；
2、小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数， 如：Ⅷ = 8；Ⅻ = 12；
3、小的数字，（限于Ⅰ、X 和C）在大的数字的左边，所表示的数等于大数减小数得到的数，如：Ⅳ= 4；Ⅸ= 9；
4、正常使用时，连写的数字重复不得超过三次。（表盘上的四点钟“IIII”例外）
5、在一个数的上面画一条横线，表示这个数扩大1000倍。


有几条须注意掌握：
1、基本数字Ⅰ、X 、C 中的任何一个，自身连用构成数目，或者放在大数的右边连用构成数目，都不能超过三个；放在大数的左边只能用一个。
2、不能把基本数字V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目，只能使用一个。
3、V 和X 左边的小数字只能用Ⅰ。
4、L 和C 左边的小数字只能用X。
5、D 和M 左边的小数字只能用C。
 
而这道题好就好在没有让我们来验证输入字符串是不是罗马数字，这样省掉不少功夫。我们需要用到map数据结构，来将罗马数字的字母转化为对应的整数值，因为输入的一定是罗马数字，那么我们只要考虑两种情况即可：
第一，如果当前数字是最后一个数字，或者之后的数字比它小的话，则加上当前数字
第二，其他情况则减去这个数字






考虑到罗马数字转换为阿拉伯数字，相应的阿拉伯数字也可以转换为罗马数字

















