题号 136、137、263、258、246、247、248、231、204、202
=====================================================


136. Single Number
------------------


Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 

给定一个整数数组，除一个元素只出现一次外，其余各元素均出现两次。找出那个只出现一次的元素。

对数组元素执行异或运算，最终结果即为所求。

由于异或运算的性质，两个相同数字的亦或等于0，而任意数字与0的亦或都等于它本身。另外，异或运算满足交换律。

a ^ b = (a & !b) || (!a & b)


.. code-block:: python

    class Solution(object):
        def singleNum(self, nums):
            """
            param {integer[]} nums
            return {integer}
            """
            ans = 0
            for num in nums:
                ans ^= num
            return ans
        def twosingleNum(self, nums):
            return reduce(operator.xor, nums)

        def threeSingleNum(self, nums):
            return reduce(lambda x, y : x ^ y, nums)


.. caution::

    先对元素进行排序，然后进行相邻两元素的对比，如a1和a2对比，a3和a4对比，如果不同，则前一个元素(a1、a3)就是所要查找的元素,实现上主要就是相邻两元素的对比，循环间隔为2，与前一元素对比，如果不同，则返回前一元素。
    如果循环执行完没有返回，则返回列表中最后一个元素，如[1, 1, 2, 2, 3]，执行的循环为(1, 3)，在循环中最后一个元素不会参与对比（奇数个元素）


.. code-block:: python

    class Solution(object):
        def singleNum(self, nums):
            nums.sort()
            for i in range(1, len(nums), 2):
                if nums[i] != nums[i-1]:
                    return nums[i-1]
            return nums[-1]


.. code-block:: java

    /**
     * @param {number[]} nums
     * @return {number}
     */
    var singleNumber = function(nums) {
        return nums.reduce((pre, cur) => pre ^ cur)
    };

    console.log(singleNumber([1,2,3,3,2,1,4]))

137. Single Number II
---------------------



Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


.. code-block:: c

    /**
     * @param {number[]} nums
     * @return {number}
     */
    var singleNumber = function(nums) {
        const arr = []
        for (let i = 0; i < 32; i++) {
            arr.unshift(nums.reduce((pre, cur) => pre + (cur >> i & 1), 0) % 3)
        }
        return parseInt(arr.join(''), 2) | 0
    };

    console.log(singleNumber([-1,-1,-1,-2]))


Single Number III
-----------------


Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
For example:
::
    Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
    #. The order of the result is not important. So in the above example, [5, 3] is also correct.
    #. Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?



.. code-block:: java

    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    var singleNumber = function(nums) {
        const axorb = nums.reduce((pre, cur) => pre ^ cur)
        const last1 = axorb ^ ((axorb - 1) & axorb)
        let a = 0
        let b = 0
        for (let num of nums){
            if ((last1 & num) === 0) {
                a ^= num
            } else {
                b ^= num
            }
        }
        return [a, b]
    };

    console.log(singleNumber([88, 2, 88, 3, 2, 5]))



263. Ugly Number
----------------

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


258. Add Digits
---------------

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:
:: 
   Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime? 



246. Strobogrammatic Number
---------------------------

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.


时间 O(N) 空间 O(1)


翻转后对称的数就那么几个，我们可以根据这个建立一个映射关系：8->8, 0->0, 1->1, 6->9, 9->6，然后从两边向中间检查对应位置的两个字母是否有映射关系就行了。比如619，先判断6和9是有映射的，然后1和自己又是映射，所以是对称数。



1. 首先我们应从0~9这些数字中分析一下什么样子的数字会出现类似的情况：
0 -> 0
1 -> 1
6 -> 9
8 -> 8
9 -> 6
于是，我们需要做的就是，用i和j分别从头、从尾部来比较，如果num[i]==num[j]并且为8，或者0，或者1，则continue，如果num[i]=='6', num[j]=='9'，或者反之，也continue；如果不continue就false；
最后，如果这个number是奇数个，我们需要对中间位再判断，只有为8、0或者1才行。否则输出false；最后，存活过这些false判断就输出为true；




247. Strobogrammatic Number II
------------------------------



A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example, Given n = 2, return ["11","69","88","96"].

找出所有的可能，必然是深度优先搜索。但是每轮搜索如何建立临时的字符串呢？因为数是“对称”的，我们插入一个字母就知道对应位置的另一个字母是什么，所以我们可以从中间插入来建立这个临时的字符串。这样每次从中间插入两个“对称”的字符，之前插入的就被挤到两边去了。这里有几个边界条件要考虑：

如果是第一个字符，即临时字符串为空时进行插入时，不能插入'0'，因为没有0开头的数字

如果n=1的话，第一个字符则可以是'0'

如果只剩下一个带插入的字符，这时候不能插入'6'或'9'，因为他们不能和自己产生映射，翻转后就不是自己了

这样，当深度优先搜索时遇到这些情况，则要相应的跳过




248. Strobogrammatic Number III
-------------------------------

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

For example,
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

Note:
Because the range might be a large number, the low and high numbers are represented as string.




231. Power of Two
-----------------

Given an integer, write a function to determine if it is a power of two.




204. Count Primes 
-----------------


Count the number of prime numbers less than a non-negative number, n.




202. Happy Number 
-----------------

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number
::
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1


