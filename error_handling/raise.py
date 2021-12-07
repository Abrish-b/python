# raise a type error
def raise_exception():
    raise TypeError


try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
# raise with message


def raise_exception_msg(message=""):
    raise NameError(message)


try:
    raise_exception_msg("Python is fun")
except NameError as ne:
    print(ne)
