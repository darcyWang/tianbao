题目序号   370、598、507、453、462、441、415、592、553、537、
============================================================



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
::
    Input: 
    Height : 5
    Width : 7
    Tree position : [2,2]
    Squirrel : [4,4]
    Nuts : [[3,0], [2,5]]
    Output: 12

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
::
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



