数学Math部分
==========


645. Set Mismatch
-----------------

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
::
   Input: nums = [1,2,2,4]
   Output: [2,3]

Note:
    #. The given array size will in the range [2, 10000].
    #. The given array's numbers won't have any order.

解决办法一:
初始化一个长度为 len(nums) + 1的列表 A,然后遍历列表 nums,统计该列表各个元素出现的个数并记录在 A 中,然后统计列表 A 元素值为 2 的索引和 0 索引即为我们所求的值

.. code:: python

   class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_num = len(nums)
        count = [0] * (len(nums)+1)
        for num in nums:
            count[num] += 1
        for i in range(1,len(nums)+1):
            if count[i] == 2:
                a = i
            if count[i] == 0:
                b = i
        return [a,b]

JS版本代码

.. code:: javascript

   /**
    * @param {number[]} nums
    * @return {number[]}
    */
   var findErrorNums = function(nums) {
       var count = new Array(nums.length + 1);
       count.fill(0);//这个方法是将初始化的数组所有元素值为0
       var arr = new Array(2);
       arr.fill(-1);
       for(var i = 0; i < nums.length; i++){
           count[nums[i]] ++;
       }
       for(var i = 1; i < count.length+1; i++){
           if(count[i] == 2){
               arr[0] = i;
               if(arr[1]!=-1) break;
           }
           if(count[i] == 0){
               arr[1] = i;
               if(arr[0]!=-1) break;            
           }
       }
       return arr;
   };



633. Sum of Square Numbers
--------------------------

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a^2 + b^2 = c.

Example 1:
::
   Input: 5
   Output: True
   Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
::
   Input: 3
   Output: False

.. code:: python

   class Solution(object):
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
               b = int((c - a * a) ** 0.5)
               if ( a * a + b * b ) == c:
                   return True
           return False

.. code:: javascript
    
    let newSquareSum = function(num) {
        const m = Math.squrt(num);
        for(var a = 0; a <= m; a++) {
            let b = parseInt(Math.squrt(num - a*a));
            if( a * a + b * b == num ) return true;
        }
        return false;
    }

628. Maximum Product of Three Numbers 
-------------------------------------

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
::
   Input: [1,2,3]
   Output: 6

Example 2:
::
   Input: [1,2,3,4]
   Output: 24

Note:
    #. The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
    #. Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

.. code:: python
    
    class Solution(object):
        def maximumProduct(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            先排序，然后找出5个数字，为什么是5个数字呢，需要考虑有负数的情况，
            把拿到的数组进行排序，找出最小的两个数字min1和min2,然后找出数组
            的最大3个数字,max1、max2和max3.
            """
            nums = sorted(nums)
            return max(nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])

    assert Solution().maximumProduct([1,2,3,4]) == 24
    assert Solution().maximumProduct([-4,-3,-2,-1,60]) == 720


370. Range Addition
-------------------


Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:
::
    Given:  length = 5,
            updates = [
                [1,  3,  2],
                [2,  4,  3],
                [0,  2, -2]
            ]

    Output: [-2, 0, 3, 5, 3]

Explanation:
::
    Initial state:  [ 0, 0, 0, 0, 0 ]

    After applying operation [1, 3, 2]:
                             [ 0, 2, 2, 2, 0 ]

    After applying operation [2, 4, 3]:
                             [ 0, 2, 5, 5, 3 ]

    After applying operation [0, 2, -2]:
                             [-2, 0, 3, 5, 3 ]




598. Range Addition II 
----------------------

Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:
::
   Input: 
   m = 3, n = 3
   operations = [[2,2],[3,3]]
   Output: 4

Explanation: 
::
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
    #. The range of m and n is [1,40000].
    #. The range of a is [1,m], and the range of b is [1,n].
    #. The range of operations size won't exceed 10,000.


507. Perfect Number 
-------------------

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:
::
   Input: 28
   Output: True
   Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8) 

解题思路:

#. 求出输入值num的平方差sqrt1
#. 判断num能否将i （i属于[2, sqrt1]）整除，如果可以，则将i和num/i加入num的因数和sum中
#. 判断num和sum是否相等，如果相等，则为完美数，否则不是

注意: 因子不包括自己，所以如果输入是1的话，因子不能有1，1不是完美数


还有一种解法是在给定的n的范围内其实只有五个符合要求的完美数字，于是就有这种枚举的解法，那么套用一句诸葛孔明的名言就是，我从未见过如此厚颜无耻之解法

num==6 || num==28 || num==496 || num==8128 || num==33550336

在给定的区间里面就只有这几个数字符合

453. Minimum Moves to Equal Array Elements
------------------------------------------

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:
::
   Input: [1,2,3]

   Output: 3

Explanation: Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]


先定义一下，sum = 数组移动前所有元素的总和，n = 数组的长度，m = 移动步数，就是答案咯
x = 最后的元素等于的值， minNum = 数组值最小的元素

sum + m * (n - 1) = x * n

x = minNum + m

sum - minNum * n = m

.. code:: python

    /**
     * @param {number[]} nums
     * @return {number}
     */
    var minMoves = function(nums) {
        var total=0;
        nums.sort(function(a,b){return a-b;});
        for(var i=0;i<nums.length;i++)
        {
            total+=nums[i];
        }
        var result=total-nums[0]*nums.length;
        return result;
    };

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)




462. Minimum Moves to Equal Array Elements II
---------------------------------------------

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:
::
    Input:  [1,2,3]

    Output:  2

Explanation:  Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

.. code-block:: python

    class Solution(object):
        def minMoves2(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums = sorted(nums)
            median = nums[len(nums)//2]
            s = 0
            for v in nums:
                s+=abs(v-median)
            return s

441. Arranging Coins 
--------------------


You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
::
    n = 5

    The coins can form the following rows:
    ¤
    ¤ ¤
    ¤ ¤

    Because the 3rd row is incomplete, we return 2.

Example 2:
::
    n = 8

    The coins can form the following rows:
    ¤
    ¤ ¤
    ¤ ¤ ¤
    ¤ ¤

    Because the 4th row is incomplete, we return 3.



415. Add Strings
----------------


Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

    #. The length of both num1 and num2 is < 5100.
    #. Both num1 and num2 contains only digits 0-9.
    #. Both num1 and num2 does not contain any leading zero.
    #. You must not use any built-in BigInteger library or convert the inputs to integer directly.

.. tip:: 

    当两个字符串实现相加的时候，我们应该可以想到既然想加都有了，那就一定会有相减、相乘咯。对吧，baby，这就是在做题目过程出现的follow up


::

    // Given two numbers represented as strings, return multiplication of the numbers as a string.

    // Note:
    // The numbers can be arbitrarily large and are non-negative.
    // Converting the input string to integer is NOT allowed.
    // You should NOT use internal library such as BigInteger.
    // Hide Company Tags Facebook Twitter
    // Hide Tags Math String
    // Hide Similar Problems (M) Add Two Numbers (E) Plus One (E) Add Binary

    /**
     * @param {string} num1
     * @param {string} num2
     * @return {string}
     */
    var multiply = function(num1, num2) {
        if(num1 === null || num2 === null || num1.length === 0 || num2.length === 0 || num1 === '0' || num2 === '0') {
            return '0';
        }
        
        var arr1 = num1.split('').reverse();
        var arr2 = num2.split('').reverse();
        var result = [];
        
        for(var i = 0; i < arr1.length; i++) {
            var carry = 0;
            var val1 = parseInt(arr1[i]);
            
            for(var j = 0; j < arr2.length; j++) {
                var val2 = parseInt(arr2[j]);
                var product = val1*val2 + carry;
                var exist = result[i+j] || 0;
                var sum = product + exist;
                var digit = sum%10;
                carry = Math.floor(sum/10);
                result[i+j] = digit;
            }
            
            if(carry > 0) {
                result[i+j] = carry;
            }
        }
        
        result.reverse();
        result = result.join('');
        
        return result;
    };

    multiply('123', '456')


第二种选择

::
    
    class Solution:
        # @param num1, a string
        # @param num2, a string
        # @return a string
        def multiply(self, num1, num2):
            # Handle with the special case that, at least of the input is 0.
            if num1 == "0" or num2 == "0":      return "0"

            result = [0] * (len(num1) + len(num2))
            num1 = [int(i) for i in num1]
            num2 = [int(i) for i in num2]

            for index1 in xrange(len(num1)):
                multiplier = num1[index1]
                temp = [i*multiplier for i in num2]         # Multiply
                temp.extend([0] * (len(num1) - index1 - 1)) # Shift

                # Add to the final result
                for resIndex in xrange(1, len(temp) + 1):
                    result[-resIndex] += temp[-resIndex]

            # Normalize the final result.
            # We do not need to consider the first element.
            # For a m-length integer multiply n-length integer, the result
            # is at most with length of m+n. Thus the first element in array
            # "result" will never be more than 9.
            for resIndex in xrange(len(result)-1, 0, -1):
                result[resIndex-1] += result[resIndex] // 10
                result[resIndex] %= 10

            # Convert the final result into string
            result = "".join([str(i) for i in result]).lstrip("0")

            return result


.. code-block:: python

    class Solution(object):
        def addStrings(self, num1, num2):
            """
            :type num1: str
            :type num2: str
            :rtype: str
            """
            def _convertInter(num):
                return ord(num) - ord('0')

            # 将两个字符串逆序后，转换为list，这里题目有要求，不能使用库函数直接把string转换为int，需要我们自己实现一个字符串转换数字的函数。
            num1, num2 = list(map(_convertInter, num1[::-1])), list(map(int, num2[::-1]))

            # 如果num2的长度 大于 num1，交换它们的顺序。
            if len(num1)<len(num2):
                num1, num2 = num2, num1

            carry = 0
            for i in range(len(num1)):
                n = num2[i] if i<len(num2) else 0 # 较短的那一位如果不够，则该位补0
                tmp = n + carry + num1[i] # 有进位，则将进位加上
                num1[i] = tmp % 10
                carry = tmp // 10

            # 最后存在进位，记得将这个进位加上。
            if carry:
                num1.append(1)
            # 这里没有要求不能将integer转换为str，所以直接使用了内建函数str()
            return ''.join(map(str, num1))[::-1]


            from itertools import izip_longest
            class Solution(object):
                def addStrings(self, num1, num2):
                    res, c = "", 0
                    for (x, y) in izip_longest(num1[::-1], num2[::-1], fillvalue='0'):
                        s = (int(x) + int(y) + c)
                        d, c = s % 10, int(s / 10)
                        res = str(d) + res

                    if c > 0: res = str(c) + res

                    return res

            class Solution(object):
                def addStrings(self, num1, num2):
                    """
                    :type num1: str
                    :type num2: str
                    :rtype: str
                    """
                    i = len(num1) - 1
                    j = len(num2) - 1
                    num = ""
                    carry = 0
                    while i >= 0 or j >= 0:
                        result = carry
                        if i >= 0:
                            result += int(num1[i])
                        if j >= 0:
                            result += int(num2[j])
                        if result >= 10:
                            carry = 1
                        else:
                            carry = 0
                        num = str(result % 10) + num
                        i -= 1
                        j -= 1
                    if carry == 1:
                        num = "1" + num
                    return num

            assert Solution().addStrings("111", "234965") == "235076"
            assert Solution().addStrings("999", "1") == "1000"




.. code-block:: python

    class Solution(object):
        def addStrings(self, num1, num2):
            """
            :type num1: str
            :type num2: str
            :rtype: str
            """
            result = []
            carry = 0
            idx1, idx2 = len(num1), len(num2)
            while idx1 or idx2 or carry:
                digit = carry
                if idx1:
                    idx1 -= 1
                    digit += int(num1[idx1])
                if idx2:
                    idx2 -= 1
                    digit += int(num2[idx2])
                carry = digit > 9
                result.append(str(digit % 10))
            return ''.join(result[::-1])

400. Nth Digit
--------------

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note: n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
::
   Input: 3
   Output: 3

Example 2:
::
   Input: 11
   Output: 0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


367. Valid Perfect Square 
-------------------------

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
::
   Input: 16
   Returns: True

Example 2:
::
   Input: 14
   Returns: False


解法I 牛顿迭代（Newton's Method）

求平方根可以转化为求函数y = x ^ 2 - num的根

迭代过程x = (x + num / x) * 1/2

.. code-block:: python

    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            x = num
            while x * x > num:
                x = (x + num / x) / 2
            return x * x == num


解法II 二分法（Binary Search）

.. code-block:: python

    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            left, right = 0, num
            while left <= right:
                mid = (left + right) / 2
                if mid * mid >= num:
                    right = mid - 1
                else:
                    left = mid + 1
            return left * left == num


.. code-block:: python

    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            L, R = 1, (num >> 1) + 1
            while L <= R:
                m = L + ((R - L) >> 1)
                mul = m ** 2
                if mul == num:
                    return True
                elif mul > num:
                    R = m - 1
                else:
                    L = m + 1
            return False


.. code-block:: python

    class Solution(object):
        def isPerfectSquare(self, num):
            """
            :type num: int
            :rtype: bool
            """
            L, R = 1, (num >> 1) + 1
            while L <= R:
                m = L + ((R - L) >> 1)
                mul = m ** 2
                if mul == num:
                    return True
                elif mul > num:
                    R = m - 1
                else:
                    L = m + 1
            return False


69. Sqrt(x) 
-----------

Implement int sqrt(int x).

Compute and return the square root of x.

这道题目的答案就是上面题目答案修改一下

.. code-block:: javascript

    /**
     * @param {number} num
     * @return {boolean}
     */
    var isPerfectSquare = function(num) {
        var lo = 1;
        var hi = num;
        var isPS = false;

        if (num === 1) {
            isPS = true;
        }

        while (lo <= hi) {
            var mid = lo + Math.floor((hi - lo) / 2);
            var midSquare = mid * mid;
            if (midSquare === num) {
                isPS = true;
                break;
            } else if (midSquare > num) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }

        return isPS;
    };








326. Power of Three 
-------------------

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

.. code-block:: python

    class Solution(object):
        def isPowerOfThree(self, n):
            """
            :type n:int
            :rtype : bool
            """

            if(n <= 0):
                return False
            while n%3 == 0:
                n /= 3
            return n == 1

        def onePowerOfThree(self, n):
            if n <= 0:
                return False
            if n == 1:
                return True
            if n%3 == 0:
                return self.onePowerOfThree(n/3)
            else:
                return False 


.. tip:: 


    当然，题目说了不能循环或递归，上面的解法能AC但不太符合题意。考虑到输入是“Integer”，是有范围的（<2147483648），所以存在能输入的最大的3的幂次，即 3^19=1162261467。所以只要检查输入能否被它整除即可

.. code-block:: python

    class Solution(object):
        def twoPowerOfThree(self, n):
            return n > 0 and 1162261467 % n == 0




.. tip::

    还可以算出能输入的所有3的幂次，保存到list或dict中，对每次输入判断是否在这些数中即可。


.. code-block:: python

    class Solution(object):
        def threePowerOfThree(self, n):
            nums = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
            return n in nums

.. tip:: 

    取对数

.. code-block:: python

    class Solution(object):
        def threePowerOfThree(self, n):

            return n > 0 and 3 ** round(math.log(n, 3)) == 0 



268. Missing Number 
-------------------

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note: Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.



.. caution:: 

    这道题给我们n个数字，是0到n之间的数但是有一个数字去掉了，让我们寻找这个数字，要求线性的时间复杂度和常数级的空间复杂度。那么最直观的一个方法是用等差数列的求和公式求出0到n之间所有的数字之和，然后再遍历数组算出给定数字的累积和，然后做减法，差值就是丢失的那个数字
    等差数列前n项和 - 数组之和


.. code-block:: python

    class Solution(object):
        def missingNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            需要注意的是 等差数列的前n项和， 不是等差数列求和
            """
            n = len(nums)
            return n * ( n - 1 ) / 2 - sum(nums)


.. caution:: 

    这题还有一种解法，使用位操作Bit Manipulation来解的，用到了异或操作的特性，相似的题目有Single Number 单独的数字, Single Number II 单独的数字之二和Single Number III 单独的数字之三。那么思路是既然0到n之间少了一个数，我们将这个少了一个数的数组合0到n之间完整的数组异或一下，那么相同的数字都变为0了，剩下的就是少了的那个数字了，参加代码如下：

.. code-block:: python

    class Solution(object):
        def onemissing(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            a = reduce(operator.xor, nums)
            b = reduce(operator.xor, range(len(nums) + 1))
            return a ^ b


.. caution:: 

    这道题还可以用二分查找法来做，我们首先要对数组排序，然后我们用二分查找法算出中间元素的下标，然后用元素值和下标值之间做对比，如果元素值大于下标值，则说明缺失的数字在左边，此时将right赋为mid，反之则将left赋为mid+1。那么看到这里，作为读者的你可能会提出，排序的时间复杂度都不止O(n)，何必要多此一举用二分查找，还不如用上面两种方法呢。对，你说的没错，但是在面试的时候，有可能人家给你的数组就是排好序的，那么此时用二分查找法肯定要优于上面两种方法，所以这种方法最好也要掌握以下~

这个解决办法到后面自己写出来 刷二遍的时候




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

注意到0-9中有五个数字满足这种“镜像对称”，所以我们将它们放在一个哈希表中，然后遍历num中的前一半字符（包括最中间的字符），一旦发现某字符不在哈希表中，或者虽然是，但是在后面的对应位置上的字符不是它的“镜像对称”字符，就返回false。如果检查完所有的字符都没有问题，则返回true。

https://tonycao.gitbooks.io/leetcode-locked/content/LeetCode%20Locked/c1.5.html


http://www.bo-song.com/leetcode-strobogrammatic-number-ii-iii/


231. Power of Two
-----------------

Given an integer, write a function to determine if it is a power of two.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

204. Count Primes 
-----------------


Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.




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

Credits:
Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.




172. Factorial Trailing Zeroes 
------------------------------


Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.



168. Excel Sheet Column Title 
-----------------------------

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
::
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.


171. Excel Sheet Column Number 
------------------------------

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
::
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

Credits:
Special thanks to @ts for adding this problem and creating all test cases.






67. Add Binary 
--------------

Given two binary strings, return their sum (also a binary string).

For example
::
    a = "11"
    b = "1"
    Return "100". 


66. Plus One 
------------



Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.


13. Roman to Integer 
--------------------
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.


9. Palindrome Number 
--------------------

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.



7. Reverse Integer 
------------------


Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.
Have you thought about this?

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows. 


640. Solve the Equation 
-----------------------

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
::
    Input: "x+5-3+x=6+x-2"
    Output: "x=2"

Example 2:
::
    Input: "x=x"
    Output: "Infinite solutions"

Example 3:
::
    Input: "2x=x"
    Output: "x=0"

Example 4:
::
    Input: "2x+3x-6x=x+2"
    Output: "x=-1"

Example 5:
::
    Input: "x=x+2"
    Output: "No solution"




634. Find the Derangement of An Array
-------------------------------------

In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:

Input: 3
Output: 2
Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].

Note:
n is in the range of [1, 106].
题目大意：

在组合数学中，错位排列是指所有元素均不在其原始位置的排列。

给定[1, 2 , ... , n]，求其错位排列的个数。

由于结果可能很大，结果对10^9 + 7取模






625. Minimum Factorization
--------------------------
Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.

If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

Example 1
::
    Input: 48   Output: 68

Example 2
::
    Input: 15  Output: 35

题目大意：

给定正整数a，求各位相乘等于a的最小整数。

若不存在这样的整数，或者超过32位带符号整数范围，则返回0。


593. Valid Square 
-----------------


Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:

    #. All the input integers are in the range [-10000, 10000].
    #. A valid square has four equal sides with positive length and four equal angles (90-degree angles).
    #. Input points have no order.


592. Fraction Addition and Subtraction 
--------------------------------------


Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
::
    Input:"-1/2+1/2"
    Output: "0/1"

Example 2:
::
    Input:"-1/2+1/2+1/3"
    Output: "1/3"

Example 3:
::
    Input:"1/3-1/2"
    Output: "-1/6"

Example 4:
::
    Input:"5/3+1/3"
    Output: "2/1"

Note:

    #. The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
    #. Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
    #. The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
    #. The number of given fractions will be in the range [1,10].
    #. The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.



573. Squirrel Simulation

There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.

Example 1:

Input: 
Height : 5
Width : 7
Tree position : [2,2]
Squirrel : [4,4]
Nuts : [[3,0], [2,5]]
Output: 12
Explanation:

Note:

    #. All given positions won't overlap.
    #. The squirrel can take at most one nut at one time.
    #. The given positions of nuts have no order.
    #. Height and width are positive integers. 3 <= height * width <= 10,000.
    #. The given positions contain at least one nut, only one tree and one squirrel.

题目大意：

二维格子高度height，宽度width。其中包含一棵树tree，一个松鼠squirrel，以及一些坚果nuts。

求松鼠将所有坚果运送至树的位置所需的最小距离之和。

注意：

    #. 所有位置不会重叠
    #. 松鼠一次运送只能携带一枚坚果
    #. 给定坚果位置是无序的
    #. 高度和宽度是正整数，并且 3 <= height * width <= 10,000
    #. 给定位置包含至少一枚坚果，只有一棵树和一只松鼠


553. Optimal Division 
---------------------

Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.

Example:

Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
since they don't influence the operation priority. So you should return "1000/(100/10/2)". 

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2

Note:

    #. The length of the input array is [1, 10].
    #. Elements in the given array will be in range [2, 1000].
    #. There is only one optimal division for each test case.


537. Complex Number Multiplication
----------------------------------

Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
::
    Input: "1+1i", "1+1i"
    Output: "0+2i"
    Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:
::
    Input: "1+-1i", "1+-1i"
    Output: "0+-2i"
    Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:

    #. The input strings will not have extra blank.
    #. The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.




535. Encode and Decode TinyURL 
------------------------------

Note: This is a companion problem to the System Design problem: Design TinyURL.

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


523. Continuous Subarray Sum 
----------------------------


Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Note:

    #. The length of the array won't exceed 10,000.
    #. You may assume the sum of all the numbers is in the range of a signed 32-bit integer.


469. Convex Polygon
-------------------
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

Note:

    There are at least 3 and at most 10,000 points.
    Coordinates are in the range -10,000 to 10,000.
    You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.

Example 1:

[[0,0],[0,1],[1,1],[1,0]]

Answer: True

Explanation:

Example 2:

[[0,0],[0,10],[10,10],[10,0],[5,5]]

Answer: False

Explanation:

题目大意：

给定一组点，顺序相连可以组成一个多边形。判断多边形是否是凸包。

注意：

    最少3个，最多10000个点
    坐标在-10,000 到 10,000之间。
    你可以假设组成的多边形总是简单多边形。换言之，我们确保每个顶点都是两条边的交点，其他边不会相互交叉。

解题思路：

遍历顶点，判断相邻三个顶点A、B、C组成的两个向量(AB, AC)的叉积是否同负同正。




423. Reconstruct Original Digits from English 
---------------------------------------------

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:

    #. Input contains only lowercase English letters.
    #. Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
    Input length is less than 50,000.

Example 1:

Input: "owoztneoer"

Output: "012"

Example 2:

Input: "fviefuro"

Output: "45"



413. Arithmetic Slices 
----------------------

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7


A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.


397. Integer Replacement 
------------------------

Given a positive integer n and you can do operations as follow:

    If n is even, replace n with n/2.
    If n is odd, you can replace n with either n + 1 or n - 1.

What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:  8

Output:  3

Explanation:
8 -> 4 -> 2 -> 1

Example 2:

Input:  7

Output:  4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1



396. Rotate Function 
--------------------

Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:  n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.



372. Super Pow 
--------------

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8

Example2:

a = 2
b = [1,0]

Result: 1024

Credits:
Special thanks to @Stomach_ache for adding this problem and creating all test cases.



368. Largest Divisible Subset 
-----------------------------


Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)

Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]

Credits:
Special thanks to @Stomach_ache for adding this problem and creating all test cases.




365. Water and Jug Problem 
--------------------------



You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

    #. Fill any of the jugs completely with water.
    #. Empty any of the jugs.
    #. Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

Example 1: (From the famous "Die Hard" example)
::
    Input: x = 3, y = 5, z = 4
    Output: True

Example 2:
::
    Input: x = 2, y = 6, z = 5
    Output: False

Credits:
Special thanks to @vinod23 for adding this problem and creating all test cases.





360. Sort Transformed Array
---------------------------


Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
::
    nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

    Result: [3, 9, 15, 33]

    nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

    Result: [-23, -5, 1, 7]


