题目序号 213、152、139、120、91、664、518
=========================================


198. House Robber 
-----------------


You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



.. code-block:: python

    # O(n) space
    def rob1(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            res[i] = max(nums[i]+res[i-2], res[i-1])
        return res[-1]

    def rob2(self, nums):
        if not nums:
            return 0
        res = [0] * len(nums)
        for i in xrange(len(nums)):
            if i == 0:
                res[0] = nums[0]
            elif i == 1:
                res[1] = max(nums[0], nums[1])
            else:
                res[i] = max(nums[i]+res[i-2], res[i-1])
        return res[-1]
      
    # Constant space  
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        a, b = nums[0], max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            tmp = b
            b = max(nums[i]+a, b)
            a = tmp
        return b


.. code-block:: python

    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    def helper(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0:2])
        for i in xrange(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        return dp[-1]
        

    A version which uses less momery:

    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    def helper(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        a, b = nums[0], max(nums[:2])
        for i in xrange(2, len(nums)):
            a, b = b, max(b, a+nums[i])
        return b

213. House Robber II
--------------------

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


.. code-block:: python
    
    # O(n) space
    def rob1(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            res[i] = max(nums[i]+res[i-2], res[i-1])
        return res[-1]

    def rob2(self, nums):
        if not nums:
            return 0
        res = [0] * len(nums)
        for i in xrange(len(nums)):
            if i == 0:
                res[0] = nums[0]
            elif i == 1:
                res[1] = max(nums[0], nums[1])
            else:
                res[i] = max(nums[i]+res[i-2], res[i-1])
        return res[-1]
      
    # Constant space  
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        a, b = nums[0], max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            tmp = b
            b = max(nums[i]+a, b)
            a = tmp
        return b

    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        cur = nums[0]
        pre = max(nums[:2])
        for i in xrange(2, len(nums)):
            cur = max(cur+nums[i], pre)
            cur, pre = pre, cur
        return pre


337. House Robber III
---------------------


The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
::
         3
        / \
       2   3
        \   \ 
         3   1

    Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
::
         3
        / \
       4   5
      / \   \ 
     1   3   1

    Maximum amount of money the thief can rob = 4 + 5 = 9. 



152. Maximum Product Subarray 
-----------------------------


Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6. 


.. code-block:: python

    # O(2*n) space
    def maxProduct1(self, nums):
        if not nums:
            return 
        locMin = [0] * len(nums)
        locMax = [0] * len(nums)
        locMin[0] = locMax[0] = gloMax = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                locMax[i] = max(locMin[i-1]*nums[i], nums[i])
                locMin[i] = min(locMax[i-1]*nums[i], nums[i])
            else:
                locMax[i] = max(locMax[i-1]*nums[i], nums[i])
                locMin[i] = min(locMin[i-1]*nums[i], nums[i])
            gloMax = max(gloMax, locMax[i])
        return gloMax

    # O(1) space    
    def maxProduct2(self, nums):
        if not nums:
            return 
        locMin = locMax = gloMax = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                tmp = locMax
                locMax = max(locMin*nums[i], nums[i])
                locMin = min(tmp*nums[i], nums[i])
            else:
                locMax = max(locMax*nums[i], nums[i])
                locMin = min(locMin*nums[i], nums[i])
            gloMax = max(gloMax, locMax)
        return gloMax
     
    # O(1) space    
    def maxProduct(self, nums):
        if not nums:
            return 
        locMin = locMax = gloMax = nums[0]
        for i in xrange(1, len(nums)):
            tmp = locMin
            locMin = min(locMin*nums[i], nums[i], locMax*nums[i])
            locMax = max(tmp*nums[i], nums[i], locMax*nums[i])
            gloMax = max(gloMax, locMax)
        return gloMax
        


139. Word Break 
---------------


Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes. 


.. code-block:: python

    def exist(self, board, word):
        if not board:
            return False
        r, c = len(board), len(board[0])
        visited = [[False for i in xrange(c)] for j in xrange(r)]
        for i in xrange(r):
            for j in xrange(c):
                if self.dfs(board, word, visited, i, j):
                    return True
        return False
        
    def dfs(self, board, word, visited, i, j):
        if not word:
            return True
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) \
        or visited[i][j] or word[0] != board[i][j]:
            return False
        visited[i][j] = True
        res = self.dfs(board, word[1:], visited, i+1, j) or \
              self.dfs(board, word[1:], visited, i-1, j) or \
              self.dfs(board, word[1:], visited, i, j-1) or \
              self.dfs(board, word[1:], visited, i, j+1)
        visited[i][j] = False
        return res

    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
        
    def wordBreak(self, s, wordDict):
        res = []
        self.dfs(s, wordDict, '', res)
        return res

    def dfs(self, s, dic, path, res):
    # Before we do dfs, we check whether the remaining string 
    # can be splitted by using the dictionary,
    # in this way we can decrease unnecessary computation greatly.
        if self.check(s, dic): # prunning
            if not s:
                res.append(path[:-1])
                return # backtracking
            for i in xrange(1, len(s)+1):
                if s[:i] in dic:
                    # dic.remove(s[:i])
                    self.dfs(s[i:], dic, path+s[:i]+" ", res)

    # DP code to check whether a string can be splitted by using the 
    # dic, this is the same as word break I.                
    def check(self, s, dic):
        dp = [False for i in xrange(len(s)+1)]
        dp[0] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
        return dp[-1]
        


120. Triangle
-------------


Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
::
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]

    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle. 


.. code-block:: python

    # O(n*n/2) space, top-down 
    def minimumTotal1(self, triangle):
        if not triangle:
            return 
        res = [[0 for i in xrange(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    res[i][j] = res[i-1][j-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        return min(res[-1])
        
    # Modify the original triangle, top-down
    def minimumTotal2(self, triangle):
        if not triangle:
            return 
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])
        
    # Modify the original triangle, bottom-up
    def minimumTotal3(self, triangle):
        if not triangle:
            return 
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

    # bottom-up, O(n) space
    def minimumTotal(self, triangle):
        if not triangle:
            return 
        res = triangle[-1]
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
        

91. Decode Ways
---------------


 A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2. 





664. Strange Printer 
--------------------


 There is a strange printer with the following two special requirements:

    The printer can only print a sequence of the same character each time.
    At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.

Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

Example 1:

Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".

Example 2:

Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

Hint: Length of the given string will not exceed 100.


518. Coin Change 2
------------------
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
题目大意：
给定一些不同面值的硬币，和一个金钱总额。编写函数计算要得到目标金额，有多少种不同的硬币组合方式。

注意：你可以假设：

0 <= amount <= 5000
1 <= coin <= 5000
硬币个数不超过500
答案确保在32位整数范围内
解题思路：
动态规划（Dynamic Programmin）