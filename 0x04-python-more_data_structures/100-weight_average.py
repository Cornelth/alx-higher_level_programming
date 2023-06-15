#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    cum_mark = 0
    freq = 0

    for tup in my_list:
        cum_mark += tup[0] * tup[1]
        freq += tup[1]

    return (cum_mark / freq)
