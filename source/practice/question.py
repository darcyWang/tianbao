# -*- coding: utf-8 -*-
#!/usr/bin/env python


def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None

def new_second_largest(numbers):
    first, second = None, None
    for n in numbers:
        if n > first:
            first, second = n, first
        elif first > n > second:
            second = n
    return second


def third_largest(numbers):
	max1 = max2= max3=None
	for num in numbers:
	    if num > max1:
	        max2,max3 = max1,max2
	        max1=num
	    elif num > max2 and num < max1:
	        max2,max3= num,max2
	    elif num > max3 and num < max2:
	        max3 = num
        if max3 == None:
            return max1
        return max3




def new_third_largest(numbers):
    count = 0
    top = [float("-inf")] * 3
    for num in numbers:
        if num > top[0]:
            top[0], top[1], top[2] = num, top[0],top[1]
            count += 1
        elif num != top[0] and num > top[1]:
            top[1], top[2] = num, top[1]
            count += 1
        elif num != top[0] and num != top[1] and num > top[2]:
            top[2] = num
            count += 1
    if count < 3:
        return top[0]
    return top[2]

ids = [1,4,3,3,4,2,3,4,5,6,1]
news_ids = list(set(ids))
# news_ids.sort(key=ids.index)

numbers = [20,67,3,2.6,7,74,2.8,90.8,52.8,4,3,2,5,7]

def containsNearbyDuplicateOne(nums, k):
    numDict = dict()
    for x in range(len(nums)):
        idx = numDict.get(nums[x])
        if idx >= 0 and x - idx <= k:
            return True
        numDict[nums[x]] = x
    return False

def containsNearbyDuplicate(nums, k):
    lookup = {}
    for i, num in enumerate(nums):
        if num not in lookup:
            lookup[num] = i
        else:
            # It the value occurs before, check the difference.
            if i - lookup[num] <= k:
                return True
            # Update the index of the value.
            lookup[num] = i
    return False

# print containsNearbyDuplicateOne(numbers, 10)


bbb = "the sky is blue"

def reverseWords(s):
    return ' '.join(reversed(s.split()))

def reverseWords2(s):
    print " ".join(s.split()[::-1])

# print reverseWords(bbb)
# print reverseWords2(bbb)

def maxSubArray(ls):
    if len(ls) == 0:
       raise Exception("Array empty") # should be non-empty
      
    runSum = maxSum = ls[0]
    i = 0
    start = finish = 0

    for j in range(1, len(ls)):
        if ls[j] > (runSum + ls[j]):
            runSum = ls[j]
            i = j
        else:
            runSum += ls[j]

        if runSum > maxSum:
            maxSum = runSum
            start = i
            finish = j

    print "maxSum =>", maxSum
    print "start =>", start, "; finish =>", finish

maxSubArray([-2, 11, -4, 13, -5, 2])
maxSubArray([-15, 29, -36, 3, -22, 11, 19, -5])

def newmaxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if max(nums) < 0:
        return max(nums)
    global_max, local_max = float("-inf"), 0
    for x in nums:
        local_max = max(0, local_max + x)
        global_max = max(global_max, local_max)
    return global_max



print newmaxSubArray([-15, 29, -36, 3, -22, 11, 19, -5])

# print news_ids

# babys = [7,10]

# print third_largest(babys)
# print newDuplicate(babys)
# print second_largest(numbers)
# print third_largest(numbers)

# print sorted(numbers)[-3]
# print sorted(set(numbers))[-2]

# print second_largest([1,1,1,1,1,2])

# second_largest([2,2,2,2,2,1])
# => 2
# second_largest([10,7,10])
# => 10
# second_largest([1,1,1,1,1,1])
# => 1
# second_largest([1])
# => None
# second_largest([])