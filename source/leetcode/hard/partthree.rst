题目序号
=================================



89. Gray Code
-------------

https://leetcode.com/problems/gray-code/description/

.. code-block:: python

    class Solution:
        # @param {integer} n
        # @return {integer[]}
        # 9:25
        BASE = ['0', '1']

        def grayCode(self, n):
            if n == 0:
                return [0]

            result = Solution.BASE
            for i in range(n - 1):
                left = map(lambda x: '0' + x, result)
                right = map(lambda x: '1' + x, result[::-1])
                result = left + right

            return map(lambda x: int(x, 2), result)     
                
                
    def grayCode(self, n):
        res = [0]
        for i in xrange(n):
            res += map(lambda x:2**i+x, [x for x in res[::-1]])
        return res  
                
    def grayCode(self, n):
        res = [0]
        for i in xrange(n):
            res += (2**i+x for x in res[::-1])
        return res  


381. Insert Delete GetRandom O(1) - Duplicates allowed
------------------------------------------------------

https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/

.. code-block:: python

    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        # Convert 2d vector to 1d vector first can avoid 
        # the different range issues
        # self.ls = reduce(lambda x, y: x+y, vec2d, [])
        # self.ls = sum(vec2d, [])
        self.ls = [x for row in vec2d for x in row] 
        self.i = 0

    # @return {integer}
    def next(self):
        tmp = self.i
        self.i += 1
        return self.ls[tmp]

    # @return {boolean}
    def hasNext(self):
        return self.i < len(self.ls)



.. code-block:: python

    def __init__(self, dictionary):
        self.dic = collections.defaultdict(set)
        for s in dictionary:
            val = s
            if len(s) > 2:
                s = s[0]+str(len(s)-2)+s[-1]
            self.dic[s].add(val)


25.reverse nodes in k group
---------------------------


Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.


.. code-block:: python

    # Iteratively    
    def reverseKGroup(self, head, k):
        if not head or not head.next or k <= 1:
            return head
        cur, l = head, 0
        while cur:
            l += 1
            cur = cur.next
        if k > l:
            return head
        dummy = pre = ListNode(0)
        dummy.next = head
        # totally l//k groups
        for i in xrange(l//k):
            # reverse each group
            node = None
            for j in xrange(k-1):
                nxt = head.next
                head.next = node
                node = head
                head = nxt
            # update nodes and connect nodes
            tmp = head.next
            head.next = node
            pre.next.next = tmp
            tmp1 = pre.next
            pre.next = head
            head = tmp
            pre = tmp1
        return dummy.next   


23. Merge k Sorted Lists
------------------------

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
::
    Input:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    Output: 1->1->2->3->4->4->5->6

.. code-block:: python

    def mergeKLists(self, lists):
        if not lists:
            return 
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = cur = ListNode(0)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next   

145. Binary Tree Postorder Traversal
------------------------------------

https://leetcode.com/problems/binary-tree-postorder-traversal/description/


.. code-block:: python

    # recursively 
    def postorderTraversal1(self, root):
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            self.dfs(root.right, res)
            res.append(root.val)

    # iteratively        
    def postorderTraversal(self, root):
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]    
        
        
    def postorderTraversal(self, root):
        res = []
        self.dfs(root, res)
        return res[::-1]

    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.right, res)
            self.dfs(root.left, res)    

128. Longest Consecutive Sequence
---------------------------------

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


.. code-block:: python

    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best 