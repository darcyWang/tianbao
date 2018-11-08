题目序号
======================================



41. First Missing Positive
--------------------------

https://leetcode.com/problems/first-missing-positive/description/

.. code-block:: python

	# O(n) time
	def firstMissingPositive(self, nums):
	    for i in xrange(len(nums)):
	        while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
	            tmp = nums[i]-1
	            nums[i], nums[tmp] = nums[tmp], nums[i]
	    for i in xrange(len(nums)):
	        if nums[i] != i+1:
	            return i+1
	    return len(nums)+1
	    
	# O(nlgn) time
	def firstMissingPositive(self, nums):
	    nums.sort()
	    res = 1
	    for num in nums:
	        if num == res:
	            res += 1
	    return res

296. Best Meeting Point
-----------------------

https://leetcode.com/problems/best-meeting-point/

.. code-block:: python

	def minTotalDistance(self, grid):
	    if not grid:
	        return 0
	    r, c = len(grid), len(grid[0])
	    sumr = [i for i in xrange(r) for j in xrange(c) if grid[i][j]]
	    sumc = [j for i in xrange(r) for j in xrange(c) if grid[i][j]]
	    sumr.sort()
	    sumc.sort()
	    mid_row = sumr[len(sumr)/2]
	    mid_col = sumc[len(sumc)/2]
	    return sum([abs(r-mid_row) for r in sumr]) + sum([abs(c-mid_col) for c in sumc])	
		

87. Scramble String
-------------------

https://leetcode.com/problems/scramble-string/

.. code-block:: python

	# DP 
	def isScramble1(self, s1, s2):
	    if len(s1) != len(s2):
	        return False
	    if s1 == s2:
	        return True
	    if sorted(s1) != sorted(s2): # prunning
	        return False
	    for i in xrange(1, len(s1)):
	        if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
	        (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
	            return True
	    return False
	    
	# DP with memorization
	def __init__(self):
	    self.dic = {}
	    
	def isScramble(self, s1, s2):
	    if (s1, s2) in self.dic:
	        return self.dic[(s1, s2)]
	    if len(s1) != len(s2) or sorted(s1) != sorted(s2): # prunning
	        self.dic[(s1, s2)] = False
	        return False
	    if s1 == s2:
	        self.dic[(s1, s2)] = True
	        return True
	    for i in xrange(1, len(s1)):
	        if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
	        (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
	            return True
	    self.dic[(s1, s2)] = False
	    return False	

99. Recover Binary Search Tree
------------------------------

https://leetcode.com/problems/recover-binary-search-tree/


.. code-block:: python

	# average O(lgn) space (worst case O(n) space), iteratively, one-pass
	def recoverTree(self, root):
	    res, stack, first, second = None, [], None, None
	    while True:
	        while root:
	            stack.append(root)
	            root = root.left
	        if not stack:
	            break 
	        node = stack.pop()
	        # first time occurs reversed order
	        if res and res.val > node.val:
	            if not first:
	                 first = res
	            # first or second time occurs reversed order
	            second = node
	        res = node
	        root = node.right
	    first.val, second.val = second.val, first.val
	 
	# average O(lgn) space (worst case, O(n) space), recursively, one-pass 
	def recoverTree2(self, root):
	    self.prevNode = TreeNode(-sys.maxsize-1)
	    self.first, self.second = None, None
	    self.inorder(root)
	    self.first.val, self.second.val = self.second.val, self.first.val
	    
	def inorder(self, root):
	    if not root:
	        return 
	    self.inorder(root.left)
	    if not self.first and self.prevNode.val > root.val:
	        self.first, self.second = self.prevNode, root
	    if self.first and self.prevNode.val > root.val:
	        self.second = root
	    self.prevNode = root
	    self.inorder(root.right)
	    
	# average O(n+lgn) space, worst case O(2n) space, recursively, two-pass
	def recoverTree3(self, root):
	    res = []
	    self.helper(root, res)
	    first, second = None, None
	    for i in xrange(1, len(res)):
	        if not first and res[i-1].val > res[i].val:
	            first, second = res[i-1], res[i]
	        if first and res[i-1].val > res[i].val:
	            second = res[i]
	    first.val, second.val = second.val, first.val
	    
	def helper(self, root, res):
	    if root:
	        self.helper(root.left, res)
	        res.append(root)
	        self.helper(root.right, res)	

