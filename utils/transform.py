import math

def scale_matrix(scale_factor):
    return [
        [scale_factor, 0.0, 0.0, 0.0],
        [0.0, scale_factor, 0.0, 0.0],
        [0.0, 0.0, scale_factor, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]

def rotation_matrix_x(angle):
    sin_angle = math.sin(angle)
    cos_angle = math.cos(angle)
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, cos_angle, -sin_angle, 0.0],
        [0.0, sin_angle, cos_angle, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]

def rotation_matrix_y(angle):
    sin_angle = math.sin(angle)
    cos_angle = math.cos(angle)
    return [
        [cos_angle, 0.0, sin_angle, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-sin_angle, 0.0, cos_angle, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]

def matrix_multiply(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise ValueError("Jumlah kolom pada matriks pertama harus sama dengan jumlah baris pada matriks kedua.")

    result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result