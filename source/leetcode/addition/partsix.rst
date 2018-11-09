题目序号
============================

2. Add Two Numbers
------------------

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

.. code-block:: python

	def addTwoNumbers(self, l1, l2):
	    dummy = cur = ListNode(0)
	    carry = 0
	    while l1 or l2 or carry:
	        if l1:
	            carry += l1.val
	            l1 = l1.next
	        if l2:
	            carry += l2.val
	            l2 = l2.next
	        cur.next = ListNode(carry%10)
	        cur = cur.next
	        carry //= 10
	    return dummy.next	

3. Longest Substring Without Repeating Characters
-------------------------------------------------

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


.. code-block:: python

	def lengthOfLongestSubstring(self, s):
	    dic, res, start, = {}, 0, 0
	    for i, ch in enumerate(s):
	        if ch in dic:
	            # update the res
	            res = max(res, i-start)
	            # here should be careful, like "abba"
	            start = max(start, dic[ch]+1)
	        dic[ch] = i
	    # return should consider the last 
	    # non-repeated substring
	    return max(res, len(s)-start)	




