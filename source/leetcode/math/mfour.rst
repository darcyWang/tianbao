题号 136、137、263、258、246、247、248、231、204、202
=====================================================


136. Single Number
------------------


Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 



.. code-block:: python

    def singleNumber1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key

    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
        
    def singleNumber3(self, nums):
        return 2*sum(set(nums))-sum(nums)
        
    def singleNumber4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)
        
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)   

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



可能包含前面题目的答案

.. code-block:: python

    def singleNumber(self, nums):
        bit = [0] * 32
        for num in nums:
            for i in xrange(32):
                bit[i] += num >> i & 1
        res = 0
        for i, val in enumerate(bit):
            # if the single numble is negative,
            # this case should be considered separately 
            if i == 31 and val%3:
                res = -((1<<31)-res)
            else:
                res |= (val%3)*(1<<i)
        return res  


    # O(n) space, O(n) time
    def singleNumber1(self, nums):
        dic, res = {}, []
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for k, v in dic.items():
            if v == 1:
                res.append(k)
        return res
        
    # Bit manipulation, O(1) space, O(n) time
    def singleNumber(self, nums):
        # "xor" all the nums 
        tmp = 0
        for num in nums:
            tmp ^= num
        # find the rightmost "1" bit
        i = 0
        while tmp & 1 == 0:
            tmp >>= 1
            i += 1
        tmp = 1 << i
        # compute in two seperate groups
        first, second = 0, 0
        for num in nums:
            if num & tmp:
                first ^= num
            else:
                second ^= num
        return [first, second]  
        
        
    A versoin shows how to use different kinds of dictionary in Python:

    def singleNumber1(self, nums):
        count = collections.Counter(nums)
        return [k for k, v in count.iteritems() if v < 2]
        
    def singleNumber2(self, nums):
        dic = collections.defaultdict(int)
        for num in nums:
            dic[num] += 1
        return [k for k, v in dic.items() if v < 2]
        
    def singleNumber3(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        return [k for k, v in dic.items() if v < 2]
        
    def singleNumber4(self, nums):
        dic = collections.OrderedDict()
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        return [k for k, v in dic.iteritems() if v < 2]
        
    def singleNumber(self, nums):
        tmp = reduce(operator.xor, nums)
        bit = tmp & (-tmp)
        n1, n2 = 0, 0
        for num in nums:
            if num & bit:
                n1 ^= num
            else:
                n2 ^= num
        return [n1, n2] 
        
    class Solution:
        # @param {integer[]} nums
        # @return {integer[]}
        def singleNumber(self, nums):
            xor = reduce(operator.xor, nums)
            ans = reduce(operator.xor, filter(lambda x : x & xor & -xor, nums))
            return [ans, ans ^ xor] 
        
.. code-block:: python

    def singleNumber1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key

    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
        
    def singleNumber3(self, nums):
        return 2*sum(set(nums))-sum(nums)
        
    def singleNumber4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)
        
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)

263. Ugly Number
----------------

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.



.. code-block:: python

    # dynamic programming
    def nthUglyNumber(self, n):
        ugly = [0] * n
        nxt = ugly[0] = 1
        i2 = i3 = i5 = 0
        nxt2, nxt3, nxt5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
        for i in xrange(1, n):
            nxt = min(nxt2, nxt3, nxt5)
            ugly[i] = nxt
            if nxt == nxt2:
                i2 += 1
                nxt2 = ugly[i2]*2
            if nxt == nxt3:
                i3 += 1
                nxt3 = ugly[i3]*3
            if nxt == nxt5:
                i5 += 1
                nxt5 = ugly[i5]*5
        return nxt # ugly[-1]   
        
        
     def nthUglyNumber(self, n):
        if n <= 0:
            return 0
        ugly = [1] * n
        i2 = i3 = i5 = 0
        for i in xrange(1, n):
            ugly[i] = min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
            if ugly[i] == ugly[i2]*2:
                i2 += 1
            if ugly[i] == ugly[i3]*3:
                i3 += 1
            if ugly[i] == ugly[i5]*5:
                i5 += 1
        return ugly[-1]
        


258. Add Digits
---------------

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:
:: 
   Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime? 

原理：
假设输入的数字是一个5位数字num，则num的各位分别为a、b、c、d、e
有如下关系：num = a * 10000 + b * 1000 + c * 100 + d * 10 + e
即：num = (a + b + c + d + e) + (a * 9999 + b * 999 + c * 99 + d * 9)
因为 a * 9999 + b * 999 + c * 99 + d * 9 一定可以被9整除，因此num模除9的结果与 a + b + c + d + e 模除9的结果是一样的。
对数字 a + b + c + d + e 反复执行同类操作，最后的结果就是一个 1-9 的数字加上一串数字，最左边的数字是 1-9 之间的，右侧的数字永远都是可以被9整除的。
这道题最后的目标，就是不断将各位相加，相加到最后，当结果小于10时返回。因为最后结果在1-9之间，得到9之后将不会再对各位进行相加，因此不会出现结果为0的情况。
因为 (x + y) % z = (x % z + y % z) % z，又因为 x % z % z = x % z，因此结果为 (num - 1) % 9 + 1，只模除9一次，并将模除后的结果加一返回。

.. code-nlock:: javascript

    /**
     * @param {number} num
     * @return {number}
     */
    var addDigits = function(num) {
        if(num==0)
            return num;
        if(num%9==0)
            return 9;
        else return num%9;
    };

.. code-block:: python

    def addDigits1(self, num):
        return num - ((num-1)/9)*9 if num > 0 else 0
        
    def addDigits2(self, num):
        return (num-1)%9 + 1 if num > 0 else 0
        
    def addDigits3(self, num):
        return num and (num-1)%9 + 1
      
    # Recursively  
    def addDigits4(self, num):
        if 0<= num <= 9:
            return num
        tmp = 0
        while num:
            tmp += num % 10
            num //= 10
        return self.addDigits(tmp)
        
    # Iteratively
    def addDigits(self, num):
        if num == 0:
            return 0
        while num:
            if 1 <= num <= 9:
                return num
            tmp = 0
            while num:
                tmp += num % 10
                num //= 10
            num = tmp   


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


.. code-block:: python

    def isStrobogrammatic1(self, num):
        deque = collections.deque(map(int, list(num)))
        while len(deque) >= 2:
            l, r = deque.popleft(), deque.pop()
            for i in [2,3,4,5,7]:
                if i in [l, r]:
                    return False  
            if (l, r) in [(6,6), (9,9)] or (l != r and (l, r) not in [(6,9), (9,6)]):
                return False
        return not deque or deque.pop() in [0,1,8]
        
    def isStrobogrammatic(self, num):
        dic = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        l, r = 0, len(num)-1
        while l <= r:
            if num[l] not in dic or dic[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True 

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


.. code-block:: java

    public List<String> findStrobogrammatic(int n) {
        return helper(n, n);
    }

    List<String> helper(int n, int m) {
        if (n == 0) return new ArrayList<String>(Arrays.asList(""));
        if (n == 1) return new ArrayList<String>(Arrays.asList("0", "1", "8"));
        
        List<String> list = helper(n - 2, m);
        
        List<String> res = new ArrayList<String>();
        
        for (int i = 0; i < list.size(); i++) {
            String s = list.get(i);
            
            if (n != m) res.add("0" + s + "0");
            
            res.add("1" + s + "1");
            res.add("6" + s + "9");
            res.add("8" + s + "8");
            res.add("9" + s + "6");
        }
        
        return res;
    }

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


