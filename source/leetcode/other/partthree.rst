


223. Rectangle Area
-------------------


Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

.. image:: https://assets.leetcode.com/uploads/2018/10/22/rectangle_area.png

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.

.. code-block:: python

	class Solution(object):
	    def computeArea(self, A, B, C, D, E, F, G, H):
	        """
	        :type A: int
	        :type B: int
	        :type C: int
	        :type D: int
	        :type E: int
	        :type F: int
	        :type G: int
	        :type H: int
	        :rtype: int
	        """
	        return (C - A) * (D - B) + (H - F) * (G - E) - max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)


.. code-block:: python

	class Solution:
	# @param {integer} A
	# @param {integer} B
	# @param {integer} C
	# @param {integer} D
	# @param {integer} E
	# @param {integer} F
	# @param {integer} G
	# @param {integer} H
	# @return {integer}
	def computeArea(self, A, B, C, D, E, F, G, H):
	    S=(C-A)*(D-B) + (G-E)*(H-F)
	    if A>G or C<E or D<F or B>H :
	        return S
	    else:
	        s_common=(min(C,G)-max(A,E))*(min(D,H)-max(B,F))
	        return S-s_common
		
		
	def computeArea(self, A, B, C, D, E, F, G, H):
	    overlap = max(0, min(C, G)-max(A, E)) * max(0, min(D, H)-max(B, F))
	    return (C-A)*(D-B)+(G-E)*(H-F)-overlap
		









