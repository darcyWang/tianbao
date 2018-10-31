题目序号 21、28、19、206
============================================================


21. Merge Two Sorted Lists
--------------------------


Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
::
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4

.. code-block:: python

    def mergeTwoLists(self, l1, l2):
        head = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)  # or l1
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)  # or l2
                l2 = l2.next
            head = head.next
        head.next = l1 or l2
        return dummy.next
        
    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

28. Implement strStr()
----------------------

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

还没来得及仔细看答案
https://www.youtube.com/watch?v=GTJr8OvyEVQ



19. Remove Nth Node From End of List
-------------------------------------

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
::
    Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?


技巧 dummy head 和双指针。切记最后要返回dummy.next而不是head，因为有这样一种情况，删掉节点后linked list空了，那返回head的话结果显然不同。如： 输入链表为[1], n = 1, 应该返回None而不是[1]

.. code-block:: python
    
    class Solution(object):
        def removeNthFromEnd(self, head, n):
            """
            :type head: ListNode
            :type n: int
            :rtype: ListNode
            """
            dummy = ListNode(-1)
            dummy.next = head
            p, q = dummy, dummy
            
            for i in range(n):
                q = q.next
                
            while q.next:
                p = p.next
                q = q.next
            
            p.next = p.next.next
            return dummy.next

        def removeNthFromEnd(self, head, n):
            dummy = ListNode(0)
            dummy.next = head
            fast = slow = dummy
            for _ in xrange(n):
                fast = fast.next
            while fast and fast.next:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
            return dummy.next


206. Reverse Linked List
--------------------------

Reverse a singly linked list.

Example:
::
    
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL


Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


.. code-block:: python

    # Iteratively
    def reverseList1(self, head):
        node = None
        while head:
            tmp = head.next
            head.next = node
            node = head
            head = tmp
        return node
     
    # Recursively    
    def reverseList(self, head):
        return self.helper(head, None)
        
    def helper(self, head, node):
        if not head:
            return node
        tmp = head.next
        head.next = node
        return self.helper(tmp, head)



用三个指针，分别指向prev，cur 和 nxt，然后loop一圈还算比较简单.