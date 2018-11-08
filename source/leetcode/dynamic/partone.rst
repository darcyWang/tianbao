题目序号 303、276、256、265、70、53、651、650、647
============================================================


303. Range Sum Query - Immutable 
--------------------------------     


Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

    You may assume that the array does not change.
    There are many calls to sumRange function.


276. Paint Fence
----------------

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.


这道题让我们粉刷篱笆，有n个部分需要刷，有k种颜色的油漆，规定了不能有超过两个的相同颜色涂的部分，问我们总共有多少种刷法。那么我们首先来分析一下，如果n=0的话，说明没有需要刷的部分，直接返回0即可，如果n为1的话，那么有几种颜色，就有几种刷法，所以应该返回k，当n=2时，k=2时，我们可以分两种情况来统计，一种是相邻部分没有相同的，一种相同部分有相同的颜色，那么对于没有相同的，对于第一个格子，我们有k种填法，对于下一个相邻的格子，由于不能相同，所以我们只有k-1种填法。而有相同部分颜色的刷法和上一个格子的不同颜色刷法相同，因为我们下一格的颜色和之前那个格子颜色刷成一样的即可，最后总共的刷法就是把不同和相同两个刷法加起来，参见代码如下：

https://fxrcode.gitbooks.io/leetcodenotebook/content/Misc/leetcode_hao_da_an.html



256. Paint House
----------------


There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs0 is the cost of painting house 0 with color red; costs1 is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note: All costs are positive integers.


.. code-block:: python

	# O(n*3) space
	def minCost1(self, costs):
	    if not costs:
	        return 0
	    r, c = len(costs), len(costs[0])
	    dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
	    dp[0] = costs[0]
	    for i in xrange(1, r):
	        dp[i][0] = costs[i][0] + min(dp[i-1][1:3])
	        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
	        dp[i][2] = costs[i][2] + min(dp[i-1][:2])
	    return min(dp[-1])
	 
	# change original matrix   
	def minCost2(self, costs):
	    if not costs:
	        return 0
	    for i in xrange(1, len(costs)):
	        costs[i][0] += min(costs[i-1][1:3])
	        costs[i][1] += min(costs[i-1][0], costs[i-1][2])
	        costs[i][2] += min(costs[i-1][:2])
	    return min(costs[-1])

	# O(1) space    
	def minCost3(self, costs):
	    if not costs:
	        return 0
	    dp = costs[0]
	    for i in xrange(1, len(costs)):
	        pre = dp[:] # here should take care
	        dp[0] = costs[i][0] + min(pre[1:3])
	        dp[1] = costs[i][1] + min(pre[0], pre[2])
	        dp[2] = costs[i][2] + min(pre[:2])
	    return min(dp)	
		


265. Paint House II 
-------------------



There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs0 is the cost of painting house 0 with color 0; costs1 is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note: All costs are positive integers.

Follow up: Could you solve it in O(nk) runtime?


.. code-block:: python

	# dp, O(nk) space
	def minCostII1(self, costs):
	    if not costs:
	        return 0
	    r, c = len(costs), len(costs[0])
	    dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
	    dp[0] = costs[0]
	    for i in xrange(1, r):
	        for j in xrange(c):
	            dp[i][j] = costs[i][j] + min(dp[i-1][:j]+dp[i-1][j+1:])
	    return min(dp[-1])
	    
	# dp, O(k) space
	def minCostII(self, costs):
	    if not costs:
	        return 0
	    r, c = len(costs), len(costs[0])
	    cur = costs[0]
	    for i in xrange(1, r):
	        pre = cur[:]  # take care here
	        for j in xrange(c):
	            cur[j] = costs[i][j] + min(pre[:j]+pre[j+1:])
	    return min(cur)	
		
		
		
	class Solution:
	    # @param {integer[][]} costs
	    # @return {integer}
	    def minCostII(self, costs):
	        return min(reduce(lambda x, y: self.combine(y, x), costs)) if costs else 0

	    def combine(self, house, tmp):
	        m, n, i = min(tmp), len(tmp), tmp.index(min(tmp))
	        tmp = [m]*i + [min(tmp[0:i]+tmp[i+1:])] + [m]*(n-i-1)
	        return [sum(i) for i in zip(house, tmp)]	
		
		
		
	class Solution:
	    def minCostII(self, costs):
	        return min(reduce(self.combine, costs)) if costs else 0

	    def combine(self, tmp, house):
	        m, n, i = min(tmp), len(tmp), tmp.index(min(tmp))
	        tmp, tmp[i] = [m]*n, min(tmp[:i]+tmp[i+1:])
	        return map(sum, zip(house, tmp))	
		


70. Climbing Stairs 
-------------------

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer. 



53. Maximum Subarray
--------------------

 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


651. 4 Keys Keyboard
--------------------
Imagine you have a special keyboard with the following keys:

Key 1: (A): Prints one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:

Input: N = 3
Output: 3
Explanation: 
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A

Example 2:

Input: N = 7
Output: 9
Explanation: 
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

Note:

    1 <= N <= 50
    Answers will be in the range of 32-bit signed integer.

650. 2 Keys Keyboard 
--------------------


 Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

    Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Note:

    The n will be in the range [1, 1000].



647. Palindromic Substrings 
---------------------------


 Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:

    The input string length won't exceed 1000.
