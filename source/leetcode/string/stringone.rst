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



这道题木有搞明白



158. Read N Characters Given Read4 II - Call multiple times
-----------------------------------------------------------

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.


.. important::

        这道题目跟上面一样没有搞明白





151. Reverse Words in a String
------------------------------



Given an input string, reverse the string word by word.

For example
::
    Given s = "the sky is blue",
    return "blue is sky the".



For C programmers: Try to solve it in-place in O(1) space.

Clarification:

    #. What constitutes a word?
       
    A sequence of non-space characters constitutes a word.
    #. Could the input string contain leading or trailing spaces?
    
    Yes. However, your reversed string should not contain leading or trailing spaces.


    #. How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.




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


Hints:
Two-pass:
#. 1. reverse all strings:
"the sky is blue" -> "eulb si yks eht"

#. 2. reverse one word:
"eulb si yks eht" -> "blue is sky the"


.. code-block:: python

    def reverseWords(s):
        return ' '.join(reversed(s.split()))

    def reverseWords2(s):
        print " ".join(s.split()[::-1])

.. code-block:: javascript

        var hello = 'the sky is blue'.split(' ').reverse().join(' ');
        console.log(hello)


557. Reverse Words in a String III
----------------------------------

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
::
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.



JavaScript答案

.. code-block:: javascript

    var hello = "Let's take LeetCode contest".split(' ').map(s => s.split().reverse().join()).join(' ')
    console.log(hello)


551. Student Attendance Record I
--------------------------------

You are given a string representing an attendance record for a student. The record only contains the following three characters:

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


.. code-block:: Javascript

    function baby (s) {
            let twoStr = s.split('').sort().join('').toLowerCase().indexOf('aa');
            let oneStr = s.toLowerCase().indexOf('lll');
        
        if( twoStr < 0 && oneStr < 0 ) {
            return true;
        }else{
            return false;
        }
    }
    console.log(baby('ACFHPLLL'))

344. Reverse String
-------------------

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".



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

    var reverseStr = function(s, k) {
        var arr = s.split('');
        var i = 0;
        var n = arr.length;
        while(i < n) {
            var j = Math.min(i + k - 1, n - 1);
            reverse(arr,i,j);
            i += 2 * k;
        }
        return arr.join('');
    };
    function reverse(arr,i,j){
        while(i < j) {
            var tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
    }

345. Reverse Vowels of a String
-------------------------------


Write a function that takes a string as input and reverse only the vowels of a string.

::
    Example 1:
    Given s = "hello", return "holle".

    Example 2:
    Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

