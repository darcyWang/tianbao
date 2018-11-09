题目序号 690、339、112、111、108、109
=================================================





690. Employee Importance
------------------------

You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.

Note:

    #. One employee has at most one direct leader and may have several subordinates.
    #. The maximum number of employees won't exceed 2000.


339. Nested List Weight Sum
---------------------------



Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27) 




112. Path Sum
-------------

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example:
Given the below binary tree and sum = 22,
::
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


.. code-block:: python

    class Solution(object):
        def hasPathSum(self, root, sum):
            """
            :type root: TreeNode
            :type sum: int
            :rtype: bool
            """
            if not root:
                return False
            if root.left or root.right:
                return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
            else:
                return root.val == sum    

.. code-block:: python

    # DFS Recursively 
    def hasPathSum1(self, root, sum):
        res = []
        self.dfs(root, sum, res)
        return any(res)
        
    def dfs(self, root, target, res):
        if root:
            if not root.left and not root.right:
                if root.val == target:
                    res.append(True)
            if root.left:
                self.dfs(root.left, target-root.val, res)
            if root.right:
                self.dfs(root.right, target-root.val, res)

    # DFS with stack
    def hasPathSum2(self, root, sum):
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                if val == sum:
                    return True
            if curr.right:
                stack.append((curr.right, val+curr.right.val))
            if curr.left:
                stack.append((curr.left, val+curr.left.val))
        return False
        
    # BFS with queue
    def hasPathSum(self, root, sum):
        if not root:
            return False
        queue = [(root, sum-root.val)]
        while queue:
            curr, val = queue.pop(0)
            if not curr.left and not curr.right:
                if val == 0:
                    return True
            if curr.left:
                queue.append((curr.left, val-curr.left.val))
            if curr.right:
                queue.append((curr.right, val-curr.right.val))
        return False
        
    # Recursively 
    def hasPathSum1(self, root, sum):
        if not root:
            return False
        if root and not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
     
    # DFS + stack   
    def hasPathSum(self, root, sum):
        stack = [(root, sum)]
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right and node.val == value:
                    return True
                stack.append((node.right, value-node.val))
                stack.append((node.left, value-node.val))
            else:
                continue
        return False
        
        
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            if sum == root.val:
                return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        


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



.. code-block:: python

    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res
        
    def dfs(self, root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, ls+[root.val], res)
            
    def pathSum(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val]+i for i in tmp]  
            
            

    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res
        
    def dfs(self, root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, ls+[root.val], res)
            
    def pathSum2(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val]+i for i in tmp]

    # BFS + queue    
    def pathSum3(self, root, sum): 
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res
        
    # DFS + stack I  
    def pathSum4(self, root, sum): 
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res 

    # DFS + stack II   
    def pathSum5(self, root, s): 
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res
            
            
            
            
    A shorter version of previous code:

    def pathSum1(self, root, sum):
        res = []
        self.dfs(root, sum, [], res)
        return res
        
    def dfs(self, root, sum, path, res):
        if root:
            if sum == root.val and not root.left and not root.right:
                res.append(path+[root.val])
            self.dfs(root.left, sum-root.val, path+[root.val], res)
            self.dfs(root.right, sum-root.val, path+[root.val], res)
            
    def pathSum2(self, root, sum):
        res, stack = [], [(root, sum, [])]
        while stack:
            node, sum, path = stack.pop()
            if node:
                if node.val == sum and not node.left and not node.right:
                    res.append(path+[node.val])
                stack.append((node.right, sum-node.val, path+[node.val]))
                stack.append((node.left, sum-node.val, path+[node.val]))
        return res
        
    def pathSum(self, root, sum):
        res, queue = [], collections.deque([(root, sum, [])])
        while queue:
            node, sum, path = queue.popleft()
            if node:
                if node.val == sum and not node.left and not node.right:
                    res.append(path+[node.val])
                    continue
                queue.append((node.left, sum-node.val, path+[node.val]))
                queue.append((node.right, sum-node.val, path+[node.val]))
        return res
            
            


111. Minimum Depth of Binary Tree
---------------------------------


Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:
::
    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    return its minimum depth = 2.

.. code-block:: python

        
    # DFS
    def minDepth1(self, root):
        if not root:
            return 0
        if None in [root.left, root.right]:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
     
    # BFS   
    def minDepth(self, root):
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1)) 
        
        
        
    A DFS version to find the minimal depth:

    # DFS       
    def minDepth(self, root):
        if not root:
            return 0
        # res can be set as max_int
        res, stack = 9999, [(root, 1)]
        while stack:
            node, level = stack.pop()
            if node and not node.left and not node.right:
                res = min(res, level)
            if node:
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))
        return res  
        
        


108. Convert Sorted Array to Binary Search Tree
-----------------------------------------------


Given an array where elements are sorted in ascending order, convert it to a height balanced BST.


.. code-block:: python

    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        mid=len(nums)//2
        node=TreeNode(nums[mid])
        node.left=self.sortedArrayToBST(nums[0:mid])
        node.right=self.sortedArrayToBST(nums[mid+1:len(nums)])
        return node
            
            
    def sortedArrayToBST(self, nums):
        if nums:
            mid=len(nums)/2
            node=TreeNode(nums[mid])
            node.left=self.sortedArrayToBST(nums[:mid])
            node.right=self.sortedArrayToBST(nums[mid+1:])
            return node
            

 
.. code-block:: python

    def sortedArrayToBST1(self, nums):
        l, r = 0, len(nums)-1
        if l <= r:
            mid = l + (r-l)//2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root
            
    def sortedArrayToBST(self, nums):
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, l, r):
        if l <= r:
            mid = l + (r-l)//2
            root = TreeNode(nums[mid])
            root.left = self.helper(nums, l, mid-1)
            root.right = self.helper(nums, mid+1, r )
            return root        


109. Convert Sorted List to Binary Search Tree
----------------------------------------------

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

        
.. code-block:: python

    # recursively
    def sortedListToBST(self, head):
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        # here we get the middle point,
        # even case, like '1234', slow points to '2',
        # '3' is root, '12' belongs to left, '4' is right
        # odd case, like '12345', slow points to '2', '12'
        # belongs to left, '3' is root, '45' belongs to right
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root 

        
    # convert linked list to array
    def sortedListToBST1(self, head):
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return self.helper(ls, 0, len(ls)-1)

    def helper(self, ls, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(ls[start])
        mid = (start+end) >> 1
        root = TreeNode(ls[mid])
        root.left = self.helper(ls, start, mid-1)
        root.right = self.helper(ls, mid+1, end)
        return root

    # top-down approach, O(n*logn)
    def sortedListToBST2(self, head):
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        root.left = self.sortedListToBST(head)
        return root
        
    # bottom-up approach, O(n)
    def sortedListToBST3(self, head):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        return self.convert([head], 0, l-1)
        
    def convert(self, head, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(head, start, mid-1)
        root = TreeNode(head[0].val)
        root.left = l
        head[0] = head[0].next 
        root.right = self.convert(head, mid+1, end)
        return root

    # bottom-up approach, O(n)    
    def sortedListToBST(self, head):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        self.node = head
        return self.convert(0, l-1)
        
    def convert(self, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(start, mid-1)
        root = TreeNode(self.node.val)
        root.left = l
        self.node = self.node.next 
        root.right = self.convert(mid+1, end)
        return root
        
    # convert linked list to array
    def sortedListToBST1(self, head):
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return self.helper(ls, 0, len(ls)-1)

    def helper(self, ls, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(ls[start])
        mid = (start+end) >> 1
        root = TreeNode(ls[mid])
        root.left = self.helper(ls, start, mid-1)
        root.right = self.helper(ls, mid+1, end)
        return root

    # top-down approach, O(n*logn)
    def sortedListToBST2(self, head):
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        root.left = self.sortedListToBST(head)
        return root
        
    # bottom-up approach, O(n)
    def sortedListToBST3(self, head):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        return self.convert([head], 0, l-1)
        
    def convert(self, head, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(head, start, mid-1)
        root = TreeNode(head[0].val)
        root.left = l
        head[0] = head[0].next 
        root.right = self.convert(head, mid+1, end)
        return root

    # bottom-up approach, O(n)    
    def sortedListToBST(self, head):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        self.node = head
        return self.convert(0, l-1)
        
    def convert(self, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(start, mid-1)
        root = TreeNode(self.node.val)
        root.left = l
        self.node = self.node.next 
        root.right = self.convert(mid+1, end)
        return root 