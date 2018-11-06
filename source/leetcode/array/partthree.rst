题目序号 26、27、169、581、566、35、88、243、561、268
============================================================


26. Remove Duplicates from Sorted Array
---------------------------------------

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.


For example:
::

    Given input array nums = [1,1,2],
    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.




.. code-block:: JavaScript

    function sort_unique(arr) {
        if (arr.length === 0) return arr;
        arr = arr.sort(function (a, b) { return a*1 - b*1; });
        var ret = [arr[0]];
        for (var i = 1; i < arr.length; i++) { // start loop at 1 as element 0 can never be a duplicate
            if (arr[i-1] !== arr[i]) {
                ret.push(arr[i]);
            }
        }
        return ret;
    }
    console.log(sort_unique(['237','124','255','124','366','255']));
    //["124", "237", "255", "366"]

    /**
     * @param {number[]} nums
     * @return {number}
     */
    var removeDuplicates = function(nums) {
        if(nums === null || nums.length === 0) return 0;
        if(nums.length == 1) return 1;
        var count = 0;
        for(var i = 0; i< nums.length; i++) {
            if(nums[i] != nums[i+1]){
                count ++;
                nums[count] = nums[i+1];
            }
        }
        return count;
    };



Remove Duplicates from Sorted Array II
--------------------------------------

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?
For example:
:: 
    Given sorted array A = [1,1,1,2,2,3],

    Your function should return length = 5, and A is now [1,1,2,2,3].

.. code-block :: JavaScript
    
    /**
     * @param {number[]} nums
     * @return {number}
     */
    var removeDuplicates = function(nums) {
        if(nums == null || nums.length == 0) return 0;
        if(nums.length == 1) return 1;
        var count = 0;
        for(var i = 1 ; i < nums.length ; i++){
            if(nums[count] != nums[i]){
                count++;
                nums[count] = nums[i];
            }
        }
        return ++count;
    };

27. Remove Element
------------------

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
::
    Given input array nums = [3,2,2,3], val = 3

    Your function should return length = 2, with the first two elements of nums being 2.

我是这样理解的，给定一个数组，然后给定一个值，把数组里面对应的值都删除，最后返回的结果是新数组的长度

.. code-block:: python

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


.. code-block:: python

    # not in place
    def removeElement1(self, nums, val):
        res, count = [], 0
        for item in nums:
            if item != val:
                res.append(item)
                count += 1
        nums[:] = res
        return count

    # not in place    
    def removeElement2(self, nums, val):
        nums[:] = [item for item in nums if item != val]
        return len(nums)
        
    # in place
    def removeElement(self, nums, val):
        l, r, count = 0, len(nums)-1, len(nums)
        while l <= r:
            while l <= r and nums[l] == val:
                l += 1
            while l <= r and nums[r] != val:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
        for _ in xrange(l):
            del nums[0]
        return count - l




    A version which is easier to understand:

    # in place, two-pointer
    def removeElement(self, nums, val):
        l = len(nums)-1
        for i in xrange(l+1):
            if nums[i] == val:
                while l > i and nums[l] == val:
                    l -= 1
                if l == i:
                    return l
                nums[i], nums[l] = nums[l], nums[i]
        return l+1
        
    # A shorter in-place version:

     def removeElement(self, nums, val):
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return l
        
    # A even shorter in-place version:

    def removeElement(self, nums, val):
        tail = -1
        for i in xrange(len(nums)):
            if nums[i] != val:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1






169. Majority Element
---------------------

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.


给定一个长度为n的数组，寻找其中的“众数”。众数是指出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的并且数组中的众数永远存在。

#. 排序法 时间 O(NlogN) 空间 O(1) 将数组排序，这时候数组最中间的数肯定是众数。
#. 位操作法 时间 O(N) 空间 O(1) 假设一个数是最多只有32位的二进制数，那么我们从第一位到第32位，对每一位都计算所有数字在这一位上1的个数，如果这一位1的个数大于一半，说明众数的这一位是1，如果小于一半，说明大多数的这一位是0。
#. 投票法  时间 O(N) 空间 O(1) 记录一个candidate变量，还有一个counter变量，开始遍历数组。如果新数和candidate一样，那么counter加上1，否则的话，如果counter不是0，则counter减去1，如果counter已经是0，则将candidate更新为这个新的数。因为每一对不一样的数都会互相消去，最后留下来的candidate就是众数。

Majority Element II
-------------------

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.


复杂度

时间 O(N) 空间 O(1)

思路

上一题中，超过一半的数只可能有一个，所以我们只要投票出一个数就行了。而这题中，超过n/3的数最多可能有两个，所以我们要记录出现最多的两个数。同样的两个candidate和对应的两个counter，如果遍历时，某个候选数和到当前数相等，则给相应计数器加1。如果两个计数器都不为0，则两个计数器都被抵消掉1。如果某个计数器为0了，则将当前数替换相应的候选数，并将计数器初始化为1。最后我们还要遍历一遍数组，确定这两个出现最多的数，是否都是众数。



.. code-block:: python

    

    # two pass + dictionary
    def majorityElement1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num in nums:
            if dic[num] > len(nums)//2:
                return num
        
    # one pass + dictionary
    def majorityElement2(self, nums):
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            if dic[num] > len(nums)//2:
                return num
            else:
                dic[num] += 1 

    # TLE
    def majorityElement3(self, nums):
        for i in xrange(len(nums)):
            count = 0
            for j in xrange(len(nums)):
                if nums[j] == nums[i]:
                    count += 1
            if count > len(nums)//2:
                return nums[i]
                
    # Sotring            
    def majorityElement4(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        
    # Bit manipulation    
    def majorityElement5(self, nums):
        bit = [0]*32
        for num in nums:
            for j in xrange(32):
                bit[j] += num >> j & 1
        res = 0
        for i, val in enumerate(bit):
            if val > len(nums)//2:
                # if the 31th bit if 1, 
                # it means it's a negative number 
                if i == 31:
                    res = -((1<<31)-res)
                else:
                    res |= 1 << i
        return res
                
    # Divide and Conquer
    def majorityElement6(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        a = self.majorityElement(nums[:len(nums)//2])
        b = self.majorityElement(nums[len(nums)//2:])
        if a == b:
            return a
        return [b, a][nums.count(a) > len(nums)//2]
        
    # the idea here is if a pair of elements from the
    # list is not the same, then delete both, the last 
    # remaining element is the majority number
    def majorityElement(self, nums):
        count, cand = 0, 0
        for num in nums:
            if num == cand:
                count += 1
            elif count == 0:
                cand, count = num, 1
            else:
                count -= 1
        return cand 
        


581. Shortest Unsorted Continuous Subarray
------------------------------------------

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
::
    Input: [2, 6, 4, 8, 10, 9, 15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

.. tip ::
    Note:

    Then length of the input array is in range [1, 10,000].
    The input array may contain duplicates, so ascending order here means <=.





566. Reshape the Matrix
-----------------------


In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
::
    Input: 

    nums = [[1,2],
            [3,4]]
    r = 1, c = 4
    Output: 

    [[1,2,3,4]]
    Explanation:

    The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

Example 2:
::
    Input: 
    nums = [[1,2],
            [3,4]]
    r = 2, c = 4
    Output: 

    [[1,2],
     [3,4]]

    Explanation:
    There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.


Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.



35. Search Insert Position
--------------------------


Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0


88. Merge Sorted Array
----------------------

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.


243. Shortest Word Distance
---------------------------

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example
::
    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

    Given word1 = “coding”, word2 = “practice”, return 3.
    Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.



561. Array Partition I
----------------------


Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
:: 
    Input: [1,4,3,2]

    Output: 4
    Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].



268. Missing Number
-------------------

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


