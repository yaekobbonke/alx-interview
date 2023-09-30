#n = int(input("Enter the number of rows: "))
def pascal_triangle(n):
    triangle = []
    for r in range(n):
        inner_row = []
        for j in range(r + 1):
            if j == 0 or j == r:
                inner_row.append(1)
            else:
                upper_row_left = triangle[r - 1][j - 1]
                upper_row_right = triangle[r - 1][j]
                m = upper_row_left + upper_row_right
                inner_row.append(m)
        triangle.append(inner_row)
    return triangle
n = 5
if n <= 0:
    triangle = []
else:
    triangle = pascal_triangle(n)