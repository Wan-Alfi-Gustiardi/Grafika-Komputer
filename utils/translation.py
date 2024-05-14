class Matrix44:
    @staticmethod
    def create_identity():
        return [[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]]

    @staticmethod
    def translation_matrix(vector):
        if len(vector) != 3:
            raise ValueError("Translasi harus memiliki tiga elemen")
        matrix = Matrix44.create_identity()
        for i in range(3):
            matrix[3][i] = vector[i]
        return matrix

class Vector3:
    def __init__(self, values):
        if len(values) != 3:
            raise ValueError("List harus memiliki tiga elemen")
        self.x = values[0]
        self.y = values[1]
        self.z = values[2]

def to_list(vector):
    return [vector.x, vector.y, vector.z]