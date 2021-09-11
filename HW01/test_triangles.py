from HW01.triangles import classify_triangle

def test_triangles01():
    assert classify_triangle(3, 4, 5) == "Right"

def test_triangles02():
    assert classify_triangle(5, 12, 13) == "Right"

def test_triangles03():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_triangles04():
    assert classify_triangle(2, 5, 5) == "Isosceles"

def test_triangles05():
    assert classify_triangle(6, 2, 6) == "Isosceles"

def test_triangles06():
    assert classify_triangle(4, 5, 7) == "Scalene"

def test_triangles07():
    assert classify_triangle(9, 12, 16) == "Scalene"

def test_triangles08():
    assert classify_triangle(0, 0, 5) == "Error"

def test_triangles09():
    assert classify_triangle(3, 5, 20) == "Error"

def test_triangles10():
    assert classify_triangle(3, 4, 0) == "Error"

def test_triangles11():
    assert classify_triangle(-3, 4, -5) == "Error"
