题目序号
=================================




201. Bitwise AND of Numbers Range
---------------------------------

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
::
    Input: [5,7]
    Output: 4

Example 2:
::
    Input: [0,1]
    Output: 0


.. code-block:: python

    def rangeBitwiseAnd1(self, m, n):
        d = n-m
        p = 0
        while d:
            p += 1
            d /= 2
        return ((m&n)>>p)<<p
        
    def rangeBitwiseAnd2(self, m, n):
        if m == n:
            return m
        return self.rangeBitwiseAnd(m>>1, n>>1) << 1
        
    def rangeBitwiseAnd3(self, m, n):
        p = 0
        while m != n:
            m >>= 1
            n >>= 1
            p += 1
        return m << p
        
    def rangeBitwiseAnd(self, m, n):
        p = 0
        q = m^n
        while q:
            p += 1
            q >>= 1
        return ((m&n)>>p)<<p


238. Product of Array Except Self
---------------------------------

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
::
    Input:  [1,2,3,4]
    Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

.. code-block:: python

    # two-round solution     
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        for i in xrange(1, len(nums)): # from left to right 
            res[i] = res[i-1] * nums[i-1]
        tmp = 1
        for i in xrange(len(nums)-2, -1, -1): # from right to left
            tmp *= nums[i+1]
            res[i] *= tmp
        return res

277. Find the Celebrity
-----------------------

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.



.. code-block:: python

    # brute-force solution
    def findCelebrity(self, n):
        for i in xrange(n):
            tmp = range(i) + range(i+1, n)
            ind = 0
            while ind < len(tmp) and not knows(i, tmp[ind]) and knows(tmp[ind], i):
                ind += 1
            if ind == len(tmp):
                return i
        return -1


259. 3Sum Smaller
-----------------

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?


.. code-block:: python

    # O(n*n) time
    def threeSumSmaller(self, nums, target):
        count = 0
        nums.sort()
        for i in xrange(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    # if (i,j,k) works, then (i,j,k), (i,j,k-1),..., 
                    # (i,j,j+1) all work, totally (k-j) triplets
                    count += k-j
                    j += 1
                else:
                    k -= 1
        return count    
        
92. Reverse Linked List II
--------------------------

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL


.. code-block:: python

    def reverseBetween(self, head, m, n):
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in xrange(m-1):
            pre = pre.next
        cur= pre.next
        # reverse the defined part 
        node = None
        for _ in xrange(n-m+1):
            nxt = cur.next
            cur.next = node
            node = cur
            cur= nxt
        # connect three parts
        pre.next.next = cur
        pre.next = node
        return dummy.next   


61. Rotate List
---------------

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

.. code-block:: python

    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        cur, l = head, 0
        while cur:
            l += 1
            cur = cur.next
        k %= l
        if k == 0:
            return head
        fast = slow = head
        for _ in xrange(k):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        ret = slow.next
        fast.next = head
        slow.next = None
        return ret  

148. Sort List
--------------

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

.. code-block:: python

    # merge sort, recursively 
    def sortList(self, head):
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)
        
    # merge in-place without dummy node        
    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        # get the return node "head"
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                nxt = pre.next
                pre.next = r
                tmp = r.next
                r.next = nxt
                r = tmp
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head 

160. Intersection of Two Linked Lists
-------------------------------------

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.

.. code-block:: python

    # O(m+n) extra space
    def getIntersectionNode1(self, headA, headB):
        stack1, stack2 = [], []
        while headA:
            stack1.append(headA)
            headA = headA.next
        while headB:
            stack2.append(headB)
            headB = headB.next
        pre = None
        while stack1 and stack2:
            if stack1[-1] is stack2.pop():
                pre = stack1.pop()
            else:
                return pre
        return pre
        
    def getIntersectionNode2(self, headA, headB):
        l1, l2 = 0, 0
        cur1, cur2 = headA, headB
        while cur1:
            l1 += 1
            cur1 = cur1.next
        while cur2:
            l2 += 1
            cur2 = cur2.next
        if l1 < l2:
            headA, headB = headB, headA
            l1, l2 = l2, l1
        for _ in xrange(l1-l2):
            headA = headA.next
        while headA:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
    def getIntersectionNode(self, headA, headB):
        if None in (headA, headB):
            return None
        nodeA, nodeB = headA, headB
        while nodeA is not nodeB:
            if nodeA is None:
                nodeA = headB
            else:
                nodeA = nodeA.next
            if nodeB is None:
                nodeB = headA
            else:
                nodeB = nodeB.next
        return nodeA    

203. Remove Linked List Elements
--------------------------------

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

.. code-block:: python

    # O(n) space
    def removeElements1(self, head, val):
        dummy = pre = ListNode(0)
        while head:
            if head.val != val:
                pre.next = ListNode(head.val)
                pre = pre.next
            head = head.next
        return dummy.next
     
    # in-place   
    def removeElements(self, head, val):
        dummy = pre = ListNode(0)
        dummy.next = head
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return dummy.next   
        
    def removeElements(self, head, val):
        dummy = cur = ListNode(0)
        dummy.next = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


75. Sort Colors
---------------

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?


.. code-block:: python

    # count sort    
    def sortColors1(self, nums):
        c0 = c1 = c2 = 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
        nums[:c0] = [0] * c0
        nums[c0:c0+c1] = [1] * c1
        nums[c0+c1:] = [2] * c2
       
    # one pass 
    def sortColors(self, nums):
        # zero and r record the position of "0" and "2" respectively
        l, r, zero = 0, len(nums)-1, 0
        while l <= r:
            if nums[l] == 0:
                nums[l], nums[zero] = nums[zero], nums[l]
                l += 1; zero += 1
            elif nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
