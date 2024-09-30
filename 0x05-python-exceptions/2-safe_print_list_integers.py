#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    count = 0
    while printed_count < x:
        try:
            print("{:d}".format(my_list[printed_count]), end=" ")
            count += 1
        except TypeError:
            pass
        except IndexError:
            raise
        finally:
            printed_count += 1
    print()
    return count
