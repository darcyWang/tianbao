题目序号 58、293、67、125、468、22、647、583
============================================================






58. Length of Last Word
-----------------------


Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
::
    Given s = "Hello World",
    return 5.

293. Flip Game
--------------


You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip twoconsecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:
::
    [
      "--++",
      "+--+",
      "++--"
    ]
 

If there is no valid move, return an empty list [].


67. Add Binary
--------------


Given two binary strings, return their sum (also a binary string).

For example,
::
    a = "11"
    b = "1"
    Return "100".


125. Valid Palindrome
---------------------


Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example
::
    "A man, a plan, a canal: Panama" is a palindrome.
    "race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.


468. Validate IP Address
------------------------

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
::
    Input: "172.16.254.1"

    Output: "IPv4"

    Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
::
    Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

    Output: "IPv6"

    Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
::
    Input: "256.256.256.256"

    Output: "Neither"

    Explanation: This is neither a IPv4 address nor a IPv6 address.


编写函数，判断给定的IP地址是否为有效的IPv4地址或者Ipv6地址。

Ipv4地址为4个以点分隔的数字，范围0到255，例如172.16.254.1。

此外，Ipv4不允许出现前缀0。例如地址172.16.254.01是无效的。

Ipv6地址为8个以冒号分隔的16进制数字，例如2001:0db8:85a3:0000:0000:8a2e:0370:7334。允许出现前缀0，并且小写字母和大写字母可以同时出现，所以2001:db8:85a3:0:0:8A2E:0370:7334也是有效的IPv6地址。

然而，不允许出现两个连续的冒号。例如2001:0db8:85a3::8A2E:0370:7334是无效的。

此外，IPv6地址中每一个数字的长度不应大于4位，例如02001:0db8:85a3:0000:0000:8a2e:0370:7334是无效的。

注意：你可以假设测试用例中没有额外的空白字符，但是可能会包含一些特殊字符。


 $.validator.addMethod('IP4Checker', function(value) {
            var ip = "^(?:(?:25[0-5]2[0-4][0-9][01]?[0-9][0-9]?)\.){3}" +
                "(?:25[0-5]2[0-4][0-9][01]?[0-9][0-9]?)$";
                return value.match(ip);
            }, 'Invalid IP address');

            $('#form1').validate({
                rules: {
                    ip: {
                        required: true,
                        IP4Checker: true
                    }
                }
            });


//Validation
jQuery.validator.addMethod('validIP', function(value) {
    var split = value.split('.');
    if (split.length != 4) 
        return false;
            
    for (var i=0; i<split.length; i++) {
        var s = split[i];
        if (s.length==0 || isNaN(s) || s<0 || s>255)
            return false;
    }
    return true;
}, ' Invalid IP Address');

.. code-block:: python

    class Solution(object):
        def validIPAddress(self, IP):
            """
            :type IP: str
            :rtype: str
            """
            if self.validIPV4(IP):
                return 'IPv4'
            if self.validIPV6(IP):
                return 'IPv6'
            return 'Neither'

        def validIPV4(self, IP):
            parts = IP.split('.')
            if len(parts) != 4: return False
            for part in parts:
                if not part: return False
                if not part.isdigit(): return False
                if part[0] == '0' and len(part) > 1: return False
                if int(part) > 255: return False
            return True

        def validIPV6(self, IP):
            parts = IP.split(':')
            if len(parts) != 8: return False
            for part in parts:
                if not part: return False
                if len(part) > 4: return False
                if any(c not in string.hexdigits for c in part): return False
            return True


22. Generate Parentheses
------------------------

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
::
        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]


生成合法的括号对。
这里只需要搞清楚“合法(well-formed)”的概念就行了，那就是
1.左右括号数相等
2.任一位置之前的右括号数不大于左括号数

有了这样两点，那么要生成括号对总数为n的所有可能性的串。就从空字符串开始，按照上面的第二点限制，逐步添加左右括号即可。
当拿到合法的串，长度为k，时，要继续添加一个括号，那么就看这个串如果左括号的数目没有达到n，那就可以在此基础上添加一个左括号；
同时，如果串内右括号数目小于左括号数目的话，还可以在k串上添加一个右括号。
这样遍历了所有长度为k的合法串之后，我们就得到了所有合法的长度为k+1的串。
当我们生成了所有长度为2n的合法串，就得到了答案。

::

        class Solution(object):
            def bfs(self, left, right, depth, n, string, result):
                if depth == 2 * n:
                    result.append(string)
                    return
                if left < n:
                    string += '('
                    self.bfs(left + 1, right, depth + 1, n, string, result)
                    string = string[:len(string) - 1]
                if left > right:
                    string += ')'
                    self.bfs(left, right + 1, depth + 1, n, string, result)
                    string = string[:len(string) - 1]
            def generateParenthesis(self, n):
                """
                :type n: int
                :rtype: List[str]
                """
                result = []
                self.bfs(0, 0, 0, n, '', result)
                return result

647. Palindromic Substrings
---------------------------


Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.


http://www.jianshu.com/p/528f34dadbbb

function isPalindrome(s) {
  var rev = s.split("").reverse().join("");
  return s == rev;
}

function longestPalind(s){
    var maxp_length = 0,
    maxp = '';

    for(var i=0; i < s.length; i++) {
        var subs = s.substr(i, s.length);

        for(var j=subs.length; j>=0; j--) {
            var sub_subs = subs.substr(0, j);
            if (sub_subs.length <= 1)
            continue;

            //console.log('checking: '+ sub_subs);
            if (isPalindrome(sub_subs)) {
                //console.log('palindrome: '+ sub_subs);
                if (sub_subs.length > maxp_length) {
                    maxp_length = sub_subs.length;
                    maxp = sub_subs;
                }
            }
        }
    }
        
    //console.log(maxp_length, maxp);
    return maxp;
}

console.log(longestPalind("abcxyzyxabcdaaa"));





583. Delete Operation for Two Strings
-------------------------------------

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
::
    Input: "sea", "eat"
    Output: 2
    Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".


Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.

给定单词word1和word2，从word1和/或word2中删去一些字符，使得word1和word2相同，求最少删除的字符数。

注意：

单词长度不超过500
单词只包含小写字母


https://leetcode.com/articles/delete-operation-for-two-strings/