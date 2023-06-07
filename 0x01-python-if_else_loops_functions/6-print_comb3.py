#!/usr/bin/python3
for p in range(100):
    if int(p / 10) != p % 10 and int(p / 10) < p % 10:
        print("{}{}".format(int(p / 10), p % 10), end="")
        if (p != 89):
            print(", ", end="")
print("")
