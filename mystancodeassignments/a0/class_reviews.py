"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    which = input("Which class? ")
    result = which.upper()
    max101 = 0
    min101 = 0
    total101 = 0
    max001 = 0
    min001 = 0
    total001 = 0
    (a, b) = (0, 0)
    if result == "SC101":
        score101 = int(input("Score: "))
        a = 1
        max101 = score101
        min101 = score101
        total101 = score101
    elif result == "SC001":
        score001 = int(input("Score: "))
        b = 1
        max001 = score001
        min001 = score001
        total001 = score001
    else:
        if result == "-1":
            print("No class scores were entered")
            return 0

    while which != "-1":
        which = input("Which class? ")
        result = which.upper()
        if result == "SC101":
            data101 = int(input("Score: "))
            if data101 > max101:
                max101 = data101
                total101 = total101 + data101
                a += 1
                if a == 1:
                    min101 = max101

            if data101 < min101:
                min101 = data101
                total101 = total101 + data101
                a += 1
                if a == 1:
                    min101 = max101

            else:
                total101 = total101 + data101
                a += 1

        if result == "SC001":
            data001 = int(input("Score: "))
            if data001 > max001:
                max001 = data001
                total001 = total001 + data001
                b += 1
                if b == 1:
                    min001 = max001

            if data001 < min001:
                min001 = data001
                total001 = total001 + data001
                b += 1
                if b == 1:
                    min001 = max001

            else:
                total001 = total001 + data001
                b += 1

    print("=============" + "SC001" + "=============")
    if b == 0:
        print("No score for SC001")
    else:
        print("Max (001): " + str(max001))
        print("Min (001): " + str(min001))
        print("Avg (001): " + str(total001 / b))
    print("=============" + "SC101" + "=============")
    if a == 0:
        print("No score for SC101")
    else:
        print("Max (101): " + str(max101))
        print("Min (101): " + str(min101))
        print("Avg (101): " + str(total101 / a))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
