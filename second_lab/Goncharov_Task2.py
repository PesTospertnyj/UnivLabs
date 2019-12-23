# Introduction to programming Task2
# Artur Goncharov I-17b-3
from math import *
from pip._vendor.distlib.compat import raw_input

print("Introduction to programming Task2")
print("Artur Goncharov I-17b-3")
x = int(raw_input("please enter x: "))
z = int(raw_input("please enter z: "))
y = (2 * x ** 2 + x - 5) / (x + 2) + cos(x / 2 * z) / sin(x / 2 * z)
print(y)
