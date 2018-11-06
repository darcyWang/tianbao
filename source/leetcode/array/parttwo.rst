题目序号 532、643、644、605、66、1、167、448
============================================================


532. K-diff Pairs in an Array 
-----------------------------

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
:: 

    Input: [3, 1, 4, 1, 5], k = 2
    Output: 2

    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
::

    Input:[1, 2, 3, 4, 5], k = 1
    Output: 4

    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
::

    Input: [1, 3, 1, 5, 4], k = 0
    Output: 1

    Explanation: There is one 0-diff pair in the array, (1, 1).

Note:

    #. The pairs (i, j) and (j, i) count as the same pair.
    #. The length of the array won't exceed 10,000.
    #. All the integers in the given input belong to the range: [-1e7, 1e7].

寻找有多少组差的绝对值等于k的数。先对数组进行排序，然后用双指针从前向后搜索：

    #. 移动右指针，直到左右指针元素之差的绝对值大于等于k；
    #. 再移动左指针，直到左右指针元素之差的绝对值小于k；
    #. 重复1,2步直到右指针到达数组结尾，记录下出现过的k的次数；



643. Maximum Average Subarray I 
-------------------------------


Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
:: 

    Input: [1,12,-5,-6,50,3], k = 4
    Output: 12.75

    Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:

    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].
    滑动窗口（Sliding Window）




644. Maximum Average Subarray II
--------------------------------
Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
::

    Input: [1,12,-5,-6,50,3], k = 4
    Output: 12.75
    
    Explanation:
    when length is 5, maximum average value is 10.8,
    when length is 6, maximum average value is 9.16667.
    Thus return 12.75.

Note:

    1 <= k <= n <= 10,000.
    Elements of the given array will be in range [-10,000, 10,000].
    The answer with the calculation error less than 10-5 will be accepted.

题目大意：
二分枚举答案（Binary Search）
给定包含n个整数的数组，寻找长度大于等于k的连续子数组的平均值的最大值。


605. Can Place Flowers 
----------------------

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
::
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: True

Example 2:
::
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: False

Note:

#. The input array won't violate no-adjacent-flowers rule.
#. The input array size is in the range of [1, 20000].
#. n is a non-negative integer which won't exceed the input array size.

给定一个01数组代表一排花盆，0代表是可以种花，1代表不可以。种花的时候我们要确保左右两边的花盆是空的。问能不能种n株花。

.. code-block :: Javascript

    /**
     * @param {number[]} flowerbed
     * @param {number} n
     * @return {boolean}
     */
    var canPlaceFlowers = function(flowerbed, n) {
        if(n == 0) {
            return true;
        }
        var n_count = 0;
        var null_count = 0;
        flowerbed.unshift(0);
        flowerbed.push(0);
        for(let i=0; i<=flowerbed.length; i++){
            if(i == flowerbed.length || flowerbed[i] == 1) {
                if(null_count > 2) {
                    n_count += Math.floor((null_count-1)/2);
                    if(n_count >= n) {
                        return true;
                    }
                }
                null_count = 0;
            } else {
                null_count ++;
            }
        }
        return false;
    };

.. code-block :: Python

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt = 0
        for i in xrange(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i-1>=0 and flowerbed[i-1]==1:
                continue
            if i+1<len(flowerbed) and flowerbed[i+1]==1:
                continue
            flowerbed[i] = 1
            cnt += 1
        return cnt>=n

624. Maximum Distance in Arrays
-------------------------------

Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
::

    Input: [[1,2,3],
            [4,5],
            [1,2,3]]
    Output: 4

    Explanation: 
    One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.


Note:

    #. Each given array will have at least 1 number. There will be at least two non-empty arrays.
    #. The total number of the integers in all the m arrays will be in the range of [2, 10000].
    #. The integers in the m arrays will be in the range of [-10000, 10000].




.. caution ::
    对于这道题目，我想的是把数组里面的子数组都合并成一个数组，然后对合并后的数组进行排序，最后两个值相减就得到最大距离了


.. code-block:: Javascript

    var baby = [[1,2,3],
               [4,5],
               [1,2,3]], 
               hello = [];
    baby.map(function(s){ hello.push(...s)});
    var test = hello.sort().pop() - hello.sort().shift();
    console.log( test )


66. Plus One
------------

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.


.. caution::
    当时第一个反应是，把数组转成字符串然后进行数字计算 最后转化成数组。这样做太傻比了，所以需要参考别人的写法，然后基于他们的写法做出相应自己的改造


.. code-block:: Python

    class Solution(object):
        def plusOne(self, digits):
            """
            :type digits: List[int]
            :rtype: List[int]
            """
            if digits[-1] < 9:
                digits[-1] = digits[-1] + 1
            else:            
                if len(digits) == 1:
                    digits = [1,0] 
                else:
                    digits = self.plusOne(digits[:-1])  + [0]
             
            return digits
        
        
    test = Solution()
    num1 = [1,9,9,9,9,9]
    print test.plusOne(num1)



.. code-block:: Python

    class Solution:
        # @param digits, a list of integer digits
        # @return a list of integer digits
        def plusOne(self, digits):
            flag = 1
            for i in range(len(digits)-1, -1, -1):
                digits[i] = (digits[i] + 1) % 10 # 加1模10，如果没有进位则跳出循环，否则高一位加1
                if digits[i]:
                    flag = 0
                    break 
            if flag: # 如果每一位都进位了，则在数组第一位添加1
                digits.insert(0,1)
            return(digits)

.. code-block:: Javascript

    var plusOne = function(digits) {

        // at first will need to addOne 
      var addOneNow = true;  

        // start from the last element
      for (var i = digits.length - 1; i >= 0;i--){

        // if the currentDigit is less 0~8 
        if ( digits[i] < 9){

          // increment the number by 1
          digits[i]++;

           // the end
          return digits;
        }else{ // if the currentDigit is 9
         
        // make it 0, and move to the former element
         digits[i] = 0; 
        }
       }
      
       // if there is still 1 to add
       if(addOneNow){ 
       
       // make [9,9,9], [1,0,0,0] not [0,0,0]
         digits.unshift(1); 
       }
     
       return digits;
    };


1. Two Sum
----------


Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
::
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].



.. code-block :: Javascript

    var twoSum = function(nums, target) {

        var map = {};
        for(var i = 0 ; i < nums.length ; i++){
            var v = nums[i];

            if(map[target-v] >= 0){
                // 如果 target - v可以在map中找到值x，代表之前已經出現過值x， target = x + v
                // 因此回传 x的位置與目前v的位置  
                return [map[target-v],i]
            } else {
                // 使用map存储目前的數字與其位置  
                map[v] = i;
            }
        }
    };




167. Two Sum II - Input array is sorted
---------------------------------------

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.
::

    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2


Two Sum III - Data structure design
-----------------------------------

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
::
    add(1); add(3); add(5);
    find(4) -> true
    find(7) -> false



.. code-block:: python

    class TwoSum:

        def __init__(self):
            self.ctr = {}

        def add(self, number):
            if number in self.ctr:
                self.ctr[number] += 1
            else:
                self.ctr[number] = 1

        def find(self, value):
            ctr = self.ctr
            for num in ctr:
                if value - num in ctr and (value - num != num or ctr[num] > 1):
                    return True
            return False    
        
        
    class TwoSum:

        def __init__(self):
            self.ctr = collections.defaultdict(int)

        def add(self, number):
            self.ctr[number] += 1

        def find(self, value):
            ctr = self.ctr
            return any(value - num in ctr and (value - num != num or ctr[num] > 1)
                       for num in ctr)  
         



448. Find All Numbers Disappeared in an Array
---------------------------------------------

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
::
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [5,6]

给定一个整数数组，其中1 ≤ a[i] ≤ n (n = 数组长度)，一些元素出现两次，其他的出现一次。

寻找所有[1, n]中没有出现在数组中的元素。

可以不使用额外空间并在O(n)运行时间求解吗？你可以假设返回列表不算额外空间。

.. note ::

    解题思路：正负号标记法 

    #. 遍历数组nums，记当前元素为n，令nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
    #. 再次遍历nums，将正数对应的下标+1返回即为答案，因为正数对应的元素没有被上一步骤标记过。


.. code-block:: python

    def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numset = set(nums)
        length = len(nums)
        result = []
        
        for i in range(1,length+1):
            result.append(i)
        
        resultset = set(result)
        print resultset
        print numset
        final = resultset - numset
        print final
        result = list(final)
        
        return result


    print findDisappearedNumbers([4,3,2,7,8,2,3,1]);



