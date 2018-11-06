https://leetcode.com/problems/binary-tree-postorder-traversal/description/
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
	
	