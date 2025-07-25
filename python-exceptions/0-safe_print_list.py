#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end="")
                count += 1
            except IndexError:
                break
    except Exception:
        pass
    print()
    return count
