#!/usr/bin/python3

for digit in range(0, 10):
    for digitt in range(digit + 1, 10):
        if digit == 8 and digitt == 9:
            print("{}{}".format(digit, digitt))
        else:
            print("{}{}".format(digit, digitt), end=", ")
