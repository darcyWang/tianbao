题目序号 14、520、20、459、606、434、408、38、383
============================================================


14. Longest Common Prefix
-------------------------

Write a function to find the longest common prefix string amongst an array of strings.
::
    function sharedStart(array){
        var A = array.concat().sort(),  //拿到数组后进行合并排序
        a1= A[0], a2= A[A.length-1], L= a1.length, i= 0;
        while(i<L && a1.charAt(i)=== a2.charAt(i)) i++;
        return a1.substring(0, i);
    }

    sharedStart(['interspecies', 'interstelar', 'interstate'])  //=> 'inters'
    sharedStart(['throne', 'throne'])                           //=> 'throne'
    sharedStart(['throne', 'dungeon'])                          //=> ''
    sharedStart(['cheese'])                                     //=> 'cheese'
    sharedStart([])                                             //=> ''
    sharedStart(['prefix', 'suffix'])                           //=> ''




520. Detect Capital
-------------------


Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

#. All letters in this word are capitals, like "USA".
#. All letters in this word are not capitals, like "leetcode".
#. Only the first letter in this word is capital if it has more than one letter, like "Google".
#. Otherwise, we define that this word doesn't use capitals in a right way.
   
Example 1:
::
    Input: "USA"
    Output: True

Example 2:
::
    Input: "FlaG"
    Output: False


Note: 

.. hint ::
    The input will be a non-empty word consisting of uppercase and lowercase latin letters.


https://stackoverflow.com/questions/1027224/how-can-i-test-if-a-letter-in-a-string-is-uppercase-or-lowercase-using-javascrip


方法一：

#. 将单词转换为大写得到up，
#. 将单词转换为小写得到low，
#. 若word与up或与low相等，则返回true，
#. 否则去掉word的首字母得到last，
#. 若last转换为小写后仍与last相等，则返回true，否则返回false。


方法二：

#. flag为0表示首字母判断，flag为1表示首字母小写，flag为2表示首字母大写，
#. flag为1的情况下，若有大写字母出现则返回false，
#. flag为2的情况下，若有小写字母出现则flag置为3，
#. 若有大写字母出现则flag置为4，flag为3的情况下，
#. 若有大写字母出现则返回false，flag为4的情况下，
#. 若有小写字母出现则返回false。最终返回true。


20. Valid Parentheses
---------------------

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


.. code-block:: Javascript

    // Time complexity: O(n)
    function isValidParentheses(str) {
        var i = 0, l = str.length, arr = [];
        if (!l) {
            return true;
        }

        if ((l % 2) !== 0) {
            return false;
        }

        while (i < l) {
            var s = str[i];
            if (s == "{") {
                arr.push(s);
            } else if (s == "}") {
                if (arr.length) {
                    arr.pop();
                } else {
                    return false;
                }
            }
            i++;
        }
        return true;
    }

    isValidParentheses("{{{}}}"); // true
    isValidParentheses("{{}{}}"); // true
    isValidParentheses("{}{{}}"); // true
    isValidParentheses("}{}{"); // false


    function validParentheses(parens){
      var Arr=parens.split(""), counter1=0, counter2=0; 
      
      if (Arr[0]===")" || Arr[Arr.length-1]==="("){
      return false;}
      
      for (var i in Arr){
     
        if (Arr[i]=="("){
          counter1++;
        }
        
        if (Arr[i]===")"){
          counter2++;
        }
        
      }
      
      if (counter1===counter2){
        return true;
      }
      
      else return false; 
      
    }

    str= ")(()))"; 
    validParentheses(str);







459. Repeated Substring Pattern
-------------------------------

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
::
    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.

Example 2:
::
    Input: "aba"
    Output: False

Example 3:
::
    Input: "abcabcabcabc"
    Output: True
    Explanation: 
    It's the substring "abc" four times. (And the substring "abcabc" twice.)




606. Construct String from Binary Tree
--------------------------------------

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
:: 
        Input: Binary tree: [1,2,3,4]
               1
             /   \
            2     3
           /    
          4     

        Output: "1(2(4))(3)"

.. hint ::
        Explanation: Originallay it needs to be "1(2(4)())(3()())", 
        but you need to omit all the unnecessary empty parenthesis pairs. 
        And it will be "1(2(4))(3)".



Example 2:
::
    Input: Binary tree: [1,2,3,null,4]
           1
         /   \
        2     3
         \  
          4 

    Output: "1(2()(4))(3)"


.. hint ::

    Explanation: Almost the same as the first example, except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.


434. Number of Segments in a String
-----------------------------------

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:
:: 
    Input: "Hello, my name is John"
    Output: 5


408. Valid Word Abbreviation
----------------------------

Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
::
    Given s = "internationalization", abbr = "i12iz4n":

    Return true.


Example 2:
::
    Given s = "apple", abbr = "a2e":

    Return false.



38. Count and Say
-----------------

The count-and-say sequence is the sequence of integers with the first five terms as following:
::
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.


Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
::
    Input: 1
    Output: "1"


Example 2:
::
    Input: 4
    Output: "1211"



383. Ransom Note
----------------


Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.
::
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true






