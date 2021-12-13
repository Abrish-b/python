import sys
# import time

# start = time.time()


def factorize(file):
    factors = [2, 3, 4, 5, 6, 7, 8, 9]
    oneTime = 0
    for each in file:
        for factor in factors:
            if int(each) % factor == 0 and oneTime == 0:
                print("{:d} = {:d} * {:d}".format(int(each),
                      int(int(each)/factor), factor))
                oneTime += 1
            else:
                pass
        oneTime = 0


Amount = len(sys.argv)
number = []
if Amount == 1:
    print("Usage: factors <file>")
else:
    for i in range(1, Amount):
        number.append(sys.argv[i])
    for n in number:
        f = open(n, 'r')
        factorize(f)
# end = time.time()
# print("real     0m{:0.3f}s".format(end-start))
