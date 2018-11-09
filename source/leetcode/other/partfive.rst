题目序号
=================================




201. Bitwise AND of Numbers Range
---------------------------------

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
::
    Input: [5,7]
    Output: 4

Example 2:
::
    Input: [0,1]
    Output: 0


.. code-block:: python

    def rangeBitwiseAnd1(self, m, n):
        d = n-m
        p = 0
        while d:
            p += 1
            d /= 2
        return ((m&n)>>p)<<p
        
    def rangeBitwiseAnd2(self, m, n):
        if m == n:
            return m
        return self.rangeBitwiseAnd(m>>1, n>>1) << 1
        
    def rangeBitwiseAnd3(self, m, n):
        p = 0
        while m != n:
            m >>= 1
            n >>= 1
            p += 1
        return m << p
        
    def rangeBitwiseAnd(self, m, n):
        p = 0
        q = m^n
        while q:
            p += 1
            q >>= 1
        return ((m&n)>>p)<<p


238. Product of Array Except Self
---------------------------------

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
::
    Input:  [1,2,3,4]
    Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

.. code-block:: python

    # two-round solution     
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        for i in xrange(1, len(nums)): # from left to right 
            res[i] = res[i-1] * nums[i-1]
        tmp = 1
        for i in xrange(len(nums)-2, -1, -1): # from right to left
            tmp *= nums[i+1]
            res[i] *= tmp
        return res



