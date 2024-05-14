import math

def create_perspective_projection_matrix(fovy, aspect, near, far):
    ymax = near * math.tan(math.radians(fovy) / 2.0)
    xmax = ymax * aspect
    
    left = -xmax
    right = xmax
    bottom = -ymax
    top = ymax
    
    A = (right + left) / (right - left)
    B = (top + bottom) / (top - bottom)
    C = -(far + near) / (far - near)
    D = -2.0 * far * near / (far - near)
    E = 2.0 * near / (right - left)
    F = 2.0 * near / (top - bottom)

    return [
        [E, 0.0,  0.0,  0.0],
        [0.0, F,  0.0,  0.0],
        [A,  B,   C,   -1.0],
        [0.0, 0.0, D,    0.0]
    ]