class A:
    def __repr__(self):
        return "42"


a = A()
print(repr(a))
print(str(a))

"""but str doesn't apply to repr"""


class A:
    def __str__(self):
        return "42"


a = A()
print(repr(a))
print(str(a))
