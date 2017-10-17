# -*- coding: utf-8 -*-
#!/usr/bin/env python


class Solution:

    def removeDuplicates(self, A):
        if None == A:
            return 0
        len_A = len(A)
        if len_A <= 1:
            return len_A

        m = 0
        n = 1
        count = 1
        while n < len_A:
            if A[m] != A[n]:
                count = 1
                m += 1
                if m != n:
                    A[m] = A[n]
            elif count >= 2:
                count += 1
            else:
                m += 1
                count += 1
                if m != n:
                    A[m] = A[n]
            n += 1
        return m + 1

    def oneDuplicates(self, A):
        if len(A) <= 2: return len(A)
        prev = 1; curr = 2
        while curr < len(A):
            if A[curr] == A[prev] and  A[curr] == A[prev - 1]:
                curr += 1
            else:
                prev += 1
                A[prev] = A[curr]
                curr += 1
        return prev + 1
    
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        """
        for x in nums[:]:
            if x == val:
                nums.remove(x)
        return len(nums)
    def removeElementTwo(self, nums, val):
        # @param  nums a list of integers
        # @param  val  an integer, value need to be removed
        # return an integer
        while val in nums: nums.remove(val)
        return len(nums)
    def removeElementThree(self, nums, val):
        k = 0
        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
            print i
            print nums
        return k

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(c ** 0.5) + 1):
            b2 = c - a ** 2
            if (int(b2 ** 0.5)) ** 2 == b2:
                return True
        return False
    def newSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        m = int(c ** 0.5)
        for a in range( m + 1):
            b = c - a ** 2
            if ( a ** 2 + b ** 2 ) == c:
                return True
        return False

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * ( n + 1 ) / 2 - sum(nums)




test = Solution()
l1 = [1,1,1,1,1,1,1,2,2,2,2,3,4]
l2 = [1,1,1,2,2,3]
# print '测试一下题目数组去重的第二种做法，就是去掉数组中重复3次以上的元素后数组的长度是 %d'%test.oneDuplicates(l1)

# print '测试一下具体的东西 %d'%test.removeElementThree(l2, 1)

# print '测试一下我自己改写的算法 %s'%test.judgeSquareSum(999999)

print '测试一下我自己改写的算法 %s'%test.missingNumber([0, 1, 3])




















































