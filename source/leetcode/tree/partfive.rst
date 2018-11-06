题目序号 582、549、545、536、515、513、508、450、449
============================================================



582. Kill Process
-----------------


Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

Example 1:

Input: 
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation: 
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
Note:

The given kill id is guaranteed to be one of the given PIDs.
n >= 1.
题目大意：
给定n个进程，进程ID为PID，父进程ID为PPID。

当杀死一个进程时，其子进程也会被杀死。

给定进程列表和其对应的父进程列表，以及被杀死的进程ID，求所有被杀死的进程ID。

注意：

给定被杀死的进程ID一定在进程列表之中
n >= 1
解题思路：
树的层次遍历

利用孩子表示法建立进程树

然后从被杀死的进程号开始，执行层次遍历。


549. Binary Tree Longest Consecutive Sequence II
------------------------------------------------


Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
题目大意：
给定二叉树，寻找其中最长的连续的整数路径。

特别的，路径可以递增/递减。例如[1,2,3,4] 和 [4,3,2,1]均有效，但是 [1,2,4,3] 无效。另外，路径的顺序不一定必须是父亲-孩子，也可以是孩子-父亲-孩子。

http://bookshadow.com/weblog/2017/04/09/leetcode-binary-tree-longest-consecutive-sequence-ii/


545. Boundary of Binary Tree
----------------------------

Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
Example 2
::

        Input:
            ____1_____
           /          \
          2            3
         / \          / 
        4   5        6   
           / \      / \
          7   8    9  10  
       
        Ouput:
        [1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
题目大意：
给定二叉树，逆时针输出二叉树的边界。边界包括左边界、叶子节点和右边界。

左边界是指从根出发到最左侧节点经过的路径。右边界是指从根出发到最右侧节点经过的路径。

如果根节点不包含左子树或者右子树，则对应的边界不存在。注意此定义是指整棵二叉树，不包含子树。

最左侧节点是指从根节点出发尽量向左走，如果不能则向右走，到达的叶子结点。

最右侧节点定义参考最左侧节点，左右互换即可。

解题思路：
左边界、右边界根据题意求解。叶子节点通过先序遍历得到。



536. Construct Binary Tree from String
--------------------------------------


You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:

Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
Note:

There will only be '(', ')', '-' and '0' ~ '9' in the input string.
题目大意：
根据字符串重构二叉树。

输入包含数字和括号，数字代表根节点，括号内的子串代表左、右孩子。

注意：

输入字符串只包含'(', ')，'-'和数字'0'-'9'

解题思路：
递归+字符串处理

通过括号匹配将字符串拆解成root, (left), (right)三部分，递归创建二叉树



515. Find Largest Value in Each Tree Row
----------------------------------------

You need to find the largest value in each row of a binary tree.

Example:

Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]


513. Find Bottom Left Tree Value
--------------------------------



 Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
::
    Input:

        2
       / \
      1   3

    Output: 1

Example 2:
::
    Input:

            1
           / \
          2   3
         /   / \
        4   5   6
           /
          7

    Output: 7

Note: You may assume the tree (i.e., the given root node) is not NULL. 



508. Most Frequent Subtree Sum
------------------------------


 Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3

return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5

return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer. 


450. Delete Node in a BST
-------------------------

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.

Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7



449. Serialize and Deserialize BST
----------------------------------

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

