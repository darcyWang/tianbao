题目序号   157、158、151、186、557、551、344、541、345、
============================================================


157. Read N Characters Given Read4 I
------------------------------------

#. The API: int read4(char *buf) reads 4 characters at a time from a file.
#. The return value is the actual number of characters read. 
#. For example, it returns 3 if there is only 3 characters left in the file.
#. By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.


Note:
The read function will only be called once for each test case.

.. note::

    首先让我们先把题目看清楚，题目问的是读取一个文件里面的内容，算出总共有多少个字符。

    #. 简单点来说就是给你一个字符串，有一个函数叫做read4，读n个char到指定的buf去。
    #. 那么就需要一个char*4的临时buf来储存一次读出来的结果，
    #. 然后再把这个结果按要求赋给指定的buf，
    #. 如果比4小的话，就说明字符串快要读完，数字就代表剩下的几个。
    #. 特么想不通为什么一开始搞一个(char *buf)，让有的人看了一脸懵逼好么。



It took me several hours to understand what the problem is talking about.

Let's look at the very first sentence of the description, "The API: int read4(char *buf) reads 4 characters at a time from a file." I though this function read a file, which is represented by *buf. But I was wrong. The correct understanding should be like this: this function reads a file, and writes the first 4 characters to *buf, and if there are less than 4 characters to be read, then only the valid number of characters will be read and written to *buf.

Similarly, the function to be implemented, int read(char buf, int n) that reads n characters from the file, means n characters should be written to *buf.

Also the examples are very misleading. Let's say example 1,
Input: buf = "abc", n = 4
Output: "abc"
Explanation: The actual number of characters read is 3, which is "abc".
The input *buf is not "abc". The file to be read is "abc". The input, *buf , should be where the characters are written to. The output, is not the return value of read(buf, 4), but should be the actual characters in *buf after the function is called. And the return value should be an int, which is 3.

Hope this clarification helps :) 



总结一下，就是read4(*read4_buf)这个函数的意思就是从文件当中读4个字符并将其写入到read4_buf中去，返回值是实际读取到的字符个数，即如果文件中只剩3个（不到4个字符了） ，那么就只写3个字符到read4_buf中去，返回值是3

所以我们要实现的read(*buf)函数也是这样，我们要读取n个字符并写入到buf中去并且返回实际读取到的字符个数，如果不够我们就有多少写多少，然后返回实际写入的个数

那么现在我们有两种情况：
::
    n大于文件中的字符数，我们检测文件结束并停止读取并返回文件中的字符数。
    n小于或等于文件中的字符数，当读取足够的字符时返回（即n）


代码中用eof代表'end of file'

.. code-block:: python

    class Solution(object):
        def read(self, buf, n):
            """
            :type buf: Destination buffer (List[str])
            :type n: Maximum number of characters to read (int)
            :rtype: The number of characters read (int)
            """
            if n == 0 :
                return 0
            total_read, eof = 0, False
            while not eof:
                read4_buf = [''] * 4
                cur_read = read4(read4_buf)
                if (cur_read < 4):
                    eof = True
                for i in range(cur_read):
                    buf[total_read] = read4_buf[i]
                    total_read += 1
                    if total_read == n:
                        return total_read
            return total_read



.. code-block:: python

    class Solution:
        def read(self, buf, n):
            idx = 0
            while True:
                buf4 = [""]*4
                curr = min(read4(buf4),n-idx)  # curr is the number of chars that reads
                for i in xrange(curr):
                    buf[idx] = buf4[i]
                    idx+=1
                if curr!=4 or idx==n:  # return if it reaches the end of file or reaches n
                    return idx  
        
        
        
    class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        idx = 0
        while True:
            buf4 = [""]*4
            l = read4(buf4)
            self.queue.extend(buf4)
            curr = min(len(self.queue), n-idx)
            for i in xrange(curr):
                buf[idx] = self.queue.pop(0)
                idx+=1
            if curr == 0:
                break 
        return idx  
        
        
        

158. Read N Characters Given Read4 II - Call multiple times
-----------------------------------------------------------

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.


.. important::

        这道题目跟上面一样没有搞明白


我来总结一下，跟第157题不一样的地方就是，157是就读一次，158是可以读好几次 例如： 文件是‘abcdefg’

    #. 157题就读一次，给一个n就行了。n给1那buf就是‘a’, n给2那buf就是‘ab’
    #. 但是158不一样，可以多次read，比如第一次n给1，那buf是‘a’，再read一次，n给2，那'a'已经读过了，所以现在buf是'bc'了， 如果再来个n=3的话，buf就是‘def’,


总之就是一个test case 中read函数可以调用一次和调用多次的区别

.. code-block:: python

    class Solution(object):
        head, tail, buffer = 0, 0, [''] * 4 ## 定义全局变量
        
        def read(self, buf, n):
            """
            :type buf: Destination buffer (List[str])
            :type n: Maximum number of characters to read (int)
            :rtype: The number of characters read (int)
            """
            i = 0
            while i < n:
                if self.head == self.tail: ## read4 的缓存区为空的时候
                    self.head = 0
                    self.tail = read4(self.buffer) ## 开始进缓存区
                    if self.tail == 0:
                        break
                while i < n and self.head < self.tail:
                    buf[i] = self.buffer[self.head] ## 读出缓存区的变量
                    i += 1
                    self.head += 1
            return i

151. Reverse Words in a String
------------------------------



Given an input string, reverse the string word by word.

For example
::
    Given s = "the sky is blue",
    return "blue is sky the".


..code-block:: python

    # in-place
    def reverseWords(self, s):
        # reverse the whole list
        self.reverse(s, 0, len(s)-1)
        r = 0
        while r < len(s):
            l = r 
            while r < len(s) and s[r] != " ":
                r += 1
            # reverse each sublist
            self.reverse(s, l, r-1)
            r += 1
        
    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l +=1 ; r -= 1  
        
        

.. code-block:: python

    def reverseWords(s):
        return ' '.join(reversed(s.split()))

    class Solution(object):
        def reverseWords(self, s):
            """
            :type s: str
            :rtype: str
            """
            tmp = s.split()
            res = " ".join(tmp[::-1])
            return res

    def reverseWords2(s):
        print " ".join(s.split()[::-1])


    class Solution(object):
        def reverseWords(self, s):
            """
            :type s: str
            :rtype: str
            """
            tmp = s.split()
            tmp.reverse()
            res = " ".join(tmp)
            return res


.. code-block:: javascript

        var hello = 'the sky is blue'.split(' ').reverse().join(' ');
        console.log(hello)


186. Reverse Words in a String II
---------------------------------


Given an input string, reverse the string word by word.
A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces
and the words are always separated by a single space.

For example,
::
    Given s = "the sky is blue",
    return "blue is sky the".

Could you do it in-place without allocating extra space?



.. code-block:: python

    class Solution:
        # @param s, a string
        # @return a string
        def reverseWords(self, s):
            # Step 1 : split the given string into a list of words - with " " as the seperator
            s = s.split(" ")
            # Step 2 : filter out the white spaces in the list and reverse the list
            s = [element for element in s if element != ''][::-1]
            # Step 3 : join them and return 
            return ' '.join(s)          
                
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])            
        

.. code-block:: python

    def reverseWords(self, s):
        s = list(" ".join(s.split()))[::-1]
        i = 0 
        while i < len(s):
            start = i 
            while i < len(s) and not s[i].isspace():
                i += 1
            self.reverse(s, start, i-1)
            i += 1
        return "".join(s)

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1; j -= 1

Hints:


下面的解决办法是分两步走，第一步是把所有的字符串字母
Two-pass:
#. 1. reverse all strings:
"the sky is blue" -> "eulb si yks eht"

#. 2. reverse one word:
"eulb si yks eht" -> "blue is sky the"

.. code-block:: python

    class Solution(object):
        def reverseString(self, s):
            """
            :type s: str
            :rtype: str
            """
            return s[::-1]

    class Solution(object):
        def reverseString(self, s):
            """
            :type s: str
            :rtype: str
            """
            lst = list(s)
            n = len(lst)
            start, end = 0, n - 1

            while start < end:
                lst[end], lst[start]  = lst[start],lst[end]
                start += 1
                end -= 1
            return ''.join(lst)


.. code-block:: javascript

    let hello = "Let's take LeetCode contest".split(' ').map(s => s.split().reverse().join()).join(' ')
    console.log(hello)



557. Reverse Words in a String III
----------------------------------

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
::
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.

这个问题跟上面的差不多  答案应该是一样的， 可以参考一下

JavaScript答案

.. code-block:: javascript

    let hello = "Let's take LeetCode contest".split(' ').map(s => s.split().reverse().join()).join(' ')
    console.log(hello)





551. Student Attendance Record I
--------------------------------

You are given a string representing an attendance record for a student. The record only contains the following three characters:

Explaination:
::
    'A' : Absent.
    'L' : Late.
    'P' : Present.

A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
::
    Input: "PPALLP"
    Output: True

Example 2:
::
    Input: "PPALLL"
    Output: False

简单一点就是给一个字符串，判断里面是否包含两个A或者连续的LLL，返回true or false

.. code-block:: Javascript

    var checkRecord = function(s) {
        if(s.includes("LLL") || s.indexOf("A") != s.lastIndexOf("A")) return false;
        else return true;
    };
    var checkRecord = function(s) {
        return !(s.indexOf('A') >= 0 && s.indexOf('A', s.indexOf('A') + 1) >= 0 || s.indexOf('LLL') >= 0);
    };
    // 备注一下还是尼玛正则很强大啊
    var checkRecord = function(s) {
        // check if there are more than 2 As and 3 continuous Ls
        return !/^.*(A.*A|L{3,}).*$/.test(s);
    };

.. code-block:: python

    class Solution(object):
        def checkRecord(self, s):
            """
            :type s: str
            :rtype: bool
            """
            return s.count('A') <=1 and 'LLL' not in s

            return (s.count('A')<=1) and ('LLL' not in s )


    class Solution:
        def checkRecord(self, s):
            return False if 'LLL' in s or s.count('A') > 1 else True

551. Student Attendance Record II
---------------------------------

Hard模式 看看题目就行了哈

Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

Explaination:
::
    'A' : Absent.
    'L' : Late.
    'P' : Present.

A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
::
    Input: n = 2
    Output: 8 
    Explanation:
    There are 8 records with length 2 will be regarded as rewardable:
    "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"


Only "AA" won't be regarded as rewardable owing to more than one absent times. 
Note: The value of n won't exceed 100,000.


344. Reverse String
-------------------

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".


.. code-block:: javascript
    
    let s = 'hello'
    console.log(s.split('').reverse().join(''))


541. Reverse String II
----------------------


#. Given a string and an integer k, 
#. you need to reverse the first k characters for every 2k characters counting from the start of the string. 
#. If there are less than k characters left, reverse all of them. 
#. If there are less than 2k but greater than or equal to k characters, 
#. then reverse the first k characters and left the other as original.
   
Example:
::
    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"

Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]


.. code-block:: Javascript 
    
    let reverseStr = function(s, k) {
      if(s.length < k)
        return s.split("").reverse().join("");
      let res = "";
      for(let i = 0; i < s.length; i+=2*k) {
        res += s.split("").slice(i, i+k).reverse().join("");
        res += s.slice(i+k, i+2*k);
      }
      return res;
    };


.. code-block:: python
    
    class Solution(object):
        def reverseStr(self, s, k):
            """
            :type s: str
            :type k: int
            :rtype: str
            """
            length = len(s)
            for i in range(0, length, 2 * k):
                if i + k >= length:
                    s = s[:i] + s[i:][::-1]
                else:
                    s = s[:i] + s[i:i + k][::-1] + s[i + k:]
            return s

345. Reverse Vowels of a String
-------------------------------


Write a function that takes a string as input and reverse only the vowels of a string.


Example
::
    Given s = "hello", return "holle".

    Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

替换字符串里面的元音字母'aeiou'
字符串不可变，所以用list代替，最后join



.. code-block:: javascript
    
    var reverseVowels = function(s) {
        if(s === null || s.length === 0) {
            return s;
        }
        var chars = s.split('');
        var low = 0;
        var high = s.length - 1;
        var vowels = "aeiouAEIOU";
        var tmp;
        while(low < high) {
            while(low < high && vowels.indexOf(chars[low]) === -1) {
                low++;
            }
            
            while(low < high && vowels.indexOf(chars[high]) === -1) {
                high--;
            }
            
            tmp = chars[high];
            chars[high] = chars[low];
            chars[low] = tmp;
            low++;
            high--;
        }
        
        return chars.join('');
    };

.. code-block:: python

    class Solution(object):
        def reverseVowels(self, s):
            """
            :type s: str
            :rtype: str
            """
            vowels = 'aeiou'
            string = list(s)
            i, j = 0, len(s) -1
            while i <= j:
                if string[i].lower() not in vowels:
                    i += 1
                elif string[j].lower() not in vowels:
                    j -= 1
                else:
                    string[i], string[j] = string[j], string[i]
                    i += 1
                    j -= 1
            return ''.join(string)

    class Solution(object):
        def reverseVowels(self, s):
            """
            :type s: str
            :rtype: str
            """
            vowel = 'AEIOUaeiou'
            s = list(s)
            i,j = 0, len(s)-1
            while i<j:
                while s[i] not in vowel and i<j:
                    i = i + 1
                while s[j] not in vowel and i<j:
                    j = j - 1
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1
            return ''.join(s)
    
    """ 正则版本 """
    class Solution(object):
        def reverseVowels(self, s):
            """
            :type s: str
            :rtype: str
            """
            vowels = re.findall('(?i)[aeiou]', s)
            return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)











