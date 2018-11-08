



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
    


	
	