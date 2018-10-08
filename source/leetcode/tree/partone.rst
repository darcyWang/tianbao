题目序号   
============================================================






687. Longest Univalue Path 
--------------------------
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:
:: 
    Input:

              5
             / \
            4   5
           / \   \
          1   1   5

    Output: 2

Example 2:
::
    Input:

              1
             / \
            4   5
           / \   \
          4   4   5

    Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000. 


给定二叉树，求节点值全部相等的最长路径。路径不一定要通过树根。
通过递归（Recursion）来解题


.. code-block:: Python

        class Solution:
            def longestUnivaluePath(self, root):
                self.ans = 0
                self._univaluePath(root)
                return self.ans
            
            def _univaluePath(self, root):
                if root is None: return 0
                l = self._univaluePath(root.left) if root.left is not None else -1
                r = self._univaluePath(root.right) if root.right is not None else -1
                pl = l + 1 if l >= 0 and root.val == root.left.val else 0
                pr = r + 1 if r >= 0 and root.val == root.right.val else 0
                self.ans = max(self.ans, pl + pr)
                return max(pl, pr)




671. Second Minimum Node In a Binary Tree
-----------------------------------------

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
:: 
    Input: 
        2
       / \
      2   5
         / \
        5   7

    Output: 5
    Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:
::
    Input: 
        2
       / \
      2   2

    Output: -1
    Explanation: The smallest value is 2, but there isn't any second smallest value.


669. Trim a Binary Search Tree 
------------------------------

Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
:: 
    Input: 
        1
       / \
      0   2

      L = 1
      R = 2

    Output: 
        1
          \
           2

Example 2:
::
    Input: 
        3
       / \
      0   4
       \
        2
       /
      1

      L = 1
      R = 3

    Output: 
          3
         / 
       2   
      /
     1

653. Two Sum IV - Input is a BST 
--------------------------------

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
:: 
    Input: 
        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 9

    Output: True

Example 2:
::
    Input: 
        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 28

    Output: False


637. Average of Levels in Binary Tree 
-------------------------------------


Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
::
    Input:
        3
       / \
      9  20
        /  \
       15   7
    Output: [3, 14.5, 11]

    Explanation:
    The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note: The range of node's value is in the range of 32-bit signed integer.



617. Merge Two Binary Trees 
---------------------------

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
::
    Input: 
        Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
    
    Output: 
    Merged tree:
         3
        / \
       4   5
      / \   \ 
     5   4   7

Note: The merging process must start from the root nodes of both trees. 



606. Construct String from Binary Tree 
--------------------------------------


You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
::
    Input: Binary tree: [1,2,3,4]
           1
         /   \
        2     3
       /    
      4     

    Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".

Example 2:
::
    Input: Binary tree: [1,2,3,null,4]
           1
         /   \
        2     3
         \  
          4 

    Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

572. Subtree of Another Tree 
----------------------------


Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
::
    Given tree s:

         3
        / \
       4   5
      / \
     1   2

    Given tree t:

       4 
      / \
     1   2

Return true, because t has the same structure and node values with a subtree of s.

Example 2:
::
    Given tree s:

         3
        / \
       4   5
      / \
     1   2
        /
       0

    Given tree t:

       4
      / \
     1   2

    Return false. 



563. Binary Tree Tilt 
---------------------

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
::
    Input: 
             1
           /   \
          2     3
    Output: 1


Explanation: 
#. Tilt of node 2 : 0
#. Tilt of node 3 : 0
#. Tilt of node 1 : |2-3| = 1
#. Tilt of binary tree : 0 + 0 + 1 = 1

Note:
The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.



543. Diameter of Binary Tree 
----------------------------

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them. 
