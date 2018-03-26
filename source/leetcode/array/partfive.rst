题号： 
================


531. Lonely Pixel I
-------------------


Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
::
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
::
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

    #. You may assume the length of given time series array won't exceed 10000.
    #. You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.



https://www.liuchuo.net/archives/3209

https://github.com/yuanhui-yang/LeetCode/blob/master/Algorithms/teemo-attacking.cpp


442. Find All Duplicates in an Array 
------------------------------------

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:  [4,3,2,7,8,2,3,1]

Output:  [2,3]


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

    #. You must not modify the array (assume the array is read only).
    #. You must use only constant, O(1) extra space.
    #. Your runtime complexity should be less than O(n2).
    #. There is only one duplicate number in the array, but it could be repeated more than once.

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



