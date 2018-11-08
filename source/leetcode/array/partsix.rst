题号 40、39、34、33、31、18、16、15、11
================================================



39. Combination Sum 
-------------------

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    #. All numbers (including target) will be positive integers.
    #. The solution set must not contain duplicate combinations.

Example 1:
::
    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
      [7],
      [2,2,3]
    ]

Example 2:
::
    Input: candidates = [2,3,5], target = 8,
    A solution set is:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]

.. code-block:: python

    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in xrange(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)  


40. Combination Sum II
----------------------


Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    #. All numbers (including target) will be positive integers.
    #. The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
::
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]

.. code-block:: python

    def combine(self, n, k):
        res = []
        self.dfs(xrange(1,n+1), k, 0, [], res)
        return res
        
    def dfs(self, nums, k, index, path, res):
        #if k < 0:  #backtracking
            #return 
        if k == 0:
            res.append(path)
            return # backtracking 
        for i in xrange(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)       
                
                
    def combinationSum3(self, k, n):
        res = []
        self.dfs(xrange(1,10), k, n, 0, [], res)
        return res
        
    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0: # backtracking 
            return 
        if k == 0 and n == 0: 
            res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)        
                
                
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return  # backtracking 
        for i in xrange(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates, target-candidates[i], i+1, path+[candidates[i]], res)  

    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in xrange(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)          
        


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


This problem is more or less the same as Find Minimum in Rotated Sorted Array. And one key difference is as stated in the solution tag. That is, due to duplicates, we may not be able to throw one half sometimes. And in this case, we could just apply linear search and the time complexity will become O(n).

The idea to solve this problem is still to use invariants. We set l to be the left pointer and r to be the right pointer. Since duplicates exist, the invatiant is nums[l] >= nums[r] (if it does not hold, then nums[l] will simply be the minimum). We then begin binary search by comparing nums[l], nums[r] with nums[mid].

If nums[l] = nums[r] = nums[mid], simply apply linear search within nums[l..r].
If nums[mid] <= nums[r], then the mininum cannot appear right to mid, so set r = mid;
If nums[mid] > nums[r], then mid is in the first larger half and r is in the second smaller half, so the minimum is to the right of mid: set l = mid + 1.
The code is as follows.

.. code-block:: python

    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
        
        
    def search(self, nums, target):
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return nums[l] == target

    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:  # here should include "==" case
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1   

    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False            
                
                
    Here is another version which moves the right pointer one step forward when nums[mid] == nums[r], as we don't know target is in left part or in right part:

    def search(self, nums, target):
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return nums[l] == target            


31. Next Permutation 
--------------------

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
::
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1


.. code-block:: python

    def nextPermutation(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1

            
        
    def nextPermutation(self, nums):
        i = l = len(nums)-1
        while i > 0:
            # find the right most pair where nums[i] > nums[i-1]
            if nums[i] > nums[i-1]:
                tmp = 0
                for j in xrange(l, i-1, -1):
                    if nums[j] > nums[i-1]:
                        tmp = j
                        break
                # exchange nums[i-1] and the right most element which larger than nums[i-1] 
                nums[i-1], nums[tmp] = nums[tmp], nums[i-1]
                # reverse from i to the end
                for j in xrange(i, 1+i+(l-i)/2):
                    nums[j], nums[l+i-j] = nums[l+i-j], nums[j]
                break
            i -= 1
        # if nums are in descending order
        if i == 0:
            nums.reverse()
        
        
        
    def nextPermutation(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i > 0:
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = reversed(nums[i:])
        
        




18. 4Sum
--------


Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
::
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]

16. 3Sum Closest 
----------------

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


15. 3Sum
--------

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
::
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

清晰的思路：

*. 排序
*. 固定左边，如果左边重复，继续
*. 左右弄边界，去重，针对不同的左右边界情况处理

.. code-block:: python

    class Solution(object):
        def threeSum(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            n, res = len(nums), []
            nums.sort()
            for i in range(n):
                if i > 0 and nums[i] == nums[i-1]:   # 因为i=0这个元素会直接往下执行
                    continue
                l, r = i+1, n-1
                while l < r:
                    tmp = nums[i] + nums[l] + nums[r]
                    if tmp == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]: 
                            l += 1
                        while l < r and nums[r] == nums[r+1]: 
                            r -= 1
                    elif tmp > 0:
                        r -= 1
                    else:
                        l += 1
            return res

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

.. code-block:: python

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res


11. Container With Most Water 
-----------------------------

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2. 

