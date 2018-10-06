题目序号 
============================================================







536. Construct Binary Tree from String
--------------------------------------
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:

Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
Note:

There will only be '(', ')', '-' and '0' ~ '9' in the input string.

题目大意：
根据字符串重构二叉树。

输入包含数字和括号，数字代表根节点，括号内的子串代表左、右孩子。

注意：

输入字符串只包含'(', ')，'-'和数字'0'-'9'

解题思路：
递归+字符串处理

通过括号匹配将字符串拆解成root, (left), (right)三部分，递归创建二叉树





http://bookshadow.com/weblog/2017/03/12/leetcode-construct-binary-tree-from-string/


http://www.jianshu.com/p/9df545283b21





3. Longest Substring Without Repeating Characters 
-------------------------------------------------

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


5. Longest Palindromic Substring
--------------------------------


Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"


17. Letter Combinations of a Phone Number 
-----------------------------------------

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want. 




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

