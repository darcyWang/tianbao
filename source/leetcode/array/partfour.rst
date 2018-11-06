题目序号 484、118、119、621、611、565、562、560、548
============================================================


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


119. Pascal's Triangle II
-------------------------

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?


.. code-block:: python

    # O(n*n) space
    def getRow1(self, rowIndex):
        res = [[1 for _ in xrange(i+1)] for i in xrange(rowIndex+1)]
        for i in xrange(2, rowIndex+1):
            for j in xrange(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res[-1]
     
    # O(n) space, each row from left to right
    def getRow2(self, rowIndex):
        res = [1 for _ in xrange(rowIndex+1)]
        for i in xrange(2, rowIndex+1):
            pre = res[0]
            for j in xrange(1, i):
                cur = res[j]
                res[j] += pre
                pre = cur
        return res
        
    # O(n) space, each row from right to left
    def getRow(self, rowIndex):
        res = [1 for _ in xrange(rowIndex+1)]
        for i in xrange(2, rowIndex+1):
            for j in xrange(i-1, 0, -1):
                res[j] += res[j-1]
        return res

    # math
    def getRow(self, rowIndex):
        res = []
        for i in xrange(rowIndex+1):
            res.append(self.compute(rowIndex, i))
        return res
        
    def compute(self, k, i):
        return math.factorial(k)/(math.factorial(i)*math.factorial(k-i))
        
    # O(k) space
    def getRow(self, rowIndex):
        res = [0] * (rowIndex+1)
        res[0] = 1
        for i in xrange(1, rowIndex+1):
            pre = res[:]
            for j in xrange(1, i+1):
                res[j] = pre[j-1] + pre[j]
        return res  
        


.. image:: PascalTriangleAnimated2.gif


时间复杂度: O(k^2)******- 空间复杂度: O(k)
.. code-block:: python

    class Solution(object):
        def getRow(self, rowIndex):
            """
            :type rowIndex: int
            :rtype: List[int]
            """
            if rowIndex == 0:
                return [1]
            res = [1]
            for i in range(1, rowIndex+1):
                tmp = [1]
                for j in range(1, i):
                    tmp.append(res[j-1]+res[j])
                tmp.append(1)
                res = tmp
            return res


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

    #. The number of tasks is in the range [1, 10000].
    #. The integer n is in the range [0, 100].


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
::      
        Input: [2,2,3,4]
        Output: 3
        Explanation:
        Valid combinations are: 
        2,3,4 (using the first 2)
        2,3,4 (using the second 2)
        2,2,3

Note:

    #. The length of the given array won't exceed 1000.
    #. The integers in the given array are in the range of [0, 1000].


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

    #. The length of the array is in range [1, 20,000].
    #. The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


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

    #. 1 <= n <= 2000.
    #. Elements in the given array will be in range [-1,000,000, 1,000,000].

https://wlypku.github.io/2017/04/02/Leetcode-week26/

https://github.com/csujedihy/lc-all-solutions/blob/master/548.split-array-with-equal-sum/split-array-with-equal-sum.py




