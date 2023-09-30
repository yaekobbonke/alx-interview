#n = int(input("Enter the number of rows: "))
def pascal_triangle(n):
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