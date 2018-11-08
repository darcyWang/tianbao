题目序号 
============================================================



46. Permutations
----------------

Given a collection of distinct integers, return all possible permutations.

Example:
::
    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]


.. code-block:: python

    # DFS
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)  
        

47. Permutations II
-------------------


Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
::
    Input: [1,1,2]
    Output:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]


.. code-block:: python

    # DFS
    def permuteUnique(self, nums):
        res, visited = [], [False]*len(nums)
        nums.sort()
        self.dfs(nums, visited, [], res)
        return res
        
    def dfs(self, nums, visited, path, res):
        if len(nums) == len(path):
            res.append(path)
            return 
        for i in xrange(len(nums)):
            if not visited[i]: 
                if i>0 and not visited[i-1] and nums[i] == nums[i-1]:  # here should pay attention
                    continue
                visited[i] = True
                self.dfs(nums, visited, path+[nums[i]], res)
                visited[i] = False  

    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)  
                    

78. Subsets
-----------


Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
::
    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]


.. code-blokc:: python

    # DFS recursively 
    def subsets1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
        
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
            
    # Bit Manipulation    
    def subsets2(self, nums):
        res = []
        nums.sort()
        for i in xrange(1<<len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
        
    # Iteratively
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res

    # DFS  
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
        
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)    
        

90. Subsets II
--------------

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
::
    Input: [1,2,2]
    Output:
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]


131. Palindrome Partitioning
----------------------------


Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:
::
    Input: "aab"
    Output:
    [
      ["aa","b"],
      ["a","a","b"]
    ]


.. code-block:: python

    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        if not s: # backtracking
            res.append(path)
        for i in xrange(1, len(s)+1):
            if self.isPar(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
                
    def isPar(self, s):
        return s == s[::-1]


164. Maximum Gap
----------------

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.

.. code-block:: python

    class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2 or min(num) == max(num):
            return 0
        a, b = min(num), max(num)
        size = math.ceil((b-a)/(len(num)-1))
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        for n in num:
            b = bucket[(n-a)//size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))



    def maximumGap(self, nums):
        if len(nums) < 2 or max(nums)-min(nums) == 0:   # in case bsize == 0
            return 0
        maxn,minn,lenn = max(nums),min(nums),len(nums)
        bsize = (maxn - minn + 1.0) / lenn  # could have interger issue on OJ
        buckets = [[2**31-1, -1] for _ in range(lenn+1)]
        for i in nums:
            place = int( (i-minn) // bsize )
            buckets[place][0] = min(i, buckets[place][0])
            buckets[place][1] = max(i, buckets[place][1])
        res, prev = 0, buckets[0][0]
        for i in buckets:
            if i != [2**31-1, -1]:
                res = max(res, i[0]-prev)
                prev = i[1]
        return res




79. Word Search
---------------


Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
::
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.


.. code-block:: python

    Really nice way to build trie(). For space saving purpose, I rewrite your code in which way we don't need the "self.used" global variable:

    def findWords(self, board, words):
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board, i, j, trie, '', res)
        return list(set(res))

    def find(self, board, i, j, trie, path, res):
        if '#' in trie:
            res.append(path)
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] not in trie:
            return
        tmp = board[i][j]
        board[i][j] ="@"
        self.find(board, i+1, j, trie[tmp], path+tmp, res)
        self.find(board, i, j+1, trie[tmp], path+tmp, res)
        self.find(board, i-1, j, trie[tmp], path+tmp, res)
        self.find(board, i, j-1, trie[tmp], path+tmp, res)
        board[i][j] = tmp



    class Solution(object):
        def findWords(self, board, words):
            res = []
            trie = Trie()
            node = trie.root
            for w in words:
                trie.insert(w)
            for i in xrange(len(board)):
                for j in xrange(len(board[0])):
                    self.dfs(board, node, i, j, "", res)
            return res

    class Solution:
        # @param {character[][]} board
        # @param {string[]} words
        # @return {string[]}
        def findWords(self, board, words):
        #make trie
            trie={}
            for w in words:
                t=trie
                for c in w:
                    if c not in t:
                        t[c]={}
                    t=t[c]
                t['#']='#'
            self.res=set()
            self.used=[[False]*len(board[0]) for _ in range(len(board))]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    self.find(board,i,j,trie,'')
            return list(self.res)
        
        def find(self,board,i,j,trie,pre):
            if '#' in trie:
                self.res.add(pre)
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return
            if not self.used[i][j] and board[i][j] in trie:
                self.used[i][j]=True
                self.find(board,i+1,j,trie[board[i][j]],pre+board[i][j])
                self.find(board,i,j+1,trie[board[i][j]],pre+board[i][j])
                self.find(board,i-1,j,trie[board[i][j]],pre+board[i][j])
                self.find(board,i,j-1,trie[board[i][j]],pre+board[i][j])
                self.used[i][j]=False

.. code-block:: python

    def exist(self, board, word):
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res  

127. Word Ladder
----------------

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


.. code-block:: python
    
    class Solution(object):
        def ladderLength(self, beginWord, endWord, wordList):
            """
            :type beginWord: str
            :type endWord: str
            :type wordList: List[str]
            :rtype: int
            """
            distance, stack, visited, lookup = 0, [beginWord], set([beginWord]), set(wordList)
            while stack:
                next_stack = []
                for word in stack:
                    if word == endWord:
                        return distance + 1
                    for i in range(len(word)):
                        for char in 'abcdefghijklmnopqrstuvwxyz':
                            trans_word = word[:i] + char + word[i+1:]
                            if trans_word not in visited and trans_word in lookup:
                                next_stack.append(trans_word)
                                visited.add(trans_word)
                distance += 1
                stack = next_stack
            return 0


.. code-block:: python

    def ladderLength(self, beginWord, endWord, wordList):
        # wordList.add(endWord)
        queue = collections.deque([(beginWord, 1)])
        ls = string.ascii_lowercase
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in xrange(len(word)):
                for j in ls:
                    if j != word[i]:
                        newWord = word[:i]+j+word[i+1:]
                        if newWord not in visited and newWord in wordList:
                            queue.append((newWord, dist+1))
                            visited.add(newWord)  # wordList.remove(newWord)
        return 0















