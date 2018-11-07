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











