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

277. Find the Celebrity
-----------------------

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.



.. code-block:: python

    # brute-force solution
    def findCelebrity(self, n):
        for i in xrange(n):
            tmp = range(i) + range(i+1, n)
            ind = 0
            while ind < len(tmp) and not knows(i, tmp[ind]) and knows(tmp[ind], i):
                ind += 1
            if ind == len(tmp):
                return i
        return -1


