题目序号 314、311、288、249、244、187、166、138、49、36、18、3
===================================================================





314. Binary Tree Vertical Order Traversal
-----------------------------------------


Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:
::
    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

    return its vertical order traversal as:

    [
      [9],
      [3,15],
      [20],
      [7]
    ]

 

Given binary tree [3,9,20,4,5,2,7],
::
        _3_
       /   \
      9    20
     / \   / \
    4   5 2   7

     

    return its vertical order traversal as:

    [
      [4],
      [9],
      [3,5,2],
      [20],
      [7]
    ]



311. Sparse Matrix Multiplication
---------------------------------


Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:
::
    A = [
      [ 1, 0, 0],
      [-1, 0, 3]
    ]

    B = [
      [ 7, 0, 0 ],
      [ 0, 0, 0 ],
      [ 0, 0, 1 ]
    ]


         |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
    AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                      | 0 0 1 |




288. Unique Word Abbreviation
-----------------------------


An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. 
A word abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true


.. code-block:: python
    
    def isUnique(self, word):
        val = word 
        if len(word) > 2:
            word = word[0]+str(len(word)-2)+word[-1]
        # if word abbreviation not in the dictionary, or word itself in the dictionary (word itself may 
        # appear multiple times in the dictionary, so it's better using set instead of list)
        return len(self.dic[word]) == 0 or (len(self.dic[word]) == 1 and val == list(self.dic[word])[0])



249. Group Shifted Strings
--------------------------

Given a string, we can "shift" each of its letter to its successive letter, for example:"abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"

Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.


For example, given:["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],

Return:

[

  ["abc","bcd","xyz"],

  ["az","ba"],

  ["acef"],

  ["a","z"]

]



244. Shortest Word Distance II
------------------------------


This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.



187. Repeated DNA Sequences
---------------------------

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,
::
    Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

    Return: ["AAAAACCCCC", "CCCCCAAAAA"].


.. code-block:: python

    # Time O(n) one pass, Space O(10*n)
    def findRepeatedDnaSequences1(self, s):
        res, dic = [], {}
        for i in xrange(len(s)-9):
            if s[i:i+10] not in dic:
                dic[s[i:i+10]] = 1
            elif dic[s[i:i+10]] == 1:
                res.append(s[i:i+10])
                dic[s[i:i+10]] = 2
        return res
        
    # Time O(n) one pass, Space O(4*n)   
    def findRepeatedDnaSequences(self, s):
        res = []
        dic = {"A":1, "C":2, "G":3, "T":4}
        dicDNA = {}
        num = 1
        for i in xrange(len(s)):
            num = (num*4 + dic[s[i]]) & 0XFFFFF
            if i < 9:
                continue
            if num not in dicDNA:
                dicDNA[num] = 1
            elif dicDNA[num] == 1:
                res.append(s[i-9:i+1])
                dicDNA[num] = 2
        return res

    def findRepeatedDnaSequences(self, s):
        dic, res, l = {}, [], 10
        for i in xrange(len(s)-l+1):
            if s[i:i+l] in dic and dic[s[i:i+l]] == 1:
                res.append(s[i:i+l])
            dic[s[i:i+l]] = dic.get(s[i:i+l], 0) + 1
        return res



    The first method stores all the 10-letter-long sequences in dic, so the needed space is O(10n), every single letter needs 1 byte if using ASCII code, while the second method translates a 10-letter-long sequence to a 20-bit long integer, if integer is 4 bytes, then the space needed is O(4n). Two methods operate one pass, so time complexity is O(n).

    # Time O(n) one pass, Space O(10*n)
    def findRepeatedDnaSequences1(self, s):
        res, dic = [], {}
        for i in xrange(len(s)-9):
            if s[i:i+10] not in dic:
                dic[s[i:i+10]] = 1
            elif dic[s[i:i+10]] == 1:
                res.append(s[i:i+10])
                dic[s[i:i+10]] = 2
        return res
        
    # Time O(n) one pass, Space O(4*n)   
    def findRepeatedDnaSequences(self, s):
        res = []
        dic = {"A":1, "C":2, "G":3, "T":4}
        dicDNA = {}
        num = 1
        for i in xrange(len(s)):
            num = (num*4 + dic[s[i]]) & 0XFFFFF
            if i < 9:
                continue
            if num not in dicDNA:
                dicDNA[num] = 1
            elif dicDNA[num] == 1:
                res.append(s[i-9:i+1])
                dicDNA[num] = 2
        return res  
        

166. Fraction to Recurring Decimal
----------------------------------

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,
::
    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".


.. code-block:: python

    def fractionToDecimal(self, numerator, denominator):
        num, den = numerator, denominator
        if not den:  # denominator is 0
            return 
        if not num:  # numerator is 0
            return "0"
        res = []
        if (num < 0) ^ (den < 0):
            res.append("-")  # add the sign
        num, den = abs(num), abs(den)
        res.append(str(num//den))
        rmd = num % den
        if not rmd:
            return "".join(res)  # only has integral part
        res.append(".")  # has frational part
        dic = {}
        while rmd:
            if rmd in dic:   # the remainder recurs
                res.insert(dic[rmd], "(")
                res.append(")")
                break
            dic[rmd] = len(res) 
            div, rmd = divmod(rmd*10, den)
            res.append(str(div))
        return "".join(res) 


思路 1 - 时间复杂度: hard to say - 空间复杂度: O(1)******

先处理正负号
再处理整数部分
最后处理小数部分，利用字典来判断是否循环
note：对于小数处理部分，必须先进行将没有处理过的r加入到m中去

这是因为：

例如输入为4, 333
如果我们将已经处理过的r加入到m中去的话，重复数字当次就被加入m中了，下一次循环判断的时候r肯定已经在里面了

.. code-block:: python

    class Solution(object):
        def fractionToDecimal(self, numerator, denominator):
            """
            :type numerator: int
            :type denominator: int
            :rtype: str
            """
            if numerator == 0: # zero numerator
                return '0'
            res = ''
            if numerator * denominator < 0: # determine the sign
                res += '-'
            numerator, denominator = abs(numerator), abs(denominator) # remove sign of operands
            res += str(numerator / denominator) # append integer part
            if numerator % denominator == 0: # in case no fractional part
                return res
            res += '.'
            r = numerator % denominator
            m = {}
            while r: # simulate the division process
                if r in m: # meet a known remainder
                    res = res[:m[r]] + '(' + res[m[r]:] + ')' # so we reach the end of the repeating part
                    break
                m[r] = len(res) # if the remainder is first seen, remember next r/denominator index in res
                r *= 10
                res += str(r/denominator) # append the quotient digit
                r %= denominator
               
            return res


138. Copy List with Random Pointer
----------------------------------

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list. 


.. code-block:: python

    def copyRandomList(self, head):
        if not head:
            return None
        p = head
        while p:
            node = RandomListNode(p.label)
            node.next = p.next
            p.next = node
            p = p.next.next
            # p = node.next
        p = head    
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead
        
    def copyRandomList1(self, head):
        if not head:
            return 
        # copy nodes
        cur = head
        while cur:
            nxt = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = nxt
            cur = nxt
        # copy random pointers
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # separate two parts
        second = cur = head.next
        while cur.next:
            head.next = cur.next
            head = head.next
            cur.next = head.next
            cur = cur.next
        head.next = None
        return second

    # using dictionary    
    def copyRandomList(self, head):
        if not head:
            return 
        cur, dic = head, {}
        # copy nodes
        while cur:
            dic[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = head
        # copy random pointers
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[head]


49. Group Anagrams
------------------

Given an array of strings, group anagrams together.

For example, 
::
    given: ["eat", "tea", "tan", "ate", "nat", "bat"],
    
    Return:

    [
      ["ate", "eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]

Note: All inputs will be in lower-case.



36. Valid Sudoku
----------------

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

http://sudoku.com.au/TheRules.aspx


.. image:: sudoku.png

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 



.. code-block:: python

    def isValidSudoku(self, board):
        r, c = len(board), len(board[0])
        for i in xrange(r):
            for j in xrange(c):
                if not self.isValid(i, j, board):
                    return False
        return True

    def isValid(self, x, y, board):
        if board[x][y] == ".":
            return True
        tmp = board[x][y]; board[x][y] = "#"
        r, c = len(board), len(board[0])
        for i in xrange(r):
            if board[i][y] == tmp:
                return False
        for j in xrange(c):
            if board[x][j] == tmp:
                return False
        for i in xrange(x/3*3, x/3*3+3):
            for j in xrange(y/3*3, y/3*3+3):
                if board[i][j] == tmp:
                    return False
        board[x][y] = tmp
        return True
        
    def isValidSudoku(self, board):
        return self.checkRows(board) and self.checkColums(board) and self.checkSquares(board)
        
    def checkRows(self, board):
        r, c = len(board), len(board[0])
        for i in xrange(r):
            dic = dict()
            for j in xrange(c):
                if board[i][j] != ".":
                    if board[i][j] in dic:
                        return False
                    dic[board[i][j]] = 0
        return True
        
    def checkColums(self, board):
        r, c = len(board), len(board[0])
        for j in xrange(c):
            dic = dict()
            for i in xrange(r):
                if board[i][j] != ".":
                    if board[i][j] in dic:
                        return False
                    dic[board[i][j]] = 0
        return True
        
    def checkSquares(self, board):
        m, n = [0, 3, 6], [0, 3, 6]
        for p in m:
            for q in n:
                dic = dict()
                for i in xrange(p, p+3):
                    for j in xrange(q, q+3):
                        if board[i][j] != ".":
                            if board[i][j] in dic:
                                return False
                        dic[board[i][j]] = 0
        return True
        
        
        
    def isValidSudoku(self, board):
        return self.checkRowCol(board) and self.checkRowCol(zip(*board)) and self.checkSquare(board)
        
    def checkRowCol(self, board):
        for row in board:
            dic = {}
            for i in row:
                if i != "." and i in dic:
                    return False
                dic[i] = 0
        return True
        
    def checkSquare(self, board):
        for i in xrange(3):
            for j in xrange(3):
                dic = {}
                for m in xrange(3):
                    for n in xrange(3):
                        val = board[i*3+m][j*3+n]
                        if val != "." and val in dic:
                            return False
                        dic[val] = 0
        return True
        


18. 4Sum
--------

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


3. Longest Substring Without Repeating Characters
-------------------------------------------------



Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



