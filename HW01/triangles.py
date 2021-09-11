"""
Vincenzo Susi
SSW-567 Homework 1
"""


def classify_triangle(a, b, c):
    # Check for errors
    if a == 0 or b == 0 or c == 0:
        # A triangle cannot have a side length of 0
        return "Error"
    if a + b < c or a + c < b or b + c < a:
        # The sum of any two sides of a triangle must be greater than the third side
        return "Error"

    # Triangle Classifying
    if a == b and b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    elif a**2 + b**2 == c**2:
        return "Right"
    else:
        return "Scalene"


if __name__ == '__main__':
    print(classify_triangle(1, 2, 5))
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(1, 0, 3))
    print(classify_triangle(3, 3, 3))
    print(classify_triangle(7, 10, 10))
    print(classify_triangle(5, 6, 9))
