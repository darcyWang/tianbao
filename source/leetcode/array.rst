数组Array部分
============

每个模块的都是按照从easy到hard，第一遍把所有的easy和medium都过一遍，
第二遍的时候开始把部分的hard看看




414. Third Maximum Number 
-------------------------

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
::
        Input: [3, 2, 1]

        Output: 1

        Explanation: The third maximum is 1.
Example 2:
::
        Input: [1, 2]

        Output: 2

        Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
::
        Input: [2, 2, 3, 1]

        Output: 1

        Explanation: Note that the third maximum here means the third maximum distinct number.
        Both numbers with value 2 are both considered as second maximum.

.. hint::

        给定一个整数数组，返回数组中第3大的数，如果不存在，则返回最大的数字。时间复杂度应该是O(n)或者更少。

        这道题让我们求数组中第三大的数，如果不存在的话那么就返回最大的数，题目中说明了这里的第三大不能和第二大相同，必须是严格的小于，而并非小于等于。这道题并不是很难，如果知道怎么求第二大的数，那么求第三大的数的思路都是一样的。那么我们用三个变量first, second, third来分别保存第一大，第二大，和第三大的数，然后我们遍历数组，如果遍历到的数字大于当前第一大的数first，那么三个变量各自错位赋值，如果当前数字大于second，小于first，那么就更新second和third，如果当前数字大于third，小于second，那就只更新third，注意这里有个坑，就是初始化要用长整型long的最小值，否则当数组中有INT_MIN存在时，程序就不知道该返回INT_MIN还是最大值first了



        思路：

        #. 先通过归并排序把数组有序化，然后除去数组中重复的元素，最后拿到第三大的元素。
        #. Python中有个collections模块，它提供了个类Counter，用来跟踪值出现了多少次。注意key的出现顺序是根据计数的从大到小。它的一个方法most_common(n)返回一个list, list中包含Counter对象中出现最多前n个元素。
        #. heapq模块有两个函数：nlargest() 和 nsmallest() 可以从一个集合中获取最大或最小的N个元素列表。heapq.nlargest (n, heap) 查询堆中的最大元素，n表示查询元素个数
        
.. code-block:: javascript

        var thirdMax = function(nums) {
                var count = 0, max=mid=small=-2147483648;
                for (var i in nums) {
                    if (count > 0 && nums[i] == max || count > 1 && nums[i] == mid) continue;
                    count++;
                    if (nums[i] > max) {
                        small = mid;
                        mid = max;
                        max = nums[i];
                    } else if (nums[i] > mid) {
                        small = mid;
                        mid = nums[i];
                    } else if (nums[i] > small) {
                        small = nums[i];
                    }
                }
                return count < 3 ? max : small;
        };


.. caution::
        
        看到这道题目的第一个思路是 对整个数组进行排序，判断数组的长度，然后去重，选出数组的第三个数字。
        但是这样是没有什么时间复杂度和空间复杂度之类的，看了别人的答案是命名3个变量，然后赋最小值，通过循环来把值替换



217. Contains Duplicate 
-----------------------


Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct. 


判断数组里面是否有重复的元素


.. code-block:: javascript

        function hasDuplicates(array) {
            return (new Set(array)).size !== array.length;
        }

        function hasDuplicates(array) {
            var valuesSoFar = Object.create(null);
            for (var i = 0; i < array.length; ++i) {
                var value = array[i];
                if (value in valuesSoFar) {
                    return true;
                }
                valuesSoFar[value] = true;
            }
            return false;
        }

        function hasDuplicates(array) {
            var valuesSoFar = [];
            for (var i = 0; i < array.length; ++i) {
                var value = array[i];
                if (valuesSoFar.indexOf(value) !== -1) {
                    return true;
                }
                valuesSoFar.push(value);
            }
            return false;
        }

        def containsDuplicate(baby):
            return len(baby) != len(set(baby))

        def newDuplicate(baby):
            numSet = set()
            for num in baby:
                if num in numSet:
                    return True
                numSet.add(num)
            return False

判断了有重复的元素，怎么去重

.. code-block:: javascript

        var arr = [9, 9, 111, 2, 3, 4, 4, 5, 7];
        var sorted_arr = arr.slice().sort(); // You can define the comparing function here. 
                                             // JS by default uses a crappy string compare.
                                             // (we use slice to clone the array so the
                                             // original array won't be modified)
        var results = [];
        for (var i = 0; i < arr.length - 1; i++) {
            if (sorted_arr[i + 1] == sorted_arr[i]) {
                results.push(sorted_arr[i]);
            }
        }

        console.log(results);

219. Contains Duplicate II 
--------------------------

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k. 

https://github.com/jzhangnu/Leetcode-JS-Solutions/issues/43


.. caution::
        
        这道题目还是有些没搞明白，从一个数组里面判断重复的元素相间隔的距离，
        如果数组里面有很多重复的元素，该怎么搞


283. Move Zeroes 
----------------

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:

#. You must do this in-place without making a copy of the array.
#. Minimize the total number of operations.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


复杂度
时间 O(N) 空间 O(1)

实际上就是将所有的非0数向前尽可能的压缩，最后把没压缩的那部分全置0就行了。比如103040，先压缩成134，剩余的3为全置为0。过程中需要一个指针记录压缩到的位置。


.. code-block:: javascript

        var numbers = [0,0,0,0,0,0,0,0,1,2,3,5,0,6,6,0,3,4,5,6,6,7,8,9,9,0,6,55,5,5,4,33,31,2,423,5,7,657,8,679,564,345,0,231,2,3,3,32,3,3,3,4,5,6,6,7,8,9,96,5,4,4,4,3,3,3,5,6,7,8,9,9];

        var moveZeros = function (arr) {
          for(var i = arr.length; i--;) {
              if(arr[i] === 0) {
                  arr.splice(i, 1);
                  arr.push(0);
              }
          }
          return arr;
        }


        var moveZeros = function (arr) {
          return arr.filter(function(x) {return x !== 0}).concat(arr.filter(function(x) {return x === 0;}));
        }

还是没有看到Python的写法



121. Best Time to Buy and Sell Stock 
------------------------------------

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
::
        Input: [7, 1, 5, 3, 6, 4]
        Output: 5

        max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:
::
        Input: [7, 6, 4, 3, 1]
        Output: 0

        In this case, no transaction is done, i.e. max profit = 0.

这是卖股票的第一个题目，根据题意我们知道只能进行一次交易，但需要获得最大的利润，所以我们需要在最低价买入，最高价卖出，当然买入一定要在卖出之前。

对于这一题，还是比较简单的，我们只需要遍历一次数组，通过一个变量记录当前最低价格，同时算出此次交易利润，并与当前最大值比较就可以了。

.. caution::
        
        这道题目一共有四个，然后从最简单的开始。可以参考下面两个链接

        #. http://www.forz.site/2017/06/24/Best-Time-to-Buy-and-Sell-Stock/
        #. https://segmentfault.com/a/1190000003483697

.. code-block:: javascript

        /**
         * @param {number[]} prices
         * @return {number}
         * More like greedy. Reserve the partial optimal and replace it when
         * a better result is found.
         * With complextity of O(n)
         */
        var maxProfit = function (prices) {
            var length = prices.length,
                min = Infinity,
                res = -Infinity;

            for (var i = 0; i <= length - 1; i++) {
                if (prices[i] < min) {
                    min = prices[i];
                } else if (prices[i] > min && prices[i] - min > res) {
                    res = prices[i] - min;
                }
            }

            if (isFinite(res)) {
                return res;
            } else {
                return 0;
            }
        };

.. code-block:: Python

        def maxProfit(self, prices):
            if prices is None or len(prices) <= 1:
                return 0

            profit = 0
            cur_price_min = 2**31 - 1
            for price in prices:
                profit = max(profit, price - cur_price_min)
                cur_price_min = min(cur_price_min, price)

            return profit


122. Best Time to Buy and Sell Stock II 
---------------------------------------

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).




123. Best Time to Buy and Sell Stock III
----------------------------------------
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).



188. Best Time to Buy and Sell Stock IV
---------------------------------------


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

.. code-block:: Python

       def maxProfit(self, k, prices):
            n = len(prices)
            if k >= (n>>1):return self.maxProfit2(prices)
            dp =[[0 for j in xrange(n)]for i in xrange(k+1)]
     
            for i in xrange(1,k+1):
                maxTemp=-prices[0]
                for j in xrange(1,n):
                    dp[i][j]=max(dp[i][j-1],prices[j] + maxTemp)
                    maxTemp =max(maxTemp,dp[i-1][j-1] - prices[j])
            return dp[k][n-1]
     
        def maxProfit2(self,prices):
            ans = 0
            for i in xrange(1,len(prices)):
                if prices[i]>prices[i-1]:
                    ans +=prices[i]-prices[i-1]
            return ans

53. Maximum Subarray 
--------------------

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



.. code-block:: Python

        def kadane(a):

          if not a:
            raise ValueError('Empty array!')
            
          current_sum, current_start = a[0], 0
          result = (current_sum, 0, 0)

          for i, item in enumerate(a[1:], start=1):

            if current_sum + item < item:
              # discard the previous subarray, it's not optimal
              current_start = i
              current_sum = item
            else:
              current_sum += item

            if current_sum > result[0]:
              # update the maximum sum and start and end indices
              result = (current_sum, current_start, i)

          return result

JavaScript版本
https://github.com/Arnold134777/LeetCode-LintCode/blob/master/javascript/Maximum%20Subarray/main.js


189. Rotate Array 
-----------------


Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II


这道题目有一种很经典的做法：三步反转法。结合题目中给出的样例进行说明：
首先根据kk的大小，将字符串S切分为A、B两部分(A的长度为n−kn−k，B的长度为kk)，则A=”1234”，B=”567”；
将A和B分别进行反转，得A=”4321”，B=”765”，AB=”4321765”；
将AB整体进行反转，得AB=”5671234”。
这样就得到了答案，是不是很神奇？其实该方法可以通过数学原理进行说明：利用矩阵求逆的原理，假设原矩阵为AB，需要求解BA，那么求解过程如下所示：
这里应该是个数学公式
BA=(A−1B−1)−1
BA=(A−1B−1)−1
相信到这里，你对三步反转法已经有了一个深刻的认识。


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

.. code-block :: javscript

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

Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].

.. caution ::

        对于这道题目，我想的是把数组里面的子数组都合并成一个数组，然后对合并后的数组进行排序，最后两个值相减就得到最大距离了


.. code-block :: Javscript

        var baby = [[1,2,3],
                [4,5],
                [1,2,3]], hello = [];
        baby.map(function(s){ hello.push(...s)});
        var test = hello.sort().pop() - hello.sort().shift();
        console.log( test )


66. Plus One
------------


Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.


.. caution ::

        当时第一个反应是，把数组转成字符串然后进行数字计算 最后转化成数组。这样做太傻比了，所以需要参考别人的写法，然后基于他们的写法做出相应自己的改造


.. code-block :: Python

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



.. code-block :: Python

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

.. code-block :: Javscript

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
                    // 因此回傳 x的位置與目前v的位置  
                    return [map[target-v],i]
                } else {
                    // 使用map儲存目前的數字與其位置  

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
add(1); add(3); add(5);
find(4) -> true
find(7) -> false




448. Find All Numbers Disappeared in an Array
---------------------------------------------


Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]




26. Remove Duplicates from Sorted Array
---------------------------------------

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.




27. Remove Element
------------------


Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.



169. Majority Element
---------------------

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.



581. Shortest Unsorted Continuous Subarray
------------------------------------------

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
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
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
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

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


628. Maximum Product of Three Numbers
-------------------------------------

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.






119. Pascal's Triangle II
-------------------------

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?



561. Array Partition I
----------------------


Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
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

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


485. Max Consecutive Ones
-------------------------




Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000


118. Pascal's Triangle
----------------------


Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return
::
        [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ]


621. Task Scheduler 
-------------------

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:

Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:

    The number of tasks is in the range [1, 10000].
    The integer n is in the range [0, 100].






621. Task Scheduler 
-------------------


Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:

Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:

    The number of tasks is in the range [1, 10000].
    The integer n is in the range [0, 100].


这是一道贪心策略的题目。原题的大意有一定的操作系统知识背景，大致是说，给出任务集，每个时间片只能完成任意一个任务，同一类任务必须至少相隔n个时间片，求完成任务集的任务最少需要多少时间片。 
题目中给出的例子是： tasks = [‘A’,’A’,’A’,’B’,’B’,’B’], n = 2。完成的最少时间片的情况是： A -> B -> idle -> A -> B -> idle -> A -> B。链中不能出现A -> B -> A……的情况，是因为同类任务A必须中间至少相隔2个任务。 
很明显，这是一道关于贪心算法的题目。贪心的策略是：尽可能少地让计算机闲着，即尽可能少地出现链中idle的情况。题目要求，在每一轮n+1个时间间隙中，不能出现相同的任务。如果一次能有（n+1）个不同任务排成一个任务集，那么这个这个任务集是完美的，因为从这个任务集到下一个任务集，中间不需要出现idle，即计算机没有闲着的时刻。那么，接下来的问题，如果在每一轮n+1个时间间隙中，能够选择的不同种类的任务的个数，大于n+1，那么优先选择哪些任务呢？很明显，我们要优先选择那些数量多的任务，这里用到的也是贪心。比如，tasks = [‘A’,’A’,’A’,’B’,’C’,’D’], n = 2。那么完成任务的最小时间链是：A -> B -> C -> A -> D -> idle -> A，答案为7。而不是 B -> C -> D-> A -> idle -> idle -> A -> idle -> idle -> A，答案为10。在任何情况下，我们都要把任务数量多的种类的任务最优先安排，这样是为了避免到最后只剩下单独一个任务的时候消耗太多的 idle。

CPU执行任务调度，任务用字符数组tasks给出，每两个相同任务之间必须执行n个不同的其他任务或者空闲。

求最优调度策略下的CPU运行周期数。


https://github.com/kamyu104/LeetCode/blob/master/Python/task-scheduler.py


https://github.com/csujedihy/lc-all-solutions/blob/master/621.task-scheduler/task-scheduler.py





611. Valid Triangle Number 
--------------------------



Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Note:

    The length of the given array won't exceed 1000.
    The integers in the given array are in the range of [0, 1000].


对于一个三角形，只要满足两边之和大于第三边即可。这题可采用双指针遍历。

首先把数组排序一遍，保证其有序。

其次，遍历数组，每一个数字都作为第三条边的选择，然后在前面的数字中通过双指针来决定第一条边和第二条边。对于任何一个可能的三角形，比如下例，3 + 7 > 9，那么如果第二条边（7）不变，所以第一条边（3）之后的数字都可以是解。



https://aaronice.gitbooks.io/lintcode/content/two_pointers/triangle_count.html


565. Array Nesting 
------------------

A zero-indexed array A consisting of N different integers is given. The array contains all integers in the range [0, N - 1].

Sets S[K] for 0 <= K < N are defined as follows:

S[K] = { A[K], A[A[K]], A[A[A[K]]], ... }.

Sets S[K] are finite for each K and should NOT contain duplicates.

Write a function that given an array A consisting of N integers, return the size of the largest set S[K] for this array.

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

Note:

    N is an integer within the range [1, 20,000].
    The elements of A are all distinct.
    Each element of array A is an integer within the range [0, N-1].



562. Longest Line of Consecutive One in Matrix
----------------------------------------------
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:

Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.


给定01矩阵M，计算矩阵中一条线上连续1的最大长度。一条线可以为横向、纵向、主对角线、反对角线。

提示：给定矩阵元素个数不超过10,000


这道题给了我们一个二维矩阵，让我们求矩阵中最长的连续1，连续方向任意，可以是水平，竖直，对角线或者逆对角线均可。那么最直接最暴力的方法就是四个方向分别来统计最长的连续1，其中水平方向和竖直方向都比较容易，就是逐行逐列的扫描，使用一个计数器，如果当前位置是1，则计数器自增1，并且更新结果res，否则计数器清零。对于对角线和逆对角线需要进行些坐标转换，对于一个mxn的矩阵，对角线和逆对角线的排数都是m+n-1个，难点在于我们要确定每一排上的数字的坐标，如果i是从0到m+n-1之间遍历，j是在i到0之间遍历，那么对角线的数字的坐标就为(i-j, j)，逆对角线的坐标就为(m-1-i+j, j)，这是博主千辛万苦试出来的T.T，如果能直接记住，效果肯定棒！那么有了坐标转换，求对角线和逆对角线的连续1也就不是啥难事了，参见代码如下：


https://mikecoder.github.io/oj-code/2017/04/23/LongestLineofConsecutiveOneinMatrix/

560. Subarray Sum Equals K 
--------------------------

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


548. Split Array with Equal Sum
-------------------------------


Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

    0 < i, i + 1 < j, j + 1 < k < n - 1
    Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.

where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.

Example:

Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1

Note:

    1 <= n <= 2000.
    Elements in the given array will be in range [-1,000,000, 1,000,000].

https://wlypku.github.io/2017/04/02/Leetcode-week26/

https://github.com/csujedihy/lc-all-solutions/blob/master/548.split-array-with-equal-sum/split-array-with-equal-sum.py



531. Lonely Pixel I
-------------------
Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:

Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.

Note:

    The range of width and height of the input 2D array is [1,500].


533. Lonely Pixel II
--------------------
http://www.cnblogs.com/grandyang/p/6754499.html

Given a picture consisting of black and white pixels, and a positive integer N, find the number of black pixels located at some specific row R and column C that align with all the following rules:

    Row R and column C both contain exactly N black pixels.
    For all rows that have a black pixel at column C, they should be exactly the same as row R

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

Example:

Input:                                            
[['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'W', 'B', 'W', 'B', 'W']] 

N = 3
Output: 6
Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
        0    1    2    3    4    5         column index                                            
0    [['W', 'B', 'W', 'B', 'B', 'W'],    
1     ['W', 'B', 'W', 'B', 'B', 'W'],    
2     ['W', 'B', 'W', 'B', 'B', 'W'],    
3     ['W', 'W', 'B', 'W', 'B', 'W']]    
row index

Take 'B' at row R = 0 and column C = 1 as an example:
Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels. 
Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. They are exactly the same as row R = 0.

Note:

    The range of width and height of the input 2D array is [1,200].


给定一个包含字符'W'（白色）和'B'（黑色）的像素矩阵picture，以及一个整数N。

求所有同行同列恰好有N个'B'像素，并且这N行均相同的像素个数。


https://wormtooth.com/20170304-leetcode-contest22/



495. Teemo Attacking 
--------------------

 In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

Example 1:

Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. 
This poisoned status will last 2 seconds until the end of time point 2. 
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. 
So you finally need to output 4.

Example 2:

Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. 
This poisoned status will last 2 seconds until the end of time point 2. 
However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. 
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. 
So you finally need to output 3.

Note:

    You may assume the length of given time series array won't exceed 10000.
    You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.



https://www.liuchuo.net/archives/3209

https://github.com/yuanhui-yang/LeetCode/blob/master/Algorithms/teemo-attacking.cpp


442. Find All Duplicates in an Array 
------------------------------------

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]


380. Insert Delete GetRandom O(1) 
---------------------------------

Design a data structure that supports all following operations in average O(1) time.

    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();





哈希表 + 数组 （HashMap + Array）

利用数组存储元素，利用哈希表维护元素在数组中的下标

由于哈希表的新增/删除操作是O(1)，而数组的随机访问操作开销也是O(1)，因此满足题设要求

记数组为dataList，哈希表为dataMap

insert(val): 将val添至dataList末尾，并在dataMap中保存val的下标idx

remove(val): 记val的下标为idx，dataList末尾元素为tail，弹出tail并将其替换至idx处，在dataMap中更新tail的下标为idx，最后从dataMap中移除val

getRandom: 从dataList中随机选取元素返回


https://all4win78.wordpress.com/2016/08/18/leetcode-381-insert-delete-getrandom-o1-duplicates-allowed/


370. Range Addition
-------------------


Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Given:

    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]

Output:

    [-2, 0, 3, 5, 3]

Explanation:

Initial state:
[ 0, 0, 0, 0, 0 ]

After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]

After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]

After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]

解法：
这题与算法无关，是个数学题。思想是把所有需要相加的值存在第一个数，然后把这个范围的最后一位的下一位减去这个inc, 这样我所以这个范围在求最终值的时候，都可以加上这个inc，而后面的数就不会加上inc。


598. Range Addition II
----------------------


Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:

Input: 
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4
Explanation: 
Initially, M = 
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

After performing [2,2], M = 
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

After performing [3,3], M = 
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.

Note:

    The range of m and n is [1,40000].
    The range of a is [1,m], and the range of b is [1,n].
    The range of operations size won't exceed 10,000.


289. Game of Life 
-----------------

 According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.




287. Find the Duplicate Number 
------------------------------




 Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.



280. Wiggle Sort
----------------



    Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

    For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].


http://tiancao.me/Leetcode-Unlocked/LeetCode%20Locked/c1.42.html

https://nb4799.neu.edu/wordpress/?p=841
324. Wiggle Sort II
-------------------


Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example: (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].

(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note: You may assume all input has valid answer.

    Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?



http://anakinfoxe.com/blog/2016/07/16/leetcode-wiggle-sort-ii/



277. Find the Celebrity
-----------------------

Suppose you are at a party with n people (labeled from 0 to n – 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n – 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: “Hi, A. Do you know B?” to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity’s label if there is a celebrity in the party. If there is no celebrity, return -1.

如果 a 不认识任何人，不代表a是名人。
如果 a 不被任何人认识，不代表a是名人
只有当a不认识任何人，并且，a不被任何人认识，a才是名人

如果a 认识 b， a不可能是名人
如果a不认识b，b不可能是名人

就是这几个最重要的逻辑，搞清楚就行了。


http://www.jianshu.com/p/dca466058b1c

https://aquahillcf.wordpress.com/2015/09/06/leetcode-find-the-celebrity/



http://yanguango.com/2015/09/08/leetcode-find-the-celebrity.html


https://zhuhan0.blogspot.com/2017/07/leetcode-277-find-celebrity.html



259. 3Sum Smaller
-----------------

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]

Follow up:
Could you solve it in O(n2) runtime?

https://segmentfault.com/a/1190000003794736

https://github.com/awangdev/LeetCode/blob/master/Java/3Sum%20Smaller.java


245. Shortest Word Distance III
-------------------------------



This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list. 



这道题还是让我们求最短单词距离，有了之前两道题Shortest Word Distance II和Shortest Word Distance的基础，就大大降低了题目本身的难度。这道题增加了一个条件，就是说两个单词可能会相同，所以在第一题中的解法的基础上做一些修改，我最先想的解法是基于第一题中的解法二，由于会有相同的单词的情况，那么p1和p2就会相同，这样结果就会变成0，显然不对，所以我们要对word1和word2是否的相等的情况分开处理，如果相等了，由于p1和p2会相同，所以我们需要一个变量t来记录上一个位置，这样如果t不为-1，且和当前的p1不同，我们可以更新结果，如果word1和word2不等，那么还是按原来的方法做，参见代码如下：



https://github.com/kamyu104/LeetCode/blob/master/Python/shortest-word-distance-iii.py


https://segmentfault.com/a/1190000003906667

https://gist.github.com/cangoal


http://leetcode0.blogspot.com/2015/12/245-shortest-word-distance-iii-my.html

238. Product of Array Except Self 
---------------------------------

 Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

229. Majority Element II 
------------------------

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.



http://wdxtub.com/interview/14520595473082.html



https://github.com/csujedihy/lc-all-solutions/blob/master/229.majority-element-ii/majority-element-ii.py

https://blog.neoshell.moe/leetcode229.html


http://www.jiarui-blog.com/2015/10/01/leetcode-229-majority-element-ii/


http://www.jyuan92.com/blog/leetcode-majority-element-ii/


228. Summary Ranges 
-------------------


 Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.



216. Combination Sum III 
------------------------



Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]


Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.


209. Minimum Size Subarray Sum 
------------------------------


 Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.




163. Missing Ranges
-------------------



 Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].



Solution:

We go through the input array and check lower with each element - 1.

If lower == element - 1, we add the range of one number.

If lower < element - 1, we add the range from lower to element - 1.

After adding a range, we update lower to element + 1.

Need to check boundary to avoid overflow.

The time complexity is O(n) and the space complexity is O(1).






https://github.com/kamyu104/LeetCode/blob/master/Python/missing-ranges.py


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



152. Maximum Product Subarray 
-----------------------------


 Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6. 


120. Triangle
-------------

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle. 




106. Construct Binary Tree from Inorder and Postorder Traversal 
---------------------------------------------------------------



Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree. 



105. Construct Binary Tree from Preorder and Inorder Traversal 
--------------------------------------------------------------


Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree. 


90. Subsets II 
--------------

 Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]


81. Search in Rotated Sorted Array II 
-------------------------------------



    Follow up for "Search in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.


80. Remove Duplicates from Sorted Array II 
------------------------------------------


 Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length. 


79. Word Search
---------------


 Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.



78. Subsets
-----------


 Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

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


75. Sort Colors
---------------


 Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?


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



73. Set Matrix Zeroes 
---------------------

 Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.
Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


64. Minimum Path Sum 
--------------------

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



63. Unique Paths II
-------------------


Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.

Note: m and n will be at most 100.


62. Unique Paths
----------------

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

.. image:: robot_maze.png

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.



59. Spiral Matrix II 
--------------------


Given an integer n, generate a square matrix filled with elements from 1 to n的2次方 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


56. Merge Intervals 
-------------------

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]. 




55. Jump Game 
-------------

 Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false. 





54. Spiral Matrix 
-----------------


Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5]. 


48. Rotate Image 
----------------

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?



40. Combination Sum II
----------------------

 Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

39. Combination Sum 
-------------------



 Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:

[
  [7],
  [2, 2, 3]
]

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



31. Next Permutation 
--------------------

 Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

18. 4Sum
--------


Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
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
[
  [-1, 0, 1],
  [-1, -1, 2]
]




11. Container With Most Water 
-----------------------------

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2. 















































