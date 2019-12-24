import sys

while True:
    if len(sys.argv) > 1:
        blah = sys.argv[1]
    else:
        blah = 'blah'
        print("args can't be empty")
        break
    digit_string = sys.argv[1]

    if not digit_string.isdigit():
        print("error, please enter number")
        break
    elif digit_string is None or digit_string == "":
        print("enter your number please")
        break
    elif int(digit_string) < 0:
        print("enter your number please")
        break
    else:
        i = 1
        j = int(digit_string)-1
        while i < int(digit_string) + 1:
            print(" " * j, "#" * i)
            j -= 1
            i += 1
    break
