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


def containsNearbyDuplicate(self, nums, k):
    numDict = dict()
    for x in range(len(nums)):
        idx = numDict.get(nums[x])
        if idx >= 0 and x - idx <= k:
            return True
        numDict[nums[x]] = x
    return False

def containsNearbyDuplicate(self, nums, k):
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

# print news_ids

numbers = [20,67,3,2.6,7,74,2.8,90.8,52.8,4,3,2,5,7]
babys = [7,10]

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