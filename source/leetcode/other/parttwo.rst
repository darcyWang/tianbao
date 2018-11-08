



Strobogrammatic Number I, II, III
---------------------------------

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.


.. code-block:: python

    class Solution:
    # @param {string} low
    # @param {string} high
    # @return {integer}
    def strobogrammaticInRange(self, low, high):
        a=self.below(high)
        b=self.below(low,include=False)
        return a-b if a>b else 0

    '''
    get how many strobogrammatic numbers less than n
    '''
    def below(self,n,include=True):
        res=0
        for i in range(1,len(n)):
            res+=self.number(i)
        l=self.strobogrammatic(len(n))
        '''
        filter num larger than n and start with 0
        '''
        if include:
            l=[num for num in l if (len(num)==1 or num[0]!='0') and num<=n]
        else:
            l=[num for num in l if (len(num)==1 or num[0]!='0') and num<n]
        return res+len(l)

    '''
    get strobogrammatic numbers with length l
    number start with 0 would be included
    '''
    def strobogrammatic(self,l):
        res=[]
        if l==1:
            return ['0','1','8']
        if l==2:
            return ['00','11','69','96','88']
        for s in self.strobogrammatic(l-2):
            res.append('0'+s+'0')
            res.append('1'+s+'1')
            res.append('6'+s+'9')
            res.append('8'+s+'8')
            res.append('9'+s+'6')
        return res

    '''
    get number of strobogrammatic numbers of length l
    '''
    def number(self,l):
        if l==0:
            return 0
        '''
        If l is an even number, the first digit has four choices (1,6,8,9). digits 
        at other position have five choices(0,1,6,8,9)
        '''
        if l%2==0:
            return 4*(5**(l/2-1))
        '''
        If l is an odd number, the first digit has four choices (1,6,8,9) and digit 
        at the middle has 3 choices (0,1,8),other digits have 5 choices.
        digit at other position could be 0,1,6,8,9
        '''
        elif l==1:
            return 3
        else:
            return 3*(5**(l/2-1))*4 
        
        
    def strobogrammaticInRange(self, low, high):
        a, b = self.below(high), self.below(low, include=False) 
        return a -b if a > b else 0
        
    def below(self, n, include=True):
        res = 0
        for i in xrange(1, len(n)):
            res += self.number(i)
        l = self.strobogrammatic(len(n))
        if include:
            tmp = [num for num in l if num <= n]
        else:
            tmp = [num for num in l if num < n]
        return res + len(tmp)
        
    def strobogrammatic(self, n):
        return self.helper(n, n)
        
    def helper(self, m, n):
        if m == 0:
            return [""]
        if m == 1:
            return ["0", "1", "8"]
        l = self.helper(m-2, n)
        res = []
        for i in l:
            if m != n:
                res.append("0"+i+"0")
            res.append("1"+i+"1")
            res.append("6"+i+"9")
            res.append("8"+i+"8")
            res.append("9"+i+"6")
        return res

60. Permutation Sequence
------------------------

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
::
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

.. code-block:: python

    # TLE
    def getPermutation(self, n, k):
        nums = range(1, n+1)
        for i in xrange(k-1):
            self.nextPermutation(nums)
        return "".join(map(str, nums))
            
    def nextPermutation(self, nums):
        l = d = m = len(nums)-1
        while l > 0 and nums[l] <= nums[l-1]:
            l -= 1
        if l == 0:
            nums.reverse()
            return 
        k = l-1
        while nums[k] >= nums[d]:
            d -= 1
        nums[k], nums[d] = nums[d], nums[k]
        while l < m:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1; m -= 1

    # AC
    def getPermutation(self, n, k):
        res, nums = "",  range(1, n+1)
        k -= 1
        while n:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += str(nums.pop(index))
        return res


145. Binary Tree Postorder Traversal 二叉树的后序遍历
-----------------------------------------------------------


Given a binary tree, return the postorder traversal of its nodes' values.

Example:
::
    Input: [1,null,2,3]
       1
        \
         2
        /
       3

    Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?


给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

.. code-block:: python

    # recursively 
    def postorderTraversal1(self, root):
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            self.dfs(root.right, res)
            res.append(root.val)

    # iteratively        
    def postorderTraversal(self, root):
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]    
        
        
    def postorderTraversal(self, root):
        res = []
        self.dfs(root, res)
        return res[::-1]

    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.right, res)
            self.dfs(root.left, res)
        
        
        
    The first is by postorder using a flag to indicate whether the node has been visited or not.

    class Solution:
        # @param {TreeNode} root
        # @return {integer[]}
        def postorderTraversal(self, root):
            traversal, stack = [], [(root, False)]
            while stack:
                node, visited = stack.pop()
                if node:
                    if visited:
                        # add to result if visited
                        traversal.append(node.val)
                    else:
                        # post-order
                        stack.append((node, True))
                        stack.append((node.right, False))
                        stack.append((node.left, False))

            return traversal
    The 2nd uses modified preorder (right subtree first). Then reverse the result.

    class Solution:
        # @param {TreeNode} root
        # @return {integer[]}
        def postorderTraversal(self, root):
            traversal, stack = [], [root]
            while stack:
                node = stack.pop()
                if node:
                    # pre-order, right first
                    traversal.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)

            # reverse result
            return traversal[::-1]  
    

241. Different Ways to Add Parentheses
--------------------------------------

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:
::
    Input: "2-1-1"
    Output: [0, 2]
    Explanation: 
    ((2-1)-1) = 0 
    (2-(1-1)) = 2

Example 2:
::
    Input: "2*3-4*5"
    Output: [-34, -14, -10, -10, 10]
    Explanation: 
    (2*(3-(4*5))) = -34 
    ((2*3)-(4*5)) = -14 
    ((2*(3-4))*5) = -10 
    (2*((3-4)*5)) = -10 
    (((2*3)-4)*5) = 10


.. code-block:: python

    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i in xrange(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        return res
        
    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n



     def diffWaysToCompute(self, input):
        if input.isdigit():
            return [eval(input)]
        res = []
        for i, s in enumerate(input):
            if s in "+-*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                res.extend(self.compute(l, r, s))
        return res 
                
    def compute(self, l, r, op):
        return [eval(str(m)+op+str(n)) for m in l for n in r]



    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []        
        for i in xrange(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                res += [eval(str(k)+input[i]+str(j)) for k in res1 for j in res2]            
        return res


        
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i in xrange(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        return res
        
    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n  

.. code-block:: python

    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i in xrange(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        return res
        
    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n  
        
        
    An even shorter version:

     def diffWaysToCompute(self, input):
        if input.isdigit():
            return [eval(input)]
        res = []
        for i, s in enumerate(input):
            if s in "+-*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                res.extend(self.compute(l, r, s))
        return res 
                
    def compute(self, l, r, op):
        return [eval(str(m)+op+str(n)) for m in l for n in r]   
        
        
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []        
        for i in xrange(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                res += [eval(str(k)+input[i]+str(j)) for k in res1 for j in res2]            
        return res  



130. Surrounded Regions
-----------------------

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
::
    X X X X
    X O O X
    X X O X
    X O X X
    After running your function, the board should be:

    X X X X
    X X X X
    X X X X
    X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


.. code-block:: python

    # BFS
    def solve(self, board):
        queue = collections.deque([])
        for r in xrange(len(board)):
            for c in xrange(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                queue.append((r-1, c)); queue.append((r+1, c))
                queue.append((r, c-1)); queue.append((r, c+1))
            
        for r in xrange(len(board)):
            for c in xrange(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"


        
    # BFS
    def solve(self, board):
        if not board:
            return 
        r, c = len(board), len(board[0])
        for i in xrange(r):
            self.bfs(board, i, 0); self.bfs(board, i, c-1)
        for j in xrange(1, c-1):
            self.bfs(board, 0, j); self.bfs(board, r-1, j)
        # recover the board at second time
        for i in xrange(r):
            for j in xrange(c):
                if board[i][j] == "D":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        
    def bfs(self, board, i, j):
        queue = collections.deque()
        if board[i][j] == "O":
            queue.append((i, j)); board[i][j] = "D"
        while queue:
            r, c = queue.popleft()
            if r > 0 and board[r-1][c] == "O": # up
                queue.append((r-1, c)); board[r-1][c] = "D"
            if r < len(board)-1 and board[r+1][c] == "O": # down
                queue.append((r+1, c)); board[r+1][c] = "D"
            if c > 0 and board[r][c-1] == "O": # left
                queue.append((r, c-1)); board[r][c-1] = "D"
            if c < len(board[0])-1 and board[r][c+1] == "O": # right
                queue.append((r, c+1)); board[r][c+1] = "D"
        
        
    Here is a version which bfs function is embedded inside solve function:

    # BFS 
    def solve(self, board):
        if not board:
            return 
        row, col = len(board), len(board[0])
        queue = collections.deque()
        for i in xrange(row):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][col-1] == "O":
                queue.append((i, col-1))
        for j in xrange(1, col-1): 
            if board[0][j] == "O":
                queue.append((0, j))
            if board[row-1][j] == "O":
                queue.append((row-1, j))
        while queue:
            r, c = queue.popleft()
            board[r][c] = "D"
            if r > 0 and board[r-1][c] == "O": # up
                queue.append((r-1, c))
            if r < row-1 and board[r+1][c] == "O": # down
                queue.append((r+1, c))
            if c > 0 and board[r][c-1] == "O": # left
                queue.append((r, c-1))
            if c < col-1 and board[r][c+1] == "O": # right
                queue.append((r, c+1))
        # recover the board at second time
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j] == "D":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        
        

150. Evaluate Reverse Polish Notation
-------------------------------------

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

.. code-block:: python

    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in 
                    # Leetcode it should return 0
                    if l*r < 0 and l % r != 0:
                        stack.append(l/r+1)
                    else:
                        stack.append(l/r)
        return stack.pop()  
        
        
    class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack  = [] 
        for i in tokens:
            try:
                temp = int(i)
                stack.append(temp)
            except Exception, e:         
                b,a=stack[-1],stack[-2]
                stack.pop()
                stack.pop()
                if i == '+':    a = a+b
                elif i=='-':    a = a-b
                elif i=='*':    a = a*b
                elif i=='/':    a = int(a*1.0/b)
                stack.append(a)
               
        return stack[-1]    







	
	