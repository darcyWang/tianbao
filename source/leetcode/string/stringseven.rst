题目序号 21、28、19、206、215、286
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


        
    # iteratively
    def mergeTwoLists1(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
        
    # recursively    
    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            
    # in-place, iteratively        
    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next   

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



215. Kth Largest Element in an Array
-------------------------------------




Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
::
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5

Example 2:
::
    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.


.. code-block:: python

    # k+(n-k)*log(k) time
    def findKthLargest1(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)  # create a min-heap whose size is k 
        for num in nums[k:]:
            if num > heap[0]:
               heapq.heapreplace(heap, num)
            # or use:
            # heapq.heappushpop(heap, num)
        return heap[0]
      
    # O(n) time, quicksort-Partition method   
    def findKthLargest(self, nums, k):
        pos = self.partition(nums, 0, len(nums)-1)
        if pos > len(nums) - k:
            return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
        elif pos < len(nums) - k:
            return self.findKthLargest(nums[pos+1:], k)
        else:
            return nums[pos]





286. Walls and Gates
---------------------

You are given a m x n 2D grid initialized with these three possible values.

.. hint::

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. 

We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
For example, given the 2D grid:


.. hint::

    INF  -1  0  INF
    INF INF INF  -1
    INF  -1 INF  -1
      0  -1 INF INF


After running your function, the 2D grid should be:


.. hint:: 

    3  -1   0   1
    2   2   1  -1
    1  -1   2  -1
    0  -1   3   4

#. 这里附上了BFS和DFS的解法，但是显然BFS更快。最先找到gate，然后以gate为root进行BFS遍历，叶子节点为四个方向。
#. 最巧妙地部分是这里定义了static final d，来确定四个方向的位置，即通过用i，j +/- 1的方式来得到[i, j+1],[i+1,j],[i, j-1], [i-1, j]。
#. 注意在遍历四个方向时不要出界。
   

.. code-block:: python
    
    # BFS
    def wallsAndGates(self, rooms):
        if not rooms:
            return 
        r, c= len(rooms), len(rooms[0])
        for i in xrange(r):
            for j in xrange(c):
                if rooms[i][j] == 0:
                    queue = collections.deque([])
                    queue.append((i+1, j, 1)); queue.append((i-1, j, 1))
                    queue.append((i, j+1, 1)); queue.append((i, j-1, 1))
                    visited = set()
                    while queue:
                        x, y, val = queue.popleft()
                        if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] in [0, -1] or (x, y) in visited:
                            continue
                        visited.add((x, y))
                        rooms[x][y] = min(rooms[x][y], val)
                        queue.append((x+1, y, val+1)); queue.append((x-1, y, val+1))
                        queue.append((x, y+1, val+1)); queue.append((x, y-1, val+1))




    After checking this solution, the code above can be shorten by using a better prunning clause, no visited flag is needed:

    def wallsAndGates(self, rooms):
        if not rooms:
            return 
        r, c= len(rooms), len(rooms[0])
        for i in xrange(r):
            for j in xrange(c):
                if rooms[i][j] == 0:
                    queue = collections.deque([(i+1, j, 1), (i-1, j, 1), (i, j+1, 1), (i, j-1, 1)])
                    while queue:
                        x, y, val = queue.popleft()
                        if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] <= val:
                            continue
                        rooms[x][y] = val
                        queue.extend([(x+1, y, val+1), (x-1, y, val+1), (x, y+1, val+1), (x, y-1, val+1)])



