"""this is Nqueen problem Absolute soltion generator"""
"""this is using the following conecpt from wikipedia

______________________________________________________________________________________________________________________________________________________
|    1) If the remainder from dividing n by 6 is not 2 or 3 then the list is simply all even numbers followed by all odd numbers not greater than n. |
|    2) Otherwise, write separate lists of even and odd numbers (2, 4, 6, 8 – 1, 3, 5, 7).                                                           |
|    3) If the remainder is 2, swap 1 and 3 in odd list and move 5 to the end (3, 1, 7, 5).                                                          |   
|    4) If the remainder is 3, move 2 to the end of even list and 1,3 to the end of odd list (4, 6, 8, 2 – 5, 7, 1, 3).                              |  
|    5) Append odd list to the even list and place queens in the rows given by these numbers, from left to right                                     |
|       (a2, b4, c6, d8, e3, f1, g7,h5)                                                                                                              |
|____________________________________________________________________________________________________________________________________________________|

"""


import sys
print("Usage: nqueens N")


def queenGambit(num):
    soln_x = []
    soln = []
    if (num % 6) != 2 or (num % 6) != 3:
        for even in range(1, num+1):
            if even % 2 == 0:
                soln_x.append(even)
        for odd in range(1, num+1):
            if odd % 2 != 0:
                soln_x.append(odd)
    elif (num % 6) == 2:
        for even in range(1, num+1):
            if even % 2 == 0:
                soln_x.append(even)
        soln_x.append(3)
        soln_x.append(1)
        for odd in range(1, num+1):
            if odd % 2 != 0 and odd != 3 and odd != 1 and odd != 5:
                soln_x.append(odd)
        soln_x.append(5)
    elif (num % 6) == 3:
        for even in range(1, num+1):
            if even % 2 == 0 and even != 2:
                soln_x.append(even)
        soln_x.append(2)
        for odd in range(1, num+1):
            if odd % 2 != 0 and odd != 3 and odd != 1:
                soln_x.append(odd)
        soln_x.append(1)
        soln_x.append(3)
    for x, y in zip(soln_x, range(0, num)):
        soln.append([y, x-1])
    return soln


try:
    if isinstance(int(sys.argv[1]), int) and int(sys.argv[1]) >= 4:
        print("soltion for {} queens in {}x{} ChessBoard is: ".format(
            sys.argv[1], sys.argv[1], sys.argv[1]))
        print(queenGambit(int(sys.argv[1])))
        exit(0)
    elif int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

except ValueError as e:
    print("N must be a number" + str(e))
    exit(1)
