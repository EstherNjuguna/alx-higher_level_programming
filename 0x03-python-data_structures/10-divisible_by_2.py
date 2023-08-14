#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mlist = []
    for i in my_list:
        if i % 2 == 0:
            mlist.append(True)
        mlist.append(False)
    return mlist
