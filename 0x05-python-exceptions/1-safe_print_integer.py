#!/usr/bin/python3
def safe_print_integer(value):
    try:
	my_value = value / 1
        print("{:d}".format(my_value))
        return True
    except:
        print("{} is not an integer".format(value))
	return False
