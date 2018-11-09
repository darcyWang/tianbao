题目序号 351、343、338、322、309、304、300、279、264、221
============================================================


351. Android Unlock Patterns
----------------------------


Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:

    Each pattern must connect at least m keys and at most n keys.
    All the keys must be distinct.
    If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
    The order of keys used matters.

Explanation:
  

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

Example:
Given m = 1, n = 1, return 9.


343. Integer Break 
------------------

 Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


338. Counting Bits 
------------------


Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

Credits:
Special thanks to @ syedee for adding this problem and creating all test cases.




322. Coin Change 
----------------


 You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


309. Best Time to Buy and Sell Stock with Cooldown 
--------------------------------------------------



Say you have an array for which the i(th)次方 element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.



304. Range Sum Query 2D - Immutable 
-----------------------------------

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).




The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:

    You may assume that the matrix does not change.
    There are many calls to sumRegion function.
    You may assume that row1 ≤ row2 and col1 ≤ col2.




300. Longest Increasing Subsequence 
-----------------------------------


 Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.


279. Perfect Squares 
--------------------


Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

.. code-block:: python

    class Solution(object):
        def numSquares(self, n):
            """
            :type n: int
            :rtype: int
            """
           
            q1 = [0]
            q2 = []
            level = 0
            visited = [False] * (n+1)
            while True:
                level += 1
                for v in q1:
                    i = 0
                    while True:
                        i += 1
                        t = v + i * i
                        if t == n: return level
                        if t > n: break
                        if visited[t]: continue
                        q2.append(t)
                        visited[t] = True
                q1 = q2
                q2 = []
                    
            return 0


264. Ugly Number II 
-------------------

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


.. code-block:: python

    # dynamic programming
    def nthUglyNumber(self, n):
        ugly = [0] * n
        nxt = ugly[0] = 1
        i2 = i3 = i5 = 0
        nxt2, nxt3, nxt5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
        for i in xrange(1, n):
            nxt = min(nxt2, nxt3, nxt5)
            ugly[i] = nxt
            if nxt == nxt2:
                i2 += 1
                nxt2 = ugly[i2]*2
            if nxt == nxt3:
                i3 += 1
                nxt3 = ugly[i3]*3
            if nxt == nxt5:
                i5 += 1
                nxt5 = ugly[i5]*5
        return nxt # ugly[-1]


     def nthUglyNumber(self, n):
        if n <= 0:
            return 0
        ugly = [1] * n
        i2 = i3 = i5 = 0
        for i in xrange(1, n):
            ugly[i] = min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
            if ugly[i] == ugly[i2]*2:
                i2 += 1
            if ugly[i] == ugly[i3]*3:
                i3 += 1
            if ugly[i] == ugly[i5]*5:
                i5 += 1
        return ugly[-1]

221. Maximal Square 
-------------------

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:
::
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    Return 4.

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.


.. code-block:: python

    # O((m+1)*(n+1)) space, one pass
    def maximalSquare1(self, matrix):
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[0 for i in xrange(c+1)] for j in xrange(r+1)]
        res = 0
        for i in xrange(r):
            for j in xrange(c):
                dp[i+1][j+1] = (min(dp[i][j], dp[i+1][j], dp[i][j+1])+1)*int(matrix[i][j])
                res = max(res, dp[i+1][j+1]**2)
        return res
        
    # O(m*n) space, one pass  
    def maximalSquare2(self, matrix):
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in xrange(c)] for i in xrange(r)]
        res = max(max(dp))
        for i in xrange(1, r):
            for j in xrange(1, c):
                dp[i][j] = (min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1)*int(matrix[i][j])
                res = max(res, dp[i][j]**2)
        return res
        
    # O(2*n) space    
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        pre = cur = [0] * (c+1)
        res = 0
        for i in xrange(r):
            for j in xrange(c):
                cur[j+1] = (min(pre[j], pre[j+1], cur[j])+1)*int(matrix[i][j])
                res = max(res, cur[j+1]**2)
            pre = cur
            cur = [0] * (c+1)
        return res
        