题目序号 223、
============================================================




223. Rectangle Area
-------------------


Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

.. image:: https://assets.leetcode.com/uploads/2018/10/22/rectangle_area.png

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.

.. code-block:: python

    class Solution(object):
        def computeArea(self, A, B, C, D, E, F, G, H):
            """
            :type A: int
            :type B: int
            :type C: int
            :type D: int
            :type E: int
            :type F: int
            :type G: int
            :type H: int
            :rtype: int
            """
            return (C - A) * (D - B) + (H - F) * (G - E) - max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)


.. code-block:: python

    class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        S=(C-A)*(D-B) + (G-E)*(H-F)
        if A>G or C<E or D<F or B>H :
            return S
        else:
            s_common=(min(C,G)-max(A,E))*(min(D,H)-max(B,F))
            return S-s_common
        
        
    def computeArea(self, A, B, C, D, E, F, G, H):
        overlap = max(0, min(C, G)-max(A, E)) * max(0, min(D, H)-max(B, F))
        return (C-A)*(D-B)+(G-E)*(H-F)-overlap
        



83. Remove Duplicates from Sorted List
--------------------------------------


Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3


.. code-block:: python

    def deleteDuplicates(self, head):
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
        
        
    def deleteDuplicates1(self, head):
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
        
    def deleteDuplicates(self, head):
        dic = {}
        node = head
        while node:
            dic[node.val] = dic.get(node.val, 0) + 1
            node = node.next
        node = head
        while node:
            tmp = node
            for _ in xrange(dic[node.val]):
                tmp = tmp.next
            node.next = tmp
            node = node.next
        return head
        
    def deleteDuplicates(self, head):
        dic = {}
        node = head
        while node:
            dic[node.val] = dic.get(node.val, 0) + 1
            node = node.next
        node = head
        dummy = pre = ListNode(0)
        dummy.next = head
        while node:
            if dic[node.val] > 1:
                tmp = node
                for _ in xrange(dic[node.val]):
                    tmp = tmp.next
                pre.next = tmp
                node = tmp
            else:
                pre = node
                node = node.next
        return dummy.next


.. code-block:: python

    class Solution(object):
        def deleteDuplicates(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if not head:
                return head
            dummy = prev = ListNode(None)
            while head:
                if head.val == prev.val:
                    if not head.next:
                        prev.next = None
                else:
                    prev.next = head
                    prev = prev.next
                head = head.next
                
            return dummy.next

    class Solution(object):
        def deleteDuplicates(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            dummy = head
            while head:
                while head.next and head.next.val == head.val:
                    head.next = head.next.next    # skip duplicated node
                head = head.next     # not duplicate of current node, move to next node
            return dummy


82. Remove Duplicates from Sorted List II
-----------------------------------------



Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3


.. code-block:: python

    class Solution(object):
        def deleteDuplicates(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            dummy = prev = cur = ListNode(None)
            while head:
                while head and ((head.val == prev.val) or (head.next and head.next.val == head.val)):
                    prev = head
                    head = head.next
                cur.next = head
                cur = cur.next
                if head:
                    head = head.next  
                
            return dummy.next
    class Solution(object):
        def deleteDuplicates(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if not head:
                return None
            nxt, is_head_dup = head.next, False
            while nxt and nxt.val == head.val:
                nxt, is_head_dup = nxt.next, True
            head.next = self.deleteDuplicates(nxt)
            return head.next if is_head_dup else head


    def deleteDuplicates(self, head):
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next   

141. Linked List Cycle
----------------------

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?


.. code-block:: python

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        # @param head, a ListNode
        # @return a boolean
        def hasCycle(self, head):
            if not head:
                return False

            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True

            return False



用个字典记录某个点是否被访问过，时间，空间复杂度都是O（n）
.. code-block:: python
    
    class Solution(object):
        def hasCycle(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            if not head: 
                return False
            lookup = {}
            while head:
                if head in lookup:
                    return True
                lookup[head] = 1
                head = head.next
            return False

时间复杂度: O(N) 空间复杂度: O(1) 

.. code-block:: python

    class Solution(object):
        def hasCycle(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False


142. Linked List Cycle II
-------------------------


Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?



.. code-block:: python

    def detectCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # if there is a cycle
            if slow is fast:
                # the head and slow nodes move step by step
                while head:
                    if head == slow:
                        return head
                    head = head.next
                    slow = slow.next
        return None
        
        
        
    def detectCycle1(self, head):
        dic = {}
        while head:
            if head in dic:
                return head
            dic[head] = 0
            head = head.next
        return None
        
    def detectCycle(self, head):
        if not head:
            return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                fast = head
                while fast and fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None 
            
            
    def detectCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # if there is a cycle
            if slow is fast:
                # the head and slow nodes move step by step
                while head:
                    if head == slow:
                        return head
                    head = head.next
                    slow = slow.next
        return None

    Python solutions using dictionary and two-pointer:

    def detectCycle1(self, head):
        dic = {}
        while head:
            if head in dic:
                return head
            dic[head] = 0
            head = head.next
        return None
        
    def detectCycle(self, head):
        if not head:
            return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                fast = head
                while fast and fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
        
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head



143. Reorder List
-----------------


Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

    For linked list 1->2->3->4-5, the code first makes the list to be 1->2->3->4<-5 and 4->None, then make 3->None, for even number linked list: 1->2->3->4, make first 1->2->3<-4 and 3->None, and lastly do not forget to make 2->None.

.. code-block:: python

    def reorderList(self, head):
        if not head:
            return
        # ensure the first part has the same or one more node
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        p = slow.next
        slow.next = None
        node = None
        while p:
            nxt = p.next
            p.next = node
            node = p
            p = nxt
        # combine head part and node part
        p = head
        while node:
            tmp = node.next
            node.next = p.next
            p.next = node
            p = p.next.next #p = node.next
            node = tmp



124. Binary Tree Maximum Path Sum
---------------------------------


Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
::
    Input: [1,2,3]

           1
          / \
         2   3

    Output: 6

Example 2:
::
    Input: [-10,9,20,null,null,15,7]

       -10
       / \
      9  20
        /  \
       15   7

    Output: 42


.. code-block:: python

    # Recursively 
    def maxPathSum(self, root):
        self.res = -sys.maxsize-1
        self.oneSideSum(root)
        return self.res
        
    # compute one side maximal sum, 
    # (root+left children, or root+right children),
    # root is the included top-most node 
    def oneSideSum(self, root):
        if not root:
            return 0
        l = max(0, self.oneSideSum(root.left))
        r = max(0, self.oneSideSum(root.right))
        self.res = max(self.res, l+r+root.val)
        return max(l, r)+root.val



    A little bit improvement, if the root is None we can output 0 instead of MinInt, and then we can set self.res to node.val .

    def maxPathSum(self, root):
        if not root:
            return 0
        self.res = root.val
        self.oneSum(root)
        return self.res
        
    def oneSum(self, node):
        if not node:
            return 0
        l = max(0, self.oneSum(node.left))
        r = max(0, self.oneSum(node.right))
        self.res = max(self.res, node.val+l+r)
        return node.val + max(l, r)


190. Reverse Bits
-----------------



Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?


.. code-block:: python

    def reverseBits1(self, n):
        return int(bin(n)[2:].rjust(32, '0')[::-1], 2)
        
    def reverseBits2(self, n):
        bit = [0] * 32
        i = 0
        while n:
            bit[i] = n % 2
            n /= 2
            i += 1
        res = 0
        for i in xrange(32):
            res = res*2 + bit[i]
        return res
        
    def reverseBits3(self, n):
        res = 0
        for i in xrange(32):
            # (1) should not be res = res<<1 + (n>>1)&1, why???
            # res = res*2 + n%2
            res = (res<<1) + (n&1)
            n /= 2
        return res
        
    def reverseBits4(self, n):
        res = 0
        for i in xrange(32):
            # (2) here "int" should not be omitted, why??? 
            # res = int(res<<1) + int((n>>i)&1) 
            res = (res<<1) + ((n>>i)&1) 
        return res
            
    def reverseBits(self, n):
        res = 0
        for i in xrange(32):
            res += ((n>>i)&1)*(1<<(31-i))
        return res