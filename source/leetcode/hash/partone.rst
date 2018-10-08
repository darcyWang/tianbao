题目序号   
============================================================



624. Maximum Distance in Arrays
-------------------------------


Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
::
    Input:
    [[1,2,3],
     [4,5],
     [1,2,3]]

    Output: 4
    
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Note:

    #. Each given array will have at least 1 number. There will be at least two non-empty arrays.
    #. The total number of the integers in all the m arrays will be in the range of [2, 10000].
    #. The integers in the m arrays will be in the range of [-10000, 10000].

题目大意：

给定一组数组arrays，各数组递增有序，求不同数组之间最小值、最大值之间差值绝对值的最大值。
解题思路：

解法I 一趟遍历 时间复杂度O(n)，n为arrays的长度




690. Employee Importance
------------------------


You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:
::
    Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
    Output: 11

    Explanation:
    Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.

Note:

    #. One employee has at most one direct leader and may have several subordinates.
    #. The maximum number of employees won't exceed 2000.



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




599. Minimum Index Sum of Two Lists
-----------------------------------


Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
::
    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    Output: ["Shogun"]

    Explanation: The only restaurant they both like is "Shogun".

Example 2:
::
    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    Output: ["Shogun"]

    Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Note:

#. The length of both lists will be in the range of [1, 1000].
#. The length of strings in both lists will be in the range of [1, 30].
#. The index is starting from 0 to the list length minus 1.
#. No duplicates in both lists.



594. Longest Harmonious Subsequence
-----------------------------------


We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
::
    Input: [1,3,2,2,5,2,3,7]
    Output: 5

    Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note: The length of the input array will not exceed 20,000. 


575. Distribute Candies
-----------------------

Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

Example 1:
::
    Input: candies = [1,1,2,2,3,3]
    Output: 3

Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 

Example 2:
::
    Input: candies = [1,1,2,3]
    Output: 2

Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies. 

Note:

#. The length of the given array is in range [2, 10,000], and will be even.
#. The number in given array is in range [-100,000, 100,000].




500. Keyboard Row
-----------------

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below. 


Example 1:
::
    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]

Note:

#. You may use one character in the keyboard more than once.
#. You may assume the input string will only contain letters of alphabet.


463. Island Perimeter
---------------------


You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:
::
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

    Answer: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:




447. Number of Boomerangs
-------------------------


Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
::
    Input: [[0,0],[1,0],[2,0]]

    Output: 2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]



438. Find All Anagrams in a String
----------------------------------



Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
::
    Input: s: "cbaebabacd" p: "abc"

    Output: [0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
::
    Input: s: "abab" p: "ab"

    Output: [0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

