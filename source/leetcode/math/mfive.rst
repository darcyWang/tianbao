题号 172、168、171、66、397、396、372、368、365、360
=======================================================





172. Factorial Trailing Zeroes 
------------------------------


Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.




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


66. Plus One 
------------



Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.


397. Integer Replacement 
------------------------

Given a positive integer n and you can do operations as follow:

    If n is even, replace n with n/2.
    If n is odd, you can replace n with either n + 1 or n - 1.

What is the minimum number of replacements needed for n to become 1?

Example 1:
::
    Input:  8

    Output:  3

    Explanation:
    8 -> 4 -> 2 -> 1

Example 2:
::
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
::
    a = 2
    b = [3]

    Result: 8

Example2:
::
    a = 2
    b = [1,0]

    Result: 1024




368. Largest Divisible Subset 
-----------------------------


Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
::
    nums: [1,2,3]

    Result: [1,2] (of course, [1,3] will also be ok)

Example 2:
::
    nums: [1,2,4,8]

    Result: [1,2,4,8]





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


