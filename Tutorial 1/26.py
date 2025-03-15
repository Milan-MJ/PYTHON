# Write a Python program to find distance between two points (x1,y1) and (x2,y2).
import math
x1, y1 = map(float, input("Enter x1, y1: ").split())
x2, y2 = map(float, input("Enter x2, y2: ").split())
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between points:", distance)
