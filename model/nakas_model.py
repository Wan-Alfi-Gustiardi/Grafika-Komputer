import numpy as np
from OpenGL.GL import *
import ctypes
from meshes.nakas import Nakas

class NakasModel:
    def __init__(self):
        self.get_nakas_model()
        self.VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.nakas_vertices.nbytes, self.nakas_vertices, GL_STATIC_DRAW)

        self.EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.nakas_indices.nbytes, self.nakas_indices, GL_STATIC_DRAW)

        self.setup_vertex_attributes()

    def get_nakas_model(self):
        box_vertices, box_indices = Nakas.get_box_data()
        drawers1_vertices, drawers1_indices = Nakas.get_drawers1_data()
        drawers2_vertices, drawers2_indices = Nakas.get_drawers2_data()
        handle1_vertices, handle1_indices = Nakas.get_handle1_data()
        handle2_vertices, handle2_indices = Nakas.get_handle2_data()

        drawers1_indices = drawers1_indices + int(len(box_vertices) / 6)

        total_length = len(box_vertices) + len(drawers1_vertices)
        drawers2_indices = drawers2_indices + int(total_length / 6)

        total_length = total_length + len(drawers2_vertices)
        handle1_indices = handle1_indices + int(total_length / 6)

        total_length = total_length + len(handle1_vertices)
        handle2_indices = handle2_indices + int(total_length / 6)
        
        self.nakas_vertices = np.concatenate([box_vertices, drawers1_vertices, drawers2_vertices, handle1_vertices, handle2_vertices])
        self.nakas_indices = np.concatenate([box_indices, drawers1_indices, drawers2_indices, handle1_indices, handle2_vertices])

        return self.nakas_vertices, self.nakas_indices

    def setup_vertex_attributes(self):
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def draw(self):
        glDrawElements(GL_TRIANGLES, len(self.nakas_indices), GL_UNSIGNED_INT, None)
