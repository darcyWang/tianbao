题号   400、367、69、326、535、523、469、423、413
=========================================================



400. Nth Digit
--------------

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note: n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
::
   Input: 3
   Output: 3

Example 2:
::
   Input: 11
   Output: 0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


367. Valid Perfect Square 
-------------------------

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
::
   Input: 16
   Returns: True

Example 2:
::
   Input: 14
   Returns: False


解法I 牛顿迭代（Newton's Method）

求平方根可以转化为求函数y = x ^ 2 - num的根

迭代过程x = (x + num / x) * 1/2

.. code-block:: python

    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            x = num
            while x * x > num:
                x = (x + num / x) / 2
            return x * x == num


解法II 二分法（Binary Search）

.. code-block:: python

    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            left, right = 0, num
            while left <= right:
                mid = (left + right) / 2
                if mid * mid >= num:
                    right = mid - 1
                else:
                    left = mid + 1
            return left * left == num


.. code-block:: python

    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            L, R = 1, (num >> 1) + 1
            while L <= R:
                m = L + ((R - L) >> 1)
                mul = m ** 2
                if mul == num:
                    return True
                elif mul > num:
                    R = m - 1
                else:
                    L = m + 1
            return False


.. code-block:: python

    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            L, R = 1, (num >> 1) + 1
            while L <= R:
                m = L + ((R - L) >> 1)
                mul = m ** 2
                if mul == num:
                    return True
                elif mul > num:
                    R = m - 1
                else:
                    L = m + 1
            return False


69. Sqrt(x) 
-----------

Implement int sqrt(int x).

Compute and return the square root of x.

这道题目的答案就是上面题目答案修改一下

.. code-block:: javascript

    /**
     * @param {number} num
     * @return {boolean}
     */
    var isPerfectSquare = function(num) {
        var lo = 1;
        var hi = num;
        var isPS = false;

        if (num === 1) {
            isPS = true;
        }

        while (lo <= hi) {
            var mid = lo + Math.floor((hi - lo) / 2);
            var midSquare = mid * mid;
            if (midSquare === num) {
                isPS = true;
                break;
            } else if (midSquare > num) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }

        return isPS;
    };



.. code-block:: python

    # Binary search  
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1 
        
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = (r+l)/2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid > x:
                r = mid - 1
            else:
                l = mid + 1 




326. Power of Three 
-------------------

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

.. code-block:: python

    class Solution(object):
        def isPowerOfThree(self, n):
            """
            :type n:int
            :rtype : bool
            """

            if(n <= 0):
                return False
            while n%3 == 0:
                n /= 3
            return n == 1

        def onePowerOfThree(self, n):
            if n <= 0:
                return False
            if n == 1:
                return True
            if n%3 == 0:
                return self.onePowerOfThree(n/3)
            else:
                return False 


.. tip:: 


    当然，题目说了不能循环或递归，上面的解法能AC但不太符合题意。考虑到输入是“Integer”，是有范围的（<2147483648），所以存在能输入的最大的3的幂次，即 3^19=1162261467。所以只要检查输入能否被它整除即可

.. code-block:: python

    class Solution(object):
        def twoPowerOfThree(self, n):
            return n > 0 and 1162261467 % n == 0




.. tip::

    还可以算出能输入的所有3的幂次，保存到list或dict中，对每次输入判断是否在这些数中即可。


.. code-block:: python

    class Solution(object):
        def threePowerOfThree(self, n):
            nums = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
            return n in nums

.. tip:: 

    取对数

.. code-block:: python

    class Solution(object):
        def threePowerOfThree(self, n):

            return n > 0 and 3 ** round(math.log(n, 3)) == 0 




.. caution:: 

    这道题给我们n个数字，是0到n之间的数但是有一个数字去掉了，让我们寻找这个数字，要求线性的时间复杂度和常数级的空间复杂度。那么最直观的一个方法是用等差数列的求和公式求出0到n之间所有的数字之和，然后再遍历数组算出给定数字的累积和，然后做减法，差值就是丢失的那个数字
    等差数列前n项和 - 数组之和


.. code-block:: python

    class Solution(object):
        def missingNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            需要注意的是 等差数列的前n项和， 不是等差数列求和
            """
            n = len(nums)
            return n * ( n - 1 ) / 2 - sum(nums)


.. caution:: 

    这题还有一种解法，使用位操作Bit Manipulation来解的，用到了异或操作的特性，相似的题目有Single Number 单独的数字, Single Number II 单独的数字之二和Single Number III 单独的数字之三。那么思路是既然0到n之间少了一个数，我们将这个少了一个数的数组合0到n之间完整的数组异或一下，那么相同的数字都变为0了，剩下的就是少了的那个数字了，参加代码如下：

.. code-block:: python

    class Solution(object):
        def onemissing(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            a = reduce(operator.xor, nums)
            b = reduce(operator.xor, range(len(nums) + 1))
            return a ^ b


.. caution:: 

    这道题还可以用二分查找法来做，我们首先要对数组排序，然后我们用二分查找法算出中间元素的下标，然后用元素值和下标值之间做对比，如果元素值大于下标值，则说明缺失的数字在左边，此时将right赋为mid，反之则将left赋为mid+1。那么看到这里，作为读者的你可能会提出，排序的时间复杂度都不止O(n)，何必要多此一举用二分查找，还不如用上面两种方法呢。对，你说的没错，但是在面试的时候，有可能人家给你的数组就是排好序的，那么此时用二分查找法肯定要优于上面两种方法，所以这种方法最好也要掌握以下~

这个解决办法到后面自己写出来 刷二遍的时候





535. Encode and Decode TinyURL 
------------------------------

Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


523. Continuous Subarray Sum 
----------------------------


Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Note:

    #. The length of the array won't exceed 10,000.
    #. You may assume the sum of all the numbers is in the range of a signed 32-bit integer.


469. Convex Polygon
-------------------
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

Note:

    There are at least 3 and at most 10,000 points.
    Coordinates are in the range -10,000 to 10,000.
    You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.

Example 1:

[[0,0],[0,1],[1,1],[1,0]]

Answer: True

Explanation:

Example 2:

[[0,0],[0,10],[10,10],[10,0],[5,5]]

Answer: False

Explanation:

题目大意：

给定一组点，顺序相连可以组成一个多边形。判断多边形是否是凸包。

注意：

    最少3个，最多10000个点
    坐标在-10,000 到 10,000之间。
    你可以假设组成的多边形总是简单多边形。换言之，我们确保每个顶点都是两条边的交点，其他边不会相互交叉。

解题思路：

遍历顶点，判断相邻三个顶点A、B、C组成的两个向量(AB, AC)的叉积是否同负同正。




423. Reconstruct Original Digits from English 
---------------------------------------------

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:

    #. Input contains only lowercase English letters.
    #. Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
    Input length is less than 50,000.

Example 1:

Input: "owoztneoer"

Output: "012"

Example 2:

Input: "fviefuro"

Output: "45"



413. Arithmetic Slices 
----------------------

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7


A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

