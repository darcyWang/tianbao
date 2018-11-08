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



.. code-block:: python

    # O(n) time
    def findPeakElement1(self, nums):
        i = 0
        while i <= len(nums)-1:
            while i < len(nums)-1 and nums[i] < nums[i+1]:
                i += 1
            return i 

    # O(lgn) time     
    def findPeakElement2(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l 
        
    # Recursively
    def findPeakElement(self, nums):
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, l, r):
        if l == r:
            return l
        mid = l + (r-l)//2
        if nums[mid] > nums[mid+1]:
            return self.helper(nums, l, mid)
        else:
            return self.helper(nums, mid+1, r)

    # O(n) time
    def findPeakElement(self, nums):
        if not nums:
            return 0
        nums.insert(0, -(sys.maxint+1))
        nums.append(-(sys.maxint+1))
        for i in xrange(1, len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i-1
        
    # O(lgn) time
    def findPeakElement(self, nums):
        if not nums:
            return 0
        l, r = 0, len(nums)-1
        while l <= r:
            if l == r:
                return l
            mid = l + (r-l)//2
            # due to "mid" is always the left one if the length of the list is even,
            # so "mid+1" is always valid.
            if (mid-1 < 0 or nums[mid-1] < nums[mid]) and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1         
                
                
    class Solution:
        # @param nums, an integer[]
        # @return an integer
        def findPeakElement(self, nums):
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return i - 1
            return len(nums) - 1 
    Or we can even cheat it. Of course, it is "bad" :-)

    class Solution:
        # @param nums, an integer[]
        # @return an integer
        def findPeakElement(self, nums):
            return nums.index(max(nums))            
        


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

::
    [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]

Given target = 3, return true.


.. code-block:: python

    # O(m*n) space, O(lg(m*n)) time
    def searchMatrix1(self, matrix, target):
        if not matrix or target is None:
            return False
        ls = reduce(lambda x, y: x + y, [row for row in matrix], [])
        l, r = 0, len(ls)-1
        while l <= r:
            mid = l + (r-l)//2
            if ls[mid] < target:
                l = mid + 1
            elif ls[mid] > target:
                r = mid - 1
            else:
                return True
        return False
        
    # Iteratively
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = l + (r-l)//2
            row, col = mid//len(matrix[0]), mid%(len(matrix[0]))
            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                return True
        return False
     
    # Recursively 
    def searchMatrix3(self, matrix, target):
        if not matrix or target is None:
            return False
        return self.helper(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1, target)
        
    def helper(self, matrix, x1, y1, x2, y2, target):
        while x1 <= x2 and y1 <= y2:
            midx = x1 + (x2-x1)//2; midy = y1 + (y2-y1)//2
            if target < matrix[midx][midy]:
                return self.helper(matrix, x1, y1, midx-1, y2, target) or \
                self.helper(matrix, midx, y1, midx, midy-1, target)
            elif target > matrix[midx][midy]:
                return self.helper(matrix, midx+1, y1, x2, y2, target) or \
                self.helper(matrix, midx, midy+1, midx, y2, target)
            else:
                return True
        return False    
        
        
    It's nowhere near O(lg(mn)). It's not even O(mn). It's Θ(m2n), as the line

    ls = reduce(lambda x, y: x + y, [row for row in matrix], [])
    is really costly. And btw also a really complicated way to write

    ls = sum(matrix, [])    

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

