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




51. N-Queens
------------


https://leetcode.com/problems/n-queens/description/

.. code-block:: python

    def solveNQueens(self, n):
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res
     
    # nums is a one-dimension array, like [1, 3, 0, 2] means
    # first queen is placed in column 1, second queen is placed
    # in column 3, etc.
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return  # backtracking
        for i in xrange(len(nums)):
            nums[index] = i
            if self.valid(nums, index):  # pruning
                tmp = "."*len(nums)
                self.dfs(nums, index+1, path+[tmp[:i]+"Q"+tmp[i+1:]], res)

    # check whether nth queen can be placed in that column
    def valid(self, nums, n):
        for i in xrange(n):
            if abs(nums[i]-nums[n]) == n -i or nums[i] == nums[n]:
                return False
        return True 

52. N-Queens II
---------------

https://leetcode.com/problems/n-queens-ii/

.. code-block:: python
    
    def totalNQueens(self, n):
        self.res = 0
        self.dfs([-1]*n, 0)
        return self.res
        
    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1
            return 
        for i in xrange(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                self.dfs(nums, index+1)
        
    def valid(self, nums, n):
        for i in xrange(n):
            if nums[i] == nums[n] or abs(nums[n]-nums[i]) == n-i:
                return False
        return True 


4. Median of Two Sorted Arrays
------------------------------


https://leetcode.com/problems/median-of-two-sorted-arrays/description/



.. code-block:: python

    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2:  # the length is odd
            return self.findKthSmallest(nums1, nums2, l//2+1)
        else:
            return (self.findKthSmallest(nums1, nums2, l//2) +
            self.findKthSmallest(nums1, nums2, l//2+1))*0.5
        
    def findKthSmallest(self, nums1, nums2, k):
        # force nums1 is not longer than nums2
        if len(nums1) > len(nums2):
            return self.findKthSmallest(nums2, nums1, k)
        if not nums1:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        pa = min(k/2, len(nums1)); pb = k-pa  # take care here
        if nums1[pa-1] <= nums2[pb-1]:
            return self.findKthSmallest(nums1[pa:], nums2, k-pa)
        else:
            return self.findKthSmallest(nums1, nums2[pb:], k-pb)    
        
        
    class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l=len(A)+len(B)
        return self.findKth(A,B,l//2) if l%2==1 else (self.findKth(A,B,l//2-1)+self.findKth(A,B,l//2))/2.0


    def findKth(self,A,B,k):
        if len(A)>len(B):
            A,B=B,A
        if not A:
            return B[k]
        if k==len(A)+len(B)-1:
            return max(A[-1],B[-1])
        i=len(A)//2
        j=k-i
        if A[i]>B[j]:
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)
        
        
253. Meeting Rooms II
---------------------

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

时间复杂度: O(N) 空间复杂度: O(N) 

想象一下，现实生活中，先开始的会议还没结束前我们就又要开始一个会议的话，此时我们需要一个新的会议室

如果前面一堆先开始的会议都先于我们的新会议开始之前结束了，我们不需要新会议室

换句话说，如果前面一堆新开始的会议中结束最早的那个会议如果在新开始的会议之前结束了的话，我们不需要会议室

所以我们的思路是，先按照会议开始的时间排序，然后维护一个会议结束时间的最小堆，堆顶就是前面结束最早的那个会议的结束时间

那么对于一个新的会议出现时：

如果堆顶元素比新会议的开始时间更小的话，我们不需要新会议室。同时因为后面出现的新会议的开始时间更大了， 所以目前最先结束的会议永远不可能比后面新出现的会议的开始时间更大，因此我们可以pop目前最先结束的会议，即pop堆顶元素，并且将新会议的结束时间放进堆中
如果堆顶元素比新会议的开始时间更大的话，我们知道我们需要一个新的会议室，此时直接将新会议的结束时间放进堆中
最终堆的size就是我们需要的会议室数量


.. code-block:: python

    from heapq import heappush, heappop
    class Solution(object):
        def minMeetingRooms(self, intervals):
            """
            :type intervals: List[Interval]
            :rtype: int
            """
            if not intervals:
                return 0

            intervals.sort(key = lambda x:x.start)
            end = []
            for it in intervals:
                # if the first finished meeting m1 ends before the next meeting
                # we can directly pop m1, because there is no need to add a new room
                if end and end[0] <= it.start: 
                    heappop(end)
                heappush(end, it.end)
                
            return len(end)

.. code-block:: python

    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x:x.start)
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i.start >= heap[0]: 
                # means two intervals can use the same room
                heapq.heapreplace(heap, i.end)
            else:
                # a new room is allocated
                heapq.heappush(heap, i.end)
        return len(heap)


163. Missing Ranges
-------------------

Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.


Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]


.. code-block:: python

    def findMissingRanges1(self, nums, lower, upper):
        nums.insert(0, lower-1)
        nums.append(upper+1)
        res = []
        for i in xrange(len(nums)-1):
            res.append(self.generateRange(nums[i], nums[i+1]))
        return [x for x in res if x]
        
    def generateRange(self, l, r):
        if l == r or l+1 == r:
            return ""
        if l+2 == r:
            return str(l+1)
        return str(l+1)+"->"+str(r-1)

    def findMissingRanges(self, nums, lower, upper):
        nums.insert(0, lower-1)
        nums.append(upper+1)
        res = []
        for i in xrange(len(nums)-1):
            if nums[i+1]-nums[i] == 2:
                res.append(str(nums[i]+1))
            elif nums[i+1]-nums[i] > 2:
                res.append(str(nums[i]+1)+"->"+str(nums[i+1]-1))
        return res  



254. Factor Combinations
------------------------

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]


.. code-block:: python

    def getFactors(self, n):
        res = []
        self.dfs(self.factors(n)[1:-1], n, 0, [], res)
        return res
     
    def dfs(self, nums, n, index, path, res):
        tmp = reduce(lambda x,y:x*y, path, 1)
        if tmp > n:
            return  # backtracking
        if tmp == n and path:
            res.append(path)
            return  # backtracking 
        for i in xrange(index, len(nums)):
            self.dfs(nums, n, i, path+[nums[i]], res)
            
    def factors(self, n):
        res = []
        for i in xrange(1, n+1):
            if n % i == 0:
                res.append(i)
        return res  

245. Shortest Word Distance III
-------------------------------

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.


.. code-block:: python

    def shortestWordDistance(self, words, word1, word2):
        p1 = p2 = -1
        res = len(words)
        # first case: the same as Shortest Word Distance
        if word1 != word2:
            for i, w in enumerate(words):
                if w == word1:
                    p1 = i
                if w == word2:
                    p2 = i
                if p1 > -1 and p2 > -1:
                    res = min(res, abs(p1-p2))
            return res
        else:
            # pre and i record previous and current word1 respectively
            pre, i = -len(words), 0
            while i < len(words):
                while i < len(words) and words[i] != word1:
                    i += 1
                if i < len(words):
                    res = min(res, i-pre)
                pre = i
                i += 1
            return res


147. Insertion Sort List
------------------------

Sort a linked list using insertion sort.

.. image:: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5



.. code-block:: python

    def insertionSortList(self, head):
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            while head and head.next and head.val <= head.next.val:
                head = head.next
            node = head.next
            if not node:
                break
            head.next = node.next  # delete "node"
            pre = dummy 
            while node.val > pre.next.val:
                pre = pre.next 
            node.next = pre.next  # insert "node" in the right position
            pre.next = node
        return dummy.next