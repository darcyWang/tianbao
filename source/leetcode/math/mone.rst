题目序号  645、633、628、13、9、7、640、634、625、593
============================================================


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



13. Roman to Integer
--------------------


Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.


+-----------------+------+------+------+------+------+------+------+
|  Roman Number   |   I  |  V   |   X  |   L  |   C  |   D  |   M  |  
+-----------------+------+------+------+------+------+------+------+
|  Arab Number    |   1  |  5   |  10  |  50  | 100  |  500 | 1000 |
+-----------------+------+------+------+------+------+------+------+



罗马数字是最早的数字表示方式，比阿拉伯数字早2000多年，起源于罗马。
如今我们最常见的罗马数字就是钟表的表盘符号：Ⅰ，Ⅱ，Ⅲ，Ⅳ（IIII），Ⅴ，Ⅵ，Ⅶ，Ⅷ，Ⅸ，Ⅹ，Ⅺ，Ⅻ……
对应阿拉伯数字（就是现在国际通用的数字），就是1，2，3，4，5，6，7，8，9，10，11，12。（注：阿拉伯数字其实是古代印度人发明的，后来由阿拉伯人传入欧洲，被欧洲人误称为阿拉伯数字。）


1、相同的数字连写，所表示的数等于这些数字相加得到的数，如：Ⅲ = 3；
2、小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数， 如：Ⅷ = 8；Ⅻ = 12；
3、小的数字，（限于Ⅰ、X 和C）在大的数字的左边，所表示的数等于大数减小数得到的数，如：Ⅳ= 4；Ⅸ= 9；
4、正常使用时，连写的数字重复不得超过三次。（表盘上的四点钟“IIII”例外）
5、在一个数的上面画一条横线，表示这个数扩大1000倍。


有几条须注意掌握：

#. 基本数字Ⅰ、X 、C 中的任何一个，自身连用构成数目，或者放在大数的右边连用构成数目，都不能超过三个；放在大数的左边只能用一个。
#. 不能把基本数字V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目，只能使用一个。
#. V 和X 左边的小数字只能用Ⅰ。
#. L 和C 左边的小数字只能用X。
#. D 和M 左边的小数字只能用C。
 
而这道题好就好在没有让我们来验证输入字符串是不是罗马数字，这样省掉不少功夫。我们需要用到map数据结构，来将罗马数字的字母转化为对应的整数值，因为输入的一定是罗马数字，那么我们只要考虑两种情况即可：
第一，如果当前数字是最后一个数字，或者之后的数字比它小的话，则加上当前数字
第二，其他情况则减去这个数字


考虑到罗马数字转换为阿拉伯数字，相应的阿拉伯数字也可以转换为罗马数字


.. code-block:: python

                
    def romanToInt1(self, s):
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
        res = dic[s[-1]]
        for i in xrange(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        return res

    def romanToInt(self, s):
        dic = [0]*256
        dic[ord("I")] = 1; dic[ord("V")] = 5; dic[ord("X")] = 10; dic[ord("L")] = 50;
        dic[ord("C")] = 100; dic[ord("D")] = 500; dic[ord("M")] = 1000;
        res = dic[ord(s[-1])]
        for i, ch in enumerate(s[:-1:]):
            if dic[ord(ch)] < dic[ord(s[i+1])]:
                res -= dic[ord(ch)]
            else:
                res += dic[ord(ch)]
        return res          
                

    def romanToInt(self, s):
        roman = ["I", "V", "X", "L", "C", "D", "M"] # or roman = "IVXLCDM"
        integer = [1, 5, 10, 50, 100, 500, 1000]
        res = integer[roman.index(s[-1])]
        for i in xrange(len(s)-1):
            if integer[roman.index(s[i])] < integer[roman.index(s[i+1])]:
                res -= integer[roman.index(s[i])]
            else:
                res += integer[roman.index(s[i])]
        return res          
                
                
    def intToRoman1(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res, i = "", 0
        while num:
            res += (num//values[i]) * numerals[i]
            num %= values[i]
            i += 1
        return res
        
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for i, v in enumerate(values):
            res += (num//v) * numerals[i]
            num %= v
        return res          
                    
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for i, v in zip(numerals, values):
            res += (num // v) * i
            num %= v
        return res      



.. code-block:: python

    class Solution(object):
        def intToRoman(self, num):
            """
            :type num: int
            :rtype: str
            """
            numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", \
                           10: "X", 40: "XL", 50: "L", 90: "XC", \
                           100: "C", 400: "CD", 500: "D", 900: "CM", \
                           1000: "M"}
            keyset, result = sorted(numeral_map.keys()), []
            
            while num > 0:
                for key in reversed(keyset):
                    while num / key > 0:
                        num -= key
                        result += numeral_map[key]
                        
            return "".join(result)

     
    if __name__ == "__main__":
        print Solution().intToRoman(999)
        print Solution().intToRoman(3999)


.. code-block:: python

    def roman_to_int(roman, values={'M': 1000, 'D': 500, 'C': 100, 'L': 50, 
                                    'X': 10, 'V': 5, 'I': 1}):
        """Convert from Roman numerals to an integer."""
        numbers = []
        for char in roman:
            numbers.append(values[char]) 
        total = 0
        for num1, num2 in zip(numbers, numbers[1:]):
            if num1 >= num2:
                total += num1
            else:
                total -= num1
        return total + num2


.. code-block:: python

    class Solution:
        # @return an integer
        def romanToInt(self, s):
            numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
            decimal = 0
            for i in xrange(len(s)):
                if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                    decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
                else:
                    decimal += numeral_map[s[i]]
            return decimal

    if __name__ == "__main__":
        print Solution().romanToInt("IIVX")
        print Solution().romanToInt("MMMCMXCIX")



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



.. attention:: 

    一元一次方程真的很容易解，但是要用代码来解决，真真你妈也是蛋疼啊

字符串处理

#. 用'='将等式分为左右两半
#. 分别求左右两侧x的系数和常数值，记为lx, lc, rx, rc
#. 令x, c = lx - rx, rc - lc
#. 若x != 0，则x = c / x
#. 否则，若c != 0，说明方程无解
#. 否则，说明有无数组解

.. code-block:: python

    class Solution(object):
        def solveEquation(self, equation):
            """
            :type equation: str
            :rtype: str
            """
            left, right = equation.split('=')
            lx, lc = self.solve(left)
            rx, rc = self.solve(right)
            x, c = lx - rx, rc - lc
            if x: return 'x=%d' % (c / x)
            elif c: return 'No solution'
            return 'Infinite solutions'
        
        def solve(self, expr):
            x = c = 0
            num, sig = '', 1
            for ch in expr + '#':
                if '0' <= ch <= '9':
                    num += ch
                elif ch == 'x':
                    x += int(num or '1') * sig
                    num, sig = '', 1
                else:
                    c += int(num or '0') * sig
                    num, sig = '', 1
                    if ch == '-': sig = -1
            return x, c




634. Find the Derangement of An Array
-------------------------------------

In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
::
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
