题目序号 71、93、208、211、24、179、228
============================================================



71. Simplify Path
-----------------

Given an absolute path for a file (Unix-style), simplify it. 

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".


非常简单的模拟题，利用一个栈来储存当前的路径。用 "/" 将输入的全路径分割成多个部分，对于每一个部分循环处理：如果为空或者 "." 则忽略，如果是 ".." ，则出栈顶部元素（如果栈为空则忽略），其他情况直接压入栈即可。


.. code-block:: python
    
    class Solution(object):
        def simplifyPath(self, path):
            """
            :type path: str
            :rtype: str
            """
            stack = []
            for part in path.split("/"):
                if part and part != ".": # 如果为空或者 "." 则忽略
                    if part == "..":
                        if stack:
                            stack.pop()
                    else:
                        stack.append(part)
            if not stack:
                return "/"
            else:
                return "/" + "/".join(stack)


.. code-block:: python

    # with stack
    def simplifyPath1(self, path):
        stack = []
        for item in path.split("/"):
            if item not in [".", "..", ""]:
                stack.append(item)
            if item == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)
        
    # with deque
    def simplifyPath(self, path):
        deque = collections.deque()
        for item in path.split("/"):
            if item not in [".", "..", ""]:
                deque.append(item)
            if item == ".." and deque:
                deque.pop()
        return "/" + "/".join(deque)            
                
        
93. Restore IP Addresses
------------------------


Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:
:: 
    Input: "25525511135"
    Output: ["255.255.11.135", "255.255.111.35"]


.. code-block:: python

    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 4, 0, [], res)
        return res
        
    def dfs(self, s, level, index, path, res):
        if level == 0:
            l = sum(map(len, path))
            if l < len(s):
                return  # backtracking 
            else:
                res.append(".".join(path))
                return 
        for i in xrange(1, 4):
            if index+i <= len(s) and self.valid(s[index:index+i]):
                self.dfs(s, level-1, index+i, path+[s[index:index+i]], res)

    def valid(self, s):
        if len(s) == 2 and s[0] == "0":
            return False
        if len(s) == 3 and (s[0] == "0" or s > "255"):
            return False
        return True


.. code-block:: python

    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res
        
    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return # backtracking
        for i in xrange(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                #choose one digit
                if i == 1: 
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                #choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0": 
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                #choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
        
        
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res
        
    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return # backtracking
        for i in xrange(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                if s[0] == "0":  # here should be careful 
                    break

208. Implement Trie (Prefix Tree)
---------------------------------

Implement a trie with insert, search, and startsWith methods.

Example:
::
    Trie trie = new Trie();

    trie.insert("apple");
    trie.search("apple");   // returns true
    trie.search("app");     // returns false
    trie.startsWith("app"); // returns true
    trie.insert("app");   
    trie.search("app");     // returns true

Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.


.. code-block:: python

    class TrieNode(object):
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.childs = dict()
            self.isWord = False
            
            

    class Trie(object):

        def __init__(self):
            self.root = TrieNode()

        def insert(self, word):
            """
            Inserts a word into the trie.
            :type word: str
            :rtype: void
            """
            node = self.root
            for letter in word:
                child = node.childs.get(letter)
                if child is None:
                    child = TrieNode()
                    node.childs[letter] = child
                node = child
            node.isWord = True

        def search(self, word):
            """
            Returns if the word is in the trie.
            :type word: str
            :rtype: bool
            """
            node = self.root
            for i in word:
                child = node.childs.get(i)
                if child is None:
                    return False
                node = child
            return node.isWord
            

        def startsWith(self, prefix):
            """
            Returns if there is any word in the trie
            that starts with the given prefix.
            :type prefix: str
            :rtype: bool
            """
            node = self.root
            for letter in prefix:
                child = node.childs.get(letter)
                if child is None:
                    return False
                node = child
            return True
            

    # Your Trie object will be instantiated and called as such:
    # trie = Trie()
    # trie.insert("somestring")
    # trie.search("key")


.. code-block:: python

    class TrieNode():
        def __init__(self):
            self.children = collections.defaultdict(TrieNode)
            self.isWord = False
        
    class Trie():
        def __init__(self):
            self.root = TrieNode()
        
        def insert(self, word):
            node = self.root
            for w in word:
                node = node.children[w]
            node.isWord = True
        
        def search(self, word):
            node = self.root
            for w in word:
                node = node.children.get(w)
                if not node:
                    return False
            return node.isWord

211. Add and Search Word - Data structure design
------------------------------------------------


Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:
::
    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.


.. code-block:: python

    class TrieNode():
        def __init__(self):
            self.children = collections.defaultdict(TrieNode)
            self.isWord = False
        
    class WordDictionary(object):
        def __init__(self):
            self.root = TrieNode()

        def addWord(self, word):
            node = self.root
            for w in word:
                node = node.children[w]
            node.isWord = True

        def search(self, word):
            node = self.root
            self.res = False
            self.dfs(node, word)
            return self.res
        
        def dfs(self, node, word):
            if not word:
                if node.isWord:
                    self.res = True
                return 
            if word[0] == ".":
                for n in node.children.values():
                    self.dfs(n, word[1:])
            else:
                node = node.children.get(word[0])
                if not node:
                    return 
                self.dfs(node, word[1:])



24. Swap Nodes in Pairs
-----------------------

Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Good solution, here is a solution uses only one pointer:
.. code-block:: python

    def swapPairs(self, head):
        dummy = p = ListNode(0)
        dummy.next = head
        while p.next and p.next.next:
            tmp = head.next
            head.next = head.next.next
            tmp.next = head
            p.next = tmp
            # p = p.next.next
            # p = tmp.next
            p = head
            head = head.next
        return dummy.next

.. code-block:: python

    # Iteratively
    def swapPairs1(self, head):
        dummy = p = ListNode(0)
        dummy.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            p.next = tmp
            head = head.next
            p = tmp.next
        return dummy.next
     
    # Recursively    
    def swapPairs(self, head):
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head 
        
    # iteratively
    def swapPairs1(self, head):
        if not head or not head.next:
            return head
        second = head.next 
        pre = ListNode(0)
        while head and head.next:
            nxt = head.next
            head.next = nxt.next
            nxt.next = head
            pre.next = nxt
            head = head.next
            pre = nxt.next
        return second

    # recursively    
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second   


.. code-block:: python

    # Iteratively
    def swapPairs1(self, head):
        dummy = p = ListNode(0)
        dummy.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            p.next = tmp
            head = head.next
            p = tmp.next
        return dummy.next
     
    # Recursively    
    def swapPairs(self, head):
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head
        
        
        
    # iteratively
    def swapPairs1(self, head):
        if not head or not head.next:
            return head
        second = head.next 
        pre = ListNode(0)
        while head and head.next:
            nxt = head.next
            head.next = nxt.next
            nxt.next = head
            pre.next = nxt
            head = head.next
            pre = nxt.next
        return second

    # recursively    
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second
        

179. Largest Number
-------------------

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
::
    Input: [10,2]
    Output: "210"

Example 2:
::
    Input: [3,30,34,5,9]
    Output: "9534330"


Note: The result may be very large, so you need to return a string instead of an integer.

"""
Replacement for built-in funciton cmp that was removed in Python 3

Compare the two objects x and y and return an integer according to
the outcome. The return value is negative if x < y, zero if x == y
and strictly positive if x > y.
"""

.. code-block:: python

    class Solution(object):
        def largestNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: str
            """
            nums = [str(num) for num in nums]
            nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
            return ''.join(nums).lstrip('0') if ''.join(num).lstrip('0') else '0'

    class Solution(object):
        def largestNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: str
            """
            nums = [str(num) for num in nums]
            nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
            return ''.join(nums).lstrip('0') or '0'



.. code-block:: python

    # build-in function
    def largestNumber1(self, nums):
        if not any(nums):
            return "0"
        return "".join(sorted(map(str, nums), cmp=lambda n1, n2: -1 if n1+n2>n2+n1 else (1 if n1+n2<n2+n1 else 0)))
        
    # bubble sort
    def largestNumber2(self, nums):
        for i in xrange(len(nums), 0, -1):
            for j in xrange(i-1):
                if not self.compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(map(str, nums))))
        
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
        
    # selection sort
    def largestNumber3(self, nums):
        for i in xrange(len(nums), 0, -1):
            tmp = 0
            for j in xrange(i):
                if not self.compare(nums[j], nums[tmp]):
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return str(int("".join(map(str, nums))))
        
    # insertion sort
    def largestNumber4(self, nums):
        for i in xrange(len(nums)):
            pos, cur = i, nums[i]
            while pos > 0 and not self.compare(nums[pos-1], cur):
                nums[pos] = nums[pos-1]  # move one-step forward
                pos -= 1
            nums[pos] = cur
        return str(int("".join(map(str, nums))))

    # merge sort        
    def largestNumber5(self, nums):
        nums = self.mergeSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums))))
        
    def mergeSort(self, nums, l, r):
        if l > r:
            return 
        if l == r:
            return [nums[l]]
        mid = l + (r-l)//2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid+1, r)
        return self.merge(left, right)
        
    def merge(self, l1, l2):
        res, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if not self.compare(l1[i], l2[j]):
                res.append(l2[j])
                j += 1
            else:
                res.append(l1[i])
                i += 1
        res.extend(l1[i:] or l2[j:])
        return res
        
    # quick sort, in-place
    def largestNumber(self, nums):
        self.quickSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums)))) 

    def quickSort(self, nums, l, r):
        if l >= r:
            return 
        pos = self.partition(nums, l, r)
        self.quickSort(nums, l, pos-1)
        self.quickSort(nums, pos+1, r)
        
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low  
        

228. Summary Ranges
-------------------


Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
::
    Input:  [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:
::
    Input:  [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


Just collect the ranges, then format and return them.

.. code-block:: python

    class Solution(object):
        def summaryRanges(self, nums):
            """
            :type nums: List[int]
            :rtype: List[str]
            """
            ranges = []
            for i in nums:
                if not ranges or i > ranges[-1][-1] + 1:
                    ranges += [],
                ranges[-1][1:] = i,
            return ['->'.join(map(str, r)) for r in ranges]     

.. code-block:: python

    def summaryRanges(self, nums):
        if not nums:
            return []
        res, i, start = [], 0, 0
        while i < len(nums)-1:
            if nums[i]+1 != nums[i+1]:
                res.append(self.printRange(nums[start], nums[i]))
                start = i+1
            i += 1
        res.append(self.printRange(nums[start], nums[i]))
        return res

    def printRange(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)
            













