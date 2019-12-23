# Introduction to programming Task2
# Artur Goncharov I-17b-3
from pip._vendor.distlib.compat import raw_input
import math

print("Introducing to programming: Task1")
print("Artur Goncharov, I-17b")
x = int(raw_input("please enter x: "))
z = int(raw_input("please enter z: "))
if x == -2:
    print("Введенный x за областью определения функции!")
if z == 0:
    print("Введенный z за областью определения функции!")

y = (((2 * (x ** 2)) + x - 5) / (x + 2)) + (math.cos(x/(2*z))) / (math.sin(x/(2*z)))
print(y)
