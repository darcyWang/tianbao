题目序号 
============================================================



46. Permutations
----------------

Given a collection of distinct integers, return all possible permutations.

Example:
::
    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]


.. code-block:: python

    # DFS
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)  
        

47. Permutations II
-------------------


Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
::
    Input: [1,1,2]
    Output:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]


.. code-block:: python

    # DFS
    def permuteUnique(self, nums):
        res, visited = [], [False]*len(nums)
        nums.sort()
        self.dfs(nums, visited, [], res)
        return res
        
    def dfs(self, nums, visited, path, res):
        if len(nums) == len(path):
            res.append(path)
            return 
        for i in xrange(len(nums)):
            if not visited[i]: 
                if i>0 and not visited[i-1] and nums[i] == nums[i-1]:  # here should pay attention
                    continue
                visited[i] = True
                self.dfs(nums, visited, path+[nums[i]], res)
                visited[i] = False  

    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)  
                    

78. Subsets
-----------


Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
::
    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]


.. code-blokc:: python

    # DFS recursively 
    def subsets1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
        
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
            
    # Bit Manipulation    
    def subsets2(self, nums):
        res = []
        nums.sort()
        for i in xrange(1<<len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
        
    # Iteratively
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res

    # DFS  
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
        
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)    
        

90. Subsets II
--------------

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
::
    Input: [1,2,2]
    Output:
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]


131. Palindrome Partitioning
----------------------------


Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:
::
    Input: "aab"
    Output:
    [
      ["aa","b"],
      ["a","a","b"]
    ]


.. code-block:: python

    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        if not s: # backtracking
            res.append(path)
        for i in xrange(1, len(s)+1):
            if self.isPar(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
                
    def isPar(self, s):
        return s == s[::-1]


164. Maximum Gap
----------------

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.

.. code-block:: python

    class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2 or min(num) == max(num):
            return 0
        a, b = min(num), max(num)
        size = math.ceil((b-a)/(len(num)-1))
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        for n in num:
            b = bucket[(n-a)//size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))



    def maximumGap(self, nums):
        if len(nums) < 2 or max(nums)-min(nums) == 0:   # in case bsize == 0
            return 0
        maxn,minn,lenn = max(nums),min(nums),len(nums)
        bsize = (maxn - minn + 1.0) / lenn  # could have interger issue on OJ
        buckets = [[2**31-1, -1] for _ in range(lenn+1)]
        for i in nums:
            place = int( (i-minn) // bsize )
            buckets[place][0] = min(i, buckets[place][0])
            buckets[place][1] = max(i, buckets[place][1])
        res, prev = 0, buckets[0][0]
        for i in buckets:
            if i != [2**31-1, -1]:
                res = max(res, i[0]-prev)
                prev = i[1]
        return res













