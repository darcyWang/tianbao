题目序号 173、144、129、117、116、114、113、106、105、103
==============================================================




173. Binary Search Tree Iterator
--------------------------------


Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.




144. Binary Tree Preorder Traversal
-----------------------------------


Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?




129. Sum Root to Leaf Numbers
-----------------------------


Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25. 


117. Populating Next Right Pointers in Each Node II
---------------------------------------------------


Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

    You may only use constant extra space.

For example
::
    Given the following binary tree,

             1
           /  \
          2    3
         / \    \
        4   5    7

    After calling your function, the tree should look like:

             1 -> NULL
           /  \
          2 -> 3 -> NULL
         / \    \
        4-> 5 -> 7 -> NULL


116. Populating Next Right Pointers in Each Node
------------------------------------------------

Given a binary tree

struct TreeLinkNode {
    TreeLinkNode *left;
    TreeLinkNode *right;
    TreeLinkNode *next;    
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

#. You may only use constant extra space.
#. You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL




114. Flatten Binary Tree to Linked List
---------------------------------------


Given a binary tree, flatten it to a linked list in-place.

For example
::
    Given

             1
            / \
           2   5
          / \   \
         3   4   6

    The flattened tree should look like:

       1
        \
         2
          \
           3
            \
             4
              \
               5
                \
                 6


If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.


113. Path Sum II
----------------

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
::
    Given the below binary tree and sum = 22,

                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1

    return

    [
       [5,4,11,2],
       [5,8,4,5]
    ]



106. Construct Binary Tree from Inorder and Postorder Traversal
---------------------------------------------------------------



Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree. 



105. Construct Binary Tree from Preorder and Inorder Traversal
--------------------------------------------------------------

Given preorder and inorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree. 




103. Binary Tree Zigzag Level Order Traversal
---------------------------------------------


Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]


