题目序号 314、311、288、249、244、187、166、138、94、49、36、18、3
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

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].




166. Fraction to Recurring Decimal
----------------------------------

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,
::
    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".





138. Copy List with Random Pointer
----------------------------------

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list. 


94. Binary Tree Inorder Traversal
---------------------------------


Given a binary tree, return the inorder traversal of its nodes' values.

For example:
::
    Given binary tree [1,null,2,3],

       1
        \
         2
        /
       3

    return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?



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



A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 



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



