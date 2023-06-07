#!/usr/bin/python3
for p in range(100):
    if p == 99:
        print(p)
    else:
        print("{}".format('0' + str(p) if p < 10 else p), end=", ")
