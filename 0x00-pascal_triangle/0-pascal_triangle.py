#!/usr/bin/python3

'''a function def pascal_triangle(n)
    that returns a list of lists of
    integers representing the Pascal’s triangle of n
Returns an empty list if n <= 0
You can assume n will be always an integer'''


def pascal_triangle(n):
    '''returns a list of lists of
    integers representing the Pascal’s triangle of n'''

    if n <= 0:
        return []
    triangle = []
    for row in range(n):
        inner_row = []
        for j in range(row + 1):
            if j == 0 or j == row:
                inner_row.append(1)
            else:
                upper_row_left = triangle[row - 1][j - 1]
                upper_row_right = triangle[row - 1][j]
                m = upper_row_left + upper_row_right
                inner_row.append(m)
        triangle.append(inner_row)
    return triangle
