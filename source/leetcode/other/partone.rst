题目序号 71、93、208、211、
============================================================



71. Simplify Path
-----------------

Given an absolute path for a file (Unix-style), simplify it. 

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".


非常简单的模拟题，利用一个栈来储存当前的路径。用 "/" 将输入的全路径分割成多个部分，对于每一个部分循环处理：如果为空或者 "." 则忽略，如果是 ".." ，则出栈顶部元素（如果栈为空则忽略），其他情况直接压入栈即可。


.. code-block:: python
    
    class Solution(object):
        def simplifyPath(self, path):
            """
            :type path: str
            :rtype: str
            """
            stack = []
            for part in path.split("/"):
                if part and part != ".": # 如果为空或者 "." 则忽略
                    if part == "..":
                        if stack:
                            stack.pop()
                    else:
                        stack.append(part)
            if not stack:
                return "/"
            else:
                return "/" + "/".join(stack)


.. code-block:: python

    # with stack
    def simplifyPath1(self, path):
        stack = []
        for item in path.split("/"):
            if item not in [".", "..", ""]:
                stack.append(item)
            if item == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)
        
    # with deque
    def simplifyPath(self, path):
        deque = collections.deque()
        for item in path.split("/"):
            if item not in [".", "..", ""]:
                deque.append(item)
            if item == ".." and deque:
                deque.pop()
        return "/" + "/".join(deque)            
                
        
93. Restore IP Addresses
------------------------


Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:
:: 
    Input: "25525511135"
    Output: ["255.255.11.135", "255.255.111.35"]


.. code-block:: python

    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 4, 0, [], res)
        return res
        
    def dfs(self, s, level, index, path, res):
        if level == 0:
            l = sum(map(len, path))
            if l < len(s):
                return  # backtracking 
            else:
                res.append(".".join(path))
                return 
        for i in xrange(1, 4):
            if index+i <= len(s) and self.valid(s[index:index+i]):
                self.dfs(s, level-1, index+i, path+[s[index:index+i]], res)

    def valid(self, s):
        if len(s) == 2 and s[0] == "0":
            return False
        if len(s) == 3 and (s[0] == "0" or s > "255"):
            return False
        return True


208. Implement Trie (Prefix Tree)
---------------------------------

Implement a trie with insert, search, and startsWith methods.

Example:
::
    Trie trie = new Trie();

    trie.insert("apple");
    trie.search("apple");   // returns true
    trie.search("app");     // returns false
    trie.startsWith("app"); // returns true
    trie.insert("app");   
    trie.search("app");     // returns true

Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.


.. code-block:: python

    class TrieNode(object):
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.childs = dict()
            self.isWord = False
            
            

    class Trie(object):

        def __init__(self):
            self.root = TrieNode()

        def insert(self, word):
            """
            Inserts a word into the trie.
            :type word: str
            :rtype: void
            """
            node = self.root
            for letter in word:
                child = node.childs.get(letter)
                if child is None:
                    child = TrieNode()
                    node.childs[letter] = child
                node = child
            node.isWord = True

        def search(self, word):
            """
            Returns if the word is in the trie.
            :type word: str
            :rtype: bool
            """
            node = self.root
            for i in word:
                child = node.childs.get(i)
                if child is None:
                    return False
                node = child
            return node.isWord
            

        def startsWith(self, prefix):
            """
            Returns if there is any word in the trie
            that starts with the given prefix.
            :type prefix: str
            :rtype: bool
            """
            node = self.root
            for letter in prefix:
                child = node.childs.get(letter)
                if child is None:
                    return False
                node = child
            return True
            

    # Your Trie object will be instantiated and called as such:
    # trie = Trie()
    # trie.insert("somestring")
    # trie.search("key")


.. code-block:: python

    class TrieNode():
        def __init__(self):
            self.children = collections.defaultdict(TrieNode)
            self.isWord = False
        
    class Trie():
        def __init__(self):
            self.root = TrieNode()
        
        def insert(self, word):
            node = self.root
            for w in word:
                node = node.children[w]
            node.isWord = True
        
        def search(self, word):
            node = self.root
            for w in word:
                node = node.children.get(w)
                if not node:
                    return False
            return node.isWord

211. Add and Search Word - Data structure design
------------------------------------------------


Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:
::
    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.


.. code-block:: python

    class TrieNode():
        def __init__(self):
            self.children = collections.defaultdict(TrieNode)
            self.isWord = False
        
    class WordDictionary(object):
        def __init__(self):
            self.root = TrieNode()

        def addWord(self, word):
            node = self.root
            for w in word:
                node = node.children[w]
            node.isWord = True

        def search(self, word):
            node = self.root
            self.res = False
            self.dfs(node, word)
            return self.res
        
        def dfs(self, node, word):
            if not word:
                if node.isWord:
                    self.res = True
                return 
            if word[0] == ".":
                for n in node.children.values():
                    self.dfs(n, word[1:])
            else:
                node = node.children.get(word[0])
                if not node:
                    return 
                self.dfs(node, word[1:])
