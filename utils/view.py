def normalize(vec):
    norm = (vec[0]**2 + vec[1]**2 + vec[2]**2)**0.5
    if norm == 0:
        return vec
    return [vec[0] / norm, vec[1] / norm, vec[2] / norm]

def cross(a, b):
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def subtract(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def create_look_at(eye, target, up):
    forward = normalize(subtract(target, eye))
    side = normalize(cross(forward, up))
    up = normalize(cross(side, forward))

    return [
        [side[0], up[0], -forward[0], 0.],
        [side[1], up[1], -forward[1], 0.],
        [side[2], up[2], -forward[2], 0.],
        [-dot(side, eye), -dot(up, eye), dot(forward, eye), 1.0]
    ]