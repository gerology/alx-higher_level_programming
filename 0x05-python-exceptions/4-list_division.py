#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
       Args:
           my_list_1 (list) - first list of integers
           my_list_2 (list) - second list of integers
           list_length (list) - number of elements to divide
       Return:
           return a new list with divisions
    """
    new = []
    for a in range(0, list_length):
        try:
            sum = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            sum = 0
        except ZeroDivisionError:
            print("division by 0")
            sum = 0
        except IndexError:
            print("out of range")
            sum = 0
        finally:
            new.append(sum)
    return (new)
