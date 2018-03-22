题目序号 414、217、219、283、121、122、123、188
====================================================


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
    var sorted_arr = arr.slice().sort(); 
    // You can define the comparing function here. 
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
