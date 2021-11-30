
# square bi-dimensional matrix
def square_matrix_simple(matrix=[]):
    new_matrix = list()
    for row in matrix:
        new_matrix.append(list(map(lambda x: x**2, row)))
    return new_matrix

# shorter


def square_matrix_simple2(matrix=[]):
    return ([list(map(lambda x: x * x, row)) for row in matrix])


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
