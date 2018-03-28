题目序号 
============================================================





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

28. Implement strStr()
----------------------

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

还没来得及仔细看答案
https://www.youtube.com/watch?v=GTJr8OvyEVQ
