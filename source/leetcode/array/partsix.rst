题号： 
================


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

