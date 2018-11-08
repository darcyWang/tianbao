题目序号
========================================



146. LRU Cache
--------------

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

.. code-block:: python

	def __init__(self, capacity):
	    self.dic = collections.OrderedDict()
	    self.remain = capacity

	def get(self, key):
	    if key not in self.dic:
	        return -1
	    v = self.dic.pop(key) 
	    self.dic[key] = v   # set key as the newest one
	    return v

	def set(self, key, value):
	    if key in self.dic:    
	        self.dic.pop(key)
	    else:
	        if self.remain > 0:
	            self.remain -= 1  
	        else:  # self.dic is full
	            self.dic.popitem(last=False) 
	    self.dic[key] = value



	Another solution by using dictionary and deque in Python:

	def __init__(self, capacity):
	    self.deque = collections.deque([])
	    self.dic = {}
	    self.capacity = capacity

	def get(self, key):
	    if key not in self.dic:
	        return -1
	    self.deque.remove(key)
	    self.deque.append(key)
	    return self.dic[key]

	def set(self, key, value):
	    if key in self.dic:    
	        self.deque.remove(key)
	    elif len(self.dic) == self.capacity:
	        v = self.deque.popleft()  # remove the Least Recently Used element
	        self.dic.pop(v)
	    self.deque.append(key)
	    self.dic[key] = value 


.. code-block:: python

	def __init__(self, capacity):
	    self.dic = collections.OrderedDict()
	    self.remain = capacity

	def get(self, key):
	    if key not in self.dic:
	        return -1
	    v = self.dic.pop(key) 
	    self.dic[key] = v   # set key as the newest one
	    return v

	def set(self, key, value):
	    if key in self.dic:    
	        self.dic.pop(key)
	    else:
	        if self.remain > 0:
	            self.remain -= 1  
	        else:  # self.dic is full
	            self.dic.popitem(last=False) 
	    self.dic[key] = value
		
		
	def __init__(self, capacity):
	    self.deque = collections.deque([])
	    self.dic = {}
	    self.capacity = capacity

	def get(self, key):
	    if key not in self.dic:
	        return -1
	    self.deque.remove(key)
	    self.deque.append(key)
	    return self.dic[key]

	def set(self, key, value):
	    if key in self.dic:    
	        self.deque.remove(key)
	    elif len(self.dic) == self.capacity:
	        v = self.deque.popleft()  # remove the Least Recently Used element
	        self.dic.pop(v)
	    self.deque.append(key)
	    self.dic[key] = value 	
		


https://leetcode.com/problems/candy/

.. code-block:: python

	def candy(self, ratings):
	    res = len(ratings) * [1]
	    for i in xrange(1, len(ratings)):  # from left to right
	        if ratings[i] > ratings[i-1]:
	            res[i] = res[i-1] + 1
	    for i in xrange(len(ratings)-1, 0, -1):  # from right to left
	        if ratings[i-1] > ratings[i]:
	            res[i-1] = max(res[i-1], res[i]+1)
	    return sum(res)

224. Basic Calculator
---------------------


https://leetcode.com/problems/basic-calculator/description/


.. code-block:: python

	def calculate(self, s):
	    if not s:
	        return "0"
	    stack, num, sign = [], 0, "+"
	    for i in xrange(len(s)):
	        if s[i].isdigit():
	            num = num*10+ord(s[i])-ord("0")
	        if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
	            if sign == "-":
	                stack.append(-num)
	            elif sign == "+":
	                stack.append(num)
	            elif sign == "*":
	                stack.append(stack.pop()*num)
	            else:
	                tmp = stack.pop()
	                if tmp//num < 0 and tmp%num != 0:
	                    stack.append(tmp//num+1)
	                else:
	                    stack.append(tmp//num)
	            sign = s[i]
	            num = 0
	    return sum(stack)

	def calculate(self, s):
	    res, num, sign, stack = 0, 0, 1, []
	    for ss in s:
	        if ss.isdigit():
	            num = 10*num + int(ss)
	        elif ss in ["-", "+"]:
	            res += sign*num
	            num = 0
	            sign = [-1, 1][ss=="+"]
	        elif ss == "(":
	            stack.append(res)
	            stack.append(sign)
	            sign, res = 1, 0
	        elif ss == ")":
	            res += sign*num
	            res *= stack.pop()
	            res += stack.pop()
	            num = 0
	    return res + num*sign



57. Insert Interval
-------------------

https://leetcode.com/problems/insert-interval/description/


.. code-block:: python

	def insert(self, intervals, newInterval):
	    n, ret = newInterval, []
	    for index, i in enumerate(intervals):
	        if i.end < n.start:
	            ret.append(i)
	        elif n.end < i.start:
	            ret.append(n)
	            return ret + intervals[index:]
	        else:
	            n.start = min(i.start, n.start)
	            n.end = max(i.end, n.end)
	    ret.append(n)
	    return ret


	# O(nlgn) time, the same as Merge Intervals 
	# https://leetcode.com/problems/merge-intervals/
	def insert1(self, intervals, newInterval):
	    intervals.append(newInterval)
	    res = []
	    for i in sorted(intervals, key=lambda x:x.start):
	        if res and res[-1].end >= i.start:
	            res[-1].end = max(res[-1].end, i.end)
	        else:
	            res.append(i)
	    return res
	    
	# O(n) time, not in-place, make use of the 
	# property that the intervals were initially sorted 
	# according to their start times
	def insert(self, intervals, newInterval):
	    res, n = [], newInterval
	    for index, i in enumerate(intervals):
	        if i.end < n.start:
	            res.append(i)
	        elif n.end < i.start:
	            res.append(n)
	            return res+intervals[index:]  # can return earlier
	        else:  # overlap case
	            n.start = min(n.start, i.start)
	            n.end = max(n.end, i.end)
	    res.append(n)
	    return res


72. Edit Distance
-----------------

https://leetcode.com/problems/edit-distance/


.. code-block:: python

	def isOneEditDistance(self, s, t):
	    m, n = len(s), len(t)
	    if m > n:
	        return self.isOneEditDistance(t, s)
	    if n-m > 1:
	        return False
	    i, j = 0, 0
	    while i < m and j < n:
	        if s[i] != t[j]:
	            return s[i+1:] == t[j+1:] or s[i:] == t[j+1:]
	        i += 1; j += 1
	    return n-m == 1
		
	def isOneEditDistance(self, s, t):
	    if s == t:
	        return False
	    l1, l2 = len(s), len(t)
	    if l1 > l2: # force s no longer than t
	        return self.isOneEditDistance(t, s)
	    if l2 - l1 > 1:
	        return False
	    for i in xrange(len(s)):
	        if s[i] != t[i]:
	            if l1 == l2:
	                s = s[:i]+t[i]+s[i+1:]  # replacement
	            else:
	                s = s[:i]+t[i]+s[i:]  # insertion
	            break
	    return s == t or s == t[:-1]


