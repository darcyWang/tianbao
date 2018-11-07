题目序号 210、207、200、133、117、116、114、106、105
============================================================================



207. Course Schedule
--------------------


There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]

There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
::
    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.

pre-requisite问题，只需要判断最终的topological结果长度与courses数目是否相等即可

DFS 和 BFS都可以用来拓扑排序。

.. code-block:: python

    class Solution(object):
        def canFinish(self, numCourses, prerequisites):
            """
            :type numCourses: int
            :type prerequisites: List[List[int]]
            :rtype: bool
            """
            graph = collections.defaultdict(list)
            indegrees = [0] * numCourses
            
            for course, pre in prerequisites:
                graph[pre].append(course)
                indegrees[course] += 1
                
            return self.topologicalSort(graph, indegrees) == numCourses
        
        
        def topologicalSort(self, graph, indegrees):
            count = 0
            queue = []
            for i in range(len(indegrees)):
                if indegrees[i] == 0:
                    queue.append(i)
            while queue:
                course = queue.pop()
                count += 1
                for i in graph[course]:
                    indegrees[i] -= 1
                    if indegrees[i] == 0:
                        queue.append(i)
            return count

.. code-block:: python

    # BFS: from the end to the front
    def canFinish1(self, numCourses, prerequisites):
        forward = {i: set() for i in xrange(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        queue = collections.deque([node for node in forward if len(forward[node]) == 0])
        while queue:
            node = queue.popleft()
            for neigh in backward[node]:
                forward[neigh].remove(node)
                if len(forward[neigh]) == 0:
                    queue.append(neigh)
            forward.pop(node)
        return not forward  # if there is cycle, forward won't be None

    # BFS: from the front to the end    
    def canFinish2(self, numCourses, prerequisites):
        forward = {i: set() for i in xrange(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        queue = collections.deque([node for node in xrange(numCourses) if not backward[node]])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neigh in forward[node]:
                backward[neigh].remove(node)
                if not backward[neigh]:
                    queue.append(neigh)
        return count == numCourses
        
    # DFS: from the end to the front
    def canFinish3(self, numCourses, prerequisites):
        forward = {i: set() for i in xrange(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        stack = [node for node in forward if len(forward[node]) == 0]
        while stack:
            node = stack.pop()
            for neigh in backward[node]:
                forward[neigh].remove(node)
                if len(forward[neigh]) == 0:
                    stack.append(neigh)
            forward.pop(node)
        return not forward
            
    # DFS: from the front to the end    
    def canFinish(self, numCourses, prerequisites):
        forward = {i: set() for i in xrange(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        stack = [node for node in xrange(numCourses) if not backward[node]]
        while stack:
            node = stack.pop()
            for neigh in forward[node]:
                backward[neigh].remove(node)
                if not backward[neigh]:
                    stack.append(neigh)
            backward.pop(node)
        return not backward




210. Course Schedule II
-----------------------


There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]

There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.

click to show more hints.
Hints:

    This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
    Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
    Topological sort could also be done via BFS.


course schedule II 在I的基础上改了3行代码过了

论代码可重用性的重要程度,beats 97.77%


.. code-block:: python

    class Solution(object):
        def findOrder(self, numCourses, prerequisites):
            """
            :type numCourses: int
            :type prerequisites: List[List[int]]
            :rtype: List[int]
            """
            graph = collections.defaultdict(list)
            indegrees = [0] * numCourses
            
            for course, pre in prerequisites:
                graph[pre].append(course)
                indegrees[course] += 1
            
            count, stack = self.topologicalSort(graph, indegrees)
            return stack if count == numCourses else []
        
        
        def topologicalSort(self, graph, indegrees):
            count = 0
            queue = []
            stack = []
            for i in range(len(indegrees)):
                if indegrees[i] == 0:
                    queue.append(i)
            while queue:
                course = queue.pop()
                stack.append(course)
                count += 1
                for i in graph[course]:
                    indegrees[i] -= 1
                    if indegrees[i] == 0:
                        queue.append(i)
            return (count, stack)



.. code-block:: python

    
    # BFS
    def findOrder1(self, numCourses, prerequisites):
        dic = {i: set() for i in xrange(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []
        
    # DFS
    def findOrder(self, numCourses, prerequisites):
        dic = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in xrange(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []



200. Number of Islands
----------------------

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3



133. Clone Graph
----------------

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

OJ's undirected graph serialization:

Nodes are labeled uniquely.
We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

    *. First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
    *. Second node is labeled as 1. Connect node 1 to node 2.
    *. Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

Visually, the graph looks like the following:
::
       1
      / \
     /   \
    0 --- 2
         / \
         \_/


.. code-block:: python

    # BFS
    def cloneGraph1(self, node):
        if not node:
            return 
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic: # neighbor is not visited
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy
        
    # DFS iteratively
    def cloneGraph2(self, node):
        if not node:
            return 
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy
        
    # DFS recursively
    def cloneGraph(self, node):
        if not node:
            return 
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy
        
    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])


117. Populating Next Right Pointers in Each Node II
---------------------------------------------------

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

    You may only use constant extra space.

For example,
Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL



116. Populating Next Right Pointers in Each Node
------------------------------------------------

 Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

    You may only use constant extra space.
    You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL




114. Flatten Binary Tree to Linked List
---------------------------------------



 Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

click to show hints.
Hints:

If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.











106. Construct Binary Tree from Inorder and Postorder Traversal
---------------------------------------------------------------


Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree. 




105. Construct Binary Tree from Preorder and Inorder Traversal
--------------------------------------------------------------


Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree. 






