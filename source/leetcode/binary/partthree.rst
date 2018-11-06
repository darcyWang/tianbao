题目序号 162、153、81、74、50、34、33、29、668
============================================================




162. Find Peak Element
----------------------


A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.
Note:

Your solution should be in logarithmic complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.






153. Find Minimum in Rotated Sorted Array
-----------------------------------------


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.



81. Search in Rotated Sorted Array II
-------------------------------------


Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.



74. Search a 2D Matrix
----------------------

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

Given target = 3, return true.



50. Pow(x, n)
-------------

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
::
    Input: 2.00000, 10
    Output: 1024.00000

Example 2:
::
    Input: 2.10000, 3
    Output: 9.26100

Example 3:
::
    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

*. -100.0 < x < 100.0
*. n is a 32-bit signed integer, within the range [−231, 231 − 1]


.. code-block:: python
        
    class Solution:
        myPow = pow
    That's even shorter than the other more obvious "cheat":

    class Solution:
        def myPow(self, x, n):
            return x ** n
    And to calm down the haters, here's me "doing it myself":

    Recursive:

    class Solution:
        def myPow(self, x, n):
            if not n:
                return 1
            if n < 0:
                return 1 / self.myPow(x, -n)
            if n % 2:
                return x * self.myPow(x, n-1)
            return self.myPow(x*x, n/2)
    Iterative:

    class Solution:
        def myPow(self, x, n):
            if n < 0:
                x = 1 / x
                n = -n
            pow = 1
            while n:
                if n & 1:
                    pow *= x
                x *= x
                n >>= 1
            return pow  
        
        
    # I
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n & 1:
            return self.myPow(x, n/2) ** 2 * x
        else:
            return self.myPow(x, n/2) ** 2

    # II
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n & 1:
            return self.myPow(x*x, n/2) * x
        else:
            return self.myPow(x*x, n/2) 
        

.. code-block:: python

    class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n & 1:  # n 为 奇数
            return x * self.myPow(x*x, n>>1)
        else:
            return self.myPow(x*x, n>>1)

    # iterative
    class Solution(object):
        def myPow(self, x, n):
            """
            :type x: float
            :type n: int
            :rtype: float
            """
            if n < 0:
                x = 1 / x
                n = -n
            res = 1
            while n:
                if n & 1:
                    res *= x
                x *= x
                n >>= 1
            return res


34. Search for a Range
----------------------

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]. 




33. Search in Rotated Sorted Array
----------------------------------

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.


29. Divide Two Integers
-----------------------

 Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT. 



668. Kth Smallest Number in Multiplication Table
------------------------------------------------


 Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:

Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1 2 3
2 4 6
3 6 9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).

Example 2:

Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1 2 3
2 4 6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).

Note:

    The m and n will be in the range [1, 30000].
    The k will be in the range [1, m * n]

