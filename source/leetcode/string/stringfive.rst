题目序号   227、8、635、165、161、544、609、539、537、72
============================================================



227. Basic Calculator II
------------------------

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
::
    "3+2*2" = 7
    " 3/2 " = 1
    " 3+5 / 2 " = 5
    Note: Do not use the eval built-in library function.

题目重述：
#. 实现一个简易计算器，计算简单表达式字符串的值。
#. 表达式字符串只包含非负整数， +， -， *， / 运算和空白字符。整数除法的得数应当舍去小数部分。
#. 你可以假设给定的表达式总是有效的。
#. 测试样例见题目描述。

注意：不要使用内置的库函数eval。


http://www.cnblogs.com/grandyang/p/4601208.html

http://wdxtub.com/interview/14520606685216.html


https://siddontang.gitbooks.io/leetcode-solution/content/string/basic_calculator_2.html

https://segmentfault.com/a/1190000003796804

http://www.tangjikai.com/algorithms/leetcode-224-basic-calculator

http://eugeneyang.com/2016/04/21/Basic%20Calculator%20II%20-%20%E5%9F%BA%E6%9C%AC%E8%AE%A1%E7%AE%97%E5%99%A8II/


8. String to Integer (atoi)
---------------------------

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.



字符串转为整数是很常用的一个函数，由于输入的是字符串，所以需要考虑的情况有很多种。我之前有一篇文章是关于验证一个字符串是否为数字的，参见 http://www.cnblogs.com/grandyang/p/4084408.html 。在那篇文章中，详细的讨论了各种情况，包括符号，自然数，小数点的出现位置，判断他们是否是数字。个人以为这道题也应该有这么多种情况。但是这题只需要考虑数字和符号的情况：

1. 若字符串开头是空格，则跳过所有空格，到第一个非空格字符，如果没有，则返回0.

2. 若第一个非空格字符是符号+/-，则标记sign的真假，这道题还有个局限性，那就是在c++里面，+-1和-+1都是认可的，都是-1，而在此题里，则会返回0.

3. 若下一个字符不是数字，则返回0. 完全不考虑小数点和自然数的情况，不过这样也好，起码省事了不少。

4. 如果下一个字符是数字，则转为整形存下来，若接下来再有非数字出现，则返回目前的结果。

5. 还需要考虑边界问题，如果超过了整形数的范围，则用边界值替代当前值。
   


我估计没有多少人不看下面的要求就通过的吧！

这道题要求的 atoi 跟C++实现的不一样吧，比如我以为不符合要求的返回-1，而这道题要求返回0。

所以，有必要解释一下题目的要求：

1. 首先需要丢弃字符串前面的空格；

2. 然后可能有正负号（注意只取一个，如果有多个正负号，那么说这个字符串是无法转换的，返回0。比如测试用例里就有个“+-2”）；

3. 字符串可以包含0~9以外的字符，如果遇到非数字字符，那么只取该字符之前的部分，如“-00123a66”返回为“-123”；

4. 如果超出int的范围，返回边界值（2147483647或-2147483648）。

综上，要求还是有点怪的，不看要求是很难写对的，看了也不一定理解的对。






635. Design Log Storage System
------------------------------


You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.

int[] Retrieve(String start, String end, String granularity): Return the id of logs whose timestamps are within the range from start to end. Start and end all have the same format as timestamp. However, granularity means the time level for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

Example 1:

put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
Note:

There will be at most 300 operations of Put or Retrieve.
Year ranges from [2000,2017]. Hour ranges from [00,23].
Output for Retrieve has no order required.



日志系统中：

时间戳应该存储为某一起始时间点（例如1970年1月1日0时0分0秒）以来的秒数。这样字符型的时间戳被转化为整型，便于存储和查询。
时间戳连同日志记录的id，以及其他信息作为一个节点存储在特定数据结构中（链表或者搜索树）。


设计一个日志系统，该系统有两个操作，put(id,timestamp)把timestamp时刻的日志id放到日志系统中，retrieve(start,end,gra)从系统中取出timestamp范围在[start,end]之间的日志id，时间的粒度是gra。

我设计的系统是这样的，为了方便retrieve，系统中的日志都按timestamp排序了。有趣的是，在zero-padded（每部分不足补前导0）的情况下，timestamp的字符串排序就是timestamp表示的时间的排序。

定义一个Node结构体，保持一个日志，信息包括日志id和timestamp。用一个链表存储所有Node，并且当新Node插入时，采用插入排序的方法使得链表始终有序。

retrieve的时候，根据粒度，重新设置start和end，比如样例中粒度为Year时，把start改为Year固定，其他时间最小

"2016:00:00:00:00:00"
把end改为Year固定，其他时间最大

"2017:12:31:23:59:59"
这样我只需要遍历链表，把所有timestamp字符串在这个范围内的日志id取出来就好了。其他粒度也是类似的。


165. Compare Version Numbers
----------------------------


Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
Credits:
Special thanks to @ts for adding this problem and creating all test cases.





https://segmentfault.com/a/1190000003803133

https://skyyen999.gitbooks.io/-leetcode-with-javascript/content/questions/165md.html




161. One Edit Distance
----------------------




Given two strings S and T, determine if they are both one edit distance apart.




https://nb4799.neu.edu/wordpress/?p=2217

https://tonycao.gitbooks.io/leetcode-locked/content/LeetCode%20Locked/c1.9.html





544. Output Contest Matches
---------------------------


During the NBA playoffs, we always arrange the rather strong team to play with the rather weak team, like make the rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting. Now, you're given n teams, you need to output their final contest matches in the form of a string.

The n teams are given in the form of positive integers from 1 to n, which represents their initial rank. (Rank 1 is the strongest team and Rank n is the weakest team.) We'll use parentheses('(', ')') and commas(',') to represent the contest team pairing - parentheses('(' , ')') for pairing and commas(',') for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.

Example 1:

Input: 2
Output: (1,2)
Explanation: 
Initially, we have the team 1 and the team 2, placed like: 1,2.
Then we pair the team (1,2) together with '(', ')' and ',', which is the final answer.
 

Example 2:

Input: 4
Output: ((1,4),(2,3))
Explanation: 
In the first round, we pair the team 1 and 4, the team 2 and 3 together, as we need to make the strong team and weak team together.
And we got (1,4),(2,3).
In the second round, the winners of (1,4) and (2,3) need to play again to generate the final winner, so you need to add the paratheses outside them.
And we got the final answer ((1,4),(2,3)).
 

Example 3:

Input: 8
Output: (((1,8),(4,5)),((2,7),(3,6)))
Explanation: 
First round: (1,8),(2,7),(3,6),(4,5)
Second round: ((1,8),(4,5)),((2,7),(3,6))
Third round: (((1,8),(4,5)),((2,7),(3,6)))
Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).
 

Note:

The n is in range [2, 212].
We ensure that the input n can be converted into the form 2k, where k is a positive integer.


这道题讲的是NBA的季后赛对战顺序，对于一个看了十几年NBA的老粉来说，再熟悉不过了。这种对战顺序是为了避免强强之间过早对决，从而失去比赛的公平性，跟欧冠欧联那种八强就开始随机抽签匹配有本质上的区别。NBA的这种比赛机制基本弱队很难翻身，假如你是拿到最后一张季后赛门票进的，那么一上来就干联盟第一，肯定凶多吉少，很有可能就被横扫了。但是偶尔也会出现黑八的情况，但都是极其少见的，毕竟像勇士这么叼的球队毕竟不多。好了，不闲扯了，来做题吧。我们就拿NBA这种八个球队的情况来分析吧，八只球队的排名是按常规赛胜率来排的：

1 2 3 4 5 6 7 8

因为是最强和最弱来对决，其次是次强与次弱对决，以此类推可得到：

1-8  2-7  3-6  4-5

那么接下来呢，还是最强与最弱，次强与次弱这种关系：

(1-8  4-5)  (2-7  3-6)

最后胜者争夺冠军

((1-8  4-5)  (2-7  3-6))

这样一分析是不是就清楚了呢，由于n限定了是2的次方数，那么就是可以一直对半分的，比如开始有n队，第一拆分为n/2对匹配，然后再对半拆，就是n/2/2，直到拆到n为1停止，而且每次都是首与末配对，次首与次末配对，这样搞清楚了规律，代码应该就不难写了吧，参见代码如下：

https://wormtooth.com/20170318-leetcode-contest24/






609. Find Duplicate File in System
----------------------------------



Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Example 1:
Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:  
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
Note:
No order is required for the final output.
You may assume the directory name, file name and file content only has letters and digits, and the length of file content is in the range of [1,50].
The number of files given is in the range of [1,20000].
You may assume no files or directories share the same name in the same directory.
You may assume each given directory info represents a unique directory. Directory path and file info are separated by a single blank space.
Follow-up beyond contest:
Imagine you are given a real file system, how will you search files? DFS or BFS?
If the file content is very large (GB level), how will you modify your solution?
If you can only read the file by 1kb each time, how will you modify your solution?
What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
How to make sure the duplicated files you find are not false positive?



http://pythoncentral.io/finding-duplicate-files-with-python/



给定一组文件信息，包含目录路径，以及目录下包含的文件。将所有内容重复的文件分组输出。


把路径，文件名，和文件内容解析出来，对文件内容建立map，最后扫一遍map中list的大小即可，有重复的list必然大于1。

题目看着有点长，其实主要意思就一句话：查找并输出内容相同的文件的目录。比如：[“root/a 1.txt(abcd) 2.txt(efgh)”, “root/c 3.txt(abcd)”, “root/c/d 4.txt(efgh)”, “root 4.txt(efgh)”]，内容为efgh的文件有三个，内容为abcd的文件有两个，所以efgh和abcd均为重复文件，结果就是输出重复文件的目录。我们要做的工作可以分为三步：一、通过字符串操作把所有的文件目录和内容按照标准的格式一一对应分割好，存为path和content； 二、把一一对应的数据存入字典dict中，content为主键，content相同的path全部存放在content为主键对应的list中；三、找到重复文件（len(dict[content])>1），并输出结果。

https://hellokenlee.github.io/2017/06/11/leetcode-609/



 
539. Minimum Time Difference
----------------------------


Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.



给定一组24小时制的时间，格式为“小时：分钟”，求任意两组时间中分钟数间隔的最小值。




http://blog.jerkybible.com/2017/03/18/LeetCode-539-Minimum-Time-Difference/




537. Complex Number Multiplication
----------------------------------



Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i的2次方 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.




关于complex numbers的解释

https://www.khanacademy.org/math/algebra2/introduction-to-complex-numbers-algebra-2/multiplying-complex-numbers-algebra-2/a/multiplying-complex-numbers


https://github.com/demonSong/leetcode/issues/8


71. Simplify Path
-----------------




Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".




[解题思路]
利用栈的特性，如果sub string element
1. 等于“/”，跳过，直接开始寻找下一个element
2. 等于“.”，什么都不需要干，直接开始寻找下一个element
3. 等于“..”，弹出栈顶元素，寻找下一个element
4. 等于其他，插入当前elemnt为新的栈顶，寻找下一个element

最后，再根据栈的内容，重新拼path。这样可以避免处理连续多个“/”的问题。




https://www.hrwhisper.me/leetcode-simplify-path/

