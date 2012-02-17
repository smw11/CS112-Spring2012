#!/usr/bin/env python
from random import randint

s = 1
input_num = int(raw_input())
list_thing = []

#Changes the list to include random number
for _ in range(input_num):
    list_thing.append(randint(0, 20))

#prints list the first time
print list_thing

#while loop changes the list
while s:
    s = 0
    for i in range(1,input_num):
        if list_thing[i-1] > list_thing[i]:
            input_num1 = list_thing[i-1]
            input_num2 = list_thing[i]
            list_thing[i-1] = input_num2
            list_thing[i] = input_num1
            s = 1

#prints list the second time
print list_thing
