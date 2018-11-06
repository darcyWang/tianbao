题目序号 436、392、378、300、287、275、240、230、222、209
============================================================


436. Find Right Interval
------------------------


Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

    #. You may assume the interval's end point is always bigger than its start point.
    #. You may assume none of these intervals have the same start point.

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:

Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.

Example 3:

Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.




392. Is Subsequence
-------------------


Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.





300. Longest Increasing Subsequence
-----------------------------------


Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.




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


275. H-Index II
---------------

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm? 



240. Search a 2D Matrix II
--------------------------

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

For example,

Consider the following matrix:
::
    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]

Given target = 5, return true.

Given target = 20, return false.



230. Kth Smallest Element in a BST
----------------------------------

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Credits:
Special thanks to @ts for adding this problem and creating all test cases.


.. code-block:: python

    def kthSmallest(self, root, k):
        # stack records the node whether visited or not
        stack = [(root, False)]
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    # if visited is True, it means a "small" node is found
                    k -= 1
                    # if k == 0, it means k small nodes has been checked,
                    # the current node is the kth one
                    if k == 0:
                        return curr.val
                else:
                    # Add from right to left
                    stack.append((curr.right, False))
                    stack.append((curr, True))
                    stack.append((curr.left, False))    
        
    Easier idea based on inorder traversal:

    # Recursively
    def kthSmallest1(self, root, k):
        res = []
        self.inorder(root, res)
        return res[k-1]
        
    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)
     
    # Iteratively         
    def kthSmallest(self, root, k):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res[k-1]
            node = stack.pop()
            res.append(node.val)
            root = node.right   
        
        
    # averaged time complexity: log(n) + k
    def kthSmallest(self, root, k):
        self.k = k
        self.res = 0
        self.helper(root)
        return self.res
        
    def helper(self, root):
        if root:
            self.helper(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return 
            self.helper(root.right) 
        
        
    Here is an iterative version with comments:

    # log(n) + k
    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return 
            # the order of pop is the same as
            # BST order, so the first time will 
            # pop the smallest element, and so on, 
            # we track this pop operation, after k 
            # times, we get the answer
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            root = node.right   
        
        

378. Kth Smallest Element in a Sorted Matrix
--------------------------------------------

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
::
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ],
    k = 8,

    return 13.

Note:
You may assume k is always valid, 1 ≤ k ≤ n2.



222. Count Complete Tree Nodes
------------------------------

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.





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

