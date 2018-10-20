题目序号 102、98、96、95、94
==============================================================





102. Binary Tree Level Order Traversal
--------------------------------------

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
::
    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

    return its level order traversal as:

    [
      [3],
      [9,20],
      [15,7]
    ]



98. Validate Binary Search Tree
-------------------------------


Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

#. The left subtree of a node contains only nodes with keys less than the node's key.
#. The right subtree of a node contains only nodes with keys greater than the node's key.
#. Both the left and right subtrees must also be binary search trees.

Example 1:
::
        2
       / \
      1   3

    Binary tree [2,1,3], return true.

Example 2:
::
        1
       / \
      2   3

    Binary tree [1,2,3], return false. 




96. Unique Binary Search Trees
------------------------------


Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example
::
    Given n = 3, there are a total of 5 unique BST's.

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3


95. Unique Binary Search Trees II
---------------------------------

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example
::
    Given n = 3, your program should return all 5 unique BST's shown below.

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3



94. Binary Tree Inorder Traversal
---------------------------------


Given a binary tree, return the inorder traversal of its nodes' values.

For example:
::
    Given binary tree [1,null,2,3],

       1
        \
         2
        /
       3

    return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?


