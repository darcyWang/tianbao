题号 74、73、64、63、62、59、56、55、54、48
=============================================

74. Search a 2D Matrix 
----------------------

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.

The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:

::
    [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]

Given target = 3, return true.



73. Set Matrix Zeroes 
---------------------

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.
Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


64. Minimum Path Sum 
--------------------

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



63. Unique Paths II
-------------------


Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.
::
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]

The total number of unique paths is 2.

Note: m and n will be at most 100.



.. code-block:: python

    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res
        
    def dfs(self, root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, ls+[root.val], res)
            
    def pathSum2(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val]+i for i in tmp]

    # BFS + queue    
    def pathSum3(self, root, sum): 
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res
        
    # DFS + stack I  
    def pathSum4(self, root, sum): 
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res 

    # DFS + stack II   
    def pathSum5(self, root, s): 
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res


    A shorter version of previous code:

    def pathSum1(self, root, sum):
        res = []
        self.dfs(root, sum, [], res)
        return res
        
    def dfs(self, root, sum, path, res):
        if root:
            if sum == root.val and not root.left and not root.right:
                res.append(path+[root.val])
            self.dfs(root.left, sum-root.val, path+[root.val], res)
            self.dfs(root.right, sum-root.val, path+[root.val], res)
            
    def pathSum2(self, root, sum):
        res, stack = [], [(root, sum, [])]
        while stack:
            node, sum, path = stack.pop()
            if node:
                if node.val == sum and not node.left and not node.right:
                    res.append(path+[node.val])
                stack.append((node.right, sum-node.val, path+[node.val]))
                stack.append((node.left, sum-node.val, path+[node.val]))
        return res
        
    def pathSum(self, root, sum):
        res, queue = [], collections.deque([(root, sum, [])])
        while queue:
            node, sum, path = queue.popleft()
            if node:
                if node.val == sum and not node.left and not node.right:
                    res.append(path+[node.val])
                    continue
                queue.append((node.left, sum-node.val, path+[node.val]))
                queue.append((node.right, sum-node.val, path+[node.val]))
        return res



62. Unique Paths
----------------

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

.. image:: robot_maze.png

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.



59. Spiral Matrix II 
--------------------


Given an integer n, generate a square matrix filled with elements from 1 to n的2次方 in spiral order.

For example,
Given n = 3,
You should return the following matrix:
::
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]


56. Merge Intervals 
-------------------

Given a collection of intervals, merge all overlapping intervals.

For example
::
    Given [1,3],[2,6],[8,10],[15,18],
    return [1,6],[8,10],[15,18]. 




55. Jump Game 
-------------

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:

::
    A = [2,3,1,1,4], return true.

    A = [3,2,1,0,4], return false. 





54. Spiral Matrix 
-----------------


Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:
::
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]

You should return [1,2,3,6,9,8,7,4,5]. 


48. Rotate Image 
----------------

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?



