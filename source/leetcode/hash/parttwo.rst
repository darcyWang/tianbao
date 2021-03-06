题目序号 409、389、359、350、290、266、242、205
============================================================


409. Longest Palindrome
-----------------------

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
::
    Input: "abccccdd"

    Output:  7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.



389. Find the Difference
------------------------


Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:
::
    Input:
    s = "abcd"
    t = "abcde"

    Output: e

Explanation:
'e' is the letter that was added.



359. Logger Rate Limiter
------------------------

Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;

Credits:
Special thanks to @memoryless for adding this problem and creating all test cases.



350. Intersection of Two Arrays II
----------------------------------


Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?



290. Word Pattern
-----------------



Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
::
    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.



.. code-block:: python

    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return map(s.find, s) == map(t.index, t)

    def wordPattern(self, pattern, str):
        f = lambda s: map({}.setdefault, s, range(len(s)))
        return f(pattern) == f(str.split())
        
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)   
        
    def wordPattern(self, pattern, str):
        if len(pattern) != len(str.split()):
            return False
        d1, d2 = {}, {}
        for p, r in zip(pattern, str.split()):
            if p in d1:
                if d1[p] != r:
                    return False
            d1[p] = r
            if r in d2:
                if d2[r] != p:
                    return False
            d2[r] = p
        return True 



4.pattern = "abba", str = "dog dog dog dog" should return false.

因为这个的限制，所以中间加了一个loop用来查询是否这个a对应的已经出现过了。

不过其实也可以用两个dictionary来处理，可以O(n^3) -> O(n^2)


.. code-block:: python

    class Solution(object):
        def wordPattern(self, pattern, str):
            """
            :type pattern: str
            :type str: str
            :rtype: bool
            """
            strList = str.split(' ')
            if len(pattern) != len(strList):
                return False
            lookup = {}
            for i in range(len(strList)):
                if pattern[i] not in lookup:
                    for key in lookup:
                        if lookup[key] == strList[i]:
                            return False
                    lookup[pattern[i]] = strList[i]
                elif lookup[pattern[i]] != strList[i]:
                    return False
                    
            return True



另外看到一段非常简短代码，使用了map函数，有待学习


思路2

pattern 和 str 只要是同一种模式即可，所以我们可以简单将 pattern 和 str 两两组合，然后判断长度。

比如 pattern = 'aba' str = 'dog cat cat'

将它们两两组合
sp = set([('a', 'dog'),('b', 'cat') ('a', 'cat')])

sp 的长度为3。
但是 pattern 和 str 去重后的长度分别为 2。 所以则判断 pattern 和 str 不是同一种模式的，如果是的话那么 sp 的长度也应该是 2 而不是 3。 

不管 pattern 和 str 分别是什么，如果模式相同，那么它们组合后也会有相同的模式，会有相同的去重后的长度。

有没有一种可能全部长度相同但模式不同的呢？
以上面的为例：

pattern 的模式是 aba 模式。 去重后是 ab 模式。
str         则是 abb 模式。 去重后是 ab 模式。

它们两两组合后是 abc 模式， a = (a + a) b = (b + b) c = (a + b)。
如果两两组合后相同，
那么不管是组合成 
a = (a + a) b = (b + b) b = (b + b)
还是
a = (a + a) b = (b + b) a = (a + a)

都会被去重为 ab 模式。


代码：
.. code-block:: python

    class Solution(object):
        def wordPattern(self, pattern, string):
            """
            :type pattern: str
            :type str: str
            :rtype: bool
            """
            pattern = list(pattern)
            string = string.split(' ')
            if len(pattern) != len(string):
                return False
            temp = len(set(zip(pattern, string)))
            return temp == len(set(pattern)) and temp == len(set(string))


266. Palindrome Permutation
---------------------------


Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

Hint:

#. Consider the palindromes of odd vs even length. What difference do you notice? Count the frequency of each character.
#. If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?


.. code-block:: python
    
    Use collections.Counter and itertools.permutations

    class Solution(object):
        def generatePalindromes(self, s):
            d = collections.Counter(s)
            m = tuple(k for k, v in d.iteritems() if v % 2)
            p = ''.join(k*(v/2) for k, v in d.iteritems())
            return [''.join(i + m + i[::-1]) for i in set(itertools.permutations(p))] if len(m) < 2 else [] 


.. code-block:: python

    def canPermutePalindrome(self, s):
        dic = {}
        for item in s:
            dic[item] = dic.get(item, 0) + 1
        # return sum(v % 2 for v in dic.values()) < 2
        count1 = 0
        for val in dic.values():
            if val % 2 == 1:
                count1 += 1
            if count1 > 1:
                return False
        return True 


242. Valid Anagram
------------------


Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?


.. code-block:: python

    def isAnagram1(self, s, t):
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2
        
    def isAnagram2(self, s, t):
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item)-ord('a')] += 1
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2
        
    def isAnagram3(self, s, t):
        return sorted(s) == sorted(t)   


205. Isomorphic Strings
-----------------------


Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example
::
    Given "egg", "add", return true.

    Given "foo", "bar", return false.

    Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

.. code-block:: python

    def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())
            
    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in xrange(256)], [[] for _ in xrange(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)
        
    def isIsomorphic3(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        
    def isIsomorphic4(self, s, t): 
        return [s.find(i) for i in s] == [t.find(j) for j in t]
        
    def isIsomorphic5(self, s, t):
        return map(s.find, s) == map(t.find, t)

    def isIsomorphic(self, s, t):
        d1, d2 = [0 for _ in xrange(256)], [0 for _ in xrange(256)]
        for i in xrange(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i+1
            d2[ord(t[i])] = i+1
        return True
        
