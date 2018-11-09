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


.. code-block:: python

    Python solutions: DFS recursively, DFS with stack, BFS with queue.

    # DFS recursively
    def levelOrder1(self, root):
        res = []
        self.dfs(root, 0, res)
        return res
        
    def dfs(self, root, level, res):
        if not root:
            return 
        if len(res) < level+1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)
     
    # DFS + stack I   
    def levelOrder2(self, root):
        if not root:
            return []
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if len(res) < level + 1:
                res.append([])
            res[level].append(curr.val)
            if curr.right:
                stack.append((curr.right, level+1))
            if curr.left:
                stack.append((curr.left, level+1))
        return res

    # DFS + stack II  
    def levelOrder3(self, root):
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if curr:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(curr.val)
                stack.append((curr.right, level+1))
                stack.append((curr.left, level+1))
        return res

    # BFS + queue
    def levelOrder4(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level+1:
                    res.append([])
                res[level].append(curr.val)
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return res
        
    # BFS + deque
    def levelOrder(self, root):
        from collections import deque
        res, queue = [], deque([(root, 0)])
        while queue:
            curr, level = queue.popleft()
            if curr:
                if len(res) < level+1:
                    res.append([])
                res[level].append(curr.val)
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return res  
        


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

.. code-block:: python

    # recursively
    def isValidBST1(self, root):
        Min, Max = -(1<<31)-1, (1<<31)
        return self.helper(root, Min, Max)
        
    def helper(self, root, Min, Max):
        if not root: # root is None
            return True
        if not root.left and not root.right: # root has no leaf
            if Min < root.val < Max:
                return True
            else:
                return False
        if not root.left and root.right: # root only has right leaf
            return root.val < root.right.val and self.helper(root.right, root.val, Max)
        elif root.left and not root.right: # root only has left leaf
            return root.val > root.left.val and self.helper(root.left, Min, root.val)
        else: # root has both left and right leaves
            return root.left.val < root.val < root.right.val and self.helper(root.left, Min, root.val) and self.helper(root.right, root.val, Max)

    # iteratively, in-order traversal
    # O(n) time and O(n)+O(lgn) space
    def isValidBST(self, root):
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            # if root is None or all the nodes have 
            # been traversed and have no confliction 
            if not stack:
                return True
            node = stack.pop()
            # res stores the current values in in-order 
            # traversal order, node.val should larger than
            # the last element in res
            if res and node.val <= res[-1]:
                return False
            res.append(node.val)
            root = node.right



    A recursive version of the in-order traversal solution, one pass:

    def isValidBST(self, root):
        res, self.flag = [], True
        self.helper(root, res)
        return self.flag
        
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            if res and root.val <= res[-1]:
                self.flag = False
                return
            res.append(root.val)
            self.helper(root.right, res)
    A shorter recursive solution:

    def isValidBST(self, root):
        return self.helper(root, float("-inf"), float("inf"))
        
    def helper(self, root, low, high):
        if not root:
            return True
        if not root.left and not root.right:
            return low < root.val < high
        return low < root.val < high and self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)



.. code-block:: python
        
    # recursively
    def isValidBST1(self, root):
        Min, Max = -(1<<31)-1, (1<<31)
        return self.helper(root, Min, Max)
        
    def helper(self, root, Min, Max):
        if not root: # root is None
            return True
        if not root.left and not root.right: # root has no leaf
            if Min < root.val < Max:
                return True
            else:
                return False
        if not root.left and root.right: # root only has right leaf
            return root.val < root.right.val and self.helper(root.right, root.val, Max)
        elif root.left and not root.right: # root only has left leaf
            return root.val > root.left.val and self.helper(root.left, Min, root.val)
        else: # root has both left and right leaves
            return root.left.val < root.val < root.right.val and self.helper(root.left, Min, root.val) and self.helper(root.right, root.val, Max)

    # iteratively, in-order traversal
    # O(n) time and O(n)+O(lgn) space
    def isValidBST(self, root):
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            # if root is None or all the nodes have 
            # been traversed and have no confliction 
            if not stack:
                return True
            node = stack.pop()
            # res stores the current values in in-order 
            # traversal order, node.val should larger than
            # the last element in res
            if res and node.val <= res[-1]:
                return False
            res.append(node.val)
            root = node.right
        
        
        
    def isValidBST(self, root):
        res, self.flag = [], True
        self.helper(root, res)
        return self.flag
        
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            if res and root.val <= res[-1]:
                self.flag = False
                return
            res.append(root.val)
            self.helper(root.right, res)
        
        
    def isValidBST(self, root):
        return self.helper(root, float("-inf"), float("inf"))
        
    def helper(self, root, low, high):
        if not root:
            return True
        if not root.left and not root.right:
            return low < root.val < high
        return low < root.val < high and self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)
        



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


.. code-block:: python

    # DP
    def numTrees1(self, n):
        res = [0] * (n+1)
        res[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]
     
    # Catalan Number  (2n)!/((n+1)!*n!)  
    def numTrees(self, n):
        return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))      
                
        


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

.. code-block:: python

    # recursively
    def inorderTraversal1(self, root):
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
     
    # iteratively       
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right   
        
        
    similar iterative solution

    def inorderTraversal(self, root):
        ans = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                ans.append(tmpNode.val)
                root = tmpNode.right
            
        return ans  
        


