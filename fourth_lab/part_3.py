from pip._vendor.distlib.compat import raw_input

x = float(raw_input('x: '))
y = int(raw_input('y: '))
eps = 0.0001
count = 0
while abs(y - x) > eps:
    y = (y + x / y) / 2
    count = count + 1
    if count == 10:
        print(float(y))
