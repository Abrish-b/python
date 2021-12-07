# safe integer
from ctypes import memset
import sys


def safe_print_integer(value):
    try:
        print("{:d}".format(value), end="\n")
    except (ValueError, TypeError):
        return False
    else:
        return True


# safe print int with sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="\n")
        return True
    except (TypeError, ValueError) as Err:
        sys.stderr.write("Excepion: {} \n".format(Err))
        return False


value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))


#!/usr/bin/python3


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    except TypeError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
