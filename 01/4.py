def identity(size: int) -> list[list]:
    result = [[int(i==j) for j in range(size)] for i in range(size)]

    return result

def square(size: int) -> list[list]:
    result = [[j + (size*i)  for j in range(size)] for i in range(size)]

    return result

def transpose(matrix: list[list]) -> list[list]:
    rows_n = len(matrix)
    columns_n = len(matrix[0])

    result = [[matrix[r][c] for r in range(rows_n)] for c in range(columns_n)]

    return result

def multiply(a: list[list], b: list[list]) -> list[list]:
    rows_a = len(a)
    cols_a = len(a[0])

    rows_b = len(b)
    cols_b = len(b[0])

    assert cols_a == rows_b

    result = [[sum(a[r_a][i] * b[i][c_b] for i in range(cols_a)) for c_b in range(cols_b)] for r_a in range(rows_a)]

    return result



if __name__ == '__main__':
    print('1.')
    for row in identity(5):
        print(row)

    print('\n2.')
    for row in square(5):
        print(row)

    matrix = [
    ["a", "b"],
    ["c", "d"],
    ["e", "f"]
]
    print('\n3.')
    for row in transpose(matrix):
        print(row)

    a = [
    [2, 4, 1],
    [0, 3, 5]
]

    b = [
    [1, 2],
    [0, 3],
    [4, 1]
]

    print('\n4.')
    for row in multiply(a, b):
        print(row)
