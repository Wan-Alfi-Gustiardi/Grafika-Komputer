import numpy as np
from OpenGL.GL import *
import ctypes
from meshes.cupboard import Cupboard

class CupboardModel:
    def __init__(self):
        self.get_cupboard_model()
        self.VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.cupboard_vertices.nbytes, self.cupboard_vertices, GL_STATIC_DRAW)

        self.EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.cupboard_indices.nbytes, self.cupboard_indices, GL_STATIC_DRAW)

        self.setup_vertex_attributes()

    def get_cupboard_model(self):
        cupboard_vertices, cupboard_indices = Cupboard.get_cupboard_data()
        handle_vertices, handle_indices = Cupboard.get_handle_data()

        handle_indices = handle_indices + int(len(cupboard_vertices) / 6)

        self.cupboard_vertices = np.concatenate([cupboard_vertices, handle_vertices])
        self.cupboard_indices = np.concatenate([cupboard_indices, handle_indices])

        return self.cupboard_vertices, self.cupboard_indices

    def setup_vertex_attributes(self):
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def draw(self):
        glDrawElements(GL_TRIANGLES, len(self.cupboard_indices), GL_UNSIGNED_INT, None)
