#!/usr/bin/python3
    """ list_division divides list element by 2 lists"""

def list_division(my_list_1, my_list_2, list_length):
    div_list = [0]*list_length
    for i in range(list_length):
        division = 0
        try:
            division = (my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            div_list[i] = division
    return div_list
