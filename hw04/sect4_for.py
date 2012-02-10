#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?

print "1.",
print sum(nums)


# 2. Print every even number in nums
print "2. even numbers"
for i in nums:
    if not i%2:
        print i


# 3. Does nums only contain even numbers? 
only_even = False

for num in nums:
    if num%2:
        only_even= False
        break
    else:
        only_even= True

print "3.",
if only_even:
    print "only even"
else:
    print "some odd"

# 4. Generate a list every odd number less than 100. Hint: use range()
print "4.", 
y=range (1,100)
q=[]
for g in y:
    if g%2:
        q.append(g)
print q

       

# 5. [ADVANCED]  Multiply each element in nums by its index
print "5.", __
