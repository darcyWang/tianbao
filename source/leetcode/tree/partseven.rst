题目序号 173、144、129、117、116、114、113、106、105、103
==============================================================




173. Binary Search Tree Iterator
--------------------------------


Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.



.. code-block:: python

    # Definition for a  binary tree node
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class BSTIterator:
        # @param root, a binary search tree's root node
        def __init__(self, root):
            self.nodes = []
            while root:
                self.nodes.append(root)
                root = root.left

        # @return a boolean, whether we have a next smallest number
        def hasNext(self):
            return len(self.nodes) > 0

        # @return an integer, the next smallest number
        def next(self):
            ret = self.nodes.pop()
            cur = ret.right
            while cur:
                self.nodes.append(cur)
                cur = cur.left

            return ret.val
            

    # Your BSTIterator will be called like this:
    # i, v = BSTIterator(root), []
    # while i.hasNext(): v.append(i.next()) 
            
            
            
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.nodes = []
        self.count = 0
        while root:
            self.nodes.append(root)
            self.count += 1
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.count > 0

    # @return an integer, the next smallest number
    def next(self):
        ret = self.nodes.pop()
        self.count -= 1
        cur = ret.right
        while cur:
            self.nodes.append(cur)
            self.count += 1
            cur = cur.left
        return ret.val  
            
    class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.q=[]
        self.allLeftIntoStack(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.q:return False
        return True

    def hasNext(self):
        return self.q != []

    # @return an integer, the next smallest number
    def next(self):
        cur = self.q.pop()
        self.allLeftIntoStack(cur.right)
        return cur.val

    def allLeftIntoStack(self,root):
        while root:
            self.q.append(root)
            root=root.left
            
            
    class BSTIterator:
        # @param root, a binary search tree's root node
        def __init__(self, root):
            self.stack = list()
            self.pushAll(root)

        # @return a boolean, whether we have a next smallest number
        def hasNext(self):
            return self.stack

        # @return an integer, the next smallest number
        def next(self):
            tmpNode = self.stack.pop()
            self.pushAll(tmpNode.right)
            return tmpNode.val
            
        def pushAll(self, node):
            while node is not None:
                self.stack.append(node)
                node = node.left    
        


144. Binary Tree Preorder Traversal
-----------------------------------


Given a binary tree, return the preorder traversal of its nodes' values.

For example:
::
    Given binary tree {1,#,2,3},

       1
        \
         2
        /
       3

    return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

.. code-block:: python

    def inorderTraversal(self, root):
        stack, curr, res = [], root, []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr= curr.right
        return res
            
    # recursively
    def preorderTraversal1(self, root):
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)

    # iteratively
    def preorderTraversal(self, root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res  
            
    class Solution:
    # @param {TreeNode} root
    # @return {integer[]}

    def preorderTraversal(self, root):
        # Recursion: AC in 52 ms
        # ----------------------
        #
        if root == None:
            return []

        retval = [root.val]
        retval += self.preorderTraversal(root.left)
        retval += self.preorderTraversal(root.right)
        return retval
            
            
    def preorderTraversal(self, root):
        if not root:
            return []
        stack, res = [root], []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res  
            



129. Sum Root to Leaf Numbers
-----------------------------


Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,
::
    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25. 



.. code-block:: python

    # DFS recursively
    def sumNumbers1(self, root):
        if not root:
            return 0
        res = []
        self.dfs(root, root.val, res)
        return sum(res)
        
    def dfs(self, root, num, res):
        if root:
            if not root.left and not root.right:
                res.append(num)
            if root.left:
                self.dfs(root.left, num*10+root.left.val, res)
            if root.right:
                self.dfs(root.right, num*10+root.right.val, res)

    # BFS with queue         
    def sumNumbers3(self, root):
        if not root:
            return 0
        queue = []
        queue.append((root, root.val))
        res = 0
        while queue:
            curr, val = queue.pop(0)
            if not curr.left and not curr.right:
                res += val
            if curr.left:
                queue.append((curr.left, val*10+curr.left.val))
            if curr.right:
                queue.append((curr.right, val*10+curr.right.val))
        return res
        
    # DFS with explicit stack
    def sumNumbers4(self, root):
        if not root:
            return 0
        stack = [(root, root.val)]
        res = 0
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                res += val
            if curr.right:
                stack.append((curr.right, val*10+curr.right.val))
            if curr.left:
                stack.append((curr.left, val*10+curr.left.val))
        return res
        

.. code-block:: python
  
    
    # dfs + stack
    def sumNumbers1(self, root):
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value*10+node.right.val))
                if node.left:
                    stack.append((node.left, value*10+node.left.val))
        return res
        
    # bfs + queue
    def sumNumbers2(self, root):
        if not root:
            return 0
        queue, res = collections.deque([(root, root.val)]), 0
        while queue:
            node, value = queue.popleft()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.left:
                    queue.append((node.left, value*10+node.left.val))
                if node.right:
                    queue.append((node.right, value*10+node.right.val))
        return res
        
    # recursively 
    def sumNumbers(self, root):
        self.res = 0
        self.dfs(root, 0)
        return self.res
        
    def dfs(self, root, value):
        if root:
            #if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.left, value*10+root.val)
            #if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.right, value*10+root.val)
            if not root.left and not root.right:
                self.res += value*10 + root.val 
        
        

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
::
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


.. code-block:: python

    def zigzagLevelOrder(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level+1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(curr.val)
                else:
                    res[level].insert(0, curr.val)
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return res  
        
        
    def zigzagLevelOrder(self, root):
        # write your code here
        res = []
        self.dfs(root, 0, res)
        return res
        
    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)

    # dfs + stack
    def zigzagLevelOrder(self, root):
        # write your code here
        res, stack = [], [(root, 0)]
        while stack:
            cur, level = stack.pop()
            if cur:
                if len(res) < level + 1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(cur.val)
                else:
                    res[level].insert(0, cur.val)
                stack.append((cur.right, level+1))
                stack.append((cur.left, level+1))
        return res  
        


.. code-block:: python

    class Solution(object):
        def zigzagLevelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            if not root:
                return []
            res, cur_level, level_count = [], [root], 0
            while cur_level:
                next_level, tmp_res = [], []
                for node in cur_level:
                    tmp_res.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                if level_count % 2 == 0:
                    res.append(tmp_res)  
                else:
                    tmp_res.reverse()
                    res.append(tmp_res)
                level_count += 1
                cur_level = next_level
                
            return res
    
    We can solve this problem by using BFS with queue. Level information is needed in order to reverse the odd row.

    def zigzagLevelOrder(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level+1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(curr.val)
                else:
                    res[level].insert(0, curr.val)
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return res
        
        
    After some thoughts, this question can also be solved as:

    def zigzagLevelOrder(self, root):
        # write your code here
        res = []
        self.dfs(root, 0, res)
        return res
        
    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)

    # dfs + stack
    def zigzagLevelOrder(self, root):
        # write your code here
        res, stack = [], [(root, 0)]
        while stack:
            cur, level = stack.pop()
            if cur:
                if len(res) < level + 1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(cur.val)
                else:
                    res[level].insert(0, cur.val)
                stack.append((cur.right, level+1))
                stack.append((cur.left, level+1))
        return res  

