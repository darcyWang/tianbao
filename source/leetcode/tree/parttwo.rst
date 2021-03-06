题目序号 538、501、437、404、270、257、235、226
=====================================================




538. Convert BST to Greater Tree 
--------------------------------


Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:
::
        Input: The root of a Binary Search Tree like this:
                      5
                    /   \
                   2     13

        Output: The root of a Greater Tree like this:
                     18
                    /   \
                  20     13


501. Find Mode in Binary Search Tree
------------------------------------

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

*. The left subtree of a node contains only nodes with keys less than or equal to the node's key.
*. The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
*. Both the left and right subtrees must also be binary search trees.

For example:
::
    Given BST [1,null,2,2],

       1
        \
         2
        /
       2

    return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count). 



437. Path Sum III 
-----------------


You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
::
        root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

              10
             /  \
            5   -3
           / \    \
          3   2   11
         / \   \
        3  -2   1

        Return 3. The paths that sum to 8 are:

        1.  5 -> 3
        2.  5 -> 2 -> 1
        3. -3 -> 11


404. Sum of Left Leaves
-----------------------


Find the sum of all left leaves in a given binary tree.

Example:
::
        3
       / \
      9  20
        /  \
       15   7

    There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.






270. Closest Binary Search Tree Value
-------------------------------------

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

Tags: Tree Binary Search
Similar Problems: (M) Count Complete Tree Nodes, (H) Closest Binary Search Tree Value II


递归法
复杂度
时间 O(logN) 空间 O(H)

思路
根据二叉树的性质，我们知道当遍历到某个根节点时，最近的那个节点要么是在子树里面，要么就是根节点本身。所以我们根据这个递归，返回子树中最近的节点，和根节点中更近的那个就行了。

迭代法
复杂度
时间 O(logN) 空间 O(H)

思路
记录一个最近的值，然后沿着二叉搜索的路径一路比较下去，并更新这个最近值就行了。因为我们知道离目标数最接近的数肯定在二叉搜索的路径上。


.. code-block:: python

    # works for normal binary tree
    def closestValue1(self, root, target):
        if not root:
            return 0
        self.res = root.val
        self.findClosest(root, target)
        return self.res
        
    def findClosest(self, root, target):
        if root:
            if abs(root.val-target) == 0:
                self.res = root.val
                return  # backtracking 
            if abs(root.val-target) < abs(self.res - target):
                self.res = root.val
            self.findClosest(root.left, target)
            self.findClosest(root.right, target)

    # works for normal binary tree    
    def closestValue2(self, root, target):
        if not root:
            return sys.maxint
        if not root.left and not root.right:
            return root.val
        l = self.closestValue(root.left, target)
        r = self.closestValue(root.right, target)
        return min([root.val, l, r], key=lambda x:abs(x-target))

    # works for binary search tree
    def closestValue(self, root, target):
        if not root:
            return sys.maxint
        if not root.left and not root.right:
            return root.val
        node = root.right if target > root.val else root.left
        if not node:
            return root.val
        tmp = self.closestValue(node, target)
        return min((tmp, root.val), key=lambda x:abs(x-target))


Closest Binary Search Tree Value II
-----------------------------------

Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note: Given target value is a floating point. You may assume k is always valid, that is: k ≤ total nodes. You are guaranteed to have only one unique set of k values in the BST that are closest to the target. Follow up: Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

Hint:

Consider implement these two helper functions: getPredecessor(N), which returns the next smaller node to N. getSuccessor(N), which returns the next larger node to N.


中序遍历法
复杂度
时间 O(N) 空间 Max(O(K),O(H))

思路
二叉搜索树的中序遍历就是顺序输出二叉搜索树，所以我们只要中序遍历二叉搜索树，同时维护一个大小为K的队列，前K个数直接加入队列，之后每来一个新的数（较大的数），如果该数和目标的差，相比于队头的数离目标的差来说，更小，则将队头拿出来，将新数加入队列。如果该数的差更大，则直接退出并返回这个队列，因为后面的数更大，差值也只会更大。





257. Binary Tree Paths
----------------------


Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:
::
       1
     /   \
    2     3
     \
      5

    All root-to-leaf paths are:

    ["1->2->5", "1->3"]

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


.. code-block:: python

    # dfs + stack
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res
        
    # bfs + queue
    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                queue.append((node.left, ls+str(node.val)+"->"))
            if node.right:
                queue.append((node.right, ls+str(node.val)+"->"))
        return res
        
    # dfs recursively
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)    
        


235. Lowest Common Ancestor of a Binary Search Tree 
---------------------------------------------------

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
::
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


.. code-block:: python

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return 
        # p and q are on the different side of root,
        # or at least one of them is root
        if (root.val-p.val)*(root.val-q.val)<=0:
            return root
        # both p and q are on the left side of root
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # both p and q are on the right side of root
        else:
            return self.lowestCommonAncestor(root.right, p, q)  
        



226. Invert Binary Tree 
-----------------------

Invert a binary tree

Example:
::
    Input:

         4
       /   \
      2     7
     / \   / \
    1   3 6   9

    Output:

         4
       /   \
      7     2
     / \   / \
    9   6 3   1

.. code-block:: python

    def invertTree1(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root


    def invertTree(self, root):
        queue = []
        queue.append(root)
        while queue:
            curr = queue.pop(0)
            if curr:
                curr.left, curr.right = curr.right, curr.left
                queue.append(curr.left); queue.append(curr.right)
        return root

    class Solution(object):
        def invertTree(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            if not root:
                return root
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root


.. code-block:: python

    # recursively
    def invertTree1(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
            
    # BFS
    def invertTree2(self, root):
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
        
    # DFS
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root 
        
