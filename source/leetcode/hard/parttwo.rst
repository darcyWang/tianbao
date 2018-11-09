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


97. Interleaving String
-----------------------

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false


.. code-block:: python

	# O(m*n) space
	def isInterleave1(self, s1, s2, s3):
	    r, c, l= len(s1), len(s2), len(s3)
	    if r+c != l:
	        return False
	    dp = [[True for _ in xrange(c+1)] for _ in xrange(r+1)]
	    for i in xrange(1, r+1):
	        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
	    for j in xrange(1, c+1):
	        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
	    for i in xrange(1, r+1):
	        for j in xrange(1, c+1):
	            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
	               (dp[i][j-1] and s2[j-1] == s3[i-1+j])
	    return dp[-1][-1]

	# O(2*n) space
	def isInterleave2(self, s1, s2, s3):
	    l1, l2, l3 = len(s1)+1, len(s2)+1, len(s3)+1
	    if l1+l2 != l3+1:
	        return False
	    pre = [True for _ in xrange(l2)]
	    for j in xrange(1, l2):
	        pre[j] = pre[j-1] and s2[j-1] == s3[j-1]
	    for i in xrange(1, l1):
	        cur = [pre[0] and s1[i-1] == s3[i-1]] * l2
	        for j in xrange(1, l2):
	            cur[j] = (cur[j-1] and s2[j-1] == s3[i+j-1]) or \
	                     (pre[j] and s1[i-1] == s3[i+j-1])
	        pre = cur[:]
	    return pre[-1]

	# O(n) space
	def isInterleave3(self, s1, s2, s3):
	    r, c, l= len(s1), len(s2), len(s3)
	    if r+c != l:
	        return False
	    dp = [True for _ in xrange(c+1)] 
	    for j in xrange(1, c+1):
	        dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
	    for i in xrange(1, r+1):
	        dp[0] = (dp[0] and s1[i-1] == s3[i-1])
	        for j in xrange(1, c+1):
	            dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or (dp[j-1] and s2[j-1] == s3[i-1+j])
	    return dp[-1]
	    
	# DFS 
	def isInterleave4(self, s1, s2, s3):
	    r, c, l= len(s1), len(s2), len(s3)
	    if r+c != l:
	        return False
	    stack, visited = [(0, 0)], set((0, 0))
	    while stack:
	        x, y = stack.pop()
	        if x+y == l:
	            return True
	        if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
	            stack.append((x+1, y)); visited.add((x+1, y))
	        if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
	            stack.append((x, y+1)); visited.add((x, y+1))
	    return False
	            
	# BFS 
	def isInterleave(self, s1, s2, s3):
	    r, c, l= len(s1), len(s2), len(s3)
	    if r+c != l:
	        return False
	    queue, visited = [(0, 0)], set((0, 0))
	    while queue:
	        x, y = queue.pop(0)
	        if x+y == l:
	            return True
	        if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
	            queue.append((x+1, y)); visited.add((x+1, y))
	        if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
	            queue.append((x, y+1)); visited.add((x, y+1))
	    return False


174. Dungeon Game
-----------------

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

.. image:: 
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

.. code-block:: python

	# O(m*n) space
	def calculateMinimumHP1(self, dungeon):
	    if not dungeon:
	        return 
	    r, c = len(dungeon), len(dungeon[0])
	    dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
	    dp[-1][-1] = max(1, 1-dungeon[-1][-1])
	    for i in xrange(c-2, -1, -1):
	        dp[-1][i] = max(1, dp[-1][i+1]-dungeon[-1][i])
	    for i in xrange(r-2, -1, -1):
	        dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])
	    for i in xrange(r-2, -1, -1):
	        for j in xrange(c-2, -1, -1):
	            dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
	    return dp[0][0]
	    
	# O(n) space
	def calculateMinimumHP(self, dungeon):
	    if not dungeon:
	        return 
	    r, c = len(dungeon), len(dungeon[0])
	    dp = [0 for _ in xrange(c)]
	    dp[-1] = max(1, 1-dungeon[-1][-1])
	    for i in xrange(c-2, -1, -1):
	        dp[i] = max(1, dp[i+1]-dungeon[-1][i])
	    for i in xrange(r-2, -1, -1):
	        dp[-1] = max(1, dp[-1]-dungeon[i][-1])
	        for j in xrange(c-2, -1, -1):
	            dp[j] = max(1, min(dp[j], dp[j+1])-dungeon[i][j])
	    return dp[0]

	>>> from timeit import timeit
	>>> c = 100
	>>> timeit(lambda: [0 for _ in xrange(c)])
	10.002701801200814
	>>> timeit(lambda: [0] * c)
	1.77059385744343


115. Distinct Subsequences
--------------------------


Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^


.. code-block:: python

	# O(m*n) space 
	def numDistinct1(self, s, t):
	    l1, l2 = len(s)+1, len(t)+1
	    dp = [[1] * l2 for _ in xrange(l1)]
	    for j in xrange(1, l2):
	        dp[0][j] = 0
	    for i in xrange(1, l1):
	        for j in xrange(1, l2):
	            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1])
	    return dp[-1][-1]
	  
	# O(n) space  
	def numDistinct(self, s, t):
	    l1, l2 = len(s)+1, len(t)+1
	    cur = [0] * l2
	    cur[0] = 1
	    for i in xrange(1, l1):
	        pre = cur[:]
	        for j in xrange(1, l2):
	            cur[j] = pre[j] + pre[j-1]*(s[i-1] == t[j-1])
	    return cur[-1]



233. Number of Digit One
------------------------

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.


.. code-block:: python

	def countDigitOne(self, n):
	    if n <= 0:
	        return 0
	    if 1 <= n <= 9:
	        return 1
	    # compute the first bit
	    head, level = n, 1
	    while head > 9:
	        level *= 10
	        head //= 10
	    # if the first bit is 1
	    # like 191, divide it into (0-99), (0-91) and the first bit in (100, 101, 1.., 191)
	    if head == 1:
	        return  self.countDigitOne(level-1) + self.countDigitOne(n-level) + n-level +1
	    # like 491, divide it into (0-99), (100-199), (200-299, 300-399) and (400-491)
	    return (head) * self.countDigitOne(level-1) + self.countDigitOne(n-head*level) + level	
		
		

