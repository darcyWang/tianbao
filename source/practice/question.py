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
	return max1 if max3==None else max3

numbers = [20,67,3,2.6,7,74,2.8,90.8,52.8,4,3,2,5,7]

print second_largest(numbers)
print third_largest(numbers)

print sorted(numbers)[-3]
print sorted(set(numbers))[-2]

print second_largest([1,1,1,1,1,2])

# second_largest([2,2,2,2,2,1])
# => 2
# second_largest([10,7,10])
# => 10
# second_largest([1,1,1,1,1,1])
# => 1
# second_largest([1])
# => None
# second_largest([])