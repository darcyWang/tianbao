# -*- coding: utf-8 -*-
#!/usr/bin/env python


class Solution:

    def removeDuplicates(self, A):
        if None == A:
            return 0
        len_A = len(A)
        if len_A <= 1:
            return len_A

        m = 0
        n = 1
        count = 1
        while n < len_A:
            if A[m] != A[n]:
                count = 1
                m += 1
                if m != n:
                    A[m] = A[n]
            elif count >= 2:
                count += 1
            else:
                m += 1
                count += 1
                if m != n:
                    A[m] = A[n]
            n += 1
        return m + 1

    def oneDuplicates(self, A):
        if len(A) <= 2: return len(A)
        prev = 1; curr = 2
        while curr < len(A):
            if A[curr] == A[prev] and  A[curr] == A[prev - 1]:
                curr += 1
            else:
                prev += 1
                A[prev] = A[curr]
                curr += 1
        return prev + 1
        

test = Solution()
l1 = [1,1,1,1,1,1,1,2,2,2,2,3,4]
l2 = [1,1,1,2,2,3]
print '测试一下题目数组去重的第二种做法，就是去掉数组中重复3次以上的元素后数组的长度是 %d'%test.oneDuplicates(l1)























































