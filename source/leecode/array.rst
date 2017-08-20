数组Array部分
============

每个模块的都是按照从easy到hard，第一遍把所有的easy和medium都过一遍，
第二遍的时候开始把部分的hard看看




414. Third Maximum Number 
-------------------------

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:

Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.

Example 2:

Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.



219. Contains Duplicate II 
--------------------------

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k. 


283. Move Zeroes 
----------------
 Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


217. Contains Duplicate 
-----------------------


Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct. 



121. Best Time to Buy and Sell Stock 
------------------------------------

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:

Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:

Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

122. Best Time to Buy and Sell Stock II 
---------------------------------------

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

53. Maximum Subarray 
--------------------

 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.





189. Rotate Array 
-----------------


Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

532. K-diff Pairs in an Array 
-----------------------------

 Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:

    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].




643. Maximum Average Subarray I 
-------------------------------


 Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:

    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].

605. Can Place Flowers 
----------------------

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:

    The input array won't violate no-adjacent-flowers rule.
    The input array size is in the range of [1, 20000].
    n is a non-negative integer which won't exceed the input array size.



624. Maximum Distance in Arrays
-------------------------------

Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:

Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:

Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].



66. Plus One
------------


Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.



1. Two Sum
----------


Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
::

        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].


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


167. Two Sum II - Input array is sorted
---------------------------------------

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2


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

























































































































