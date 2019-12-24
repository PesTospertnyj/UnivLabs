import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
x = 0
# ax2 + bx + c = 0
# d = b2 -4ac
d = b ** 2 - 4 * a * c
print("D = ", d)
print("D = ", d ** .5)
if d > 0:
    res1 = (-b + (d ** .5)) / (2 * a)
    res2 = (-b - (d ** .5)) / (2 * a)
    print(int(res1))
    print(int(res2))
elif d == 0:
    res = -b / 2 * a
    print(res)
else:
    print("no answer, expression is wrong")
