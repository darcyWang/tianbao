题目序号
=================================



89. Gray Code
-------------

https://leetcode.com/problems/gray-code/description/

.. code-block:: python

	class Solution:
	    # @param {integer} n
	    # @return {integer[]}
	    # 9:25
	    BASE = ['0', '1']

	    def grayCode(self, n):
	        if n == 0:
	            return [0]

	        result = Solution.BASE
	        for i in range(n - 1):
	            left = map(lambda x: '0' + x, result)
	            right = map(lambda x: '1' + x, result[::-1])
	            result = left + right

	        return map(lambda x: int(x, 2), result)		
				
				
	def grayCode(self, n):
	    res = [0]
	    for i in xrange(n):
	        res += map(lambda x:2**i+x, [x for x in res[::-1]])
	    return res	
				
	def grayCode(self, n):
	    res = [0]
	    for i in xrange(n):
	        res += (2**i+x for x in res[::-1])
	    return res	