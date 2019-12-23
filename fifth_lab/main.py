# Introduction to programming Task2
# Artur Goncharov I-17b-3

print("Introducing to programming: Task1")
print("Artur Goncharov, I-17b")

# ----------------------------------------------------------------------------------------------------------------------

n = int(input("Введите натуральное число"))
if n <= 0:
    print("Вы ввели не натуральное число!")
    exit(1)
count = 1
deliteli = 0
while count < n:
    if n % count == 0:
        i = 2
        while i < count - 1:
            if count % i == 0:
                deliteli += 1
            i += 1
        if deliteli == 0:
            print(count)
    count += 1

# ----------------------------------------------------------------------------------------------------------------------

N = int(input("Enter N"))
M = int(input("Enter M"))

i = N
while i < M:
    if i % 3 == 0 and i % 2 == 0:
        print(i)
    i += 1

# ----------------------------------------------------------------------------------------------------------------------

answer = 0
i = 1
while i < n:
    if i * (i + 1) * (i + 2) == n:
        answer = 1
        break
    i += 1
if answer == 1:
    print("yes")
if answer == 0:
    print("nope")

# ----------------------------------------------------------------------------------------------------------------------

N = int(input("Enter N"))
i = 1
while i < N:
    if i % 10 == 3:
        print(i)
    i += 1


# ----------------------------------------------------------------------------------------------------------------------
# d = dict
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# i = 1
# m = map()
# while True:
#     fib = fibonacci(i)
#     if fib > 1000:
#         break
#     d.update()
