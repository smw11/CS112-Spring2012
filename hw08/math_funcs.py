#!/usr/bin/env python

# Distance formula
#   calculate a function called "distance" to calculate the distance between two points.
#   http://www.purplemath.com/modules/distform.htm
#   ex: 
#      >>> distance((0,0), (3,4))
#      5

# def distance(a, b):
import math

#defines distance as a function, which performs the distance formula and returns the answer promptly
def distance((x1, y1), (x2, y2)):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

#User inputs four numbers, serving as the respective coordinates
x1 = int(raw_input("Enter the first number in your first coordinate: "))
y1 = int(raw_input("Enter the second number in your first coordinate: "))
x2 = int(raw_input("Enter the first number in your second coordinate: "))
y2 = int(raw_input("Enter the second number in your second coordinate: "))

#The distance is printed ^_^
print "The distance between your two points is ", distance((x1, y1), (x2,y2))


# ADVANCED
# Normalizing Vectors
#   normalize a vector of length N.  If given all zeros, just spit back the same vector
#   http://www.fundza.com/vectors/normalize/index.html

#   ex:
#     >>> normalize((1,1))
#     [0.70710678118654746, 0.70710678118654746]
#     >>> normalize([0,0,0])
#     [0,0,0]
#     >>> normalize([1,1,1,1])
#     [0.25, 0.25, 0.25, 0.25]

# def normalize(vec):
