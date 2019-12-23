# Introduction to programming Task2
# Artur Goncharov I-17b-3

print("Introducing to programming: Task1")
print("Artur Goncharov, I-17b")

prev_s = 1000
s = 0
e = 10 - 4
n = 3


def f(n):
    return (1 / (n * 3 - 2)) * (n * 3 + 1)


while abs(prev_s - s) > e:
    prev_s = s
    s += f(n)
    print(s)
    n += 1

print(s)
