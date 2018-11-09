题目序号 366、298、285、255、250、156、236、199
============================================================




366. Find Leaves of Binary Tree
-------------------------------

Given a binary tree, find all leaves and then remove those leaves. Then repeat the previous steps until the tree is empty.

Example:
Given binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Returns [4, 5, 3], [2], [1].

Explanation:
1. Remove the leaves [4, 5, 3] from the tree

          1
         / 
        2          
2. Remove the leaf [2] from the tree

          1          
3. Remove the leaf [1] from the tree

          []         
Returns [4, 5, 3], [2], [1].

 

Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.

 

这道题给了我们一个二叉树，让我们返回其每层的叶节点，就像剥洋葱一样，将这个二叉树一层一层剥掉，最后一个剥掉根节点。那么题目中提示说要用DFS来做，思路是这样的，每一个节点从左子节点和右子节点分开走可以得到两个深度，由于成为叶节点的条件是左右子节点都为空，所以我们取左右子节点中较大值加1为当前节点的深度值，知道了深度值就可以将节点值加入到结果res中的正确位置了，求深度的方法我们可以参见Maximum Depth of Binary Tree中求最大深度的方法，参见代码如下：



298. Binary Tree Longest Consecutive Sequence
---------------------------------------------

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example
::
       1
        \
         3
        / \
       2   4
            \
             5
    Longest consecutive sequence path is 3-4-5, so return 3.

       2
        \
         3
        /
       2    
      /
     1
    Longest consecutive sequence path is 2-3',not3-2-1', so return `2'.




285. Inorder Successor in BST
-----------------------------

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

 

这道题让我们求二叉搜索树的某个节点的中序后继节点，那么我们根据BST的性质知道其中序遍历的结果是有序的， 是我最先用的方法是用迭代的中序遍历方法，然后用一个bool型的变量b，初始化为false，我们进行中序遍历，对于遍历到的节点，我们首先看如果此时b已经为true，说明之前遍历到了p，那么此时我们返回当前节点，如果b仍为false，我们看遍历到的节点和p是否相同，如果相同，我们此时将b赋为true，那么下一个遍历到的节点就能返回了，参见代码如下：




255. Verify Preorder Sequence in Binary Search Tree
---------------------------------------------------


Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
You may assume each number in the sequence is unique.

Follow up:
#. Could you do it using only constant space complexity?
Brute-force solution:
The idea to solve the problem is: a[0] must be the root of the BST. Then we start from index 1 and iterate until a number which is greater than root, mark as i. All the numbers less than i must be less than root, number greater than i must be greater than root. Then we can recursively validate the BST.


#. 先复习一下BST，给定一个节点，其左子树的所有节点都小于该节点，右子树的所有节点都大于该节点；preorder序列是指在遍历该BST的时候，先记录根节点，再遍历左子树，然后遍历右子树；所以一个preorder序列有这样一个特点，左子树的序列必定都在右子树的序列之前；并且左子树的序列必定都小于根节点，右子树的序列都大于根节点；
#. 根据上面的特点很容易通过递归的方式完成：
#. 如果序列只有一个元素，那么肯定是正确的，对应只有一个节点的树；
#. 如果多于一个元素，以当前节点为根节点；并从当前节点向后遍历，直到大于根节点的节点出现（或者到尾巴），那么根节点之后，该大节点之前的，是左子树；该大节点及之后的组成右子树；递归判断左右子树即可；
那么什么时候一个序列肯定不是一个preorder序列呢？前面得到的右子树，如果在其中出现了比根节点还小的数，那么就可以直接返回false了；



250. Count Univalue Subtrees
----------------------------


Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
::
    Given binary tree,

                  5
                 / \
                1   5
               / \   \
              5   5   5
     

    return 4.

 

这道题让我们求相同值子树的个数，就是所有节点值都相同的子树的个数，之前有道求最大BST子树的题Largest BST Subtree，感觉挺像的，都是关于子树的问题，解题思路也可以参考一下，我们可以用递归来做，第一种解法的思路是先序遍历树的所有的节点，然后对每一个节点调用判断以当前节点为根的字数的所有节点是否相同，判断方法可以参考之前那题Same Tree，用的是分治法的思想，分别对左右字数分别调用递归，参见代码如下：

.. code-block:: python

    def countUnivalSubtrees(self, root):
        self.count = 0
        self.checkUni(root)
        return self.count

    # bottom-up, first check the leaf nodes and count them, 
    # then go up, if both children are "True" and root.val is 
    # equal to both children's values if exist, then root node
    # is uniValue suntree node. 
    def checkUni(self, root):
        if not root:
            return True
        l, r = self.checkUni(root.left), self.checkUni(root.right)
        if l and r and (not root.left or root.left.val == root.val) and \
        (not root.right or root.right.val == root.val):
            self.count += 1
            return True
        return False


156. Binary Tree Upside Down
----------------------------

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
For example:
::
    Given a binary tree {1,2,3,4,5},
        1
       / \
      2   3
     / \
    4   5
    return the root of the binary tree [4,5,2,#,#,3,1].
       4
      / \
     5   2
        / \
       3   1  


.. code-block:: python

    # suppose the root.left part has been upsideDowned,
    # then connect the root node (not root) to the right 
    # side of the right-most node of the already upsideDowned
    # root.left part, root.right to the left side
    def upsideDownBinaryTree(self, root):
        if not root or (not root.left and not root.right):
            return root
        node = self.upsideDownBinaryTree(root.left)
        tmp = node
        while tmp.right:
            tmp = tmp.right
        tmp.right = TreeNode(root.val)
        tmp.left = root.right
        return node 
        
        
    # Iteratively 
    def upsideDownBinaryTree(self, root):
        if not root:
            return root
        l, r = root.left, root.right
        root.left, root.right = None, None
        while l:
            newL, newR = l.left, l.right
            l.left, l.right = r, root
            root, l, r = l, newL, newR
        return root 


236. Lowest Common Ancestor of a Binary Tree
--------------------------------------------



Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
::
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.




199. Binary Tree Right Side View
--------------------------------

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
::
    Given the following binary tree,

       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---

    You should return [1, 3, 4].

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.


.. code-block:: python

    # DFS recursively
    def rightSideView(self, root):
        res = []
        self.dfs(root, 0, res)
        return [x[0] for x in res]
        
    def dfs(self, root, level, res):
        if root:
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            self.dfs(root.right, level+1, res)
            self.dfs(root.left, level+1, res)

    # DFS + stack
    def rightSideView2(self, root):
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if curr:
                if len(res) < level+1:
                    res.append([])
                res[level].append(curr.val)
                stack.append((curr.right, level+1))
                stack.append((curr.left, level+1))
        return [x[-1] for x in res]
            
    # BFS + queue
    def rightSideView(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level+1:
                    res.append([])
                res[level].append(curr.val)
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return [x[-1] for x in res]


    The solution above is level order traversal indeed, here is the revised version. The return value only includes the elements we need:

    # DFS recursively
    def rightSideView1(self, root):
        res = []
        self.dfs(root, 0, res)
        return res
        
    def dfs(self, root, level, res):
        if root:
            if len(res) == level:
                res.append(root.val)
            self.dfs(root.right, level+1, res)
            self.dfs(root.left, level+1, res)

    # DFS + stack
    def rightSideView2(self, root):
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if curr:
                if len(res) == level:
                    res.append(curr.val)
                stack.append((curr.left, level+1))
                stack.append((curr.right, level+1))
        return res
            
    # BFS + queue
    def rightSideView3(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) == level:
                    res.append(curr.val)
                queue.append((curr.right, level+1))
                queue.append((curr.left, level+1))
        return res
        













