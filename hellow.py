from math import pi as PI
from datetime import datetime
data = {'first': 'Hodor', 'last': 'Hodor!'}
data1 = [4, 8, 15, 16, 23, 42]
number = int(45.55)
clock = datetime.today()
c1 = clock.strftime("%b-%d-%Y")
print('{first} {last}'.format(**data))
print('{:06.2f}'.format(3.141592653589793))
print('{d[4]} {d[5]}'.format(d=data1))
print(c1)
print('{:%Y-%m-%d %H:%M}'.format(datetime.today()))
