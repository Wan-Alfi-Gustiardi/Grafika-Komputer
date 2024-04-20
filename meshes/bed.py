import numpy as np

class Bed:
    def get_frame_data():
        frame_vertices = [
            0.691075, -0.063902, -0.399850, 0.096831, 0.080843, 0.055785,
            0.691075, -0.193835, -0.399850, 0.096831, 0.080843, 0.055785,
            0.691075, -0.063902, 0.399850, 0.096831, 0.080843, 0.055785,
            0.691075, -0.193835, 0.399850, 0.096831, 0.080843, 0.055785,
            -0.308550, -0.063902, -0.399850, 0.096831, 0.080843, 0.055785,
            -0.308550, -0.193835, -0.399850, 0.096831, 0.080843, 0.055785,
            -0.308550, -0.063902, 0.399850, 0.096831, 0.080843, 0.055785,
            -0.308550, -0.193835, 0.399850, 0.096831, 0.080843, 0.055785,
            -0.351616, -0.193835, -0.399850, 0.096831, 0.080843, 0.055785,
            -0.351616, -0.193835, 0.399850, 0.096831, 0.080843, 0.055785,
            -0.351616, -0.063902, 0.399850, 0.096831, 0.080843, 0.055785,
            -0.351616, -0.063902, -0.399850, 0.096831, 0.080843, 0.055785,
            -0.308550, 0.168436, 0.399850, 0.096831, 0.080843, 0.055785,
            -0.308550, 0.168436, -0.399850, 0.096831, 0.080843, 0.055785,
            -0.351616, 0.168436, 0.399850, 0.096831, 0.080843, 0.055785,
            -0.351616, 0.168436, -0.399850, 0.096831, 0.080843, 0.055785,
        ]

        frame_indices = [
            4, 2, 0,
            2, 7, 3,
            4, 12, 6,
            1, 7, 5,
            0, 3, 1,
            4, 1, 5,
            10, 8, 9,
            5, 11, 4,
            6, 9, 7,
            7, 8, 5,
            13, 14, 12,
            11, 13, 4,
            6, 14, 10,
            10, 15, 11,
            4, 6, 2,
            2, 6, 7,
            4, 13, 12,
            1, 3, 7,
            0, 2, 3,
            4, 0, 1,
            10, 11, 8,
            5, 8, 11,
            6, 10, 9,
            7, 9, 8,
            13, 15, 14,
            11, 15, 13,
            6, 12, 14,
            10, 14, 15,
        ]

        return np.array(frame_vertices, dtype=np.float32), np.array(frame_indices, dtype=np.uint32)
    
    def get_mattress_data():
        mattress_vertices = [
            0.677747, 0.011726, -0.383856, 0.753938, 0.75468, 0.800915,
            0.677747, -0.063902, -0.383856, 0.753938, 0.75468, 0.800915,
            0.677747, 0.011726, 0.383856, 0.753938, 0.75468, 0.800915,
            0.677747, -0.063902, 0.383856, 0.753938, 0.75468, 0.800915,
            -0.308550, 0.011726, -0.383856, 0.753938, 0.75468, 0.800915,
            -0.308550, -0.063902, -0.383856, 0.753938, 0.75468, 0.800915,
            -0.308550, 0.011726, 0.383856, 0.753938, 0.75468, 0.800915,
            -0.308550, -0.063902, 0.383856, 0.753938, 0.75468, 0.800915,
        ]

        mattress_indices = [
            4, 2, 0,
            2, 7, 3,
            1, 7, 5,
            0, 3, 1,
            4, 1, 5,
            4, 6, 2,
            2, 6, 7,
            1, 3, 7,
            0, 2, 3,
            4, 0, 1,
        ]

        return np.array(mattress_vertices, dtype=np.float32), np.array(mattress_indices, dtype=np.uint32)
    
    def get_first_pillow_data():
        first_pillow_vertices = [
            -0.212277, 0.011726, 0.087138, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.026208, 0.063049, 0.718012, 0.237273, 0.075974,
            -0.120251, 0.026208, 0.087138, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.026208, 0.063049, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.011726, 0.087138, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.048458, 0.063049, 0.718012, 0.237273, 0.075974,
            -0.120251, 0.048458, 0.087138, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.062940, 0.087138, 0.718012, 0.237273, 0.075974,
            -0.245082, 0.026208, 0.087138, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.062940, 0.287949, 0.718012, 0.237273, 0.075974,
            -0.245082, 0.048458, 0.287949, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.048458, 0.312039, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.026208, 0.312039, 0.718012, 0.237273, 0.075974,
            -0.245082, 0.026208, 0.287949, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.011726, 0.287949, 0.718012, 0.237273, 0.075974,
            -0.120251, 0.048458, 0.287949, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.062940, 0.287949, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.048458, 0.312039, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.026208, 0.312039, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.011726, 0.287949, 0.718012, 0.237273, 0.075974,
            -0.120251, 0.026208, 0.287949, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.048458, 0.063049, 0.718012, 0.237273, 0.075974,
            -0.245082, 0.048458, 0.087138, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.062940, 0.087138, 0.718012, 0.237273, 0.075974,
        ]

        first_pillow_indices = [
            4, 14, 0,
            17, 12, 18,
            21, 3, 1,
            23, 16, 7,
            10, 8, 13,
            7, 6, 5,
            4, 3, 2,
            1, 0, 8,
            9, 10, 11,
            12, 13, 14,
            15, 16, 17,
            18, 19, 20,
            21, 22, 23,
            19, 12, 14,
            1, 22, 21,
            23, 10, 9,
            14, 8, 0,
            16, 6, 7,
            4, 20, 19,
            2, 5, 6,
            7, 21, 23,
            0, 3, 4,
            11, 13, 12,
            9, 17, 16,
            18, 15, 17,
            6, 20, 2,
            4, 19, 14,
            17, 11, 12,
            21, 5, 3,
            23, 9, 16,
            10, 22, 8,
            19, 18, 12,
            1, 8, 22,
            23, 22, 10,
            14, 13, 8,
            16, 15, 6,
            4, 2, 20,
            2, 3, 5,
            7, 5, 21,
            0, 1, 3,
            11, 10, 13,
            9, 11, 17,
            18, 20, 15,
            6, 15, 20,
        ]

        return np.array(first_pillow_vertices, dtype=np.float32), np.array(first_pillow_indices, dtype=np.uint32)
    
    def get_second_pillow_data():
        second_pillow_vertices = [
            -0.212277, 0.011726, -0.287950, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.026208, -0.312039, 0.718012, 0.237273, 0.075974,
            -0.120251, 0.026208, -0.287950, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.026208, -0.312039, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.011726, -0.287950, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.048458, -0.312039, 0.718012, 0.237273, 0.075974,
            -0.120251, 0.048458, -0.287950, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.062940, -0.287950, 0.718012, 0.237273, 0.075974,
            -0.245081, 0.026208, -0.287950, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.062940, -0.087139, 0.718012, 0.237273, 0.075974,
            -0.245081, 0.048458, -0.087139, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.048458, -0.063049, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.026208, -0.063049, 0.718012, 0.237273, 0.075974,
            -0.245081, 0.026208, -0.087139, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.011726, -0.087139, 0.718012, 0.237273, 0.075974,
            -0.120251, 0.048458, -0.087139, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.062940, -0.087139, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.048458, -0.063049, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.026208, -0.063049, 0.718012, 0.237273, 0.075974,
            -0.153055, 0.011726, -0.087139, 0.718012, 0.237273, 0.075974,
            -0.120251, 0.026208, -0.087139, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.048458, -0.312039, 0.718012, 0.237273, 0.075974,
            -0.245081, 0.048458, -0.287950, 0.718012, 0.237273, 0.075974,
            -0.212277, 0.062940, -0.287950, 0.718012, 0.237273, 0.075974,
        ]

        second_pillow_indices = [
            4, 14, 0,
            17, 12, 18,
            21, 3, 1,
            23, 16, 7,
            10, 8, 13,
            7, 6, 5,
            4, 3, 2,
            1, 0, 8,
            9, 10, 11,
            12, 13, 14,
            15, 16, 17,
            18, 19, 20,
            21, 22, 23,
            19, 12, 14,
            1, 22, 21,
            23, 10, 9,
            14, 8, 0,
            16, 6, 7,
            4, 20, 19,
            2, 5, 6,
            7, 21, 23,
            0, 3, 4,
            11, 13, 12,
            9, 17, 16,
            18, 15, 17,
            6, 20, 2,
            4, 19, 14,
            17, 11, 12,
            21, 5, 3,
            23, 9, 16,
            10, 22, 8,
            19, 18, 12,
            1, 8, 22,
            23, 22, 10,
            14, 13, 8,
            16, 15, 6,
            4, 2, 20,
            2, 3, 5,
            7, 5, 21,
            0, 1, 3,
            11, 10, 13,
            9, 11, 17,
            18, 20, 15,
            6, 15, 20,
        ]

        return np.array(second_pillow_vertices, dtype=np.float32), np.array(second_pillow_indices, dtype=np.uint32)
    
    def get_blanket_data():
        blanket_vertices = [
            0.677747, 0.011726, -0.383856, 0.177704, 0.747082, 0.800828,
            0.677747, 0.011726, 0.383856, 0.177704, 0.747082, 0.800828,
            0.677747, -0.034135, 0.383856, 0.177704, 0.747082, 0.800828,
            -0.043671, -0.034135, 0.383856, 0.177704, 0.747082, 0.800828,
            0.677747, -0.034135, -0.383856, 0.177704, 0.747082, 0.800828,
            -0.043671, -0.034135, -0.383856, 0.177704, 0.747082, 0.800828,
            0.677747, 0.016724, 0.383856, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.016724, 0.383856, 0.177704, 0.747082, 0.800828,
            0.677747, 0.016724, -0.383856, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.016724, -0.383856, 0.177704, 0.747082, 0.800828,
            0.677747, 0.011726, 0.389854, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.011726, 0.389854, 0.177704, 0.747082, 0.800828,
            -0.043671, -0.034135, 0.389854, 0.177704, 0.747082, 0.800828,
            0.677747, -0.034135, 0.389854, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.011726, -0.389854, 0.177704, 0.747082, 0.800828,
            0.677747, 0.011726, -0.389854, 0.177704, 0.747082, 0.800828,
            -0.043671, -0.034135, -0.389854, 0.177704, 0.747082, 0.800828,
            0.677747, -0.034135, -0.389854, 0.177704, 0.747082, 0.800828,
            0.677747, 0.016724, 0.383856, 0.177704, 0.747082, 0.800828,
            0.677747, 0.011726, 0.389854, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.011726, 0.389854, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.016724, 0.383856, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.016724, -0.383856, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.011726, -0.389854, 0.177704, 0.747082, 0.800828,
            0.677747, 0.011726, -0.389854, 0.177704, 0.747082, 0.800828,
            0.677747, 0.016724, -0.383856, 0.177704, 0.747082, 0.800828,
            0.110008, -0.034135, -0.383856, 0.177704, 0.747082, 0.800828,
            0.110008, -0.034135, 0.383856, 0.177704, 0.747082, 0.800828,
            0.110008, 0.016724, 0.383856, 0.177704, 0.747082, 0.800828,
            0.110008, 0.016724, -0.383856, 0.177704, 0.747082, 0.800828,
            0.110008, 0.011726, 0.389854, 0.177704, 0.747082, 0.800828,
            0.110008, -0.034135, 0.389854, 0.177704, 0.747082, 0.800828,
            0.110008, 0.011726, -0.389854, 0.177704, 0.747082, 0.800828,
            0.110008, -0.034135, -0.389854, 0.177704, 0.747082, 0.800828,
            0.110008, 0.016724, 0.383856, 0.177704, 0.747082, 0.800828,
            0.110008, 0.011726, 0.389854, 0.177704, 0.747082, 0.800828,
            0.110008, 0.016724, -0.383856, 0.177704, 0.747082, 0.800828,
            0.110008, 0.011726, -0.389854, 0.177704, 0.747082, 0.800828,
            0.110008, 0.021722, 0.383856, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.021722, 0.383856, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.021722, -0.383856, 0.177704, 0.747082, 0.800828,
            0.110008, 0.021722, -0.383856, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.011726, -0.395852, 0.177704, 0.747082, 0.800828,
            0.110008, 0.011726, -0.395852, 0.177704, 0.747082, 0.800828,
            0.110008, 0.011726, 0.395852, 0.177704, 0.747082, 0.800828,
            -0.043671, 0.011726, 0.395852, 0.177704, 0.747082, 0.800828,
        ]

        blanket_indices = [
            2, 31, 27,
            0, 6, 1,
            1, 18, 19,
            30, 19, 35,
            1, 13, 2,
            15, 33, 32,
            5, 33, 26,
            0, 15, 25,
            32, 23, 37,
            4, 15, 0,
            7, 34, 28,
            25, 37, 36,
            29, 25, 36,
            29, 22, 9,
            6, 34, 18,
            34, 19, 18,
            15, 37, 24,
            26, 17, 4,
            32, 42, 14,
            11, 35, 20,
            30, 13, 10,
            27, 12, 3,
            29, 6, 8,
            9, 41, 29,
            28, 39, 7,
            11, 44, 30,
            2, 13, 31,
            0, 8, 6,
            1, 6, 18,
            19, 10, 1,
            30, 10, 19,
            1, 10, 13,
            15, 17, 33,
            5, 16, 33,
            25, 8, 0,
            15, 24, 25,
            32, 14, 23,
            4, 17, 15,
            7, 21, 34,
            25, 24, 37,
            29, 8, 25,
            29, 36, 22,
            6, 28, 34,
            34, 35, 19,
            15, 32, 37,
            26, 33, 17,
            32, 43, 42,
            11, 30, 35,
            30, 31, 13,
            27, 31, 12,
            29, 28, 6,
            9, 40, 41,
            28, 38, 39,
            11, 45, 44,
        ]

        return np.array(blanket_vertices, dtype=np.float32), np.array(blanket_indices, dtype=np.uint32)
    
    def get_back_side_blanket_data():
        back_side_blanket_vertices = [
            -0.043671, 0.011726, -0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.011726, 0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, -0.034135, 0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, -0.034135, -0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.016724, 0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.016724, -0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.011726, 0.389854, 0.718012, 0.237273, 0.075974,
            -0.043671, -0.034135, 0.389854, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.011726, -0.389854, 0.718012, 0.237273, 0.075974,
            -0.043671, -0.034135, -0.389854, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.011726, 0.389854, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.016724, 0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.016724, -0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.011726, -0.389854, 0.718012, 0.237273, 0.075974,
            0.110008, 0.016724, 0.383856, 0.718012, 0.237273, 0.075974,
            0.110008, 0.016724, -0.383856, 0.718012, 0.237273, 0.075974,
            0.110008, 0.011726, 0.389854, 0.718012, 0.237273, 0.075974,
            0.110008, -0.034135, 0.389854, 0.718012, 0.237273, 0.075974,
            0.110008, 0.011726, -0.389854, 0.718012, 0.237273, 0.075974,
            0.110008, -0.034135, -0.389854, 0.718012, 0.237273, 0.075974,
            0.110008, 0.016724, 0.383856, 0.718012, 0.237273, 0.075974,
            0.110008, 0.011726, 0.389854, 0.718012, 0.237273, 0.075974,
            0.110008, 0.016724, -0.383856, 0.718012, 0.237273, 0.075974,
            0.110008, 0.011726, -0.389854, 0.718012, 0.237273, 0.075974,
            0.110008, 0.021722, 0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.021722, 0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.021722, -0.383856, 0.718012, 0.237273, 0.075974,
            0.110008, 0.021722, -0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, -0.034135, -0.395852, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.011726, -0.395852, 0.718012, 0.237273, 0.075974,
            0.110008, 0.011726, -0.395852, 0.718012, 0.237273, 0.075974,
            0.110008, -0.034135, -0.395852, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.011726, -0.395852, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.021722, -0.383856, 0.718012, 0.237273, 0.075974,
            0.110008, 0.011726, -0.395852, 0.718012, 0.237273, 0.075974,
            0.110008, 0.021722, -0.383856, 0.718012, 0.237273, 0.075974,
            0.110008, 0.011726, 0.395852, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.011726, 0.395852, 0.718012, 0.237273, 0.075974,
            -0.043671, -0.034135, 0.395852, 0.718012, 0.237273, 0.075974,
            0.110008, -0.034135, 0.395852, 0.718012, 0.237273, 0.075974,
            0.110008, 0.021722, 0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.021722, 0.383856, 0.718012, 0.237273, 0.075974,
            -0.043671, 0.011726, 0.395852, 0.718012, 0.237273, 0.075974,
            0.110008, 0.011726, 0.395852, 0.718012, 0.237273, 0.075974,
        ]

        back_side_blanket_indices = [
            1, 5, 0,
            1, 6, 11,
            15, 24, 14,
            0, 9, 3,
            7, 37, 6,
            2, 6, 1,
            0, 12, 13,
            11, 42, 41,
            12, 32, 13,
            26, 24, 27,
            4, 26, 5,
            30, 28, 29,
            8, 28, 9,
            9, 31, 19,
            19, 30, 18,
            33, 34, 32,
            22, 33, 12,
            13, 34, 23,
            22, 34, 35,
            37, 39, 36,
            16, 39, 17,
            17, 38, 7,
            41, 43, 40,
            20, 43, 21,
            21, 42, 10,
            20, 41, 40,
            1, 4, 5,
            11, 4, 1,
            6, 10, 11,
            15, 27, 24,
            0, 8, 9,
            7, 38, 37,
            2, 7, 6,
            0, 5, 12,
            13, 8, 0,
            11, 10, 42,
            12, 33, 32,
            26, 25, 24,
            4, 25, 26,
            30, 31, 28,
            8, 29, 28,
            9, 28, 31,
            19, 31, 30,
            33, 35, 34,
            22, 35, 33,
            13, 32, 34,
            22, 23, 34,
            37, 38, 39,
            16, 36, 39,
            17, 39, 38,
            41, 42, 43,
            20, 40, 43,
            21, 43, 42,
            20, 11, 41,
        ]

        return np.array(back_side_blanket_vertices, dtype=np.float32), np.array(back_side_blanket_indices, dtype=np.uint32)